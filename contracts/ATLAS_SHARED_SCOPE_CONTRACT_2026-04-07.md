# ATLAS Shared Scope Contract

## Purpose

This repo is the narrow shared-library layer for Atlas.

Its task is to hold reusable contracts and portable logic used by more than one repo.

## Good Citizens

- question constitutions
- article-type labels and lightweight classifiers
- relevance decisions
- article-bundle models
- tiny normalizers and validators

## Bad Citizens

- extraction orchestration
- web server code
- UI code
- repo-specific DB services
- heavyweight model clients
- operational scripts

## Initial Export

- `atlas_shared.relevance`
- `atlas_shared.intake`
- `atlas_shared.topic_bank`
- `atlas_shared.classifier_system`

## Governing Principle

If a module cannot be imported and tested without one particular repo's runtime,
it does not belong here.

## Canonical identity field

The canonical article-identity field in `atlas_shared` is `paper_id`.
All shared dataclasses, routing results, intake records, and registry facts
use `paper_id` at the package boundary.

Consumer repos may alias this to `article_id` in their own APIs or UI copy.
But when crossing the `atlas_shared` boundary, the canonical name is
`paper_id`.
