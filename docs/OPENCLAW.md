# OpenClaw Integration

OpenClaw is treated as the executor. Afu Brain is the decision layer before the
executor.

It also provides a behavior-proof pattern for OpenClaw-style memory, gateway,
skill, and safety changes:

```text
parameter/state at T
  -> OpenClaw-visible behavior at T+1
  -> inspectable proof that the change affected later behavior
```

See [`ROLLING_COGNITION_AUDIT.md`](ROLLING_COGNITION_AUDIT.md) for the public
lagged parameter-to-behavior audit.

## Principle

OpenClaw receives constrained plans, not raw ambiguous human intent.

```text
owner request
  -> Afu Brain decision
  -> OpenClaw constrained plan
  -> execution result
  -> owner feedback
```

## Plan Shape

```json
{
  "mode": "dry_run",
  "allowed": false,
  "allowed_preparation": true,
  "required_confirmation": true,
  "skills": ["files.read", "contract.red_flags"],
  "blocked_final_action": "external_send"
}
```

## Executor Rules

- Respect `allowed=false`.
- Run only listed skills.
- Do not infer extra tools from the original user request.
- Do not perform `blocked_final_action`.
- Return structured result and side effects.
- Let Afu Brain update memory from owner feedback.

## Behavior Proof for OpenClaw Changes

When an OpenClaw-compatible integration changes memory retrieval, session
lifecycle, channel routing, skill dispatch, or safety policy, the strongest
evidence is not only a unit test. It is a behavior audit:

- What parameter changed?
- Which later behavior window should improve?
- Did the agent become less repetitive, safer, more direct, or more grounded?
- Can the proof be shared without exposing raw private logs?

Afu Brain's public audit format is designed for that exact review loop.

## File Vault Tools

File search is preparation, not final execution.

```json
{
  "intent": "file_search",
  "decision": "ask",
  "allowed_preparation": true,
  "required_confirmation": true,
  "skills": ["vault.search", "vault.rank", "vault.audit"],
  "blocked_final_action": "external_file_action"
}
```

OpenClaw may search a local vault index and return ranked candidates. It must
ask before opening an external file, sending, sharing, deleting, moving, or
fetching provider-hosted private content.
