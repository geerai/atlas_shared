from __future__ import annotations

from dataclasses import dataclass
import json
from importlib import resources
from pathlib import Path
from typing import Any, Iterable, Mapping

from .relevance import QuestionConstitution


DEFAULT_CURATED_BANK = "question_constitutions_curated_30.json"
DEFAULT_STARTER_BANK = "question_constitutions_starter.json"


@dataclass(frozen=True)
class TopicConstitutionRecord:
    """
    One panel-derived topic constitution.

    The source question is retained because students and Scholar searches used
    the question wording, but the operational unit is the topic/subtopic
    boundary specified by the panel.
    """

    question_id: str
    question_text: str
    topic: str
    subtopic: str = ""
    panel_status: str = "draft"
    constitution_version: str = "v0"
    panel_markdown_path: str = ""
    source_question_bank: str = ""
    raw: Mapping[str, Any] | None = None

    @classmethod
    def from_mapping(cls, obj: Mapping[str, Any]) -> "TopicConstitutionRecord":
        return cls(
            question_id=str(obj.get("question_id") or obj.get("id") or ""),
            question_text=str(obj.get("question_text") or obj.get("question") or ""),
            topic=str(obj.get("topic") or ""),
            subtopic=str(obj.get("subtopic") or ""),
            panel_status=str(obj.get("panel_status") or "draft"),
            constitution_version=str(obj.get("constitution_version") or obj.get("version") or "v0"),
            panel_markdown_path=str(obj.get("panel_markdown_path") or ""),
            source_question_bank=str(obj.get("source_question_bank") or ""),
            raw=dict(obj),
        )

    @property
    def topic_key(self) -> str:
        if self.subtopic:
            return f"{self.topic} / {self.subtopic}"
        return self.topic

    def to_question_constitution(self) -> QuestionConstitution:
        return QuestionConstitution.from_panel_spec(self.raw or {})


@dataclass(frozen=True)
class TopicConstitutionBank:
    version: str
    records: tuple[TopicConstitutionRecord, ...]
    source_path: str = ""

    @classmethod
    def from_mapping(cls, obj: Mapping[str, Any], *, source_path: str = "") -> "TopicConstitutionBank":
        records = tuple(
            TopicConstitutionRecord.from_mapping(item)
            for item in obj.get("questions", [])
            if isinstance(item, Mapping)
        )
        return cls(
            version=str(obj.get("version") or "unknown"),
            records=records,
            source_path=source_path,
        )

    @property
    def constitutions(self) -> tuple[QuestionConstitution, ...]:
        return tuple(record.to_question_constitution() for record in self.records)

    @property
    def topics(self) -> tuple[str, ...]:
        return tuple(sorted({record.topic for record in self.records if record.topic}))

    def by_topic(self, topic: str) -> tuple[TopicConstitutionRecord, ...]:
        wanted = topic.strip().lower()
        return tuple(record for record in self.records if record.topic.lower() == wanted)

    def by_question_id(self, question_id: str) -> TopicConstitutionRecord | None:
        wanted = question_id.strip().lower()
        for record in self.records:
            if record.question_id.lower() == wanted:
                return record
        return None

    def panel_dossier_paths(self) -> tuple[str, ...]:
        return tuple(record.panel_markdown_path for record in self.records if record.panel_markdown_path)


def _read_packaged_json(name: str) -> Mapping[str, Any]:
    package_root = resources.files("atlas_shared")
    text = (package_root / "data" / name).read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, Mapping):
        raise ValueError(f"Topic constitution bank {name} must be a JSON object")
    return data


def load_topic_constitution_bank(path: str | Path | None = None) -> TopicConstitutionBank:
    """
    Load the panel-derived topic constitution bank.

    When no path is supplied, the curated 30-topic bank is preferred. If that is
    absent in a stripped install, the smaller starter bank is used.
    """

    if path is not None:
        source = Path(path)
        data = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(data, Mapping):
            raise ValueError(f"Topic constitution bank {source} must be a JSON object")
        return TopicConstitutionBank.from_mapping(data, source_path=str(source))

    try:
        data = _read_packaged_json(DEFAULT_CURATED_BANK)
        return TopicConstitutionBank.from_mapping(data, source_path=f"atlas_shared/data/{DEFAULT_CURATED_BANK}")
    except FileNotFoundError:
        data = _read_packaged_json(DEFAULT_STARTER_BANK)
        return TopicConstitutionBank.from_mapping(data, source_path=f"atlas_shared/data/{DEFAULT_STARTER_BANK}")


def load_question_constitutions(path: str | Path | None = None) -> tuple[QuestionConstitution, ...]:
    return load_topic_constitution_bank(path).constitutions


def topic_records_for_questions(
    question_ids: Iterable[str],
    *,
    bank: TopicConstitutionBank | None = None,
) -> tuple[TopicConstitutionRecord, ...]:
    active_bank = bank or load_topic_constitution_bank()
    records: list[TopicConstitutionRecord] = []
    for question_id in question_ids:
        record = active_bank.by_question_id(question_id)
        if record is not None:
            records.append(record)
    return tuple(records)
