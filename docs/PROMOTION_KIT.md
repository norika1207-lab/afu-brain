# Promotion Kit

Use these drafts as starting points. Do not spam the same wording everywhere.
Each community should get a version that fits how people talk there.

## Core Message

```text
Agents already have hands.
Afu Brain gives them judgment before execution.
```

```text
Models can propose.
Tools can act.
Afu Brain decides whether action should happen at all.
```

```text
Afu / Alfred is voice-first: speak to the assistant, let it reason over memory,
then let the decision brain decide what can safely happen.

Twilio, Google, STT/TTS, and model providers are bring-your-own-account.
The open-source repo publishes the brain and safety contract, not private keys.
```

## Short Post

```text
I open-sourced Afu Brain.

It is a model-agnostic safety and decision layer for tool-using agents.
It grew out of a working voice-first Alfred/Afu butler flow.

The idea is simple:
Agents already have hands.
They need judgment before execution.

Alfred listens.
Afu Model / Afu Brain turns memory into decision parameters.
MASL blocks or approval-gates unsafe action.
OpenClaw executes only what survives the gate.

Voice, phone, SMS, calendar, Drive, Gmail, STT/TTS, and model providers are
bring-your-own-account. The repo does not ship Twilio or Google credentials.

Live pilot:
900 model decisions requested
5 unsafe raw direct-exec decisions
0 unsafe executions after the gate
8 live decision-simulation arenas feeding pressure-tested lessons

GitHub:
https://github.com/norika1207-lab/afu-brain

Demo:
https://charenix.com/static/alfred-lobster-brain-demo.html
```

## X / Twitter Launch

Use this when you want to connect the project directly to the OpenClaw / Hermes
agent ecosystem. Keep it humble: tag people as relevant context, not as a demand
for attention.

```text
I open-sourced Afu Brain v0.1.0.

Agents already have hands.
They need judgment before execution.

Afu Brain is a model-agnostic safety + decision layer between a human-facing assistant and an executor like OpenClaw.

Alfred listens.
Afu Model / Afu Brain turns memory into decision parameters.
MASL blocks or approval-gates unsafe actions.
OpenClaw executes only what survives the gate.

The voice-first interface was already working privately before Google-style
voice-first web assistants became this week's obvious product direction. The
open-source piece is the local decision brain behind that interface.

Early pilot:
900 live model decisions requested
5 unsafe raw direct-exec decisions
0 unsafe executions after the gate
8 live decision-simulation arenas for uncertainty, feedback, and correction loops

Inspired by the agent ecosystem around @steipete / OpenClaw and @NousResearch @Teknium / Hermes Agent, but focused on the missing middle:

memory-aware judgment before tool execution.

GitHub:
https://github.com/norika1207-lab/afu-brain

Demo:
https://charenix.com/static/alfred-lobster-brain-demo.html

#AIAgents #AgenticAI #OpenSourceAI #LocalFirst #AISafety #PersonalAI #OpenClaw #HermesAgent
```

## X / Twitter Short Version

```text
I open-sourced Afu Brain v0.1.0.

Agents already have hands.
Afu Brain gives them judgment before execution.

900 live decisions requested
5 unsafe raw direct-exec decisions
0 unsafe executions after the gate
8 live decision-simulation arenas

GitHub:
https://github.com/norika1207-lab/afu-brain

Demo:
https://charenix.com/static/alfred-lobster-brain-demo.html

#AIAgents #AgenticAI #OpenSourceAI #AISafety #LocalFirst #OpenClaw #HermesAgent
```

## Hacker News

Title:

```text
Show HN: Afu Brain - a memory-aware safety gate for tool-using agents
```

First comment:

```text
I built this because tool-using agents can now touch files, email, browsers,
contracts, and home automation, but many stacks still rely on prompting for
execution safety.

Afu Brain is an open reference implementation of a model-agnostic safety layer
between a human-facing assistant and an executor such as OpenClaw.

The current release includes schemas, policies, a deterministic Python gate,
sample decisions, docs, an architecture demo, and a public observatory.

I am especially looking for feedback on the decision contract and safety
boundary.
```

## Reddit / Discord

```text
I open-sourced a small reference stack for a problem I keep seeing in tool-using
agents:

Once an agent can send email, delete files, touch contracts, or trigger
payments, prompting alone is not enough.

So I built Afu Brain: a model-agnostic decision gate that sits between the
assistant interface and the executor.

It classifies intent/risk, upgrades unsafe actions, requires approval before
external action, and returns a structured decision contract.

The private Alfred deployment is voice-first and can connect to user-owned
providers such as Twilio and Google. The open repo intentionally keeps those
credentials and private memories out of source control.

Repo:
https://github.com/norika1207-lab/afu-brain

Demo:
https://charenix.com/static/alfred-lobster-brain-demo.html

I would love technical feedback on the schema and policy design.
```

## LinkedIn

```text
I just open-sourced Afu Brain, a model-agnostic safety and decision layer for
tool-using AI agents.

The motivation is simple: agents can now touch files, email, contracts,
browsers, and home automation. Once an action becomes external or irreversible,
prompting alone is not enough.

Afu Brain sits between the human-facing assistant and the executor:

- Alfred hears the human
- Afu Brain turns memory into decision parameters
- MASL blocks or approval-gates unsafe action
- OpenClaw executes only what survives the gate

Early pilot:
- 900 live model decisions requested
- 5 unsafe raw direct-exec decisions
- 0 unsafe executions after the gate

GitHub:
https://github.com/norika1207-lab/afu-brain
```

## Chinese Post

```text
我把 Afu Brain 開源了。

它不是另一個對話介面，而是放在 AI agent 和工具執行層中間的安全決策腦。

現在 agent 已經有手了：可以碰檔案、email、瀏覽器、合約、付款、刪除、家庭自動化。
但它們缺的是執行前的判斷力。

Afu Brain 的位置是：

Alfred 聽懂人類。
Afu Model / Afu Brain 把長期記憶轉成決策參數。
MASL 擋下或 approval-gate 高風險行動。
OpenClaw 只執行通過 gate 的動作。

阿福本來就是 voice-first：使用者可以用網頁或 App 說話，阿福聽、判斷、回答，再決定哪些工具可以動。Twilio、Google、STT/TTS、模型供應商都採用 BYO account / BYO key；開源 repo 不附私人金鑰、不附電話號碼、不附 Google OAuth token。

目前 pilot：
900 個 live model decisions
5 個 raw unsafe direct-exec decisions
gate 後 0 個 unsafe executions

GitHub：
https://github.com/norika1207-lab/afu-brain

Demo：
https://charenix.com/static/alfred-lobster-brain-demo.html
```

## Posting Order

1. Personal social account: launch announcement.
2. Hacker News: one Show HN, no vote requests.
3. Reddit / Discord: one or two relevant communities only.
4. Follow-up article: why tool-using agents need a post-model safety gate.
5. Second wave: after adding a stronger local install demo.
