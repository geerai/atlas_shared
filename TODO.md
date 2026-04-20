# Atlas Shared TODO

## Panel Coverage Expansion

- [ ] Inventory every Atlas topic currently used by Article Finder, Article Eater, Knowledge Atlas, and course-facing question banks.
- [ ] Compare that inventory against `src/atlas_shared/data/question_constitutions_curated_30.json`.
- [ ] Identify topics without panel dossiers in `docs/panels/`.
- [ ] Generate or commission panel dossiers for uncovered topics, using the existing SQ panel format: in-criteria, out-criteria, hard cases, false friends, evidence markers, article-type guidance, escalation triggers, and unresolved ambiguities.
- [ ] Promote each completed dossier into the curated topic constitution bank so intake, topic routing, edge-case detection, and novelty handling all use the same evidence base.
- [ ] Add tests that fail when a canonical topic has no corresponding topic constitution or panel evidence record.

The goal is full topic coverage: no active Atlas topic should depend on an implicit local classifier, an old folder, or an undocumented agent judgment.
