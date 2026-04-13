# AG Wrapper Command Spec

Chosen invocation:

```bash
/path/to/ag_wrapper question-relevance
```

This is sufficient for the current code.

## Why It Is Sufficient

The AF integration already accepts an arbitrary command array for AG adjudication.

Relevant path:
- [pipeline.py](/Users/davidusa/REPOS/Article_Finder_v3_2_3/eater_interface/pipeline.py)

The software does not require AG's internal CLI shape. It requires only a stable wrapper boundary.

## Contract

The wrapper must:

1. accept a single subcommand:
   - `question-relevance`
2. read the adjudication prompt from `stdin`
3. return exactly one JSON object on `stdout`
4. exit `0` on success
5. exit non-zero on failure

## Output JSON

The output must match the adjudicator contract in:
- [AG_RELEVANCE_ADJUDICATOR_CONTRACT_2026-04-07.md](/Users/davidusa/REPOS/atlas_shared/contracts/AG_RELEVANCE_ADJUDICATOR_CONTRACT_2026-04-07.md)

## Future Growth

This wrapper can later grow into something like:

```bash
ag broker --task question-relevance --json
```

without changing AF, provided the wrapper remains present and continues to support:

```bash
/path/to/ag_wrapper question-relevance
```

So the wrapper is the stable public boundary; AG's internals may evolve behind it.
