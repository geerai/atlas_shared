from __future__ import annotations

from atlas_shared.literature_body import aggregate_literature_body_quality
from atlas_shared.paper_quality import (
    EffectSize,
    FingerprintField,
    PaperQualityFingerprint,
    PreregRecord,
)


def _fp(
    paper_id: str,
    n: int,
    design_type: str,
    prereg: bool,
    effect_width: float,
    metric: str = "d",
    replication_count: int = 0,
    open_data: bool = False,
) -> PaperQualityFingerprint:
    half_width = effect_width / 2
    return PaperQualityFingerprint(
        paper_id=paper_id,
        extractor_version="synthetic-v1",
        n_total=FingerprintField(value=n),
        design_type=FingerprintField(value=design_type),
        preregistration=FingerprintField(
            value=PreregRecord(url=f"https://osf.io/{paper_id}" if prereg else "", verified=prereg)
        ),
        replication_count=FingerprintField(value=replication_count),
        primary_effect_size=FingerprintField(
            value=EffectSize(
                value=0.30,
                metric=metric,
                ci_lower=0.30 - half_width,
                ci_upper=0.30 + half_width,
                computed_or_reported="reported",
                origin="reported",
            )
        ),
        open_data_url=FingerprintField(value=f"https://data/{paper_id}" if open_data else ""),
        open_data_verified=FingerprintField(value=open_data),
    )


def test_literature_body_quality_summarizes_ten_paper_fixture() -> None:
    fingerprints = (
        _fp("P1", 40, "online", True, 0.40, replication_count=1, open_data=True),
        _fp("P2", 50, "online", False, 0.50),
        _fp("P3", 60, "lab_experiment", True, 0.60, open_data=True),
        _fp("P4", 70, "lab_experiment", False, 0.70),
        _fp("P5", 80, "field_experiment", True, 0.80),
        _fp("P6", 90, "field_experiment", False, 0.90, replication_count=2),
        _fp("P7", 100, "observational_cohort", True, 1.00, metric="r"),
        _fp("P8", 110, "observational_cohort", False, 1.10, metric="r"),
        _fp("P9", 120, "meta_analysis", True, 1.20, metric="r", open_data=True),
        _fp("P10", 130, "theoretical", False, 1.30, metric="r"),
    )

    result = aggregate_literature_body_quality(
        "T1", fingerprints, replication_registry_paper_ids=("P4",)
    )

    assert result.topic_id == "T1"
    assert result.total_primary_paper_count == 10
    assert result.preregistration_fraction == 0.5
    assert result.weighted_median_sample_size == 90.0
    assert {k: round(v, 2) for k, v in result.median_effect_ci_width_by_metric.items()} == {
        "d": 0.65,
        "r": 1.15,
    }
    assert result.replication_coverage_fraction == 0.3
    assert result.open_data_availability_fraction == 0.3
