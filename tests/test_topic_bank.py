from __future__ import annotations

import json
from pathlib import Path

from atlas_shared.intake import PreExtractionIntakeGate
from atlas_shared.topic_bank import (
    TopicConstitutionBank,
    load_question_constitutions,
    load_topic_constitution_bank,
    topic_records_for_questions,
)


def test_default_topic_bank_loads_panel_derived_constitutions() -> None:
    bank = load_topic_constitution_bank()

    assert len(bank.records) >= 30
    assert bank.source_path.endswith("question_constitutions_curated_30.json")
    assert "Attention Restoration Theory" in bank.topics
    assert bank.by_question_id("SQ-001") is not None
    assert bank.by_question_id("SQ-001").panel_status == "llm_panel_drafted"  # type: ignore[union-attr]
    assert load_question_constitutions()[0].question_id.startswith("SQ-")


def test_topic_bank_can_feed_pre_extraction_intake_gate() -> None:
    constitutions = load_question_constitutions()
    gate = PreExtractionIntakeGate(constitutions)
    result = gate.assess(
        {
            "paper_id": "PDF-3001",
            "title": "Natural environments restore directed attention after urban walks",
            "abstract": (
                "An experiment with participants compared natural environments with urban environments "
                "and measured directed attention using a backward digit span task."
            ),
        }
    )

    assert result.intake_decision == "accept_candidate"
    assert result.routing_target == "article_eater"
    assert result.primary_topic == "Attention Restoration Theory"
    assert "SQ-001" in result.matched_question_ids


def test_topic_records_for_questions_returns_panel_metadata() -> None:
    records = topic_records_for_questions(("SQ-001", "missing"))

    assert len(records) == 1
    assert records[0].question_id == "SQ-001"
    assert records[0].topic_key.startswith("Attention Restoration Theory")
    assert records[0].to_question_constitution().question_id == "SQ-001"


def test_topic_bank_loads_explicit_path(tmp_path: Path) -> None:
    source = tmp_path / "bank.json"
    source.write_text(
        json.dumps(
            {
                "version": "test",
                "questions": [
                    {
                        "question_id": "SQ-X",
                        "question_text": "Does a new built-environment topic matter?",
                        "topic": "Emergent Topic",
                        "subtopic": "Boundary",
                        "panel_status": "panel_reviewed",
                        "constitution_version": "v1",
                    }
                ],
            }
        )
    )

    bank = load_topic_constitution_bank(source)

    assert isinstance(bank, TopicConstitutionBank)
    assert bank.version == "test"
    assert bank.records[0].topic_key == "Emergent Topic / Boundary"
