# 安全設計｜Safety design

## 核心原則｜Core principle

EntityGuard 只負責標示風險同分流，**永遠唔會自行修正 transcript**。If the system is unsure, it must stop rather than guess.

## 三個安全狀態｜Three safe states

| State | 中文 | English |
|---|---|---|
| `CONFIRM_ENTITIES` | 顯示關鍵資料，要求講者確認 | Display critical content for explicit confirmation |
| `ASK_CLARIFICATION` | 中立地再問一次 | Ask again without selecting an interpretation |
| `REFER_TO_HUMAN` | 停止自動流程，交由獲授權人員覆核 | Stop automation for authorised review |

## P0 高風險內容｜P0 content

金額、百分比、日期、年齡、否定詞、保障／不保障、claim certainty、正式保障及不保術語都要經過安全狀態，先可以進入下一步。

Amounts, percentages, dates, ages, negation, coverage polarity, claim certainty and formal benefit/exclusion terms must never pass silently.

## 明確禁止｜Never allowed

- 靜默改數字、日期、否定詞或術語 / silent correction;
- 推斷保障、資格、承保或理賠結果 / insurance decision inference;
- 視 Baseline／Context 差異為無關重要 / suppressing disagreement;
- 聲音無法覆核仍然繼續 / continuing without reviewable evidence;
- 將 transcript confirmation 當成 coverage confirmation。

## 已驗證流程｜Validated paths

Five deterministic acceptance scenarios cover critical-entity confirmation, coverage ambiguity, missing content, A/B disagreement and A/B agreement. All five passed in the documented snapshot.

呢個測試只證明控制流程按設計運作，唔等於 production safety certification。

## Known gap

Finite rules may miss paraphrases, unseen terms, negation scope and acoustic errors shared by both model conditions. Human review and an offline benchmark remain necessary.
