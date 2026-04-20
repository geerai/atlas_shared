# Pre-Extraction Intake Contract

Date: 2026-04-17

## Purpose

Article Finder and Article Eater must share one conservative first gate for newly
arrived PDFs. This gate decides whether a paper is an intake candidate, an edge
case, a metadata hold, a manual-review case, or a clear false positive. It is not
a V7 extraction step and must not use dependent variables, independent variables,
measures, sensors, claims, or other Article Eater extraction outputs.

The canonical implementation is:

`atlas_shared.intake.PreExtractionIntakeGate`

The canonical topic evidence source is:

`atlas_shared.topic_bank.load_topic_constitution_bank()`

## Allowed Inputs

The gate may use only information available before Article Eater extraction:

- `paper_id`
- title
- abstract
- filename
- DOI
- Zotero tags
- author keywords
- first-page text or arrival-time OCR when available
- preliminary article-type label when supplied by the source
- PDF hash and source metadata

The gate must treat missing abstracts and missing first-page text as a metadata
problem, not as evidence of irrelevance.

## Required Outputs

The gate must return a `PreExtractionIntakeResult` with these fields:

- `intake_decision`
- `routing_target`
- `domain_relevance`
- `article_type`
- `confidence`
- `needs_manual_review`
- `reasons`
- `primary_topic`
- `primary_bundle_id`
- `topic_candidates`
- `matched_question_ids`
- `edge_case_kind`
- `novelty_signal`
- `topic_expansion_candidate`
- `new_topic_candidate`
- `proposed_topic_label`
- `adjacent_topics`
- `facts`

The `facts` field must contain registry-ready `RegistryFact` records, including
at least:

- `article_type_preliminary`
- `pre_extraction_intake_decision`

When a topic is routed, it should also contain `topic_routing_preliminary`. When
novelty is detected, it should also contain `novelty_preservation`.

## Decision Vocabulary

Allowed `intake_decision` values:

- `accept_candidate`
- `edge_case`
- `needs_abstract`
- `needs_pdf_text`
- `manual_review`
- `reject_clear_false_positive`

Allowed `routing_target` values:

- `article_eater`
- `manual_review`
- `hold_for_metadata`
- `reject`

## Rejection Rule

The gate must be conservative. It may emit `reject_clear_false_positive` only
when all of the following are true:

- substantive pre-extraction metadata exists
- clear false-positive evidence is present
- no Atlas built-environment, human-response, topic, or novelty signal is present

The absence of an existing topic is never sufficient reason to reject a paper.

## Novelty Rule

If a paper has credible Atlas-domain signals but does not fit an existing topic
constitution, the gate must preserve it as `edge_case` or `manual_review`.

It must set one or both of:

- `topic_expansion_candidate`
- `new_topic_candidate`

It must also provide `proposed_topic_label` when it can derive one from the
title, keywords, or domain signals.

## Panel Evidence Rule

The panel dossiers and curated question constitutions are part of the evidence
base for the module. They are not merely instructions for Google Scholar search.

Student-facing questions should be treated as topic constitutions:

- `question_text` preserves the question wording.
- `topic` and `subtopic` define the operational topic boundary.
- `in-criteria` become acceptance indicators.
- `out-criteria` and false friends become exclusion terms.
- hard cases and escalation triggers become edge-case indicators.
- evidence markers become required or supporting evidence terms.

Article Finder should load the shared topic bank and use it for first-pass
intake, edge-case preservation, and routing. Article Eater should store the
resulting facts as provenance and should not reinterpret the panel files with a
separate local classifier.

## Process Tracking

Every intake decision must be representable as registry facts. Downstream
systems should store these facts in their process ledger or classification
registry rather than inventing local table formats.

Article Finder should use the intake result to populate its operational routing
fields. Article Eater should treat the result as provenance and should not rerun
a separate first-gate classifier.

## Anti-Reinvention Rule

Agents working in Article Finder, Article Eater, or Knowledge Atlas must import
the shared intake gate from `atlas_shared` rather than creating a new local
first-pass relevance classifier. Repo-specific code may orchestrate when the
gate runs and where facts are stored; it must not redefine the decision
vocabulary or rejection rule.
