# Question Constitution LLM Workflow

## Principle

The constitution is not to be derived from keywords alone.

An LLM should draft each constitution from:

- the source question
- the topic and subtopic
- any existing search hints
- examples of plausible on-topic papers
- examples of plausible near misses

The draft must explicitly separate:

- in-criteria
- out-criteria
- hard-case criteria
- false friends
- evidence markers

## Minimal Prompt Pattern

Give the model:

- the question in plain language
- the intended topic
- a few likely positive examples
- a few likely negative examples
- the instruction to produce structured fields rather than prose only

Require output fields such as:

- `environment_terms`
- `outcome_terms`
- `exclusion_terms`
- `edge_terms`
- `accept_indicators`
- `reject_indicators`
- `edge_case_indicators`
- `required_evidence_terms`

## Human Panel Role

The panel should not start from a blank page if that can be avoided.

The sensible division is:

- LLM drafts the first constitution.
- The panel corrects the boundaries.
- The approved result enters the constitution bank.

## Intake Usage

At AF intake, the constitution filter should:

1. run the heuristic relevance pass
2. call an LLM adjudicator for borderline cases or low-confidence cases
3. then produce `send_to_eater`, `review`, or `reject`

That keeps LLM cost bounded while preserving better judgment at the boundary.
