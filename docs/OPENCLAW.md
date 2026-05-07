# OpenClaw Integration

OpenClaw is treated as the executor. Afu Brain is the decision layer before the
executor.

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

