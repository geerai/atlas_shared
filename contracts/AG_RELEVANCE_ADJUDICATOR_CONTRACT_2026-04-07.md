# AG Relevance Adjudicator Contract

AG is to be treated as a local broker over subscribed models, not as a network API dependency.

## Purpose

The heuristic filter should handle the easy cases. AG should adjudicate only:

- borderline cases
- low-confidence cases
- cases where the constitution's hard-case criteria are triggered

## Invocation Contract

An AG command must:

1. read a plain-text prompt from `stdin`
2. return exactly one JSON object on `stdout`
3. exit with status `0` on success

If AG cannot adjudicate, it should exit non-zero or emit no JSON. In that case the caller falls back to the heuristic result.

## Required Output Shape

```json
{
  "verdict": "accept|edge_case|reject",
  "confidence": 0.0,
  "reasons": ["..."],
  "needs_manual_review": false,
  "source": "ag::<model-or-policy>",
  "edge_case_kind": "none|near_miss|topic_expansion_candidate|new_topic_candidate|undetermined",
  "novelty_signal": 0.0,
  "topic_expansion_candidate": false,
  "new_topic_candidate": false,
  "proposed_topic_label": "",
  "adjacent_topics": []
}
```

The novelty fields matter because edge cases are often where topic boundaries broaden or new topics begin to emerge.

## Architectural Principle

The filter should not know which subscribed model AG used.

That choice belongs to AG.

The filter asks only for a structured adjudication and receives only a structured adjudication.
