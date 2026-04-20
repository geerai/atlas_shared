from __future__ import annotations

from atlas_shared.classifier_system import (
    AdaptiveClassifierSubsystem,
    ClassificationEvidence,
    PDFSurfaceSnapshot,
)
from atlas_shared.relevance import QuestionConstitution


def _constitutions() -> tuple[QuestionConstitution, ...]:
    return (
        QuestionConstitution(
            question_id="Q-LIGHT",
            question_text="Does daylight improve alertness in workplaces?",
            topic="Lighting",
            environment_terms=("daylight", "window", "lighting"),
            outcome_terms=("alertness", "fatigue"),
            exclusion_terms=("microscopy",),
            required_evidence_terms=("participants", "experiment", "p <"),
        ),
        QuestionConstitution(
            question_id="Q-NATURE",
            question_text="Does nature exposure reduce stress in adults?",
            topic="Biophilia",
            environment_terms=("nature", "forest", "green space"),
            outcome_terms=("stress", "mood"),
            exclusion_terms=("adhd",),
            edge_terms=("restoration", "attention"),
            required_evidence_terms=("participants",),
        ),
    )


class _StubSurfaceExtractor:
    def extract(self, evidence, *, max_pages: int = 4, max_chars: int = 8000):
        return PDFSurfaceSnapshot(
            source="stub_surface_extractor",
            extraction_mode="stub",
            pages_read=2,
            pdf_path=evidence.pdf_path,
            raw_text=(
                "Abstract\n"
                "An office experiment tested daylight exposure and alertness.\n"
                "Introduction\n"
                "Window access may improve alertness and reduce fatigue in offices.\n"
                "Methods\n"
                "Participants completed an experiment with p < .05.\n"
                "Discussion\n"
                "Daylight improved alertness under realistic office conditions."
            ),
            section_headings=("Abstract", "Introduction", "Methods", "Discussion"),
            first_page_excerpt="An office experiment tested daylight exposure and alertness.",
            abstract_excerpt="An office experiment tested daylight exposure and alertness.",
            intro_excerpt="Window access may improve alertness and reduce fatigue in offices.",
            methods_excerpt="Participants completed an experiment with p < .05.",
            conclusion_excerpt="Daylight improved alertness under realistic office conditions.",
        )


def test_bibliographic_only_stage_requests_more_evidence() -> None:
    subsystem = AdaptiveClassifierSubsystem(_constitutions())

    result = subsystem.classify(
        {
            "paper_id": "PDF-BIB-1",
            "title": "Built environment paper",
        },
        allow_surface_creation=False,
    )

    assert result.evidence_stage == "bibliographic_only"
    assert result.next_action == "need_abstract_or_keywords"
    assert result.needs_more_evidence is True


def test_metadata_text_stage_can_reach_intake_decision() -> None:
    subsystem = AdaptiveClassifierSubsystem(_constitutions())

    result = subsystem.classify(
        {
            "paper_id": "PDF-META-1",
            "title": "Daylight improves alertness in office workers",
            "abstract": (
                "An experiment with 72 participants found that daylight exposure "
                "improved alertness and reduced fatigue in office workstations (p < .01)."
            ),
            "keywords": ["daylight", "alertness", "office"],
        },
        allow_surface_creation=False,
    )

    assert result.evidence_stage == "metadata_text"
    assert result.question_summary.best_verdict == "accept"
    assert result.stable_topic_routing is not None
    assert result.stable_topic_routing.primary_topic == "Lighting"
    assert result.intake_result is not None
    assert result.intake_result.intake_decision == "accept_candidate"
    assert result.next_action == "ready_for_intake_decision"


def test_pdf_surface_stage_can_create_lightweight_evidence() -> None:
    subsystem = AdaptiveClassifierSubsystem(
        _constitutions(),
        surface_extractor=_StubSurfaceExtractor(),
    )

    result = subsystem.classify(
        ClassificationEvidence(
            paper_id="PDF-SURF-1",
            title="Windows and workplace outcomes",
            pdf_path="/tmp/fake.pdf",
        )
    )

    assert result.surface_snapshot is not None
    assert result.surface_snapshot.extraction_mode == "stub"
    assert result.evidence_stage == "pdf_surface_light"
    assert "surface_extraction" in result.analysis_steps_run
    assert result.stable_topic_routing is not None
    assert result.stable_topic_routing.primary_topic == "Lighting"
    assert result.next_action == "ready_for_downstream_extraction"


def test_extraction_aware_stage_uses_operationalization_fields() -> None:
    subsystem = AdaptiveClassifierSubsystem(_constitutions())

    result = subsystem.classify(
        {
            "paper_id": "PDF-EXTRACT-1",
            "title": "Lighting and fatigue in office work",
            "methods_surface_summary": "Participants completed an office lighting experiment with p < .05.",
            "independent_variables": "daylight exposure, window access",
            "dependent_variables": "alertness, fatigue",
            "measurement_inventory": [
                {
                    "outcome": "alertness",
                    "measure_name": "alertness rating",
                    "instrument_name": "self report scale",
                    "sensor_name": "wrist actigraph",
                }
            ],
        },
        allow_surface_creation=False,
    )

    assert result.evidence_stage == "extraction_aware"
    assert "measurement_terms" in result.available_evidence_types
    assert "sensor_terms" in result.available_evidence_types
    assert result.stable_topic_routing is not None
    assert result.stable_topic_routing.primary_topic == "Lighting"
    assert result.next_action == "ready_for_topic_routing"


def test_active_topic_overlay_is_reported_separately_from_stable_topics() -> None:
    subsystem = AdaptiveClassifierSubsystem(_constitutions())

    result = subsystem.classify(
        {
            "paper_id": "PDF-OVERLAY-1",
            "title": "Forest bathing reduces stress in adults",
            "abstract": (
                "Participants exposed to forest bathing showed lower stress and improved mood "
                "after nature exposure."
            ),
        },
        active_topic_overlay=[
            {
                "topic_id": "overlay-1",
                "label": "Nature Exposure and Restoration",
                "keywords": ["forest bathing", "nature exposure", "restoration", "stress"],
            }
        ],
        allow_surface_creation=False,
    )

    assert result.active_topic_matches
    assert result.active_topic_matches[0].label == "Nature Exposure and Restoration"
    assert result.question_summary.enabled is True
    assert result.stable_topic_routing is not None
    assert result.stable_topic_routing.primary_topic == "Biophilia"
