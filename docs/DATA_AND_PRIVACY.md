# Data and Privacy Model

Afu Brain separates private human memory from shared cognition.

## Private by Default

The following data belongs to the owner and must stay in the owner's deployment
unless they explicitly export it:

- calendar events
- contacts and relationship graph
- files and document contents
- email/message content
- location history
- health or family context
- personal preferences and corrections
- API keys and auth tokens

Public Afu Brain releases must never include real owner data.

## Shared by Design

The following data can be shared as an upgrade layer:

- MASL policy updates
- intent ontology improvements
- risk taxonomy changes
- skill routing rules
- benchmark results
- anonymized failure cases
- RAG seed entries that contain no private owner data
- cognition parameters learned from public simulation environments

## Observatory Mode

Users may opt in to receive daily brain upgrades from the public observatory.

They may also opt in to submit anonymized feedback:

```json
{
  "decision_id": "local-random-id",
  "intent": "contract",
  "risk": "high",
  "decision": "ask",
  "owner_feedback": "right",
  "private_content": "[redacted]"
}
```

The observatory should accept only redacted decision metadata, not raw private
messages or files.

## Disconnect Mode

Users can disconnect the public feed and train their own local brain:

```text
AFU_BRAIN_FEED_URL=
AFU_BRAIN_MODE=local
```

In disconnected mode, Afu Brain still works with local policies and local owner
memory. It simply stops inheriting public observatory upgrades.

## Export Rule

Any export must pass through a redaction layer:

- remove direct identifiers
- remove raw file text
- remove raw messages
- remove exact locations
- remove keys/tokens/secrets
- keep only intent, risk, decision, policy version, skill route, and feedback

