# Adaptive Classifier Subsystem Contract

Date: 2026-04-18

## Purpose

Atlas needs one canonical paper-classification subsystem that can operate across
multiple evidence levels.

It must not assume that a paper always arrives with the same information. In one
case it may have only a title. In another it may have title, abstract, and
keywords. In another it may have a local PDF path but no abstract. In a later
stage it may also have methods summaries, science summaries, independent and
dependent variables, and operationalization fields.

The canonical implementation lives in:

`atlas_shared.classifier_system.AdaptiveClassifierSubsystem`

## Governing Distinctions

The subsystem must keep these distinctions explicit:

1. **Evidence stage**
   This is how much trustworthy information is available about one paper.

2. **Stable topic bank**
   This is the panel-derived constitutional evidence base. It is the default
   Atlas topic boundary source.

3. **Active topic overlay**
   This is a temporary or operational topic list that a caller wants to test in
   the current run. It may be narrower, broader, or differently named than the
   stable topic bank.

4. **Analysis pass**
   This is a classifier action run over the available evidence. The same
   evidence stage may support multiple analysis passes.

## Evidence Stages

Allowed evidence stages:

- `bibliographic_only`
- `metadata_text`
- `pdf_surface_light`
- `extraction_aware`

### `bibliographic_only`

Allowed inputs:

- `paper_id`
- title
- DOI
- filename
- authors
- year
- Zotero tags or equivalent source tags

At this stage the subsystem may:

- guess article type weakly
- score likely domain fit weakly
- recommend the next evidence-gathering action

At this stage it must not make hard exclusion decisions solely from missing
information.

### `metadata_text`

Adds:

- abstract
- keywords
- short source notes

At this stage the subsystem may:

- run article-type classification
- run constitutional relevance against the stable topic bank
- run active-topic-overlay matching
- produce a conservative intake recommendation

### `pdf_surface_light`

Adds one or more of:

- first-page text
- quick PDF text extraction
- rough OCR output
- section headings
- short intro/methods/conclusion snippets

If a PDF path or bytes are available and confidence remains low, the subsystem
may create this evidence itself by invoking a lightweight surface extractor.

The surface extractor must prefer:

1. native text extraction
2. lightweight OCR fallback only when native extraction fails or is empty

The light surface extractor is allowed to gather:

- first 1 to 4 pages of text
- section headings
- abstract candidate
- intro opening
- methods opening
- conclusion or discussion opening

It is not a full extraction step and must remain cheap.

### `extraction_aware`

Adds one or more of:

- methods surface summary
- science summary
- independent variables
- dependent variables
- measurement terms
- instrument terms
- sensor terms
- topic hints

At this stage the subsystem may refine:

- article type
- constitutional relevance
- stable topic routing
- active topic overlay fit

## Analysis Passes

The subsystem may run these passes when evidence permits:

- article-type classification
- conservative intake recommendation
- constitutional question relevance
- stable-topic bundle routing
- active-topic-overlay matching
- optional adjudication for borderline cases

The subsystem must record which passes were run.

## Stable Topic Bank

The default stable topic source is:

`atlas_shared.topic_bank.load_topic_constitution_bank()`

The stable topic bank is panel-derived evidence. It is not merely a search-prompt
library.

## Active Topic Overlay

The subsystem must accept a caller-supplied active topic list distinct from the
stable topic bank.

An active topic overlay entry may contain:

- `topic_id`
- `label`
- `description`
- `keywords`
- `inclusion_terms`
- `exclusion_terms`
- `source`

Overlay matching must be reported separately from stable topic routing.

## Output Contract

The subsystem must return one canonical result object with at least:

- inferred `evidence_stage`
- `available_evidence_types`
- `article_type`
- `intake_result` when applicable
- `question_summary`
- `stable_topic_routing`
- `active_topic_matches`
- `surface_snapshot` when created or supplied
- `analysis_steps_run`
- `next_action`
- `needs_more_evidence`

## `next_action` Vocabulary

Allowed next-action values:

- `need_abstract_or_keywords`
- `extract_pdf_surface`
- `review_borderline_case`
- `ready_for_intake_decision`
- `ready_for_downstream_extraction`
- `ready_for_topic_routing`

## Anti-Reinvention Rule

Article Finder, Article Eater, and Knowledge Atlas should use this shared
subsystem or its shared primitives rather than each defining new local
first-pass article-type and topic-fit logic.

Repo-local code may still provide:

- registry sinks
- lifecycle logging
- embedding taxonomy scorers
- UI presentation
- queue orchestration

But those repo-local pieces should adapt to this subsystem's contract rather
than redefining the evidence stages or decision vocabulary.

## Boundary With Other Classifiers

This subsystem does not replace every classifier already in Atlas.

- `PreExtractionIntakeGate` remains the narrow conservative first gate.
- The embedding centroid classifier in Article Finder remains a separate topic
  taxonomy scorer.
- Repo-local orchestration may combine those outputs.

What changes is that there is now one canonical shared representation of:

- what evidence is available
- what evidence may be created cheaply
- which shared passes should run at that level
- what the next classification action should be
