# Literature-Body Quality Contract

Date: 2026-04-23

Canonical implementation:

`atlas_shared.literature_body.aggregate_literature_body_quality`

## Scope

This contract defines a pure aggregation layer over paper-quality fingerprints
for topic-level literature bodies. It gives Knowledge Atlas a stable structure
for reporting the maturity, openness, and replication coverage of a set of
papers without embedding database or UI assumptions in the shared package.

## Inputs

The aggregator accepts:

- a `topic_id`
- a sequence of `PaperQualityFingerprint` objects
- optional paper IDs from replication-registry sources

## Outputs

The aggregator returns `LiteratureBodyQuality` with five required summary
statistics:

- preregistration fraction
- design-weighted median sample size
- median effect-size confidence-interval width by metric
- replication-coverage fraction
- open-data-availability fraction

## Success Conditions

The function must be deterministic, must not read or write a database, and must
return `None` rather than invented values when a statistic has no usable input.

## Non-Promises

This contract does not define topic membership, replication-registry ingestion,
claim-level warrant logic, or final UI presentation. Those are downstream
responsibilities.

## Test Coverage

`tests/test_literature_body.py` uses a synthetic ten-paper fixture and asserts
all five required statistics.

## References

- `docs/PAPER_QUALITY_SYSTEM_DESIGN_2026-04-23.md` §6.
- Knowledge Atlas `contracts/schemas/paper_quality.sql`.
