# RAG Packs

Afu Brain RAG packs are shared cognition packages for decision-making agents.
They are not raw memory dumps.

OpenClaw already has useful memory and RAG plugins. Afu Brain uses RAG for a
different layer: execution judgment.

```text
memory RAG:      what context should the agent remember?
Afu Brain RAG:  what decision policy should constrain execution?
```

## What Ships in v0.1

```text
rag-packs/
  masl-safety-v0.1.jsonl
  openclaw-decision-cases-v0.1.jsonl
  memory-parameter-examples-v0.1.jsonl
  battlenix-reasoning-seeds-v0.1.jsonl
```

These packs are public examples. They contain aggregate lessons, policy
patterns, and safe decision cases. They do not include private owner memory or
production database exports.

## Retrieval Layers

Use separate retrieval namespaces instead of one large mixed corpus:

| Layer | Use |
|---|---|
| Policy RAG | MASL rules, approval gates, unsafe action classes |
| Decision Case RAG | request -> decision -> allowed skills -> blocked action |
| Memory Parameter RAG | long-term preference as operational policy |
| Social Cognition RAG | interaction uptake, rejection, influence, correction |
| Battlenix Reasoning RAG | doubt, observation, counterexample, ordered reasoning |
| Evidence RAG | benchmark failures, fixes, and safety regressions |

## Local Demo

```bash
PYTHONPATH=packages python3 -m afu_brain.rag_demo
```

The reference retriever is lexical and dependency-free. Production deployments
can replace it with LanceDB, Qdrant, Chroma, sqlite-vec, BM25, rerankers, or an
OpenClaw memory plugin.

## Public Pack Item

```json
{
  "id": "masl-contract-approval-001",
  "pack": "masl-safety",
  "version": "0.1.0",
  "kind": "policy_rule",
  "intent": "contract",
  "risk": "high",
  "decision": "ask",
  "skills": ["files.read", "contract.red_flags", "approval.before_send"],
  "tags": ["contract", "legal", "approval", "openclaw", "masl"],
  "text": "Contract and legal-document tasks may be analyzed, summarized, and checked for red flags, but external sending, signing, accepting, or forwarding requires owner approval.",
  "lesson": "Legal context upgrades the task to high risk even when the request sounds like a summary.",
  "source": "lobster-observatory-aggregate",
  "weight": 1.0,
  "private_data": false
}
```

## Privacy Boundary

Public RAG packs must not contain:

- private owner documents
- raw personal messages
- API keys or credentials
- exact private calendars, contacts, addresses, or locations
- production DB dumps
- voice assets
- unredacted logs

Private deployments can build local packs from private data, but those packs
should not be published.

## Why RAG Before a Nano Model

RAG should come before distillation.

```text
Step 1: publish safe aggregate RAG packs
Step 2: run a local router with retrieved policy/cases
Step 3: collect repeated successful routes
Step 4: distill high-frequency behavior into a nano decision model
Step 5: keep RAG as the update and memory layer
```

This lets Afu Brain save expensive model calls immediately while keeping policy
updates inspectable.
