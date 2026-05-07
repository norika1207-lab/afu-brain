<p align="center">
  <img src="assets/lobster-observatory.png" alt="Afu Brain and Lobster Observatory public cognition surface" width="100%">
</p>

<h1 align="center">Afu Brain</h1>

<p align="center">
  <strong>Private memory. Shared cognition. Safe execution.</strong>
</p>

<p align="center">
  An OpenClaw-compatible, model-agnostic safety and decision brain for agents that can use tools.
  Alfred listens, Afu Brain decides, OpenClaw executes only what survives the gate.
</p>

<p align="center">
  <a href="https://charenix.com/static/alfred-lobster-brain-demo.html"><strong>Architecture Demo</strong></a>
  ·
  <a href="https://charenix.com/lobster/dashboard/?lang=en"><strong>Live Observatory</strong></a>
  ·
  <a href="docs/EVIDENCE.md"><strong>Evidence</strong></a>
  ·
  <a href="docs/MASL.md"><strong>MASL</strong></a>
  ·
  <a href="docs/OPENCLAW.md"><strong>OpenClaw</strong></a>
  ·
  <a href="docs/RAG_PACKS.md"><strong>RAG Packs</strong></a>
  ·
  <a href="LAUNCH.md"><strong>Launch</strong></a>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-open%20technical%20preview-111827">
  <img alt="Safety" src="https://img.shields.io/badge/MASL-model--agnostic%20safety-0f766e">
  <img alt="Memory" src="https://img.shields.io/badge/memory-local--first-7c3aed">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2563eb">
</p>

## The Problem

Open-source agents already have hands: tools, browsers, files, shells, cameras,
microphones, APIs, and home automation.

What they usually lack is judgment before execution.

If an agent can send email, review contracts, delete files, start payments, or
control a home environment, prompt instructions are not enough. The system needs
a deterministic layer after model output and before irreversible action.

## What Afu Brain Is

Afu Brain is an OpenClaw-compatible MASL butler brain for personal agents. It
turns private human long-term memory into safe decisions, skill routing, risk
classification, and approval gates.

```text
Afu / Alfred        human interface and private long-term memory
Afu Brain          shared cognition, MASL policy, risk gate, learning loop
OpenClaw           execution layer
```

The interface is not the product. The trained decision brain is the product.

## Why It Matters

**Hermes learns skills. Afu Brain decides when a skill must not run.**

**OpenClaw gives agents hands. Afu Brain gives them judgment.**

The architecture is visual and interactive:

<p align="center">
  <a href="https://charenix.com/static/alfred-lobster-brain-demo.html">
    <img src="assets/alfred-lobster-brain-demo.png" alt="Alfred Web x Lobster Brain x OpenClaw interactive architecture demo" width="100%">
  </a>
</p>

```text
Alfred hears the human.
Afu Brain / Lobster Brain turns memory into decision parameters.
MASL blocks or approval-gates unsafe action.
OpenClaw executes only what survives the gate.
```

## Evidence Snapshot

Current results are early pilot evidence, not a peer-reviewed safety guarantee.
They are the reason this project is more than a prompt wrapper.

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

Short version:

```text
The model proposes.
Afu Brain defends.
OpenClaw executes only what survives the gate.
```

Read the public summary in [`docs/EVIDENCE.md`](docs/EVIDENCE.md).

## Example

Input:

```text
Review the contract I uploaded. If there are red flags, do not send it without my approval.
```

Afu Brain decision:

```json
{
  "intent": "contract",
  "risk": "high",
  "decision": "ask",
  "can_execute": false,
  "allowed_preparation": true,
  "blocked_final_action": "external_send",
  "skills": ["files.read", "contract.red_flags", "approval.before_send"],
  "reason": "Contract review is legal/high-impact. Analysis is allowed; sending requires owner approval."
}
```

OpenClaw may read the file and draft an analysis. It may not send, commit, or
perform the external legal action until the owner confirms.

## What Users Get

Users bring their own model keys and choose their own voice stack. This repo does
not ship API keys, private owner memory, production databases, or voice clone
assets.

```text
Your keys.
Your voice.
Your memory.
Shared brain upgrades only if you opt in.
```

Users can subscribe to shared cognition upgrades from the public observatory, pin
a known feed version, or disconnect entirely and train their own local brain.

