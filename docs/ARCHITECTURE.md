# Architecture

Afu Brain is a MASL reference stack:

```text
Human principal
  -> Afu / Alfred interface
  -> private owner memory
  -> Afu Brain recomputation
  -> MASL safety gate
  -> OpenClaw / executor
  -> result and owner feedback
  -> future brain update
```

## Layer 1: Afu / Alfred Interface

The interface is a zero-interface butler surface:

- voice input
- push-to-talk web or app flows
- speech-to-text
- text-to-speech
- camera/file input
- phone/SMS/call channels through user-owned telephony accounts
- calendar and reminders
- relationship memory
- document and contract memory
- owner corrections and preferences

It should collect human life context. It should not directly execute
irreversible operations.

Private Alfred deployments can wire this layer to Twilio, Google OAuth,
speech-to-text, text-to-speech, and local or hosted LLM providers. Users bring
their own accounts and keys. Afu Brain keeps the decision boundary independent
of those providers.

## Layer 2: Private Owner Memory

Private owner memory is never shared by default.

Examples:

- people and relationships
- appointments and travel
- files and contract history
- promises and follow-ups
- communication preferences
- safety preferences
- recurring owner corrections

This data stays local or inside the owner's chosen deployment.

## Layer 3: Shared Afu Brain

The shared brain is the public upgrade layer:

- MASL intent ontology
- risk taxonomy
- skill routing policies
- anti-template behavior loops
- social intelligence metrics
- RAG seed packs
- benchmark cases
- observatory-derived cognition parameters

Users may subscribe to this layer or disconnect and train their own.

## Afu Model

Afu Model is the small local decision brain direction inside this architecture.
It is not the voice interface and it is not a general chat LLM. It compresses
repeated safe decisions, RAG lessons, MASL policies, file-vault routes, and owner
corrections into a local router that can emit inspectable decision fields before
tools execute.

## Layer 4: MASL Gate

MASL stands for Model-Agnostic Safety Layer.

The model proposes. The gate decides.

The gate is deterministic and auditable:

```text
allow  -> reversible low-risk execution may proceed
ask    -> prepare only; require owner confirmation
block  -> do not execute
```

Core gate checks:

- reversibility classification
- schema-fit verification
- approval policy
- default-deny on ambiguity
- owner-specific safety preferences

## Layer 5: OpenClaw / Executor

The executor receives constrained plans only.

It may execute allowed steps, prepare reversible context, or draft outputs. It
must not perform the blocked final action unless the MASL gate and owner approval
permit it.
