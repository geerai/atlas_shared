from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal, Mapping, Protocol

if TYPE_CHECKING:
    from .article_types import ArticleTypeDecision
    from .bundle_router import BundleRoutingResult
    from .relevance import ArticleCandidate, QuestionConstitution, RelevanceAssessment


SchemaVersion = Literal[
    "v1",
    "pre_extraction_intake_v1",
]


@dataclass(frozen=True)
class RegistryFact:
    dimension: str
    label: str
    confidence: float | None = None
    schema_version: SchemaVersion = "v1"
    paper_id: str | None = None
    question_id: str | None = None
    bundle_id: str | None = None
    topic_label: str | None = None
    edge_case_kind: str | None = None
    novelty_signal: float | None = None
    details_json: Mapping[str, Any] = field(default_factory=dict)


class SupportsClassificationRegistry(Protocol):
    def record_article_type(self, article: "ArticleCandidate", decision: "ArticleTypeDecision") -> Any: ...

    def record_question_assessment(
        self,
        article: "ArticleCandidate",
        constitution: "QuestionConstitution",
        assessment: "RelevanceAssessment",
    ) -> Any: ...

    def record_question_summary(
        self,
        article: "ArticleCandidate",
        summary: Mapping[str, Any],
    ) -> Any: ...

    def record_bundle_routing(
        self,
        article: "ArticleCandidate",
        routing: "BundleRoutingResult",
    ) -> Any: ...
