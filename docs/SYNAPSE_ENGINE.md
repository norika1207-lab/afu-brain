# Afu Brain Synapse Engine

Don’t rent intelligence every time. Grow a brain that knows you.

The synapse engine is the first executable reference for Afu Brain as a local,
owner-aware cognition layer. It does not try to be a giant general model. It
turns memory, public RAG lessons, repeated language checks, and MASL policy into
an inspectable brain decision before OpenClaw can execute tools.

## What It Proves

Afu Brain is not only numeric routing. Every decision exposes meaning:

- what the owner asked for
- what hidden risk or pressure was detected
- which OpenClaw action is allowed, gated, or blocked
- which public cognition pack influenced the decision
- which synapse parameters changed and why
- whether a frontier teacher is needed before local distillation
- whether the generated reply is safe to publish or too repetitive

## Decision Contract

The reference contract is `BrainDecision`.

```text
owner request
  -> MASL / OpenClaw gate
  -> public RAG retrieval
  -> meaning trace
  -> synapse update
  -> style and publication gate
  -> local/frontier route
```

The output is schema-backed in `schemas/brain_decision.schema.json`.

## Demo

Run:

```bash
PYTHONPATH=packages python3 -m afu_brain.evolution_demo
```

Machine-readable output:

```bash
PYTHONPATH=packages python3 -m afu_brain.evolution_demo --json
```

The demo includes:

- approval-aware contract review
- repeated phrasing suppression before publishing
- irreversible payment blocking

## Afu Model Path

The current engine is deterministic so builders can inspect the contract. A
future **Afu Model** does not replace the contract. It learns to emit the same
fields faster and more personally as a compact local decision brain:

- `meaning_trace`
- `synapse_updates`
- `style_contract`
- `publication_gate`
- `route`

Large models become occasional teachers. The owner brain keeps the distilled
judgment locally.
