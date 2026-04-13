from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Sequence


@dataclass(frozen=True)
class ArticleTypeDecision:
    value: str
    confidence: float
    source: str
    evidence: tuple[str, ...] = ()


class HeuristicArticleTypeClassifier:
    """
    Lightweight cross-repo article-type classifier.

    This is intentionally smaller than AE's richer classifier. It is meant to be
    portable and dependency-light, while still being good enough for intake and
    relevance gating.
    """

    TYPE_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
        (
            "meta_analysis",
            (
                r"\bmeta[- ]analysis\b",
                r"\beffect sizes?\b",
                r"\bforest plot\b",
                r"\bmeta-regress",
            ),
        ),
        (
            "systematic_review",
            (
                r"\bsystematic review\b",
                r"\bprisma\b",
                r"\binclusion criteria\b",
                r"\bexclusion criteria\b",
                r"\bliterature search\b",
            ),
        ),
        (
            "narrative_review",
            (
                r"\bnarrative review\b",
                r"\bliterature review\b",
                r"\bwe reviewed\b",
                r"\boverview of\b",
            ),
        ),
        (
            "protocol",
            (
                r"\bstudy protocol\b",
                r"\bprotocol for\b",
                r"\bregistered protocol\b",
                r"\bpre-registr",
            ),
        ),
        (
            "case_study",
            (
                r"\bcase study\b",
                r"\bsingle case\b",
                r"\bcase report\b",
            ),
        ),
        (
            "mixed_methods",
            (
                r"\bmixed methods?\b",
                r"\bqualitative and quantitative\b",
                r"\bconvergent design\b",
            ),
        ),
        (
            "qualitative_research",
            (
                r"\bqualitative\b",
                r"\binterviews?\b",
                r"\bthematic analysis\b",
                r"\bgrounded theory\b",
                r"\bethnograph",
            ),
        ),
        (
            "theoretical",
            (
                r"\btheoretical\b",
                r"\bconceptual framework\b",
                r"\bframework for\b",
                r"\bwe argue\b",
                r"\bmodel of\b",
            ),
        ),
        (
            "commentary",
            (
                r"\bcommentary\b",
                r"\beditorial\b",
                r"\bperspective\b",
                r"\bletter to the editor\b",
            ),
        ),
        (
            "empirical_research",
            (
                r"\bexperiment(?:al)?\b",
                r"\bparticipants?\b",
                r"\bn\s*=\s*\d+\b",
                r"\bp\s*[<=>]\s*\.?\d+\b",
                r"\banova\b",
                r"\bregression\b",
                r"\brandomi[sz]ed\b",
                r"\bresults\b",
                r"\bmethods\b",
            ),
        ),
    )

    def classify(
        self,
        *,
        abstract: str = "",
        title: str = "",
        keywords: Sequence[str] = (),
    ) -> ArticleTypeDecision:
        text = " \n".join(
            piece for piece in (title, abstract, " ".join(keywords)) if piece
        ).lower()

        if not text.strip():
            return ArticleTypeDecision(
                value="unknown",
                confidence=0.0,
                source="heuristic_classifier",
                evidence=("no title, abstract, or keywords available",),
            )

        best_type = "unknown"
        best_score = 0
        evidence: list[str] = []

        for article_type, patterns in self.TYPE_PATTERNS:
            matches: list[str] = []
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    matches.append(pattern)
            if len(matches) > best_score:
                best_type = article_type
                best_score = len(matches)
                evidence = [f"matched {pattern}" for pattern in matches]

        if best_type == "unknown":
            return ArticleTypeDecision(
                value="unknown",
                confidence=0.15,
                source="heuristic_classifier",
                evidence=("no article-type patterns matched",),
            )

        confidence = min(0.45 + 0.12 * best_score, 0.92)
        return ArticleTypeDecision(
            value=best_type,
            confidence=confidence,
            source="heuristic_classifier",
            evidence=tuple(evidence),
        )
