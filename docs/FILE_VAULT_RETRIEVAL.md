# File Vault Retrieval

This reference contract abstracts the public lessons from Alfred's file-vault
search work without publishing private files, LINE data, production database
schemas, or admin implementation details.

The goal is simple: when an owner asks for a file, Afu Brain should know the
difference between retrieval preparation and file execution.

## Boundary

Allowed preparation:

- detect explicit file-search intent
- search a local/private vault index
- rank candidates by metadata, source, category, and prior feedback
- show a small result page
- store redacted search audit metadata

Requires owner confirmation:

- open an external file
- send or share a file
- delete, move, or overwrite a file
- fetch private message/file content from a provider API

## Contract

The reference implementation is in `packages/afu_brain/file_vault.py`.

```text
owner query
  -> explicit file_search intent gate
  -> query profile and office taxonomy
  -> candidate ranking
  -> redacted audit trace
  -> OpenClaw receives only allowed vault tools
```

Run:

```bash
PYTHONPATH=packages python3 -m afu_brain.file_vault_demo
```

## Why It Belongs In The Brain

File retrieval is not just keyword matching. The brain needs to decide:

- whether the current request really permits a file tool
- which source is appropriate for the owner and context
- whether the result is a candidate list or an executable action
- whether rejected results should be penalized next time
- which private details must stay outside public RAG packs

This is the same pattern used by Afu Brain's larger decision contract: local
context can improve action quality without exposing private owner data.
