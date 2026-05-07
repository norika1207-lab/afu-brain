"""Afu Brain synapse engine.

This module is the first reference implementation of the "brain" layer:
it turns owner memory, recent interaction traces, public RAG lessons, and a
candidate action/reply into an inspectable cognition decision.

It intentionally has no external model dependency. A production deployment can
replace the scoring functions with a distilled local model while preserving the
same decision contract.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable
import math
import re

from .gate import Decision, decide
from .rag import RagItem, retrieve_for_decision


SYNAPSE_VERSION = "2026.05.08"


@dataclass
class SynapseUpdate:
    name: str
    before: float
    after: float
    delta: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class BrainDecision:
    request: str
    intent: str
    risk: str
    route: str
    can_handle_locally: bool
    needs_frontier_teacher: bool
    openclaw_decision: Decision
    rag_namespaces: list[str]
    rag_lessons: list[dict[str, Any]]
    synapse_updates: list[SynapseUpdate]
    style_contract: dict[str, Any]
    publication_gate: dict[str, Any]
    cost_model: dict[str, Any]
    meaning_trace: dict[str, Any]
    source_version: str = SYNAPSE_VERSION

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["openclaw_decision"] = self.openclaw_decision.to_dict()
        data["synapse_updates"] = [x.to_dict() for x in self.synapse_updates]
        return data


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def fingerprint(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", str(text or ""))
    text = re.sub(r"[，。！？、；：「」『』（）()\[\]{}\s\"'`~!?,.;:：]", "", text)
    return text.lower()[:240]


def char_similarity(a: str, b: str) -> float:
    aa, bb = fingerprint(a), fingerprint(b)
    if not aa or not bb:
        return 0.0
    sa, sb = set(aa), set(bb)
    return len(sa & sb) / max(1, min(len(sa), len(sb)))


def template_risk(candidate: str, recent_outputs: Iterable[str]) -> float:
    candidate = normalize(candidate)
    if not candidate:
        return 0.0
    max_sim = max((char_similarity(candidate, prev) for prev in recent_outputs), default=0.0)
    repeated_opening = 0.0
    opening = candidate[:18]
    if len(opening) >= 8:
        repeated_opening = 1.0 if any(normalize(prev).startswith(opening) for prev in recent_outputs) else 0.0
    phrase_hits = sum(
        1
        for phrase in [
            "我先重檢你的前提",
            "我現在保留的疑點",
            "沒有找到清晰的 edge",
            "先讀題",
            "反例壓力",
            "哲學深度",
            "not another slogan",
        ]
        if phrase.lower() in candidate.lower()
    )
    return clamp(max_sim * 0.72 + repeated_opening * 0.18 + min(phrase_hits, 3) * 0.12)


def infer_meaning_trace(text: str) -> dict[str, Any]:
    t = normalize(text)
    lower = t.lower()
    premise_terms = ["if", "because", "unless", "前提", "如果", "因為", "除非", "假設"]
    responsibility_terms = ["send", "pay", "delete", "approve", "寄出", "付款", "刪除", "批准", "承擔"]
    uncertainty_terms = ["maybe", "not sure", "red flag", "可能", "不確定", "紅旗", "心虛", "怕"]
    hidden_pressure_terms = ["do not send", "without approval", "不要寄", "先不要", "不要直接", "你看得出來"]
    return {
        "premise_signals": [x for x in premise_terms if x in lower or x in t],
        "responsibility_signals": [x for x in responsibility_terms if x in lower or x in t],
        "uncertainty_signals": [x for x in uncertainty_terms if x in lower or x in t],
        "hidden_pressure_signals": [x for x in hidden_pressure_terms if x in lower or x in t],
        "interpretation": (
            "The request contains execution pressure and should be converted into an approval-aware plan."
            if any(x in lower for x in ["do not send", "without approval"]) or "不要" in t
            else "The brain should identify intent, evidence needs, and whether this can be handled locally."
        ),
    }


def update_param(params: dict[str, float], name: str, delta: float, reason: str) -> SynapseUpdate:
    before = float(params.get(name, 0.5))
    after = clamp(before + delta)
    params[name] = after
    return SynapseUpdate(name=name, before=round(before, 4), after=round(after, 4), delta=round(after - before, 4), reason=reason)


def estimate_cost(request: str, can_handle_locally: bool, needs_frontier: bool) -> dict[str, Any]:
    rough_tokens = max(160, math.ceil(len(request) / 3) + 420)
    frontier_cost_units = rough_tokens if needs_frontier else 0
    local_cost_units = 35 if can_handle_locally else 70
    avoided = max(0, rough_tokens - frontier_cost_units)
    return {
        "rough_frontier_tokens_if_rented": rough_tokens,
        "frontier_tokens_used_by_brain_route": frontier_cost_units,
        "local_cost_units": local_cost_units,
        "estimated_tokens_avoided": avoided,
        "claim": "Repeated judgment is converted into local cognition instead of re-renting cloud reasoning.",
    }


def style_contract_for(owner_memory: dict[str, Any], candidate: str, risk: float) -> dict[str, Any]:
    prefs = owner_memory.get("style_preferences", {})
    avoid = list(prefs.get("avoid", []))
    if risk >= 0.55:
        avoid.extend(["recent opening", "generic reassurance", "template scaffold"])
    return {
        "tone": prefs.get("tone", "direct, specific, owner-aware"),
        "must_include": ["specific uncertainty", "next safe action"] if risk >= 0.35 else ["specific next step"],
        "must_avoid": sorted(set(avoid)),
        "candidate_summary": normalize(candidate)[:180],
    }


def decide_brain(
    request: str,
    *,
    owner_memory: dict[str, Any] | None = None,
    candidate_reply: str = "",
    rag_items: Iterable[RagItem] = (),
) -> BrainDecision:
    """Return a cognition decision for an owner request.

    The function is deterministic and inspectable. It is designed as the
    contract a future distilled local model should learn to emit.
    """

    owner_memory = dict(owner_memory or {})
    params = dict(owner_memory.get("synapses") or {})
    recent_outputs = list(owner_memory.get("recent_outputs") or [])

    gate_decision = decide({"text": request})
    namespaces, hits = retrieve_for_decision(
        request,
        rag_items,
        intent=gate_decision.intent,
        risk=gate_decision.risk,
        top_k=4,
    )
    risk = template_risk(candidate_reply, recent_outputs)
    meaning_trace = infer_meaning_trace(request)

    updates: list[SynapseUpdate] = []
    if gate_decision.required_confirmation:
        updates.append(update_param(params, "tool_restraint", 0.05, "The request touches external commitment or approval boundaries."))
    if meaning_trace["uncertainty_signals"] or meaning_trace["hidden_pressure_signals"]:
        updates.append(update_param(params, "hidden_pressure_reading", 0.04, "The text carries hesitation, constraint, or latent risk."))
    if risk >= 0.45:
        updates.append(update_param(params, "template_resistance", 0.06, "Candidate language resembles recent or banned scaffolds."))
        updates.append(update_param(params, "imitation_risk", -0.04, "The brain suppresses repeated phrasing before publication."))
    if hits:
        updates.append(update_param(params, "rag_uptake", 0.03, "Relevant shared cognition was retrieved before deciding."))

    can_handle_locally = gate_decision.intent in {"receipt", "travel", "email", "contract", "hearing", "mood"}
    needs_frontier = gate_decision.intent in {"contract"} and not owner_memory.get("contract.red_flags_first")
    if risk >= 0.72:
        needs_frontier = False
    if gate_decision.decision == "block":
        can_handle_locally = True
        needs_frontier = False

    route = (
        "block_execution"
        if gate_decision.decision == "block"
        else "frontier_teacher_then_distill"
        if needs_frontier
        else "local_brain_then_openclaw_prepare"
        if gate_decision.allowed_preparation
        else "local_brain_reply_only"
    )

    publication_gate = {
        "can_publish": bool(risk < 0.72),
        "template_risk": round(risk, 4),
        "reason": "Candidate is publishable." if risk < 0.72 else "Candidate is too template-like; silence or regenerate from evidence.",
    }

    rag_lessons = [
        {
            "score": round(score, 4),
            "id": item.id,
            "pack": item.pack,
            "text": item.text,
            "lesson": item.lesson,
        }
        for score, item in hits
    ]

    return BrainDecision(
        request=request,
        intent=gate_decision.intent,
        risk=gate_decision.risk,
        route=route,
        can_handle_locally=can_handle_locally,
        needs_frontier_teacher=needs_frontier,
        openclaw_decision=gate_decision,
        rag_namespaces=namespaces,
        rag_lessons=rag_lessons,
        synapse_updates=updates,
        style_contract=style_contract_for(owner_memory, candidate_reply, risk),
        publication_gate=publication_gate,
        cost_model=estimate_cost(request, can_handle_locally, needs_frontier),
        meaning_trace=meaning_trace,
    )
