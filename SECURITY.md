# Security Policy

## Never Commit

- `.env` files
- API keys
- OAuth client secrets
- JWT signing keys
- private owner memory
- production database files
- raw user messages
- voice clone assets
- credentials from OpenAI, Anthropic, Gemini, Google, Apple, ElevenLabs, Stripe,
  Line, Telegram, Slack, Gmail, or other services

## Pre-Release Checklist

Run:

```bash
./scripts/scan_secrets.sh
```

Then manually check:

```bash
git status --short
git diff --cached
```

## Reporting

If you find a leaked secret, rotate it immediately. Do not open a public issue
containing the secret value.

