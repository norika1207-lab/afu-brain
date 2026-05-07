# MASL: Model-Agnostic Safety Layer

MASL is the safety pattern behind Afu Brain.

## Invariants

1. The LLM does not make irreversible decisions.
2. The safety gate is deterministic.
3. The gate is model-agnostic.
4. Reversible and irreversible actions are gated differently.

## Decision Contract

A model or parser may propose:

```json
{
  "intent": "email",
  "confidence": 0.86,
  "risk": "medium",
  "skills": ["email.search", "draft.reply"],
  "requested_final_action": "send_email"
}
```

The MASL gate returns:

```json
{
  "decision": "ask",
  "can_execute": false,
  "allowed_preparation": true,
  "blocked_final_action": "send_email",
  "required_confirmation": true
}
```

## Default Policy

- Unknown intent becomes `clarify`.
- Mood support does not route into tools.
- Payment and deletion are critical.
- Legal/contract actions are high risk.
- External communication may draft but must not send without approval.
- File read is usually reversible; file overwrite is not.
- Generated skills must match the current input schema before activation.

## Why Model-Agnostic

The safety claim is not that the model always classifies correctly. The claim is
that the gate refuses unsafe commitments even if the model is incomplete,
malformed, overconfident, adversarial, or replaced by another provider.

