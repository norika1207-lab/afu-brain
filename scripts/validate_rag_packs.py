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


def validate_manifest(root: Path, pack_names: set[str]) -> list[str]:
    path = root / "manifest.json"
    errors: list[str] = []
    if not path.exists():
        errors.append(f"{path} is required")
        return errors
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path} invalid JSON: {exc}"]
    if manifest.get("privacy", {}).get("production_database_dump") is not False:
        errors.append(f"{path} privacy.production_database_dump must be false")
    declared = {p.get("pack") for p in manifest.get("packs", []) if isinstance(p, dict)}
    missing = pack_names - declared
    if missing:
        errors.append(f"{path} missing packs {sorted(missing)}")
    for pack in manifest.get("packs", []):
        file_name = pack.get("file")
        if file_name and not (root / file_name).exists():
            errors.append(f"{path} references missing file {file_name}")
    return errors


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
    pack_names: set[str] = set()
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
                if item.get("pack"):
                    pack_names.add(str(item["pack"]))
    errors.extend(validate_manifest(root, pack_names))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(ids)} public RAG items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
