# atlas_shared

Shared contracts and lightweight decision logic for the Atlas system.

This repo is for code that genuinely belongs to more than one Atlas repo.

It should contain:

- stable dataclasses and schemas
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

That module supports:

1. article-type classification
2. question constitution parsing
3. relevance assessment
4. question-level article bundles
