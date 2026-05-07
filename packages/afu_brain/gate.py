"""Minimal deterministic MASL gate.

This reference implementation intentionally does not call any external model.
It shows the contract boundary: model output or heuristic intent goes in,
deterministic policy decision comes out.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


POLICY_VERSION = "2026.05.07"


@dataclass
class Decision:
    intent: str
    risk: str
    decision: str
    can_execute: bool
    allowed_preparation: bool
    required_confirmation: bool
    blocked_final_action: str | None
    skills: list[str]
    reason: str
    source_policy_version: str = POLICY_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def infer_intent(text: str) -> str:
    """Small demo intent classifier.

    Production deployments should replace this with a model/parser proposal,
    then still pass the proposal through the deterministic gate.
    """

    t = (text or "").lower()

    if any(x in t for x in ["pay", "payment", "transfer", "付款", "轉帳", "匯款"]):
        return "payment"
    if any(x in t for x in ["delete", "remove forever", "overwrite", "刪除", "覆寫"]):
        return "delete"
    if any(x in t for x in ["contract", "legal", "red flag", "合約", "紅旗"]):
        return "contract"
    if any(x in t for x in ["email", "reply", "send", "client", "客戶", "回信", "寄出"]):
        return "email"
    if any(x in t for x in ["receipt", "invoice", "expense", "收據", "發票", "記帳"]):
        return "receipt"
    if any(x in t for x in ["travel", "trip", "route", "weather", "行程", "旅行", "天氣"]):
        return "travel"
    if any(x in t for x in ["sad", "tired", "stress", "難過", "累", "壓力"]):
        return "mood"
    if any(x in t for x in ["hear me", "did you hear", "收到嗎", "聽到嗎"]):
        return "hearing"
    return "clarify"


def decide(request: dict[str, Any]) -> Decision:
    text = str(request.get("stt_text") or request.get("text") or "")
    proposed_intent = str(request.get("intent") or infer_intent(text))

    if proposed_intent == "receipt":
        return Decision(
            intent="receipt",
            risk="low",
            decision="allow",
            can_execute=True,
            allowed_preparation=True,
            required_confirmation=False,
            blocked_final_action=None,
            skills=["camera.ocr", "expense.save", "memory.write_policy"],
            reason="Receipt capture is reversible when core fields are readable.",
        )

    if proposed_intent == "travel":
        return Decision(
            intent="travel",
            risk="low",
            decision="allow",
            can_execute=True,
            allowed_preparation=True,
            required_confirmation=False,
            blocked_final_action=None,
            skills=["calendar.read", "weather.check", "route.recommend"],
            reason="Travel and reminder recommendations are reversible.",
        )

    if proposed_intent == "email":
        return Decision(
            intent="email",
            risk="medium",
            decision="ask",
            can_execute=False,
            allowed_preparation=True,
            required_confirmation=True,
            blocked_final_action="send_email",
            skills=["email.search", "relationship.context", "draft.reply", "approval.before_send"],
            reason="External communication may draft but must not send without owner approval.",
        )

    if proposed_intent == "contract":
        return Decision(
            intent="contract",
            risk="high",
            decision="ask",
            can_execute=False,
            allowed_preparation=True,
            required_confirmation=True,
            blocked_final_action="external_send",
            skills=["files.read", "contract.red_flags", "approval.before_send"],
            reason="Contract review is legal/high-impact. Analysis is allowed; sending requires owner approval.",
        )

    if proposed_intent == "payment":
        return Decision(
            intent="payment",
            risk="critical",
            decision="block",
            can_execute=False,
            allowed_preparation=True,
            required_confirmation=True,
            blocked_final_action="move_money",
            skills=["payment.prepare", "approval.required"],
            reason="Payment is irreversible/high-impact and cannot execute directly.",
        )

    if proposed_intent == "delete":
        return Decision(
            intent="delete",
            risk="critical",
            decision="block",
            can_execute=False,
            allowed_preparation=False,
            required_confirmation=True,
            blocked_final_action="delete_or_overwrite",
            skills=["approval.required"],
            reason="Deletion or overwrite is destructive and cannot execute directly.",
        )

    if proposed_intent == "mood":
        return Decision(
            intent="mood",
            risk="none",
            decision="allow",
            can_execute=False,
            allowed_preparation=False,
            required_confirmation=False,
            blocked_final_action=None,
            skills=[],
            reason="Mood support is not a tool execution task.",
        )

    if proposed_intent == "hearing":
        return Decision(
            intent="hearing",
            risk="none",
            decision="allow",
            can_execute=False,
            allowed_preparation=False,
            required_confirmation=False,
            blocked_final_action=None,
            skills=[],
            reason="The owner is checking whether Afu heard them.",
        )

    return Decision(
        intent="clarify",
        risk="none",
        decision="ask",
        can_execute=False,
        allowed_preparation=False,
        required_confirmation=False,
        blocked_final_action=None,
        skills=[],
        reason="Default-deny on ambiguity. Ask a clarifying question before tool use.",
    )

