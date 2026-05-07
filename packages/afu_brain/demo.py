"""Run the local Afu Brain demo."""

from __future__ import annotations

import json

from .gate import decide


def main() -> None:
    sample = {
        "stt_text": "Review the contract I uploaded. If there are red flags, do not send it without my approval.",
        "input_modes": ["text", "file"],
        "owner_memory": {
            "risk_preferences": {
                "contract.red_flags_first": 1.0,
                "external_send.requires_approval": 1.0,
            }
        },
    }
    print(json.dumps(decide(sample).to_dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

