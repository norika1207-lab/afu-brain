# Voice-First Afu / Alfred and Afu Model

## What This Is

Afu started as a working voice-first butler interface: the human speaks, Alfred
listens, the brain decides what is safe to do, and the executor acts only within
the approved boundary.

This project separates that stack into inspectable layers:

```text
voice/web interface -> private memory -> Afu Model -> MASL gate -> tools
```

The public repository does not ship private user data, API keys, phone numbers,
voice clones, or production credentials. It documents the architecture and ships
the open decision layer that other builders can run with their own accounts.

## Afu Model

**Afu Model** is the small local decision brain direction inside Afu Brain. It is
not a general chat LLM.

It is meant to compress repeated safe decisions from:

- private owner memory
- public RAG packs
- MASL safety rules
- file-vault retrieval contracts
- OpenClaw skill-routing examples
- live simulation feedback
- owner corrections

The goal is a tiny local model/router that learns to emit the same inspectable
decision fields faster and more personally:

- intent
- risk
- approval requirement
- allowed preparation
- blocked final action
- skill route
- style contract
- publication gate
- evidence trace

Large frontier models can still teach, draft, or handle unusual tasks. Afu Model
is the local decision layer that remembers the owner's patterns and keeps the
tool boundary auditable.

## Voice-First Interface

The private Alfred implementation already uses a full voice loop:

- browser or app microphone capture
- speech-to-text
- memory-aware chat/routing
- text-to-speech reply
- optional phone/SMS/call workflows
- owner approval before high-risk external action

This is the same product direction now visible across voice-first AI assistant
announcements, including recent Google-style web voice assistant demos: a web or
app surface where the assistant can listen, speak, see files/camera context, and
route real actions. Afu's difference is the explicit post-model decision layer
before execution.

## Bring Your Own Accounts

Afu Brain is provider-agnostic. Users bring their own service accounts and keys.

Common deployment choices include:

- Twilio for phone calls, SMS, and telephony workflows
- Google accounts for Calendar, Drive, Gmail, OAuth, and related productivity
  data
- a speech-to-text provider or browser speech recognition
- a text-to-speech provider or browser speech synthesis
- local or hosted LLM providers
- private storage chosen by the owner

The open repo intentionally does not bundle these credentials. A deployment can
wire them in, but the decision contract stays the same:

```text
provider proposes data or channel access
Afu Model / Afu Brain decides risk and route
MASL gates execution
the owner confirms high-impact actions
```

## Timing And Positioning

Voice-first web agents are becoming an obvious platform direction. Afu/Alfred
was already implemented as a working voice butler before this wave became widely
visible in major public announcements.

The claim is not that Afu is a replacement for a major platform assistant. The
claim is narrower and more important for builders:

```text
voice interface is not enough
tool access is not enough
the missing layer is a local decision brain before execution
```

Afu Brain publishes that missing layer.