## What You Can Build

Afu Brain is a reference stack for people building personal agents that need to
act in the real world without trusting a model blindly.

Use it to build:

- a local-first voice butler
- a memory-aware desktop agent
- an approval-gated OpenClaw skill router
- a contract or email review assistant that cannot send without approval
- a receipt, travel, calendar, or household workflow agent
- a shared cognition feed for many private assistants
- a benchmark harness for model-agnostic agent safety

The first release is intentionally small: a deterministic gate, schemas,
policies, examples, and docs. The goal is to make the execution contract easy to
inspect before adding more adapters.

## What Is Open

This repository is designed to be safe to publish.

Open components:

- deterministic MASL gate
- policy ontology
- decision contract schema
- OpenClaw / AgentSkill entry point
- public RAG manifest and namespace router
- public RAG packs for MASL, OpenClaw decision routing, memory parameters, social cognition, evidence patterns, and ordered reasoning
- private-memory schema examples
- observatory feed format
- sample RAG pack format
- launch, evidence, and architecture docs

Private-by-design components:

- owner files, calendars, contacts, messages, and location history
- API keys and model credentials
- voice provider credentials and voice clones
- production Charenix / Lobster Observatory databases

## How It Works

Afu Brain separates a personal agent into three responsibilities.

| Layer | Responsibility | Public in this repo |
|---|---|---|
| Afu / Alfred | hears the human, collects context, owns private memory | schema and integration docs |
| Afu Brain | classifies intent, upgrades risk, routes skills, enforces MASL | reference gate and policies |
| OpenClaw | executes tools, files, browser, home, or environment actions | adapter contract and skill entry |

The model can propose a decision. It cannot directly authorize execution.

```text
model_output
  -> schema validation
  -> intent allowlist
  -> risk upgrade
  -> approval policy
  -> skill compatibility check
  -> execution decision
```

The gate returns one of four execution modes:

| Decision | Meaning |
|---|---|
| `execute` | low-risk reversible action may proceed |
| `prepare` | draft, analyze, or stage work, but do not commit |
| `ask` | owner approval is required before final action |
| `block` | direct execution is not allowed |

## Decision Contract

Every executor-facing plan should become a structured decision object.

```json
{
  "intent": "email",
  "risk": "medium",
  "decision": "ask",
  "can_execute": false,
  "allowed_preparation": true,
  "required_confirmation": true,
  "blocked_final_action": "external_send",
  "skills": ["email.draft", "approval.before_send"],
  "reason": "External communication may be drafted, but sending requires owner approval."
}
```

The executor should treat this object as the contract. If `can_execute=false`,
the tool layer must not perform the final external action.

See [`schemas/decision_contract.schema.json`](schemas/decision_contract.schema.json)
and [`policies/masl_policy.json`](policies/masl_policy.json).

## Quickstart

```bash
git clone https://github.com/norika1207-lab/afu-brain.git
cd afu-brain
cp .env.example .env
python3 -m pip install -e .
python3 -m afu_brain.demo
```

The demo uses local sample data only. It does not call an external model or a
production service.

Expected demo behavior:

```text
decision=ask
risk=high
can_execute=false
blocked_final_action=external_send
```

Run the public shared-cognition RAG router:

```bash
PYTHONPATH=packages python3 -m afu_brain.rag_cli "Review the contract I uploaded. Do not send it without approval."
```

Expected RAG behavior:

```text
namespaces: masl-safety, openclaw-decision-cases, memory-parameter-examples
```

## Integration Modes

### 1. Local-only

Use the default policies and keep all memory on the user's machine.

```text
private memory -> local Afu Brain -> local executor
```

This mode is best for privacy-first experiments and offline small-model
deployments.

### 2. Shared cognition feed

Subscribe to public aggregate upgrades from the observatory.

```text
private memory -> local Afu Brain
shared policy/RAG updates -> local Afu Brain
```

The feed may include policy updates, benchmark results, safe/unsafe routing
examples, and RAG packs. It must not include private owner data.

See [`docs/OBSERVATORY_FEED.md`](docs/OBSERVATORY_FEED.md) and
[`docs/RAG_UPGRADES.md`](docs/RAG_UPGRADES.md).

### 3. OpenClaw execution

