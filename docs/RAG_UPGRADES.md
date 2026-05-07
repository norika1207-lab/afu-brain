# RAG Upgrade Packs

Afu Brain can ship RAG packs that improve routing and safety without shipping
private owner memory.

See [`RAG_PACKS.md`](RAG_PACKS.md) for the concrete v0.1 pack format, local
retriever, and privacy boundary.

## What a RAG Pack Contains

- examples of safe/unsafe intent routing
- approval-gate patterns
- schema-fit examples
- document risk checklists
- anti-template correction notes
- social-intelligence metric definitions
- benchmark failures and fixes

## What a RAG Pack Must Not Contain

- private owner documents
- raw user messages
- exact personal calendar data
- credentials
- proprietary voice assets
- unredacted production logs

## Pack Format

```json
{
  "pack_id": "contract-risk-2026-05",
  "version": "2026.05.07",
  "entries": [
    {
      "id": "contract-send-approval",
      "kind": "routing_example",
      "text": "If a contract task includes sending, signing, accepting, or forwarding, analyze first and require approval before external action.",
      "tags": ["contract", "legal", "approval", "irreversible"]
    }
  ]
}
```

## Nanomodel Direction

The long-term direction is to compress accumulated public observatory traces into
small local models. Until then, RAG packs and deterministic MASL policies can
already reduce expensive frontier-model calls by moving repeated decisions into
local memory and routing policy.
