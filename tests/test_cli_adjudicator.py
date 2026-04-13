from __future__ import annotations

from pathlib import Path
import sys

from atlas_shared.cli_adjudicator import AGCommandAdjudicator
from atlas_shared.relevance import (
    AdjudicationRequest,
    ArticleCandidate,
    ArticleTypeDecision,
    QuestionConstitution,
    RelevanceAssessment,
)


def test_ag_command_adjudicator_accepts_json_from_local_broker(tmp_path: Path) -> None:
    script = tmp_path / "ag_stub.py"
    script.write_text(
        "\n".join(
            [
                "import json, sys",
                "sys.stdin.read()",
                "print(json.dumps({",
                "  'verdict': 'accept',",
                "  'confidence': 0.84,",
                "  'reasons': ['AG broker selected a subscribed model and accepted the article.'],",
                "  'needs_manual_review': False,",
                "  'source': 'ag::stub',",
                "  'edge_case_kind': 'topic_expansion_candidate',",
                "  'novelty_signal': 0.76,",
                "  'topic_expansion_candidate': True,",
                "  'new_topic_candidate': False,",
                "  'proposed_topic_label': 'Nature Exposure and Restoration',",
                "  'adjacent_topics': ['Nature and Attention', 'Affect Regulation']",
                "}))",
            ]
        )
    )

    request = AdjudicationRequest(
        constitution=QuestionConstitution(
            question_id="Q1",
            question_text="Does daylight improve alertness?",
            topic="Lighting",
            environment_terms=("daylight",),
            outcome_terms=("alertness",),
        ),
        article=ArticleCandidate(
            paper_id="PDF-1",
            title="Daylight improves alertness",
            abstract="An experiment with participants found improved alertness.",
        ),
        heuristic_assessment=RelevanceAssessment(
            paper_id="PDF-1",
            question_id="Q1",
            bundle_id="bundle-lighting",
            article_type=ArticleTypeDecision(
                value="empirical_research",
                confidence=0.9,
                source="test",
            ),
            verdict="edge_case",
            confidence=0.6,
            needs_manual_review=True,
            reasons=("Heuristic gate left this for review.",),
        ),
    )

    adjudicator = AGCommandAdjudicator([sys.executable, str(script)])
    result = adjudicator.adjudicate(request)

    assert result is not None
    assert result.verdict == "accept"
    assert result.source == "ag::stub"
    assert result.topic_expansion_candidate is True
    assert result.novelty_signal == 0.76
