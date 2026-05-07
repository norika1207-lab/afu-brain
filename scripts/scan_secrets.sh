#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "Scanning Afu Brain package for likely secrets..."

if find . -type f \( -name ".env" -o -name "*.pem" -o -name "*.key" -o -name "*.p12" -o -name "*.p8" -o -name "*.db" -o -name "*.sqlite" -o -name "*.sqlite3" \) | grep -q .; then
  echo "Blocked: private credential/database-like files found."
  find . -type f \( -name ".env" -o -name "*.pem" -o -name "*.key" -o -name "*.p12" -o -name "*.p8" -o -name "*.db" -o -name "*.sqlite" -o -name "*.sqlite3" \)
  exit 1
fi

PATTERN='(sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{20,}|xox[baprs]-[0-9A-Za-z-]{20,}|ghp_[0-9A-Za-z]{20,}|github_pat_[0-9A-Za-z_]{20,}|-----BEGIN (RSA |EC |OPENSSH |PRIVATE )?PRIVATE KEY-----|ANTHROPIC_API_KEY=.+|OPENAI_API_KEY=.+|GEMINI_API_KEY=.+|ELEVENLABS_API_KEY=.+|STRIPE_SECRET_KEY=.+|GOOGLE_CLIENT_SECRET=.+|JWT_SECRET=.+)'

if command -v rg >/dev/null 2>&1; then
  if rg -n --hidden --glob '!.git' --glob '!scripts/scan_secrets.sh' "$PATTERN" .; then
    echo "Blocked: likely secret pattern found."
    exit 1
  fi
else
  if grep -RInE "$PATTERN" . --exclude-dir=.git --exclude=scripts/scan_secrets.sh; then
    echo "Blocked: likely secret pattern found."
    exit 1
  fi
fi

echo "No likely secrets found."

