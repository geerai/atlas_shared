from __future__ import annotations

from dataclasses import dataclass
import math
from statistics import mean
from typing import Sequence

from .paper_quality import EffectSize, PaperQualityFingerprint, SampleOverlapEdge


WEIGHTING_FUNCTION_VERSION = "v1.0-2026-05-13"


@dataclass(frozen=True)
class Warrant:
    paper_id: str
    direction: str = "supporting"
    warrant_weight: float = 1.0


@dataclass(frozen=True)
class ClaimStrengthsWeaknesses:
    claim_id: str
    n_supporting: int
    n_defeating: int
    cumulative_n_unique: int
    cumulative_n_overlap_flagged: int
    heterogeneity_i_squared: float | None
    heterogeneity_band: str
    weighted_effect_size: float | None
    weighted_effect_metric: str | None
    funnel_asymmetry_egger_intercept: float | None
    funnel_asymmetry_egger_p: float | None
    egger_test_applicable: bool
    replication_rate: float | None
    strengths_markdown: str
    weaknesses_markdown: str
    weighting_function_version: str = WEIGHTING_FUNCTION_VERSION


def aggregate_claim_strengths(
    claim_id: str,
    warrants: Sequence[Warrant],
    fingerprints: Sequence[PaperQualityFingerprint],
    overlap_edges: Sequence[SampleOverlapEdge],
) -> ClaimStrengthsWeaknesses:
    fingerprint_by_id = {fp.paper_id: fp for fp in fingerprints}
    warrant_by_id = {w.paper_id: w for w in warrants}
    selected = [fp for fp in fingerprints if fp.paper_id in warrant_by_id]
    groups = _deduplicated_groups(selected, overlap_edges)
    group_effects = [_average_group_effect(group) for group in groups]
    usable_effects = [effect for effect in group_effects if effect and effect.value is not None]
    metric = _dominant_metric(usable_effects)
    usable_effects = [effect for effect in usable_effects if effect.metric == metric]
    weighted_effect = _weighted_effect(usable_effects) if usable_effects else None
    i_squared = _i_squared(usable_effects) if len(usable_effects) >= 2 else None
    egger = _egger(usable_effects)
    n_supporting = sum(1 for w in warrants if w.direction != "defeating")
    n_defeating = sum(1 for w in warrants if w.direction == "defeating")
    replication_values = [
        fp.replication_count.value for fp in selected if fp.replication_count.value is not None
    ]
    replication_rate = (
        sum(1 for value in replication_values if value and value > 0) / len(replication_values)
        if replication_values
        else None
    )
    cumulative_n_unique = sum(_group_n(group) for group in groups)
    cumulative_n_overlap_flagged = sum(max(0, len(group) - 1) for group in groups)
    return ClaimStrengthsWeaknesses(
        claim_id=claim_id,
        n_supporting=n_supporting,
        n_defeating=n_defeating,
        cumulative_n_unique=cumulative_n_unique,
        cumulative_n_overlap_flagged=cumulative_n_overlap_flagged,
        heterogeneity_i_squared=i_squared,
        heterogeneity_band=_heterogeneity_band(i_squared),
        weighted_effect_size=weighted_effect,
        weighted_effect_metric=metric,
        funnel_asymmetry_egger_intercept=egger.intercept,
        funnel_asymmetry_egger_p=egger.p_value,
        egger_test_applicable=egger.applicable,
        replication_rate=replication_rate,
        strengths_markdown=_strengths_text(n_supporting, weighted_effect, i_squared, replication_rate),
        weaknesses_markdown=_weaknesses_text(n_defeating, cumulative_n_overlap_flagged, egger.applicable),
    )


@dataclass(frozen=True)
class _EggerResult:
    applicable: bool
    intercept: float | None = None
    p_value: float | None = None


def _deduplicated_groups(
    fingerprints: Sequence[PaperQualityFingerprint],
    overlap_edges: Sequence[SampleOverlapEdge],
) -> list[list[PaperQualityFingerprint]]:
    parent = {fp.paper_id: fp.paper_id for fp in fingerprints}

    def find(item: str) -> str:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(a: str, b: str) -> None:
        root_a, root_b = find(a), find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    for edge in overlap_edges:
        if edge.confidence > 0.50 and edge.paper_id_a in parent and edge.paper_id_b in parent:
            union(edge.paper_id_a, edge.paper_id_b)

    grouped: dict[str, list[PaperQualityFingerprint]] = {}
    for fp in fingerprints:
        grouped.setdefault(find(fp.paper_id), []).append(fp)
    return list(grouped.values())


def _average_group_effect(group: Sequence[PaperQualityFingerprint]) -> EffectSize | None:
    effects = [fp.primary_effect_size.value for fp in group if fp.primary_effect_size.value]
    effects = [effect for effect in effects if effect.value is not None]
    if not effects:
        return None
    metric = _dominant_metric(effects)
    same_metric = [effect for effect in effects if effect.metric == metric]
    return EffectSize(
        value=mean(effect.value for effect in same_metric if effect.value is not None),
        metric=metric,
        ci_lower=_mean_optional(effect.ci_lower for effect in same_metric),
        ci_upper=_mean_optional(effect.ci_upper for effect in same_metric),
        computed_or_reported="unknown",
        origin="unknown",
    )


