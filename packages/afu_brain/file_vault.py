"""File vault retrieval reference contract.

This module abstracts the public lessons from Alfred's file-vault retrieval
work: normalize file metadata, infer office-document categories, rank candidates
with explicit query terms, and emit auditable search traces without publishing
private files or raw owner data.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Iterable
import re


OFFICE_FILE_TAXONOMY: dict[str, dict[str, list[Any]]] = {
    "contract": {
        "primary": ["contract", "agreement", "nda", "合約", "契約", "協議書", "保密", "委任"],
        "secondary": [["notary", "authorization", "公證書", "授權書"], ["mou", "memo", "備忘錄", "意向書"]],
    },
    "quote": {
        "primary": ["quote", "quotation", "price", "報價", "報價單", "估價", "價格", "費用"],
        "secondary": [["invoice", "receipt", "請款", "收據"], ["po", "purchase", "採購", "訂單"]],
    },
    "invoice": {
        "primary": ["invoice", "receipt", "payment", "發票", "請款", "收據", "付款", "帳款"],
        "secondary": [["quote", "po", "報價", "採購單"], ["statement", "對帳", "明細"]],
    },
    "meeting": {
        "primary": ["meeting", "minutes", "agenda", "會議", "會議記錄", "摘要", "決議", "待辦"],
        "secondary": [["transcript", "recording", "逐字稿", "錄音"], ["deck", "proposal", "簡報", "提案"]],
    },
    "proposal": {
        "primary": ["proposal", "deck", "ppt", "plan", "提案", "簡報", "企劃", "方案", "計畫"],
        "secondary": [["report", "analysis", "報告", "分析"], ["quote", "sow", "報價", "範疇"]],
    },
    "certificate": {
        "primary": ["certificate", "passport", "license", "證明", "證件", "公證書", "簽證", "護照", "執照"],
        "secondary": [["contract", "authorization", "合約", "委託書"], ["insurance", "保單", "證書"]],
    },
    "office_admin": {
        "primary": ["form", "sop", "hr", "admin", "申請", "表單", "行政", "人事", "採購", "核銷"],
        "secondary": [["notice", "workflow", "公告", "流程"], ["invoice", "meeting", "發票", "會議"]],
    },
}

FALLBACK_KEYWORDS = ["file", "document", "attachment", "version", "draft", "signed", "client", "project", "檔案", "文件", "附件", "版本", "草稿", "簽名", "客戶", "專案"]


@dataclass
class VaultCandidate:
    file_key: str
    name: str
    source: str
    path_hint: str = ""
    group_name: str = ""
    mime_type: str = ""
    summary: str = ""
    keywords: list[str] = field(default_factory=list)
    categories: list[dict[str, Any]] = field(default_factory=list)
    matched_keywords: list[str] = field(default_factory=list)
    score: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class VaultSearchDecision:
    query: str
    intent: str
    allowed_tool: str
    requires_confirmation_before: list[str]
    terms: list[str]
    category: str
    fallback_terms: list[str]
    results: list[VaultCandidate]
    audit: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["results"] = [x.to_dict() for x in self.results]
        return data


def norm_text(value: str) -> str:
    return str(value or "").strip().lower()


def query_terms(text: str) -> list[str]:
    raw = str(text or "")
    parts = [p for p in re.split(r"[\s,，。;；:：/\\_\-\(\)\[\]【】「」]+", raw) if p]
    hits: list[str] = []
    for word in FALLBACK_KEYWORDS:
        if word in raw:
            hits.append(word)
    low = norm_text(raw)
    for cfg in OFFICE_FILE_TAXONOMY.values():
        for word in cfg["primary"]:
            if norm_text(word) and norm_text(word) in low:
                hits.append(word)
        for group in cfg["secondary"]:
            for word in group:
                if norm_text(word) and norm_text(word) in low:
                    hits.append(word)
    return list(dict.fromkeys(parts + hits))


def file_keywords(name: str, *, group_name: str = "", mime_type: str = "", path_hint: str = "") -> list[str]:
    source = " ".join([name or "", group_name or "", mime_type or "", path_hint or ""])
    keywords: list[str] = [t for t in query_terms(source) if len(t) >= 2]
    low = norm_text(source)
    for category, cfg in OFFICE_FILE_TAXONOMY.items():
        matched = [w for w in cfg["primary"] if norm_text(w) and norm_text(w) in low]
        if matched:
            keywords.append(category)
            keywords.extend(matched[:6])
            for secondary in cfg["secondary"][:1]:
                keywords.extend(secondary[:3])
    if "." in (name or ""):
        ext = name.rsplit(".", 1)[-1].lower()
        keywords.extend([ext, ext.upper()])
    if mime_type:
        keywords.append(str(mime_type).split("/")[-1])
    if group_name:
        keywords.append(group_name)
    keywords.extend(FALLBACK_KEYWORDS)
    deduped: list[str] = []
    for keyword in keywords:
        keyword = str(keyword or "").strip()
        if keyword and keyword not in deduped:
            deduped.append(keyword)
        if len(deduped) >= 16:
            break
    return deduped


def category_scores(name: str, keywords: Iterable[str]) -> list[dict[str, Any]]:
    hay = norm_text(" ".join([name or "", " ".join(keywords)]))
    scores: list[dict[str, Any]] = []
    for category, cfg in OFFICE_FILE_TAXONOMY.items():
        primary_hits = [w for w in cfg["primary"] if norm_text(w) in hay]
        secondary_hits: list[str] = []
        for group in cfg["secondary"]:
            secondary_hits.extend([w for w in group if norm_text(w) in hay])
        score = len(primary_hits) * 3 + len(secondary_hits)
        if score:
            scores.append({"category": category, "score": score, "primary_hits": primary_hits[:5], "secondary_hits": secondary_hits[:5]})
    scores.sort(key=lambda x: (x["score"], x["category"]), reverse=True)
    return scores


def query_profile(query: str, fallback: int = 0) -> dict[str, Any]:
    terms = query_terms(query)
    low = norm_text(query)
    category = ""
    for name, cfg in OFFICE_FILE_TAXONOMY.items():
        if name in low or any(norm_text(w) in low for w in cfg["primary"]):
            category = name
            break
    fallback_terms: list[str] = []
    if category and fallback:
        groups = OFFICE_FILE_TAXONOMY[category]["secondary"]
        fallback_terms = list(groups[min(max(fallback - 1, 0), len(groups) - 1)] if groups else [])
        terms.extend(fallback_terms)
    return {"category": category, "terms": list(dict.fromkeys(terms)), "fallback_terms": fallback_terms}


def rank_vault_records(query: str, records: Iterable[dict[str, Any]], *, fallback: int = 0, rejected_keys: Iterable[str] = (), limit: int = 10) -> VaultSearchDecision:
    record_list = list(records)
    profile = query_profile(query, fallback)
    terms = profile["terms"] or [query]
    rejected = set(rejected_keys)
    results: list[VaultCandidate] = []
    for raw in record_list:
        name = str(raw.get("name") or raw.get("filename") or "")
        keywords = file_keywords(
            name,
            group_name=str(raw.get("group_name") or ""),
            mime_type=str(raw.get("mime_type") or raw.get("mime") or ""),
            path_hint=str(raw.get("path") or raw.get("path_hint") or ""),
        )
        categories = category_scores(name, keywords)
        hay = norm_text(" ".join([name, str(raw.get("group_name") or ""), " ".join(keywords), str(raw.get("summary") or "")]))
        matched = [t for t in terms if norm_text(t) and norm_text(t) in hay]
        overlap = len(matched) / max(len(terms), 1)
        score = overlap * 100
        if profile["category"] and categories and categories[0]["category"] == profile["category"]:
            score += 35
        if categories:
            score += min(float(categories[0]["score"]) * 4, 32)
        file_key = str(raw.get("file_key") or raw.get("id") or name)
        if file_key in rejected:
            score -= 80
        if score > 0:
            results.append(
                VaultCandidate(
                    file_key=file_key,
                    name=name,
                    source=str(raw.get("source") or "vault"),
                    path_hint=str(raw.get("path") or raw.get("path_hint") or ""),
                    group_name=str(raw.get("group_name") or ""),
                    mime_type=str(raw.get("mime_type") or raw.get("mime") or ""),
                    summary=str(raw.get("summary") or "")[:240],
                    keywords=keywords,
                    categories=categories,
                    matched_keywords=matched,
                    score=round(score, 2),
                )
            )
    results.sort(key=lambda x: (x.score, x.name), reverse=True)
    trimmed = results[: max(1, limit)]
    return VaultSearchDecision(
        query=query,
        intent="file_search",
        allowed_tool="vault.search",
        requires_confirmation_before=["open_external_file", "send_file", "delete_file", "share_file"],
        terms=list(terms),
        category=str(profile["category"]),
        fallback_terms=list(profile["fallback_terms"]),
        results=trimmed,
        audit={
            "result_count": len(trimmed),
            "record_count": len(record_list),
            "rejected_keys_applied": sorted(rejected),
            "stores_raw_private_content": False,
        },
    )
