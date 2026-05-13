from __future__ import annotations

import json
import sqlite3
import subprocess

from atlas_shared import worker_loop


def _init_db(path) -> None:
    conn = sqlite3.connect(path)
    conn.executescript(
        """
        CREATE TABLE paper_quality_batches (
          batch_id TEXT PRIMARY KEY,
          pass_type TEXT NOT NULL,
          paper_ids TEXT NOT NULL,
          batch_size INTEGER NOT NULL,
          status TEXT NOT NULL DEFAULT 'pending',
          current_assignee TEXT,
          claimed_at TEXT,
          last_progress_at TEXT,
          completed_at TEXT,
          papers_done INTEGER NOT NULL DEFAULT 0,
          papers_failed INTEGER NOT NULL DEFAULT 0,
          notification_events TEXT NOT NULL DEFAULT '[]',
          reclamation_count INTEGER NOT NULL DEFAULT 0
        );
        CREATE TABLE paper_quality_jobs (
          job_id TEXT PRIMARY KEY,
          paper_id TEXT NOT NULL,
          pass_type TEXT NOT NULL,
          batch_id TEXT,
          status TEXT NOT NULL DEFAULT 'pending',
          claimed_at TEXT,
          completed_at TEXT,
          artifact_path TEXT,
          attempt_count INTEGER NOT NULL DEFAULT 0,
          UNIQUE (paper_id, pass_type)
        );
        CREATE TABLE hard_rule_violations (
          violation_id INTEGER PRIMARY KEY AUTOINCREMENT,
          paper_id TEXT NOT NULL,
          rule_id TEXT NOT NULL,
          field_name TEXT,
          violation_state TEXT NOT NULL,
          violation_timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
          requires_dk_review INTEGER NOT NULL DEFAULT 1
        );
        CREATE VIEW paper_quality_progress AS
        SELECT
          paper_id,
          MAX(CASE WHEN pass_type = 'extract_codex' AND status = 'done'
                   THEN completed_at END) AS codex_done_at,
          MAX(CASE WHEN pass_type = 'extract_claude' AND status = 'done'
                   THEN completed_at END) AS claude_done_at,
          MAX(CASE WHEN pass_type = 'verify_gemini' AND status = 'done'
                   THEN completed_at END) AS gemini_done_at,
          NULL AS active_workers,
          COUNT(*) AS pass_count,
          SUM(CASE WHEN status = 'done' THEN 1 ELSE 0 END) AS pass_done_count
        FROM paper_quality_jobs
        GROUP BY paper_id;
        """
    )
    conn.execute(
        """
        INSERT INTO paper_quality_batches
          (batch_id, pass_type, paper_ids, batch_size)
        VALUES ('B1', 'extract_codex', '["P1", "P2"]', 2)
        """
    )
    for paper_id in ("P1", "P2"):
        conn.execute(
            """
            INSERT OR IGNORE INTO paper_quality_jobs
              (job_id, paper_id, pass_type, batch_id)
            VALUES (?, ?, 'extract_codex', 'B1')
            """,
            (f"J-{paper_id}", paper_id),
        )
    conn.commit()
    conn.close()


def test_claim_next_batch_is_atomic_for_two_workers(tmp_path) -> None:
    db_path = tmp_path / "pq.db"
    _init_db(db_path)
    worker_loop.configure_worker_loop(db_path, repo_path=tmp_path)

    first = worker_loop.claim_next_batch("w1", "extract_codex", "codex")
    second = worker_loop.claim_next_batch("w2", "extract_codex", "codex")

    assert first is not None
    assert first.batch_id == "B1"
    assert first.current_assignee == "codex:w1"
    assert second is None

    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT status FROM paper_quality_batches").fetchone()[0] == "in_progress"
    assert conn.execute("SELECT sum(attempt_count) FROM paper_quality_jobs").fetchone()[0] == 2


def test_job_done_path_is_idempotent_and_updates_batch_once(tmp_path) -> None:
    db_path = tmp_path / "pq.db"
    _init_db(db_path)
    worker_loop.configure_worker_loop(db_path, repo_path=tmp_path)
    batch = worker_loop.claim_next_batch("w1", "extract_codex", "codex")
    assert batch is not None

    worker_loop.mark_paper_done(batch, "P1", "artifacts/P1.json")
    worker_loop.mark_paper_done(batch, "P1", "artifacts/P1.json")

    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT status FROM paper_quality_jobs WHERE paper_id='P1'").fetchone()[0] == "done"
    assert conn.execute("SELECT papers_done FROM paper_quality_batches").fetchone()[0] == 1


def test_refresh_mirror_for_paper_uses_atomic_final_file(tmp_path) -> None:
    db_path = tmp_path / "pq.db"
    _init_db(db_path)
    worker_loop.configure_worker_loop(
        db_path,
        mirror_path="data/paper_quality_progress.json",
        repo_path=tmp_path,
    )
    batch = worker_loop.claim_next_batch("w1", "extract_codex", "codex")
    assert batch is not None
    worker_loop.mark_paper_done(batch, "P1", "artifacts/P1.json")

    worker_loop.refresh_mirror_for_paper("P1")

    mirror = tmp_path / "data" / "paper_quality_progress.json"
    payload = json.loads(mirror.read_text())
    assert payload["paper_id"] == "P1"
    assert payload["progress"]["pass_done_count"] == 1
    assert not list(mirror.parent.glob("*.tmp"))


def test_push_failure_handler_repulls_recommits_and_retries(tmp_path, monkeypatch) -> None:
    db_path = tmp_path / "pq.db"
    _init_db(db_path)
    worker_loop.configure_worker_loop(db_path, mirror_path="progress.json", repo_path=tmp_path)
    calls: list[list[str]] = []

    def fake_run(args, cwd, check, capture_output, text):
        calls.append(args)
        if args == ["git", "push"] and calls.count(args) == 1:
            raise subprocess.CalledProcessError(1, args)
        return subprocess.CompletedProcess(args, 0, "", "")

    monkeypatch.setattr(worker_loop.subprocess, "run", fake_run)

    worker_loop.push_to_github("retry progress")

    assert calls == [
        ["git", "push"],
        ["git", "pull", "--ff-only"],
        ["git", "add", "progress.json"],
        ["git", "commit", "-m", "retry progress"],
        ["git", "push"],
    ]


def test_record_hard_rule_violation_inserts_json_state(tmp_path) -> None:
    db_path = tmp_path / "pq.db"
    _init_db(db_path)
    worker_loop.configure_worker_loop(db_path, repo_path=tmp_path)

    worker_loop.record_hard_rule_violation(
        "P1", "HARD_RULE_8", {"conversation_count": 1}, field_name="sample_country"
    )

    conn = sqlite3.connect(db_path)
    state = conn.execute("SELECT violation_state FROM hard_rule_violations").fetchone()[0]
    assert json.loads(state) == {"conversation_count": 1}
