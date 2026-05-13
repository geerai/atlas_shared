from __future__ import annotations

from atlas_shared.claim_strengths import Warrant, aggregate_claim_strengths
from atlas_shared.paper_quality import (
    EffectSize,
    FingerprintField,
    PaperQualityFingerprint,
    SampleOverlapEdge,
)


def _fp(paper_id: str, n: int, effect: float, lo: float, hi: float, replications: int = 0):
    return PaperQualityFingerprint(
        paper_id=paper_id,
        extractor_version="synthetic-v1",
        n_total=FingerprintField(value=n),
        primary_effect_size=FingerprintField(
            value=EffectSize(
                value=effect,
                metric="d",
                ci_lower=lo,
                ci_upper=hi,
                computed_or_reported="reported",
                origin="reported",
            )
        ),
        replication_count=FingerprintField(value=replications),
    )


def test_aggregate_claim_strengths_reports_expected_five_paper_values() -> None:
    fingerprints = (
        _fp("P1", 100, 0.20, 0.00, 0.40, 1),
        _fp("P2", 120, 0.30, 0.10, 0.50, 0),
        _fp("P3", 80, 0.40, 0.15, 0.65, 1),
        _fp("P4", 90, 0.10, -0.15, 0.35, 0),
        _fp("P5", 110, 0.50, 0.25, 0.75, 0),
    )
    warrants = tuple(Warrant(fp.paper_id) for fp in fingerprints)

    result = aggregate_claim_strengths("C1", warrants, fingerprints, ())

    assert result.claim_id == "C1"
    assert result.n_supporting == 5
    assert result.n_defeating == 0
    assert result.cumulative_n_unique == 500
    assert result.cumulative_n_overlap_flagged == 0
    assert round(result.weighted_effect_size or 0, 3) == 0.291
    assert round(result.heterogeneity_i_squared or 0, 1) == 38.1
    assert result.heterogeneity_band == "moderate"
    assert result.egger_test_applicable is False
    assert result.funnel_asymmetry_egger_p is None
    assert result.replication_rate == 0.4
    assert "fewer than ten" in result.weaknesses_markdown


def test_aggregate_claim_strengths_deduplicates_overlapping_sixth_paper() -> None:
    fingerprints = (
        _fp("P1", 100, 0.20, 0.00, 0.40),
        _fp("P2", 120, 0.30, 0.10, 0.50),
        _fp("P3", 80, 0.40, 0.15, 0.65),
        _fp("P4", 90, 0.10, -0.15, 0.35),
        _fp("P5", 110, 0.50, 0.25, 0.75),
        _fp("P6", 130, 0.70, 0.45, 0.95),
    )
    warrants = tuple(Warrant(fp.paper_id) for fp in fingerprints)
    overlaps = (
        SampleOverlapEdge(
            paper_id_a="P5",
            paper_id_b="P6",
            overlap_kind="shared_subjects",
            confidence=0.70,
            detected_by="manual",
        ),
    )

    result = aggregate_claim_strengths("C1", warrants, fingerprints, overlaps)

    assert result.n_supporting == 6
    assert result.cumulative_n_unique == 510
    assert result.cumulative_n_overlap_flagged == 1
    assert round(result.weighted_effect_size or 0, 3) == 0.307
