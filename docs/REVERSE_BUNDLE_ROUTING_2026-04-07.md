# Reverse Bundle Routing

The question filter can indeed be used in reverse.

Instead of asking:

- "Is this paper relevant to this question?"

one may ask:

- "Which question bundles or topics best fit this paper?"

## Method

1. Take one article.
2. Score it against many question constitutions.
3. Reject constitutions whose out-criteria or false-friend criteria fire strongly.
4. Keep accepted and edge-case constitutions.
5. Aggregate those kept constitutions by topic.
6. Rank topics by:
   - accepted evidence
   - edge-case evidence
   - confidence
   - novelty and topic-expansion signals

## Decision Tree

At the level of one constitution, the tree is approximately:

1. If out-criteria fire strongly, reject.
2. If both the environment side and outcome side are satisfied, accept.
3. If only one side is satisfied, or a hard-case indicator fires, mark edge-case.
4. If nothing material fires, reject.

Then across many constitutions:

1. group kept results by topic
2. sum weighted evidence
3. choose the strongest topic as primary
4. keep the next strongest topics as alternatives rather than discarding them

## Why This Is Better Than Pure Taxonomy Matching

The taxonomy alone gives broad conceptual proximity.

The constitution bank gives:

- in-criteria
- out-criteria
- edge-case criteria
- false friends

That makes topic assignment less naive.

## Emergence Tracking

When the adjudicator marks an edge case as:

- `topic_expansion_candidate`
- `new_topic_candidate`

the router preserves that signal. This lets the system notice not merely a borderline article, but a possible broadening of an existing topic or the birth of a new one.
