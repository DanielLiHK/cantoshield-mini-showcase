# 結果與評分｜Results and scoring

## 主要發現｜Key finding

| 指標 Metric | Baseline | Context-assisted | 差異 Difference |
|---|---:|---:|---:|
| 關鍵概念保留率 Safety-critical concept recall | 93.8% (45/48) | **97.9% (47/48)** | +4.1 percentage points |
| 每句安全通過率 Case-level safety pass | 85.0% (17/20) | **95.0% (19/20)** | +10.0 percentage points |
| 完成轉錄 Completed transcripts | 20/20 | 20/20 | — |

加入保險術語 context 後，20句入面有2句喺安全概念層面得到改善，18句維持不變，冇出現關鍵概念倒退。

With insurance glossary context, two of 20 cases improved at the safety-concept level, 18 were unchanged and none regressed.

## 評分單位｜Unit of scoring

每句都有事先定義嘅安全概念及可接受同義形式。所有預期概念都出現，該句先算通過。評估器唔會修改或修補 ASR 輸出。

Each utterance has pre-declared safety concepts and accepted meaning-preserving aliases. A case passes only when every expected concept is present. The evaluator does not edit or repair ASR output.

| 例子 Example | 評分原則 Scoring rule |
|---|---|
| `20%`／「兩成」 | 視為同一概念 / Treated as the same concept |
| 「三萬蚊」／`HKD 30,000` | 視為同一金額 / Treated as the same amount |
| `pre-existing condition` | 必須保留 `pre-` 範圍 / The `pre-` scope must be preserved |
| `唔保障`／`保障` | 唔可以視為相同 / Must not be treated as equivalent |

## 安全分流結果｜Safety-routing result

| 下一步 Safe next action | 個案 Cases | 中文意思 | English meaning |
|---|---:|---|---|
| `CONFIRM_ENTITIES` | 13 | 顯示關鍵內容並取得明確確認 | Show critical content and obtain explicit confirmation |
| `ASK_CLARIFICATION` | 6 | 因替代選項、不確定性或極性而再次提問 | Ask again because alternatives, uncertainty or polarity matter |
| `REFER_TO_HUMAN` | 1 | 因預期正式術語缺失而停止自動處理 | Stop automation because an expected formal term is missing |

## 結果解讀｜Interpretation

Context 對專業術語同中英夾雜有幫助，但唔能夠取代人手確認。結論唔係「ASR已經安全」，而係「context可以減少部分錯誤，而 guard 必須處理剩餘風險」。

Context helped with domain terminology and code-switching, but it cannot replace human confirmation. The conclusion is not that ASR is safe; it is that context can reduce some errors while the guard must handle residual risk.

## 測試範圍｜Scope

| 項目 Item | 測試設定 Test setting |
|---|---|
| 語音 Speech | 一位自願參與者、20句合成香港廣東話 / One consenting speaker and 20 synthetic Hong Kong Cantonese utterances |
| 環境 Environment | 安靜錄音 / Clean audio |
| 模型 Model | `qwen3-asr-flash-2026-02-10` |
| Region | Singapore |
| 結論限制 Claim boundary | 描述性 pilot；唔係信賴區間、公平性量度或 production benchmark / Descriptive pilot; not a confidence interval, fairness measure or production benchmark |

去識別化 machine-readable 結果可喺 [`results/`](../results/) 查看。De-identified machine-readable outcomes are available in [`results/`](../results/).

