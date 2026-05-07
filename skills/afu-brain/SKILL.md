---
name: afu-brain
description: Use Afu Brain as a MASL butler brain before executing OpenClaw or other agent tools. It turns private owner memory and human intent into safe decisions, skill routing, and approval gates.
version: 0.1.0
homepage: https://charenix.com
metadata: {"openclaw":{"homepage":"https://github.com/YOUR_ORG/afu-brain","requires":{"env":["AFU_BRAIN_ENDPOINT"]},"primaryEnv":"AFU_BRAIN_ENDPOINT"}}
---

# Afu Brain

Private memory. Shared cognition. Safe execution.

Use this skill before executing high-impact tools, generated skills, external
communication, deletion, payment, contract/legal workflows, or ambiguous owner
requests.

## Rule

Never execute irreversible actions directly from raw human language.

Ask Afu Brain for a decision first.

## Decision Flow

1. Send the owner request, available private memory summary, and proposed tool
   action to Afu Brain.
2. Receive `allow`, `ask`, or `block`.
3. Execute only if the decision is `allow`.
4. If the decision is `ask`, prepare reversible context and request owner
   confirmation.
5. If the decision is `block`, do not execute.
6. Write the result and owner feedback back to the brain.

## Environment

```text
AFU_BRAIN_ENDPOINT=http://127.0.0.1:8787
AFU_BRAIN_TOKEN=optional-local-token
```

## Example

Owner:

```text
Review the contract I uploaded. If there are red flags, do not send it without my approval.
```

Expected decision:

```json
{
  "intent": "contract",
  "risk": "high",
  "decision": "ask",
  "can_execute": false,
  "allowed_preparation": true,
  "blocked_final_action": "external_send",
  "skills": ["files.read", "contract.red_flags", "approval.before_send"]
}
```

