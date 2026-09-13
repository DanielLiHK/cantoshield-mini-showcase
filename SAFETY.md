# 安全設計｜Safety design

## 核心原則｜Core principle

EntityGuard 只負責標示風險同分流，**永遠唔會自行修正轉錄**。如果系統唔確定，就必須停止，唔可以估答案。

EntityGuard only flags risk and routes the next action. It **never corrects a transcript by itself**. If the system is unsure, it must stop rather than guess.

## 三個安全狀態｜Three safe states

| 狀態 State | 中文 | English |
|---|---|---|
| `CONFIRM_ENTITIES` | 顯示關鍵資料，要求講者確認 | Display critical content for explicit confirmation |
| `ASK_CLARIFICATION` | 中立地再問一次 | Ask again without selecting an interpretation |
| `REFER_TO_HUMAN` | 停止自動流程，交由獲授權人員覆核 | Stop automation for authorised review |

## 高風險內容｜Safety-critical content

金額、百分比、日期、年齡、否定詞、保障／不保障、claim certainty、正式保障及不保術語都唔可以靜默通過。

Amounts, percentages, dates, ages, negation, coverage polarity, claim certainty and formal benefit or exclusion terms must never pass silently.

## 明確禁止｜Never allowed

| 中文 | English |
|---|---|
| 靜默改數字、日期、否定詞或術語 | Silently correct numbers, dates, negation or terminology |
| 推斷保障、資格、承保或理賠結果 | Infer coverage, eligibility, underwriting or claim outcomes |
| 隱藏 Baseline／Context 分歧 | Suppress disagreement between Baseline and Context |
| 聲音無法覆核仍然繼續 | Continue when reviewable evidence is unavailable |
| 將轉錄確認當成保障確認 | Treat transcript confirmation as coverage confirmation |

## 控制測試｜Control checks

五個 deterministic 情境覆蓋關鍵資料確認、保障語意不清、內容缺失、A/B分歧及A/B一致。五個情境全部通過。

Five deterministic scenarios cover critical-entity confirmation, ambiguous coverage, missing content, A/B disagreement and A/B agreement. All five passed.

呢個結果只證明控制邏輯按設計運作，唔係 production safety certification。This result shows that the control logic behaved as designed; it is not a production safety certification.

## 剩餘風險｜Residual risk

有限規則可能漏咗改寫句式、未見過嘅術語、否定詞範圍，或者兩個模型條件共同出現嘅聲學錯誤，因此仍然需要人手覆核同離線 benchmark。

Finite rules may miss paraphrases, unseen terms, negation scope or acoustic errors shared by both model conditions. Human review and an offline benchmark therefore remain necessary.

