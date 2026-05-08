<p align="center">
  <img src="assets/lobster-observatory.png" alt="Afu Brain and Lobster Observatory public cognition surface" width="100%">
</p>

<h1 align="center">Afu Brain</h1>

<p align="center">
  <strong>Behavior proof, memory judgment, and safety gates for OpenClaw-compatible agents.</strong>
</p>

<p align="center">
  Models can propose. Tools can act. Afu Brain proves whether memory changed later behavior, then decides whether action should happen at all.
</p>

<p align="center">
  <strong>Don’t rent intelligence every time. Grow a brain that knows you.</strong>
</p>

<p align="center">
  <a href="https://charenix.com/static/alfred-lobster-brain-demo.html"><strong>Architecture Demo</strong></a>
  ·
  <a href="https://charenix.com/lobster/dashboard/?lang=en"><strong>Live Observatory</strong></a>
  ·
  <a href="docs/EVIDENCE.md"><strong>Evidence</strong></a>
  ·
  <a href="docs/ROLLING_COGNITION_AUDIT.md"><strong>Rolling Cognition Audit</strong></a>
  ·
  <a href="docs/MASL.md"><strong>MASL</strong></a>
  ·
  <a href="docs/OPENCLAW.md"><strong>OpenClaw</strong></a>
  ·
  <a href="docs/RAG_PACKS.md"><strong>RAG Packs</strong></a>
  ·
  <a href="docs/SYNAPSE_ENGINE.md"><strong>Synapse Engine</strong></a>
  ·
  <a href="docs/FILE_VAULT_RETRIEVAL.md"><strong>File Vault Retrieval</strong></a>
  ·
  <a href="docs/VOICE_FIRST_AFU_MODEL.md"><strong>Afu Model</strong></a>
  ·
  <a href="LAUNCH.md"><strong>Launch</strong></a>
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-open%20technical%20preview-111827">
  <img alt="Safety" src="https://img.shields.io/badge/MASL-model--agnostic%20safety-0f766e">
  <img alt="Memory" src="https://img.shields.io/badge/memory-local--first-7c3aed">
  <img alt="Behavior Proof" src="https://img.shields.io/badge/behavior--proof-rolling%20cognition-0e7490">
  <img alt="OpenClaw" src="https://img.shields.io/badge/OpenClaw-compatible-f97316">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-2563eb">
</p>

## The Problem

Open-source agents already have hands: tools, browsers, files, shells, cameras,
microphones, APIs, and home automation.

What they usually lack is judgment before execution.

If an agent can send email, review contracts, delete files, start payments, or
control a home environment, prompt instructions are not enough. The system needs
a deterministic layer after model output and before irreversible action.

```text
OpenClaw gives agents hands.
Afu Brain gives them the judgment to stop.
```

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

The working Alfred/Afu direction is voice-first: browser or app microphone in,
speech-to-text, memory-aware routing, text-to-speech out, and explicit approval
before risky external action. That puts Afu in the same product direction as
recent voice-first web assistant launches, but with a different emphasis: the
open part is the local decision brain that sits after model output and before
tools execute.

The small-model direction is called **Afu Model**. Afu Model is not a general
chatbot. It is a compact local decision brain that learns routing, risk,
approval, file-vault retrieval, and publication boundaries from RAG packs,
MASL policy, live simulation feedback, and owner corrections.

Put differently: most Agent Skills make an agent better at doing a specific
thing. **Afu Brain LLM / Afu Model** makes the agent better at deciding which
skill should run, whether it is safe to run, what must be prepared first, and
what must wait for the owner.

The first synapse engine is now executable. It converts owner memory, public RAG
lessons, repeated language checks, and OpenClaw policy into an inspectable
`BrainDecision`: meaning trace, synapse updates, style contract, publication
gate, cost route, and tool boundary.

For OpenClaw builders, Afu Brain focuses on the missing evidence layer around
`memory-core`, skill execution, and agent safety:

```text
memory event at T
  -> cognition parameter update
  -> behavior at T+1
  -> proof that the parameter changed later behavior
```

That makes it useful when maintainers ask for real behavior proof, not only a
mock, prompt, or subjective demo.

