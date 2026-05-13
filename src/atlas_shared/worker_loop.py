from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import tempfile
import time
from typing import Any, Callable, Mapping


PassType = str


@dataclass(frozen=True)
class Batch:
    batch_id: str
    pass_type: PassType
    paper_ids: tuple[str, ...]
    batch_size: int
    status: str
    current_assignee: str | None = None
    papers_done: int = 0
    papers_failed: int = 0


@dataclass(frozen=True)
class WorkerLoopConfig:
    db_path: Path
    mirror_path: Path = Path("data/paper_quality_progress.json")
    repo_path: Path = Path(".")
    push_every_papers: int = 50


_CONFIG: WorkerLoopConfig | None = None
_PAPERS_SINCE_LAST_PUSH = 0


def configure_worker_loop(
    db_path: str | Path,
    mirror_path: str | Path = "data/paper_quality_progress.json",
    repo_path: str | Path = ".",
    push_every_papers: int = 50,
) -> WorkerLoopConfig:
    global _CONFIG
    _CONFIG = WorkerLoopConfig(
        db_path=Path(db_path),
        mirror_path=Path(mirror_path),
        repo_path=Path(repo_path),
        push_every_papers=push_every_papers,
    )
    return _CONFIG


def claim_next_batch(worker_id: str, pass_type: PassType, my_pool: str) -> Batch | None:
    cfg = _require_config()
    assignee = f"{my_pool}:{worker_id}"
    with _connect(cfg) as conn:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute(
            """
            SELECT batch_id, pass_type, paper_ids, batch_size, status, current_assignee,
                   papers_done, papers_failed
              FROM paper_quality_batches
             WHERE pass_type = ?
               AND status IN ('pending', 'reclaimable')
             ORDER BY claimed_at IS NOT NULL, batch_id
             LIMIT 1
            """,
            (pass_type,),
        ).fetchone()
        if row is None:
            conn.commit()
            return None
        updated = conn.execute(
            """
            UPDATE paper_quality_batches
               SET status = 'in_progress',
                   current_assignee = ?,
                   claimed_at = CURRENT_TIMESTAMP,
                   last_progress_at = CURRENT_TIMESTAMP,
                   reclamation_count = reclamation_count + CASE
                       WHEN status = 'reclaimable' THEN 1 ELSE 0 END
             WHERE batch_id = ?
               AND status IN ('pending', 'reclaimable')
            """,
            (assignee, row["batch_id"]),
        ).rowcount
        if updated != 1:
            conn.rollback()
            return None
        conn.execute(
            """
            UPDATE paper_quality_jobs
               SET status = 'in_progress',
                   claimed_at = COALESCE(claimed_at, CURRENT_TIMESTAMP),
                   attempt_count = attempt_count + 1
             WHERE batch_id = ?
               AND pass_type = ?
               AND status = 'pending'
            """,
            (row["batch_id"], pass_type),
        )
        conn.commit()
        return _batch_from_row(row, status="in_progress", current_assignee=assignee)


def job_already_done(paper_id: str, pass_type: PassType) -> bool:
    cfg = _require_config()
    with _connect(cfg) as conn:
        row = conn.execute(
            """
            SELECT 1 FROM paper_quality_jobs
             WHERE paper_id = ? AND pass_type = ? AND status = 'done'
             LIMIT 1
            """,
            (paper_id, pass_type),
        ).fetchone()
    return row is not None


def mark_paper_done(batch: Batch, paper_id: str, artifact_path: str) -> None:
    _update_job_in_batch(batch, paper_id, "done", artifact_path=artifact_path)


def mark_paper_failed_in_batch(batch: Batch, paper_id: str, reason: str) -> None:
    _update_job_in_batch(batch, paper_id, "failed", artifact_path=None, reason=reason)


def mark_paper_skipped_in_batch(batch: Batch, paper_id: str, reason: str) -> None:
    _update_job_in_batch(batch, paper_id, "done", artifact_path=f"skipped:{reason}")


def mark_batch_done(batch: Batch) -> None:
    cfg = _require_config()
    with _connect(cfg) as conn:
        conn.execute(
            """
            UPDATE paper_quality_batches
               SET status = 'done',
                   completed_at = CURRENT_TIMESTAMP,
                   last_progress_at = CURRENT_TIMESTAMP
             WHERE batch_id = ?
            """,
            (batch.batch_id,),
        )


def record_hard_rule_violation(
    paper_id: str,
    rule_id: str,
    violation_state: Mapping[str, Any],
    field_name: str | None = None,
) -> None:
    cfg = _require_config()
    with _connect(cfg) as conn:
        conn.execute(
            """
            INSERT INTO hard_rule_violations
              (paper_id, rule_id, field_name, violation_state, requires_dk_review)
            VALUES (?, ?, ?, ?, 1)
            """,
            (paper_id, rule_id, field_name, json.dumps(dict(violation_state), sort_keys=True)),
        )


