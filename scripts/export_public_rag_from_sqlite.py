#!/usr/bin/env python3
"""Export public aggregate RAG lessons from a Lobster-style SQLite database.

This script is intentionally conservative:
- it opens SQLite in read-only mode;
- it emits aggregate lessons only;
- it does not export raw messages, owner memory, credentials, or DB rows.

Use it as a template for private deployments that want to turn their own local
telemetry into a public or private RAG pack.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable
import json
from pathlib import Path
import sqlite3


def connect_readonly(path: Path) -> sqlite3.Connection:
    uri = f"file:{path}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def has_table(conn: sqlite3.Connection, table: str) -> bool:
    row = conn.execute(
        "select 1 from sqlite_master where type='table' and name=?",
        (table,),
    ).fetchone()
    return row is not None


def count_rows(conn: sqlite3.Connection, table: str) -> int:
    if not has_table(conn, table):
        return 0
    return int(conn.execute(f"select count(*) from {table}").fetchone()[0])


def public_item(
    *,
    item_id: str,
    pack: str,
    kind: str,
    intent: str,
    risk: str,
    decision: str,
    skills: list[str],
    tags: list[str],
    text: str,
    lesson: str,
    weight: float,
) -> dict:
    return {
        "id": item_id,
        "pack": pack,
        "version": "0.1.0",
        "kind": kind,
        "intent": intent,
        "risk": risk,
        "decision": decision,
        "skills": skills,
        "tags": tags,
        "text": text,
        "lesson": lesson,
        "source": "local-sqlite-aggregate",
        "weight": weight,
        "private_data": False,
    }


def build_items(conn: sqlite3.Connection) -> Iterable[dict]:
    lounge_messages = count_rows(conn, "lounge_messages")
    interactions = count_rows(conn, "lobster_conversation_interactions")
    experience_events = count_rows(conn, "lobster_experience_events")
    cognitive_events = count_rows(conn, "lobster_cognitive_events")
    command_results = count_rows(conn, "lobster_command_results")

    if lounge_messages or interactions:
        yield public_item(
            item_id="aggregate-social-uptake-001",
            pack="social-cognition",
            kind="social_cognition",
            intent="chat",
            risk="low",
            decision="prepare",
            skills=["conversation.read_recent", "memory.write_policy", "tone.match"],
            tags=["aggregate", "social-cognition", "uptake", "feedback-loop"],
            text=(
                "Conversation telemetry can be distilled into public social-cognition lessons "
                "without exporting raw messages. Track acceptance, rejection, correction, and "
                "topic drift as routing signals before drafting replies."
            ),
            lesson=(
                f"Observed aggregate surface: {lounge_messages} lounge messages and "
                f"{interactions} interaction records. Export lessons, not transcripts."
            ),
            weight=1.05,
        )

    if experience_events or cognitive_events:
        yield public_item(
            item_id="aggregate-learning-loop-001",
            pack="evidence-patterns",
            kind="evidence_pattern",
            intent="benchmark",
            risk="medium",
            decision="prepare",
            skills=["memory.evaluate_routing", "decision.audit", "rag.compare_before_after"],
            tags=["aggregate", "learning-loop", "observatory", "evaluation"],
            text=(
                "A public observatory should expose whether repeated interactions change routing, "
                "risk posture, and correction behavior. The shared brain should publish aggregate "
                "policy upgrades while keeping private memory local."
            ),
            lesson=(
                f"Observed aggregate surface: {experience_events} experience events and "
                f"{cognitive_events} cognitive events. This is suitable for RAG upgrades before "
                "training a nano decision router."
            ),
            weight=1.15,
        )

    if command_results:
        yield public_item(
            item_id="aggregate-execution-safety-001",
            pack="masl-safety",
            kind="policy_rule",
            intent="security",
            risk="critical",
            decision="block",
            skills=["tool.dry_run", "approval.before_execute", "decision.audit"],
            tags=["aggregate", "execution-safety", "masl", "openclaw"],
            text=(
                "Execution telemetry should be audited at the decision boundary: preparation may "
                "proceed, but irreversible external actions must survive MASL policy and approval "
                "before tool execution."
            ),
            lesson=(
                f"Observed aggregate surface: {command_results} command results. Publish policy "
                "patterns and failure classes, not raw command payloads."
            ),
            weight=1.2,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Export safe aggregate Afu Brain RAG lessons.")
    parser.add_argument("sqlite_db", type=Path, help="Path to local SQLite database.")
    parser.add_argument("--out", type=Path, required=True, help="Output JSONL file.")
    args = parser.parse_args()

    with connect_readonly(args.sqlite_db) as conn:
        items = list(build_items(conn))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")

    print(f"Exported {len(items)} aggregate RAG items to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
