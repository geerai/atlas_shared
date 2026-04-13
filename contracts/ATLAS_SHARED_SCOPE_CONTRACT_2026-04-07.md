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

## Governing Principle

If a module cannot be imported and tested without one particular repo's runtime,
it does not belong here.
