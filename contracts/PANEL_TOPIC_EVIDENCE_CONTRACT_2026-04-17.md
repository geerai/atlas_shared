# Panel Topic Evidence Contract

Date: 2026-04-17

## Claim

The student-facing questions are also topic definitions. The panel dossiers that
define central cases, clear rejections, hard cases, false friends, evidence
markers, and escalation triggers are evidence for shared classification. They
must not remain as prose-only artifacts for Google Scholar search.

## Canonical Artifacts

- Topic bank loader: `atlas_shared.topic_bank.load_topic_constitution_bank`
- Curated topic JSON: `atlas_shared/data/question_constitutions_curated_30.json`
- Panel dossiers: `docs/panels/SQ-*.md`
- Intake gate: `atlas_shared.intake.PreExtractionIntakeGate`
- Bundle router: `atlas_shared.bundle_router.QuestionBundleRouter`

## How Panel Fields Map Into Classification

- `Question`: human-readable topic inquiry and search framing.
- `Topic / Subtopic`: canonical routing label.
- `In-Criteria`: central acceptance cases.
- `Out-Criteria`: clear rejection cases.
- `Hard Cases`: edge-case and manual-review rules.
- `False Friends`: exclusion terms and high-confidence reject evidence.
- `Evidence Markers`: required or supporting evidence terms.
- `Article Type Guidance`: allowed, marginal, and rejected article types.
- `Escalation Triggers`: conditions requiring subscribed model adjudication.
- `Unresolved Ambiguities`: candidates for topic expansion or human review.

## Required Use

Any Atlas repo that performs article intake, topic routing, question relevance,
or article-type classification must consume the shared topic bank rather than
re-parsing panel markdown or creating local topic lists.

Repo-specific code may decide where results are stored. It may not change the
shared decision vocabulary or silently convert panel edge cases into rejects.

## Edge Case Principle

Hard cases are not noise. They are explicit classification knowledge.

If a paper matches hard-case language, unresolved ambiguity, or credible adjacent
topic evidence, the correct output is `edge_case`, `manual_review`,
`topic_expansion_candidate`, or `new_topic_candidate`, not `off_topic`.

## Process Tracking

Classification systems must record which topic constitution version was used.
At minimum, a stored fact should include:

- `question_id`
- `topic`
- `subtopic`
- `constitution_version`
- `panel_status`
- `source_question_bank`
- the intake or routing decision
- confidence
- reasons

This prevents future agents from reinventing the same topic boundaries from
scratch or consulting obsolete local folders.