Use Afu Brain as the decision layer before OpenClaw or another executor.

```text
Afu Brain decision -> OpenClaw dry-run -> approval gate -> execution
```

See [`docs/OPENCLAW.md`](docs/OPENCLAW.md) and
[`skills/afu-brain/SKILL.md`](skills/afu-brain/SKILL.md).

## Public Proof Surface

The live Lobster Observatory is the evidence surface for the shared brain. It is
not required for local use, but it shows cognition evolving in public:

- 20-agent mentor/student lineages
- social intelligence scoring
- interaction replay
- cognition cartography
- mode-collapse and anti-template correction
- Battlenix literacy traces
- ontological thinking traces
- MASL / OpenClaw decision benchmarks

Links:

- [Architecture demo](https://charenix.com/static/alfred-lobster-brain-demo.html)
- [Live observatory](https://charenix.com/lobster/dashboard/?lang=en)
- [RAG packs](docs/RAG_PACKS.md)
- [Launch note](LAUNCH.md)
- [Promotion kit](docs/PROMOTION_KIT.md)

## Safety Boundary

Afu Brain is a safety layer, not a magic proof that agents can never fail.

It currently aims to enforce:

- payment and deletion cannot run as direct low-risk actions
- contract and legal actions require approval before external commitment
- external email can be drafted, but sending requires approval
- malformed or unknown decisions fall back to safe handling
- high-risk actions are converted into `ask` or `block`

It does not claim:

- real-world safety proof
- peer review
- unbiased benchmark coverage
- safe execution for every OpenClaw skill
- replacement for human judgment in legal, medical, financial, or physical-risk domains

See [`docs/EVIDENCE.md`](docs/EVIDENCE.md) for claims and caveats.

## Why Memory Matters

Most assistants use memory to sound more personal. Afu Brain uses memory to
change decision parameters.

Examples:

```json
{
  "receipt.ask_only_when_amount_missing": 1.0,
  "email.draft_only_before_send": 1.0,
  "contract.red_flags_first": 1.0,
  "owner.dislikes_repeated_confirmation": 0.88
}
```

That means the same user request can become safer and less repetitive over time
without forcing every run through an expensive frontier model.

## Repository Map

```text
docs/                         architecture, evidence, launch docs
schemas/                      JSON schemas for contracts and feeds
policies/                     default MASL policies
rag-packs/                    public shared-cognition RAG packs
examples/                     safe public sample inputs/outputs
skills/afu-brain/SKILL.md     OpenClaw / AgentSkill entry point
packages/afu_brain/           minimal Python reference gate
assets/                       public README visuals
scripts/export_public_rag_from_sqlite.py  read-only aggregate RAG exporter
scripts/scan_secrets.sh       pre-release secret scanner
```

## Roadmap

- publish benchmark harness and generated cases
- add human-labeled evaluation set
- add confidence intervals and raw-output hashes
- add OpenClaw dry-run adapters for common skills
- add local small-model routing examples
- add feed pinning and upgrade verification
- add staged live execution tiers
- publish a formal MASL technical report

## FAQ

### Is this another chatbot?

No. Afu / Alfred can be the conversational interface, but Afu Brain is the
decision and safety layer between language and action.

### Does this require a specific model?

No. The gate is model-agnostic. Users can bring Gemini, GPT, Claude, local
models, or another provider.

### Does the public observatory receive my private memory?

No. The public observatory is for shared cognition, policy upgrades, aggregate
evidence, and RAG packs. Private owner memory should remain local unless the user
explicitly builds a different deployment.

### Can I disconnect from the shared brain?

Yes. Pin a feed version, disconnect entirely, or train your own local policy and
RAG packs.

### Why not just prompt the model better?

Prompting can shape a model's output. It cannot guarantee that a model's output
is safe to execute. Afu Brain enforces policy after generation and before tools
act.

## Safety Rule

Never commit real `.env`, private DB files, owner memory exports, auth tokens,
OAuth credentials, API keys, or voice clone assets to this repository.

Run before release:

```bash
./scripts/scan_secrets.sh
```

## Status

Afu Brain is a public reference stack draft for the Alfred / Lobster Brain /
OpenClaw ecosystem. It is ready for technical review, early adopters, and
open-source collaborators who care about memory-aware agent safety.
