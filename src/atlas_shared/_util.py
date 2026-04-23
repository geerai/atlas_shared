from __future__ import annotations

from typing import Any, Sequence


def _split_terms(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return ()


def _assessment_weight(item: Any) -> float:
    if item.verdict == "accept":
        return 1.0 * item.confidence
    if item.verdict == "edge_case":
        return 0.45 * item.confidence
    return 0.0
