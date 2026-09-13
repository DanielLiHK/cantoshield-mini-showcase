"""Small, vendor-neutral EntityGuard demonstration.

It routes high-risk text for confirmation or clarification. It never rewrites
the transcript and it never makes an insurance decision.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


CRITICAL_TERMS = (
    "共同保險", "墊底費", "自付費", "deductible", "coinsurance",
    "claim", "保障", "不保障", "日間手術", "已有病",
    "pre-existing condition", "合資格費用", "個別不保項目",
    "一般不保事項", "訂明診斷成像檢測", "MRI", "PET-CT",
    "chemo", "化療", "標靶治療", "免疫治療",
)
NEGATIONS = ("唔", "不", "冇", "無", "未", "not", "no")
NUMBER = re.compile(r"(?:HK\$|港元)?\s*\d[\d,.]*\s*(?:%|蚊|萬|千|日|號|歲)?", re.I)
CHINESE_NUMBER = re.compile(r"[零〇一二兩三四五六七八九十百千萬億]+(?:成|萬蚊|千蚊|蚊|日|號|歲)?")
AMBIGUITY = ("保障定唔保障", "究竟", "定係", "未必")


@dataclass(frozen=True)
class Decision:
    action: str
    reasons: tuple[str, ...]


def inspect(text: str) -> Decision:
    lowered = text.lower()
    reasons: list[str] = []
    if NUMBER.search(text) or CHINESE_NUMBER.search(text):
        reasons.append("number_or_date_requires_confirmation")
    if any(token.lower() in lowered for token in NEGATIONS):
        reasons.append("negation_requires_confirmation")
    if any(term.lower() in lowered for term in CRITICAL_TERMS):
        reasons.append("insurance_or_medical_term_requires_confirmation")
    if any(marker in text for marker in AMBIGUITY):
        reasons.append("ambiguity_requires_clarification")
        return Decision("ASK_CLARIFICATION", tuple(reasons))
    if not reasons:
        return Decision("ASK_CLARIFICATION", ("no_critical_entity_detected",))
    return Decision("CONFIRM_ENTITIES", tuple(reasons))