def refresh_mirror_for_paper(paper_id: str) -> None:
    cfg = _require_config()
    with _connect(cfg) as conn:
        progress = conn.execute(
            """
            SELECT paper_id, codex_done_at, claude_done_at, gemini_done_at,
                   active_workers, pass_count, pass_done_count
              FROM paper_quality_progress
             WHERE paper_id = ?
            """,
            (paper_id,),
        ).fetchone()
        jobs = conn.execute(
            """
            SELECT pass_type, status, batch_id, artifact_path, completed_at
              FROM paper_quality_jobs
             WHERE paper_id = ?
             ORDER BY pass_type
            """,
            (paper_id,),
        ).fetchall()
    payload = {
        "paper_id": paper_id,
        "progress": dict(progress) if progress else None,
        "jobs": [dict(row) for row in jobs],
        "updated_at_epoch": time.time(),
    }
    _atomic_json_write(cfg.repo_path / cfg.mirror_path, payload)


def commit_local(message: str) -> None:
    cfg = _require_config()
    _run_git(["git", "add", str(cfg.mirror_path)], cfg.repo_path)
    _run_git(["git", "commit", "-m", message], cfg.repo_path)


def push_to_github(message: str) -> None:
    cfg = _require_config()
    try:
        _run_git(["git", "push"], cfg.repo_path)
    except subprocess.CalledProcessError:
        _run_git(["git", "pull", "--ff-only"], cfg.repo_path)
        commit_local(message)
        _run_git(["git", "push"], cfg.repo_path)


def papers_since_last_push() -> int:
    return _PAPERS_SINCE_LAST_PUSH


def run_worker(
    worker_id: str,
    pass_type: PassType,
    extractor: Callable[[str], str | None],
    my_pool: str = "default",
) -> None:
    global _PAPERS_SINCE_LAST_PUSH
    cfg = _require_config()
    while True:
        batch = claim_next_batch(worker_id, pass_type, my_pool)
        if batch is None:
            return
        for paper_id in batch.paper_ids:
            if job_already_done(paper_id, pass_type):
                continue
            try:
                artifact_path = extractor(paper_id)
            except Exception as exc:  # pragma: no cover - adapter-specific failures
                mark_paper_failed_in_batch(batch, paper_id, str(exc))
                continue
            if artifact_path is None:
                mark_paper_skipped_in_batch(batch, paper_id, "extractor_returned_none")
            else:
                mark_paper_done(batch, paper_id, artifact_path)
                refresh_mirror_for_paper(paper_id)
                _PAPERS_SINCE_LAST_PUSH += 1
                if _PAPERS_SINCE_LAST_PUSH >= cfg.push_every_papers:
                    commit_local(f"Update paper-quality progress through {paper_id}")
                    push_to_github(f"Update paper-quality progress through {paper_id}")
                    _PAPERS_SINCE_LAST_PUSH = 0
        mark_batch_done(batch)


def _update_job_in_batch(
    batch: Batch,
    paper_id: str,
    status: str,
    artifact_path: str | None = None,
    reason: str | None = None,
) -> None:
    cfg = _require_config()
    with _connect(cfg) as conn:
        conn.execute("BEGIN IMMEDIATE")
        rowcount = conn.execute(
            """
            UPDATE paper_quality_jobs
               SET status = ?,
                   completed_at = CASE WHEN ? IN ('done', 'failed') THEN CURRENT_TIMESTAMP ELSE completed_at END,
                   artifact_path = COALESCE(?, artifact_path)
             WHERE paper_id = ?
               AND pass_type = ?
               AND batch_id = ?
               AND status != 'done'
            """,
            (status, status, artifact_path, paper_id, batch.pass_type, batch.batch_id),
        ).rowcount
        if rowcount:
            if status == "failed":
                conn.execute(
                    """
                    UPDATE paper_quality_batches
                       SET papers_failed = papers_failed + 1,
                           last_progress_at = CURRENT_TIMESTAMP,
                           notification_events = json_insert(
                               notification_events,
                               '$[#]',
                               json_object('paper_id', ?, 'status', 'failed', 'reason', ?)
                           )
                     WHERE batch_id = ?
                    """,
                    (paper_id, reason or "", batch.batch_id),
                )
            else:
                conn.execute(
                    """
                    UPDATE paper_quality_batches
                       SET papers_done = papers_done + 1,
                           last_progress_at = CURRENT_TIMESTAMP
                     WHERE batch_id = ?
                    """,
                    (batch.batch_id,),
                )
        conn.commit()


def _batch_from_row(row: sqlite3.Row, **overrides: Any) -> Batch:
    data = dict(row)
    data.update(overrides)
    return Batch(
        batch_id=str(data["batch_id"]),
        pass_type=str(data["pass_type"]),
        paper_ids=tuple(json.loads(data["paper_ids"])),
        batch_size=int(data["batch_size"]),
        status=str(data["status"]),
        current_assignee=data.get("current_assignee"),
        papers_done=int(data.get("papers_done") or 0),
        papers_failed=int(data.get("papers_failed") or 0),
    )


def _connect(cfg: WorkerLoopConfig) -> sqlite3.Connection:
    conn = sqlite3.connect(cfg.db_path, timeout=30.0)
    conn.row_factory = sqlite3.Row
    return conn


def _require_config() -> WorkerLoopConfig:
    if _CONFIG is None:
        raise RuntimeError("worker_loop is not configured; call configure_worker_loop(db_path)")
    return _CONFIG


def _atomic_json_write(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
            fh.write("\n")
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def _run_git(args: list[str], cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True)
