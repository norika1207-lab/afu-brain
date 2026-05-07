# Afu Brain Launch

**Private memory. Shared cognition. Safe execution.**

Afu Brain is now open source:

```text
https://github.com/norika1207-lab/afu-brain
```

## One-Sentence Pitch

Agents already have hands. Afu Brain gives them judgment before execution.

## What It Is

Afu Brain is a model-agnostic safety and decision layer for agents that can use
tools.

```text
Alfred hears the human.
Afu Brain turns memory into decision parameters.
MASL blocks or approval-gates unsafe action.
OpenClaw executes only what survives the gate.
```

## Why It Exists

Tool-using agents can now touch files, email, browsers, contracts, payments,
deletion, and home automation.

Prompting alone is not enough once action becomes external or irreversible.

Afu Brain adds a deterministic gate after model output and before tool
execution.

## Current Evidence

Early pilot evidence:

| Evaluation | Result |
|---|---:|
| Dry-run generated cases | 1000 |
| Dry-run passed | 1000 / 1000 |
| Dry-run unsafe cases blocked | 450 / 450 |
| Live requested decisions | 900 |
| Live completed decisions | 841 |
| Live raw unsafe direct-exec decisions | 5 |
| Live gated unsafe executions | 0 |
| Memory routing improvement | 33.3% -> 80.2% -> 93.3% |

These are pilot results, not a peer-reviewed safety guarantee.

## Links

- GitHub: https://github.com/norika1207-lab/afu-brain
- Architecture demo: https://charenix.com/static/alfred-lobster-brain-demo.html
- Live observatory: https://charenix.com/lobster/dashboard/?lang=en
- Evidence: https://github.com/norika1207-lab/afu-brain/blob/main/docs/EVIDENCE.md

## What Feedback Would Help

- Is the decision contract clear enough for executor authors?
- Are the MASL safety boundaries strict enough?
- Which OpenClaw / desktop-agent adapters should come first?
- What examples would make local-first adoption easier?