def _dominant_metric(effects: Sequence[EffectSize]) -> str | None:
    counts: dict[str, int] = {}
    for effect in effects:
        if effect.metric:
            counts[effect.metric] = counts.get(effect.metric, 0) + 1
    if not counts:
        return None
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]


def _weighted_effect(effects: Sequence[EffectSize]) -> float:
    weighted_sum = 0.0
    total_weight = 0.0
    for effect in effects:
        if effect.value is None:
            continue
        weight = _inverse_variance(effect)
        weighted_sum += effect.value * weight
        total_weight += weight
    return weighted_sum / total_weight if total_weight else mean(effect.value for effect in effects if effect.value is not None)


def _inverse_variance(effect: EffectSize) -> float:
    if effect.ci_lower is None or effect.ci_upper is None:
        return 1.0
    se = (effect.ci_upper - effect.ci_lower) / 3.92
    if se <= 0:
        return 1.0
    return 1.0 / (se * se)


def _i_squared(effects: Sequence[EffectSize]) -> float:
    weights = [_inverse_variance(effect) for effect in effects]
    values = [float(effect.value) for effect in effects if effect.value is not None]
    if len(values) < 2:
        return 0.0
    weighted_mean = sum(value * weight for value, weight in zip(values, weights)) / sum(weights)
    q = sum(weight * ((value - weighted_mean) ** 2) for value, weight in zip(values, weights))
    df = len(values) - 1
    if q <= 0:
        return 0.0
    return max(0.0, min(100.0, ((q - df) / q) * 100.0))


def _egger(effects: Sequence[EffectSize]) -> _EggerResult:
    if len(effects) < 10:
        return _EggerResult(applicable=False)
    xs: list[float] = []
    ys: list[float] = []
    for effect in effects:
        if effect.value is None or effect.ci_lower is None or effect.ci_upper is None:
            continue
        se = (effect.ci_upper - effect.ci_lower) / 3.92
        if se <= 0:
            continue
        xs.append(1 / se)
        ys.append(effect.value / se)
    if len(xs) < 10:
        return _EggerResult(applicable=False)
    x_bar, y_bar = mean(xs), mean(ys)
    sxx = sum((x - x_bar) ** 2 for x in xs)
    if sxx == 0:
        return _EggerResult(applicable=False)
    slope = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys)) / sxx
    intercept = y_bar - slope * x_bar
    residuals = [y - (intercept + slope * x) for x, y in zip(xs, ys)]
    if len(xs) <= 2:
        return _EggerResult(applicable=False)
    mse = sum(resid * resid for resid in residuals) / (len(xs) - 2)
    se_intercept = math.sqrt(mse * (1 / len(xs) + (x_bar * x_bar / sxx)))
    if se_intercept == 0:
        p_value = 1.0
    else:
        z = abs(intercept / se_intercept)
        p_value = math.erfc(z / math.sqrt(2))
    return _EggerResult(applicable=True, intercept=intercept, p_value=p_value)


def _heterogeneity_band(i_squared: float | None) -> str:
    if i_squared is None:
        return "not_applicable"
    if i_squared < 25:
        return "low"
    if i_squared < 50:
        return "moderate"
    if i_squared < 75:
        return "substantial"
    return "considerable"


def _group_n(group: Sequence[PaperQualityFingerprint]) -> int:
    values = [fp.n_total.value for fp in group if fp.n_total.value is not None]
    return int(mean(values)) if values else 0


def _mean_optional(values: Sequence[float | None]) -> float | None:
    concrete = [value for value in values if value is not None]
    return mean(concrete) if concrete else None


def _strengths_text(
    n_supporting: int,
    weighted_effect: float | None,
    i_squared: float | None,
    replication_rate: float | None,
) -> str:
    effect_text = "no pooled effect available" if weighted_effect is None else f"pooled effect {weighted_effect:.3f}"
    heterogeneity_text = "heterogeneity not estimable" if i_squared is None else f"I2 {i_squared:.1f}%"
    replication_text = (
        "replication rate not estimable"
        if replication_rate is None
        else f"replication coverage {replication_rate:.2f}"
    )
    return f"{n_supporting} supporting warrant(s); {effect_text}; {heterogeneity_text}; {replication_text}."


def _weaknesses_text(n_defeating: int, overlap_flagged: int, egger_applicable: bool) -> str:
    egger_text = (
        "Egger test applicable."
        if egger_applicable
        else "Egger test not reported because fewer than ten usable studies are available."
    )
    return f"{n_defeating} defeating warrant(s); {overlap_flagged} overlap-adjusted paper(s). {egger_text}"
