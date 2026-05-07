"""Command line retrieval helper for public Afu Brain RAG packs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .gate import infer_intent
from .rag import load_rag_dir, retrieve_for_decision


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Retrieve Afu Brain public RAG context.")
    parser.add_argument("query", help="User request or agent plan to retrieve policy context for.")
    parser.add_argument("--rag-dir", default=None, help="Directory containing *.jsonl RAG packs.")
    parser.add_argument("--risk", default=None, help="Optional risk hint: low, medium, high, critical.")
    parser.add_argument("--top-k", type=int, default=5, help="Number of RAG items to return.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = Path(__file__).resolve().parents[2]
    rag_dir = Path(args.rag_dir) if args.rag_dir else repo_root / "rag-packs"
    items = load_rag_dir(rag_dir)
    intent = infer_intent(args.query)
    namespaces, results = retrieve_for_decision(
        args.query,
        items,
        intent=intent,
        risk=args.risk,
        top_k=args.top_k,
    )

    if args.json:
        print(
            json.dumps(
                {
                    "query": args.query,
                    "intent": intent,
                    "namespaces": namespaces,
                    "results": [
                        {
                            "score": score,
                            "id": item.id,
                            "pack": item.pack,
                            "kind": item.kind,
                            "risk": item.risk,
                            "decision": item.decision,
                            "skills": item.skills,
                            "text": item.text,
                            "lesson": item.lesson,
                        }
                        for score, item in results
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    print(f"query: {args.query}")
    print(f"inferred_intent: {intent}")
    print(f"namespaces: {', '.join(namespaces)}")
    for score, item in results:
        print("\n---")
        print(f"score: {score:.2f}")
        print(item.to_prompt_context())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
