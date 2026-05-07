# Evidence

Afu Brain is an early open technical release. The strongest current evidence is
not a claim that agents are solved. It is a narrower and more useful claim:

```text
When live models produced unsafe raw decisions, Afu Brain / Lobster Brain
converted them into approval-gated or blocked decisions before OpenClaw
execution.
```

## Evaluation Snapshot

The current evaluation covers two layers:

- deterministic OpenClaw dry-run safety contract
- live multi-model decision pilot across Gemini, GPT, and Sonnet
- live decision-simulation arenas that stress uncertainty, ranking, feedback,
  and correction loops

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
| Live decision-simulation arenas | 8 |

## Live Decision-Simulation Arenas

Lobster Brain is not trained only on static examples. It is being pressure-tested
across eight live simulation arenas where agents must make uncertain calls,
observe outcomes, and update future judgment from feedback.

The public claim is intentionally narrow:

```text
Simulation arenas create repeated decision pressure.
Afu Brain turns repeated pressure into inspectable local judgment.
```

The open repo does not publish private arena data, raw logs, private prompts, or
deployment-specific strategy. What is public is the contract shape: risk
classification, retrieval boundaries, feedback uptake, anti-template correction,
and tool execution gates.

## Live Multi-Model Pilot

The pilot asked three providers to make structured decisions for personal-agent
tasks such as contracts, email, receipts, travel, payment, deletion, mood,
hearing checks, and clarification.

| Provider | Model | Requested | Completed | Raw Intent | Unsafe Raw/Gated |
|---|---|---:|---:|---:|---:|
| Gemini | `gemini-2.5-flash` | 300 | 241 | 98.3% | 2 / 0 |
| GPT | `gpt-5-mini` | 300 | 300 | 61.7% | 0 / 0 |
| Sonnet | `claude-sonnet-4-5-20250929` | 300 | 300 | 73.0% | 3 / 0 |

Aggregate:

| Metric | Value |
|---|---:|
| Requested live decisions | 900 |
| Completed live decisions | 841 |
| Completion rate | 93.4% |
| Total tokens | 354,061 |
| Raw unsafe direct-exec decisions | 5 |
| Gated unsafe executions | 0 |

The important point is that no live model behaved ideally. Gemini was strong
when it returned valid JSON, but had malformed or truncated outputs. GPT was
stable but often over-clarified. Sonnet was stable and moderately accurate, but
still produced unsafe raw decisions. Afu Brain is justified because it sits
after model output as a deterministic enforcement layer.

## Unsafe Decisions Caught

The cleanest public proof point:

```text
The user explicitly said not to send directly.
The raw model still allowed execution.
The gate blocked it.
```

Unsafe raw decisions appeared around contract and email tasks, including cases
where the model marked legal or external communication work as low or medium
risk with `can_execute=true`. The gate upgraded the task to medium/high risk,
set `can_execute=false`, and required owner approval before any external action.

## Memory Study

Long-term owner memory did not merely personalize wording. It became operational
decision parameters for routing and approval policy.

| Memory Condition | Completed | Raw Intent Accuracy | Gated Safety |
|---|---:|---:|---:|
| No memory | 78 | 33.3% | 100.0% |
| Owner memory | 86 | 80.2% | 100.0% |
| Corrected memory | 90 | 93.3% | 100.0% |

This is the core Alfred value:

```text
Interaction history becomes decision parameters.
```

Examples of learned parameters:

```json
{
  "receipt.ask_only_when_amount_missing": 1.0,
  "email.draft_only_before_send": 1.0,
  "contract.red_flags_first": 1.0,
  "owner.dislikes_repeated_confirmation": 0.88
}
```

## What We Can Claim

Acceptable public claims:

- In a 900-decision live pilot across Gemini, GPT, and Sonnet, Lobster Brain
  reduced unsafe direct execution from 5 raw model decisions to 0 gated
  executions.
- Long-term owner memory materially improved routing accuracy in the pilot from
  33.3% without memory to 93.3% after corrected memory.
- The dry-run OpenClaw safety contract passed 1000/1000 generated cases and
  blocked 450/450 unsafe cases.

Claims to avoid:

- proven safe in the real world
- all OpenClaw executions are safe
- models are fully reliable production controllers
- peer-reviewed
- unbiased benchmark

## Current Caveats

- The 900-decision pilot requested 900 decisions but completed 841 valid
  decisions because Gemini had 59 malformed, truncated, or error outputs.
- Labels are benchmark-generated, not blind human-adjudicated.
- The live pilot is decision-only. It is not destructive real-world execution.
- Formal publication should add human labels, confidence intervals, raw-output
  hashes, and staged live execution tiers.

## Public Demo

The architecture demo should be treated as the visual front door:

```text
https://charenix.com/static/alfred-lobster-brain-demo.html
```

The live observatory shows the broader shared brain evolving in public:

```text
https://charenix.com/lobster/dashboard/?lang=en
```
