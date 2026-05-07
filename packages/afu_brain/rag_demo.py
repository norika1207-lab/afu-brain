"""Run a local Afu Brain RAG demo."""

from __future__ import annotations

from pathlib import Path

from .gate import infer_intent
from .rag import load_rag_dir, retrieve


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    items = load_rag_dir(repo_root / "rag-packs")
    query = "Review the contract I uploaded. If there are red flags, do not send it without my approval."
    intent = infer_intent(query)
    results = retrieve(query, items, intent=intent, top_k=4)
    print(f"query: {query}")
    print(f"inferred_intent: {intent}")
    for score, item in results:
        print("\n---")
        print(f"score: {score:.2f}")
        print(item.to_prompt_context())


if __name__ == "__main__":
    main()
