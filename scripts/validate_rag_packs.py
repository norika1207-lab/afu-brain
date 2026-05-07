#!/usr/bin/env python3
"""Validate public Afu Brain RAG packs."""

from __future__ import annotations

import json
from pathlib import Path
import sys


REQUIRED = {"id", "pack", "version", "kind", "text", "private_data"}
ALLOWED_KIND = {
    "policy_rule",
    "decision_case",
    "memory_parameter",
    "social_cognition",
    "reasoning_seed",
    "evidence_pattern",
}


def validate_item(path: Path, line_no: int, item: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED - set(item)
    if missing:
        errors.append(f"{path}:{line_no} missing {sorted(missing)}")
    if item.get("kind") not in ALLOWED_KIND:
        errors.append(f"{path}:{line_no} invalid kind {item.get('kind')!r}")
    if item.get("private_data") is not False:
        errors.append(f"{path}:{line_no} private_data must be false for public packs")
    for field in ("id", "pack", "version", "text"):
        if not str(item.get(field, "")).strip():
            errors.append(f"{path}:{line_no} empty {field}")
    return errors


def main() -> int:
    root = Path("rag-packs")
    errors: list[str] = []
    ids: set[str] = set()
    for path in sorted(root.glob("*.jsonl")):
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{path}:{line_no} invalid JSON: {exc}")
                    continue
                errors.extend(validate_item(path, line_no, item))
                item_id = item.get("id")
                if item_id in ids:
                    errors.append(f"{path}:{line_no} duplicate id {item_id}")
                ids.add(item_id)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(ids)} public RAG items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
