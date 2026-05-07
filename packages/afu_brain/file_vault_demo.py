"""Run a public file-vault retrieval demo."""

from __future__ import annotations

import json

from .file_vault import rank_vault_records


SAMPLE_RECORDS = [
    {
        "file_key": "demo-contract-001",
        "name": "Client_NDA_signed_2026.pdf",
        "source": "local_vault",
        "group_name": "Legal",
        "mime_type": "application/pdf",
        "path": "redacted://legal/Client_NDA_signed_2026.pdf",
        "summary": "Signed NDA and confidentiality terms.",
    },
    {
        "file_key": "demo-quote-001",
        "name": "Q2_quotation_client.xlsx",
        "source": "drive_index",
        "group_name": "Sales",
        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "path": "redacted://sales/Q2_quotation_client.xlsx",
        "summary": "Pricing proposal and line-item quote.",
    },
    {
        "file_key": "demo-meeting-001",
        "name": "product_meeting_minutes.md",
        "source": "line_group_index",
        "group_name": "Product",
        "mime_type": "text/markdown",
        "path": "redacted://line/product_meeting_minutes.md",
        "summary": "Decision log and next actions from product meeting.",
    },
]


def main() -> None:
    decision = rank_vault_records("Find the signed NDA contract", SAMPLE_RECORDS, limit=5)
    print(json.dumps(decision.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
