# Observatory Feed

Afu Brain can consume public shared-brain updates from a live observatory. Users
can disconnect this feed and train their own local brain.

## What the Feed May Include

- MASL policy updates
- intent ontology versions
- skill routing rules
- RAG seed entries
- benchmark results
- cognition parameter defaults
- anti-template and mode-collapse corrections
- social intelligence metric definitions
- live pilot evidence summaries
- rolling cognition audit summaries

## What the Feed Must Not Include

- private owner memory
- raw personal messages
- private files
- API keys
- auth tokens
- production database dumps
- voice clone assets

## Update Contract

Each feed item should include:

```json
{
  "feed_version": "2026.05.07",
  "kind": "policy_update",
  "id": "contract-red-flags-before-send",
  "summary": "Contract tasks may analyze first but require approval before external send.",
  "applies_to": ["contract", "email"],
  "risk": "high",
  "source": "lobster-observatory",
  "created_at": "2026-05-07T00:00:00Z"
}
```

## User Control

Users should be able to choose:

- subscribe to public feed
- pin a known feed version
- disconnect entirely
- use local-only policies
- publish their own feed

## Evidence Items

Benchmark and pilot items may be shared as aggregate evidence. They must not
include raw owner data, private messages, provider credentials, or production DB
exports.

Example:

```json
{
  "kind": "benchmark_result",
  "id": "lobster-brain-live-pilot-900",
  "summary": "900 live decisions were requested across Gemini, GPT, and Sonnet; 5 raw unsafe direct-exec decisions became 0 gated unsafe executions.",
  "payload": {
    "requested_decisions": 900,
    "completed_decisions": 841,
    "raw_unsafe_direct_exec": 5,
    "gated_unsafe_executions": 0
  }
}
```

Rolling cognition audit items should follow the same boundary. They may include
parameter names, aggregate row counts, lagged correlations, sanitized panel
metrics, and report URLs. They must not include raw conversations or one-on-one
chat text.
