# atlas_shared

Shared contracts and lightweight decision logic for the Atlas system.

This repo is for code that genuinely belongs to more than one Atlas repo.

It should contain:

- stable dataclasses and schemas
- conservative pre-extraction intake gates
- panel-derived topic constitutions
- question constitutions
- article-type vocabularies
- question/article relevance logic
- article-bundle logic
- small bibliographic normalizers

It should not contain:

- Article Finder orchestration
- Article Eater extraction pipeline code
- Knowledge Atlas page logic
- repo-specific database access
- heavyweight runtime dependencies

Initial module:

- `atlas_shared.relevance`
- `atlas_shared.intake`
- `atlas_shared.topic_bank`
- `atlas_shared.classifier_system`

That module supports:

1. article-type classification
2. question constitution parsing
3. relevance assessment
4. question-level article bundles
5. pre-extraction PDF intake that preserves adjacent and novel-topic papers
6. loading panel-derived topic constitutions as a shared evidence base
7. staged evidence-aware classification across bibliographic, metadata, light-PDF, and extraction-aware evidence levels
8. active topic overlays kept distinct from the stable panel-derived topic bank

The first gate for newly arrived PDFs is `atlas_shared.intake.PreExtractionIntakeGate`.
It may use only arrival-time metadata, abstracts, keywords, tags, and first-page
text. It must not depend on Article Eater extraction outputs. It rejects only
clear false positives; plausible but unclassified papers become `edge_case` or
`manual_review` records with classification facts that downstream registries can
persist.

The panel dossiers and curated constitution JSON are evidence for topic
boundaries, not merely prompts for Google Scholar. Use
`atlas_shared.topic_bank.load_topic_constitution_bank()` to load them, then pass
`bank.constitutions` into the intake gate or bundle router.

For the broader staged subsystem, use
`atlas_shared.classifier_system.AdaptiveClassifierSubsystem`.
It accepts uneven evidence, may create a cheap PDF surface when a local PDF is
available, and reports both stable-topic routing and active-topic-overlay
matches without conflating them.
