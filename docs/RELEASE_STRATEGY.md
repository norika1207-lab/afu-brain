# Release Strategy

## Public Positioning

**Afu Brain: The Local Brain For Tool-Using AI Agents**

Afu Brain turns private human memory, public cognition, and live simulation
feedback into safe agent decisions before tools execute.

## Launch Lines

```text
The interface hears the human.
The brain remembers the life.
The executor acts only after MASL says it is safe.
```

```text
Hermes learns skills. Afu Brain decides when a skill must not run.
OpenClaw gives agents hands. Afu Brain gives them judgment.
```

```text
Models can propose.
Tools can act.
Afu Brain decides whether action should happen at all.
```

```text
Open-source agents already have hands.
What they lack is a trained decision brain between language and action.

In our live pilot across Gemini, GPT, and Sonnet:
900 live decisions requested.
5 unsafe raw model decisions.
0 unsafe executions after Afu Brain / Lobster Brain.
8 live decision-simulation arenas producing pressure-tested lessons.
```

## First-Viewport GitHub Story

The README should make three things obvious in the first screen:

- Afu / Alfred is the zero-interface human memory layer.
- Afu Brain / Lobster Brain is the model-agnostic MASL decision layer.
- OpenClaw is the executor that only acts after the gate approves.

The demo should be the visual hook:

```text
https://charenix.com/static/alfred-lobster-brain-demo.html
```

The evidence table should appear before long architecture detail. People should
see immediately that this is not only a pretty dashboard.

## What to Open Source First

- deterministic MASL gate
- policy ontology
- schemas
- AgentSkill entry point
- OpenClaw adapter contract
- sample RAG pack
- sample observatory feed
- safe demo cases
- benchmark harness
- public evidence summary

## What to Keep Private

- owner memory exports
- production DBs
- model/API keys
- voice assets
- private logs
- hosted service credentials

## Why Open Source

Each component could be a separate product. Open source makes the architecture
legible as a new standard:

```text
private memory + shared brain + safe execution
```

The open core builds trust by making the safety boundary and decision contract
inspectable. Private deployments can extend the same contract without exposing
owner memory, production logs, or deployment-specific strategy.

## Claims Discipline

Use strong but precise claims:

- 900-decision live pilot
- 5 unsafe raw model decisions
- 0 gated unsafe executions
- dry-run 1000/1000 passed
- 450/450 unsafe dry-run cases blocked
- memory routing improved from 33.3% to 93.3%

Avoid claiming real-world proof, peer review, unbiased benchmarks, or universal
OpenClaw safety until those studies exist.
