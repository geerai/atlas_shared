from __future__ import annotations

from dataclasses import dataclass
from statistics import median
from typing import Mapping, Sequence

from .paper_quality import PaperQualityFingerprint


DESIGN_TYPE_WEIGHTS: Mapping[str, float] = {
    "lab_experiment": 1.0,
    "field_experiment": 1.25,
    "observational_cohort": 0.9,
    "online": 0.8,
    "secondary_analysis": 0.7,
    "meta_analysis": 1.4,
    "theoretical": 0.0,
}


@dataclass(frozen=True)
class LiteratureBodyQuality:
    topic_id: str
    total_primary_paper_count: int
    preregistration_fraction: float | None
    weighted_median_sample_size: float | None
    median_effect_ci_width_by_metric: Mapping[str, float]
    replication_coverage_fraction: float | None
    open_data_availability_fraction: float | None


def aggregate_literature_body_quality(
    topic_id: str,
    fingerprints: Sequence[PaperQualityFingerprint],
    replication_registry_paper_ids: Sequence[str] = (),
) -> LiteratureBodyQuality:
    total = len(fingerprints)
    prereg_values = [
        bool(fp.preregistration.value and fp.preregistration.value.verified)
        for fp in fingerprints
        if fp.preregistration.value is not None
    ]
    replication_ids = set(replication_registry_paper_ids)
    replication_hits = [
        fp.paper_id in replication_ids or bool(fp.replication_count.value and fp.replication_count.value > 0)
        for fp in fingerprints
    ]
    open_data_values = [
        bool(fp.open_data_url.value and fp.open_data_verified.value) for fp in fingerprints
    ]
    return LiteratureBodyQuality(
        topic_id=topic_id,
        total_primary_paper_count=total,
        preregistration_fraction=_fraction(prereg_values),
        weighted_median_sample_size=_weighted_median_sample_size(fingerprints),
        median_effect_ci_width_by_metric=_median_ci_width_by_metric(fingerprints),
        replication_coverage_fraction=_fraction(replication_hits),
        open_data_availability_fraction=_fraction(open_data_values),
    )


def _fraction(values: Sequence[bool]) -> float | None:
    if not values:
        return None
    return sum(1 for value in values if value) / len(values)


def _weighted_median_sample_size(fingerprints: Sequence[PaperQualityFingerprint]) -> float | None:
    expanded: list[float] = []
    for fp in fingerprints:
        if fp.n_total.value is None:
            continue
        design_type = fp.design_type.value or "lab_experiment"
        weight = DESIGN_TYPE_WEIGHTS.get(str(design_type), 1.0)
        repeats = max(1, round(weight * 4))
        expanded.extend([float(fp.n_total.value)] * repeats)
    if not expanded:
        return None
    return float(median(expanded))


def _median_ci_width_by_metric(
    fingerprints: Sequence[PaperQualityFingerprint],
) -> dict[str, float]:
    by_metric: dict[str, list[float]] = {}
    for fp in fingerprints:
        effect = fp.primary_effect_size.value
        if not effect or not effect.metric or effect.ci_width is None:
            continue
        by_metric.setdefault(effect.metric, []).append(effect.ci_width)
    return {metric: float(median(widths)) for metric, widths in by_metric.items()}
