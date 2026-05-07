"""Local RAG pack loader and lexical retriever.

This module intentionally has no external dependencies. It is not meant to
replace a vector database. It provides the reference contract for public Afu
Brain RAG packs and a deterministic fallback retriever for local demos.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
import re
from typing import Any, Iterable


TOKEN_RE = re.compile(r"[A-Za-z0-9_./:-]+|[\u4e00-\u9fff]")
DEFAULT_NAMESPACES = (
    "masl-safety",
    "openclaw-decision-cases",
    "memory-parameter-examples",
    "social-cognition",
    "evidence-patterns",
    "battlenix-reasoning-seeds",
)


@dataclass
class RagItem:
    id: str
    pack: str
    version: str
    kind: str
    text: str
    private_data: bool
    intent: str | None = None
    risk: str | None = None
    decision: str | None = None
    skills: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    lesson: str = ""
    source: str = ""
    weight: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "RagItem":
        return cls(
            id=str(raw["id"]),
            pack=str(raw["pack"]),
            version=str(raw["version"]),
            kind=str(raw["kind"]),
            text=str(raw["text"]),
            private_data=bool(raw["private_data"]),
            intent=raw.get("intent"),
            risk=raw.get("risk"),
            decision=raw.get("decision"),
            skills=list(raw.get("skills") or []),
            tags=list(raw.get("tags") or []),
            lesson=str(raw.get("lesson") or ""),
            source=str(raw.get("source") or ""),
            weight=float(raw.get("weight", 1.0) or 1.0),
            metadata=dict(raw.get("metadata") or {}),
        )

    def to_prompt_context(self) -> str:
        bits = [f"[{self.pack}:{self.id}]", self.text]
        if self.lesson:
            bits.append(f"Lesson: {self.lesson}")
        if self.intent or self.risk or self.decision:
            bits.append(
                "Route: "
                + ", ".join(
                    x
                    for x in [
                        f"intent={self.intent}" if self.intent else "",
                        f"risk={self.risk}" if self.risk else "",
                        f"decision={self.decision}" if self.decision else "",
                    ]
                    if x
                )
            )
        return "\n".join(bits)


def tokenize(text: str) -> set[str]:
    return {m.group(0).lower() for m in TOKEN_RE.finditer(text or "")}


def load_rag_pack(path: str | Path) -> list[RagItem]:
    items: list[RagItem] = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            item = RagItem.from_dict(raw)
            if item.private_data:
                raise ValueError(f"{path}:{line_no} contains private_data=true")
            items.append(item)
    return items


def load_rag_dir(path: str | Path) -> list[RagItem]:
    root = Path(path)
    items: list[RagItem] = []
    for p in sorted(root.glob("*.jsonl")):
        items.extend(load_rag_pack(p))
    return items


def select_namespaces(query: str, *, intent: str | None = None) -> list[str]:
    """Choose public RAG namespaces for a decision query.

    This keeps Afu Brain as one RAG system while allowing independent pack
    upgrades. Production deployments can replace this lexical router with a
    learned nano-router later.
    """

    text = f"{intent or ''} {query}".lower()
    namespaces = {"masl-safety", "openclaw-decision-cases"}

    if any(x in text for x in ("remember", "memory", "preference", "owner", "history", "receipt", "contract")):
        namespaces.add("memory-parameter-examples")
    if any(x in text for x in ("chat", "tone", "relationship", "reply", "social", "feedback", "correction")):
        namespaces.add("social-cognition")
    if any(x in text for x in ("benchmark", "evidence", "failure", "regression", "unsafe", "test", "metric")):
        namespaces.add("evidence-patterns")
    if any(x in text for x in ("reason", "doubt", "rank", "order", "counterexample", "philosophy", "battle")):
        namespaces.add("battlenix-reasoning-seeds")

    ordered = [ns for ns in DEFAULT_NAMESPACES if ns in namespaces]
    return ordered


def filter_by_namespace(items: Iterable[RagItem], namespaces: Iterable[str]) -> list[RagItem]:
    selected = set(namespaces)
    return [item for item in items if item.pack in selected]


def retrieve(
    query: str,
    items: Iterable[RagItem],
    *,
    intent: str | None = None,
    risk: str | None = None,
    top_k: int = 5,
) -> list[tuple[float, RagItem]]:
    q_tokens = tokenize(query)
    scored: list[tuple[float, RagItem]] = []
    for item in items:
        haystack = " ".join(
            [
                item.text,
                item.lesson,
                item.intent or "",
                item.risk or "",
                item.decision or "",
                " ".join(item.skills),
                " ".join(item.tags),
            ]
        )
        overlap = len(q_tokens & tokenize(haystack))
        score = float(overlap) * item.weight
        if intent and item.intent == intent:
            score += 4.0
        if risk and item.risk == risk:
            score += 2.0
        if item.kind == "policy_rule":
            score += 0.5
        if score > 0:
            scored.append((score, item))
    scored.sort(key=lambda x: (x[0], x[1].weight, x[1].id), reverse=True)
    return scored[:top_k]


def retrieve_for_decision(
    query: str,
    items: Iterable[RagItem],
    *,
    intent: str | None = None,
    risk: str | None = None,
    top_k: int = 5,
) -> tuple[list[str], list[tuple[float, RagItem]]]:
    namespaces = select_namespaces(query, intent=intent)
    scoped_items = filter_by_namespace(items, namespaces)
    return namespaces, retrieve(query, scoped_items, intent=intent, risk=risk, top_k=top_k)
