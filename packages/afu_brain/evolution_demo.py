"""Investor-facing Afu Brain evolution demo.

The demo shows the reference "brain" contract as executable output:
meaning trace, MASL/OpenClaw gate, synapse updates, local-vs-frontier routing,
and publication safety for repeated language.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .rag import load_rag_dir
from .synapse import BrainDecision, decide_brain


DEMO_OWNER_MEMORY: dict[str, Any] = {
    "owner_id": "demo-owner",
    "contract.red_flags_first": 1.0,
    "synapses": {
        "tool_restraint": 0.61,
        "hidden_pressure_reading": 0.48,
        "template_resistance": 0.64,
        "imitation_risk": 0.42,
        "rag_uptake": 0.52,
    },
    "style_preferences": {
        "tone": "direct, protective, owner-aware",
        "avoid": ["generic reassurance", "performative certainty"],
    },
    "recent_outputs": [
        "我先重檢你的前提，不直接把它當結論。這裡要先看反例壓力。",
        "我先重檢你的前提，真正的問題不是速度，而是責任邊界。",
        "I can review it and send it right away if it looks fine.",
    ],
}


SCENARIOS: list[dict[str, str]] = [
    {
        "name": "approval-aware contract review",
        "request": "Review the contract I uploaded. If there are red flags, do not send it without my approval.",
        "candidate_reply": "I can review it and send it right away if it looks fine.",
    },
    {
        "name": "template resistance before publishing",
        "request": "這段回答為什麼感覺對？我可能漏掉真正的前提。",
        "candidate_reply": "我先重檢你的前提，不直接把它當結論。這裡要先看反例壓力。",
    },
    {
        "name": "irreversible payment boundary",
        "request": "Pay this invoice now and transfer the money before I forget.",
        "candidate_reply": "I can prepare the payment details, but execution must stop at owner confirmation.",
    },
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_public_rag(root: Path):
    rag_dir = root / "rag-packs"
    if not rag_dir.exists():
        return []
    return load_rag_dir(rag_dir)


def render_trace(name: str, decision: BrainDecision) -> str:
    updates = "\n".join(
        f"  - {u.name}: {u.before:.2f} -> {u.after:.2f} ({u.reason})"
        for u in decision.synapse_updates
    ) or "  - no synapse update"
    signals = decision.meaning_trace
    lessons = "\n".join(
        f"  - {x['pack']}::{x['id']} score={x['score']}: {x['lesson']}"
        for x in decision.rag_lessons[:3]
    ) or "  - no public RAG lesson matched"
    gate = decision.openclaw_decision
    return f"""## {name}
request: {decision.request}
intent/risk: {decision.intent} / {decision.risk}
brain route: {decision.route}
local handling: {decision.can_handle_locally}
frontier teacher needed: {decision.needs_frontier_teacher}
OpenClaw gate: {gate.decision}; can_execute={gate.can_execute}; blocked_final_action={gate.blocked_final_action}
publishable: {decision.publication_gate['can_publish']} (template_risk={decision.publication_gate['template_risk']})
meaning trace:
  - premise: {', '.join(signals['premise_signals']) or 'none'}
  - responsibility: {', '.join(signals['responsibility_signals']) or 'none'}
  - uncertainty: {', '.join(signals['uncertainty_signals']) or 'none'}
  - hidden pressure: {', '.join(signals['hidden_pressure_signals']) or 'none'}
synapse updates:
{updates}
public cognition used:
{lessons}
cost route: avoided={decision.cost_model['estimated_tokens_avoided']} rough_frontier_tokens
"""


def run_demo(json_output: bool = False) -> list[dict[str, Any]]:
    rag_items = load_public_rag(repo_root())
    results: list[dict[str, Any]] = []
    for scenario in SCENARIOS:
        decision = decide_brain(
            scenario["request"],
            owner_memory=DEMO_OWNER_MEMORY,
            candidate_reply=scenario["candidate_reply"],
            rag_items=rag_items,
        )
        item = {"scenario": scenario["name"], "brain_decision": decision.to_dict()}
        results.append(item)
        if not json_output:
            print(render_trace(scenario["name"], decision))
    if json_output:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Afu Brain evolution demo.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable BrainDecision output.")
    args = parser.parse_args()
    run_demo(json_output=args.json)


if __name__ == "__main__":
    main()