It is not only a policy table. Lobster Brain is also being pressure-tested in
eight live decision-simulation arenas, where agents must make uncertain calls,
receive outcome feedback, and convert repeated lessons into safer local
judgment. The public repo exposes the decision contracts and redacted learning
patterns, not private arena data.

## Why It Matters

**Hermes learns skills. Afu Brain decides when a skill must not run.**

**OpenClaw gives agents hands. Afu Brain gives them judgment.**

This is the missing middle between language and execution:

```text
Find the file.
Rank the evidence.
Read the risk.
Prepare the action.
Stop before the dangerous step.
```

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
| Live decision-simulation arenas | 8 |
| Rolling cognition persona-hour rows | 1,743 |
| Rolling parameter/outcome tests | 140 |
| Hot-brain personas audited | 20 |

Short version:

```text
The model proposes.
Afu Brain defends.
OpenClaw executes only what survives the gate.
```

The newest evidence layer is a rolling cognition audit: parameters at time `T`
are tested against behavior quality at `T+1`. It asks whether a growing agent's
parameters explain later interaction quality, uptake, risk respect, and template
cleanliness.

This is the same kind of artifact OpenClaw contributors need when a PR changes
memory, session behavior, tool execution, or safety policy: a lagged,
parameter-to-behavior audit that can be inspected without exposing private logs.

Read the public summaries in [`docs/EVIDENCE.md`](docs/EVIDENCE.md) and
[`docs/ROLLING_COGNITION_AUDIT.md`](docs/ROLLING_COGNITION_AUDIT.md).

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

Run the evolution demo:

```bash
PYTHONPATH=packages python3 -m afu_brain.evolution_demo
```

It prints three inspection traces: approval-aware contract review, repeated
phrasing suppression, and irreversible payment blocking. Use `--json` to inspect
the schema-backed `BrainDecision` output.

Run the file vault retrieval demo:

```bash
PYTHONPATH=packages python3 -m afu_brain.file_vault_demo
```

It shows how Afu Brain ranks private file candidates while keeping file opening,
sending, sharing, deletion, and provider content fetches behind confirmation.

## What Users Get

Users bring their own model keys and choose their own voice stack. This repo does
not ship API keys, private owner memory, production databases, or voice clone
assets.

```text
Your keys.
Your voice.
Your memory.
Your Twilio account.
Your Google account.
Shared brain upgrades only if you opt in.
```

Users can subscribe to shared cognition upgrades from the public observatory, pin
a known feed version, or disconnect entirely and train their own local brain.

Typical private deployments connect the same decision layer to provider accounts
the owner controls:

- Twilio for phone, SMS, and call workflows
- Google OAuth for Calendar, Drive, Gmail, and productivity context
- browser or provider speech-to-text
- browser or provider text-to-speech
- local or hosted LLMs

The repo provides the decision contract and reference brain. It does not provide
hosted telephony, Google credentials, voice clones, or user accounts.

## What You Can Build

Afu Brain is a reference stack for people building personal agents that need to
act in the real world without trusting a model blindly.

Use it to build:

- a local-first voice butler
- a full-voice web assistant with push-to-talk, STT, TTS, memory, and approval gates
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
- local synapse engine and `BrainDecision` contract
- file vault retrieval contract for tool calling
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

Afu Brain separates a personal agent into four responsibilities.

| Layer | Responsibility | Public in this repo |
|---|---|---|
| Afu / Alfred | hears the human, collects context, owns private memory | schema and integration docs |
| Afu Brain LLM / Afu Model | learns owner-specific routing, risk, approval, and skill-selection decisions | synapse engine, RAG packs, decision contract |
| Afu Brain MASL gate | validates decisions, upgrades risk, blocks unsafe execution | reference gate and policies |
| OpenClaw | executes tools, files, browser, home, or environment actions | adapter contract and skill entry |

The model can propose a decision. It cannot directly authorize execution.

```text
model_output
  -> Afu Brain LLM / Afu Model route proposal
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
packages/afu_brain/           reference gate, synapse engine, and file vault retrieval
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

### Is this only an interface?

No. Afu / Alfred can be the human-facing interface, but Afu Brain is the
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
