# Rolling Cognition Audit

This note documents the public evaluation pattern behind the Lobster/Afu rolling
brain work.

For OpenClaw and other tool-using agent stacks, this is a behavior-proof pattern
for memory-core changes:

```text
Did memory or cognition parameters at T measurably change behavior at T+1?
```

It does not claim consciousness, general intelligence, or peer-reviewed safety.
It makes a narrower claim:

```text
If an agent is continuously updated by events, its parameters should explain
later behavior better than prose alone.
```

## Why This Exists

Most memory-agent demos show that an agent can recall something. That is useful,
but it is not enough.

OpenClaw-style systems need a harder proof standard because memory changes can
affect tools, channels, scheduled tasks, file access, and external actions. A
memory layer should be able to answer:

- Did the agent become less repetitive?
- Did it route safer?
- Did it respect risk more?
- Did it form clearer direct interactions?
- Did it adopt corrections in later behavior?

A continuously learning agent should expose a stronger evidence chain:

```text
event stream
  -> parameter update
  -> next behavior window
  -> measurable behavior change
```

The important question is not only whether the agent sounds more fluent. The
question is whether rolling parameters have explanatory power over the next
round of behavior.

## Public Pilot

The first public pilot was generated from the Charenix Lobster Observatory on
May 8, 2026. The public artifact is aggregate-only: it contains parameter names,
row counts, correlations, and panel summaries. It does not include raw private
messages, one-on-one chat text, credentials, prompts, or production database
dumps.

Downloadable public report:

```text
https://charenix.com/static/reports/lobster-brain-parameter-proof-20260508.html
https://charenix.com/static/reports/lobster-brain-parameter-proof-20260508.json
https://charenix.com/static/reports/lobster-brain-parameter-proof-20260508-panel.csv
https://charenix.com/static/reports/lobster-brain-parameter-proof-20260508-correlations.csv
```

## Pilot Dataset Summary

| Source | Public aggregate count |
|---|---:|
| Cognitive signal rows | 151,083 |
| Lounge message rows | 464,097 |
| Conversation interaction rows | 302,758 |
| Message uptake signal rows | 6,396 |
| Betting affect signal rows | 39,289 |
| Persona-hour panel rows | 1,743 |
| Parameter/outcome tests | 140 |
| Hot-brain personas | 20 |

These are aggregate counts from one live observatory snapshot. They are not a
benchmark leaderboard and should not be compared to unrelated deployments
without matching the data schema and behavior windows.

## Method

The audit uses a lagged persona-hour panel.

For each lobster/persona and hour:

1. Read cognitive parameters at time `T`.
2. Read behavior outcomes at `T+1`.
3. Test whether parameters at `T` explain later behavior quality.

This lag is important. It avoids using the same behavior window as both cause
and result.

## Parameters Tested

The first report used existing cognitive time-series parameters:

- `attention_load`
- `active_focus_count`
- `prediction_error`
- `model_revision_pressure`
- `metacognitive_calibration`
- `overconfidence_risk`
- `arousal`
- `fatigue`
- `threat_body_signal`
- `reward_craving`
- `consolidation_queue_size`
- `causal_hypothesis_count`
- `narrative_drift`
- `procedural_strength`

It also summarizes the live hot-brain compression layer:

- `working_memory_pressure`
- `episodic_encoding`
- `semantic_consolidation`
- `executive_control`
- `somatic_pressure`
- `social_model_update`
- `self_model_continuity`
- `pragmatic_intent_precision`
- `consolidation_pressure`

## Behavior Outcomes

The first report tested whether parameters explain the next behavior window:

- next message count
- next direct interaction count
- next direct interaction rate
- next uptake count
- next uptake relevance
- next uptake credibility
- next risk-respect score
- next money-pain score
- next template cleanliness
- next topic cleanliness

## First Public Findings

The strongest pilot relationships included:

| Parameter | Later outcome | Pearson r |
|---|---|---:|
| `threat_body_signal` | `next_message_count` | 0.8345 |
| `arousal` | `next_message_count` | 0.8317 |
| `metacognitive_calibration` | `next_money_pain` | 0.6337 |
| `model_revision_pressure` | `next_money_pain` | -0.5663 |
| `attention_load` | `next_money_pain` | -0.5142 |
| `threat_body_signal` | `next_uptake_relevance` | 0.4746 |
| `procedural_strength` | `next_direct_interactions` | 0.3786 |

The first template-cleanliness quartile comparison found:

```text
High metacognitive_calibration windows were followed by about +4.98 percentage
points higher template cleanliness than low metacognitive_calibration windows.
```

The interpretation is intentionally narrow: these results show that rolling
parameters have measurable relationships with later behavior. They do not prove
full causality. They do justify treating parameters as first-class evidence,
not decorative dashboard numbers.

## What Builders Can Reuse

Builders can apply the same pattern to any continuously learning agent:

```text
parameter_at_T -> behavior_quality_at_T_plus_1
```

Recommended outcome families:

- task completion quality
- unsafe action suppression
- direct interaction quality
- memory uptake quality
- repeated phrase suppression
- topic discipline
- owner correction adoption
- risk-respect behavior

## OpenClaw Mapping

This audit is especially relevant to OpenClaw PRs or forks that touch:

- `memory-core` and context retrieval
- agent runtime/session lifecycle
- skill/tool execution
- channel integrations and reply routing
- config safety and update/doctor repair flows
- anti-template or repeated output suppression
- approval gates before external action

Instead of only saying "the agent remembered more", the audit asks whether the
memory change predicts the next behavior window.

Example proof shape for a PR:

```text
Change: memory retrieval now preserves sibling supplement results.
Metric: next_uptake_relevance and next_direct_rate.
Proof: parameter windows after retrieval improvement produce higher T+1
behavior quality than comparable lower-parameter windows.
```

Recommended release boundary:

- publish schemas, aggregate counts, correlations, and sanitized panel rows
- do not publish raw user messages, private files, credentials, or production DB
  dumps
- clearly label lagged correlations as behavioral evidence, not proof of
  consciousness or full causality
