# Non-API Adjudicator Options

The adjudicator need not be an API client.

For Atlas, the cleaner arrangement is often:

- AF or AE performs the deterministic first pass.
- A local subscribed AI CLI performs the borderline adjudication.
- The CLI may be Codex, Claude Code, or an AG broker that selects among several models.

## Preferred Design

Use AG as the broker when available.

That means:

- the filter sends AG a structured adjudication prompt
- AG chooses the most suitable subscribed model
- AG returns strict JSON

The filter does not need to know whether the answer came from Claude, Codex, or some other subscribed model.

## Implemented Bridges

- `ShellCommandAdjudicator`
- `CodexCLIAdjudicator`
- `ClaudeCLIAdjudicator`

The shell-command bridge is the most general and is the right place to integrate AG.

There is now also a dedicated wrapper class:

- `AGCommandAdjudicator`
