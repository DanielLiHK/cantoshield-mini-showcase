# 結果與評分｜Results and scoring

## 主要發現｜Key finding

| Metric | Baseline | Context-assisted | Difference |
|---|---:|---:|---:|
| Safety-critical concept recall | 93.8% (45/48) | **97.9% (47/48)** | +4.1 percentage points |
| Case-level safety pass | 85.0% (17/20) | **95.0% (19/20)** | +10.0 percentage points |
| Completed transcripts | 20/20 | 20/20 | — |

Context-assisted ASR improved two of the 20 cases and caused no safety-concept regression in this dataset. Eighteen cases were unchanged at the semantic safety level.

加入保險術語 context 後，20句入面有2句喺安全概念層面得到改善，18句維持不變，冇出現關鍵概念倒退。

## 評分單位｜Unit of scoring

研究先為每句定義安全概念，例如：

- `20%` 同「兩成」視為同一概念；
- 「三萬蚊」同 `HKD 30,000` 視為同一概念；
- `pre-existing condition` 必須保留 `pre-` 範圍；
- `唔保障` 唔可以同 `保障` 當成一樣。

Each utterance has pre-declared concepts and accepted meaning-preserving aliases. A case passes only when every expected concept is found. The evaluator does not edit or repair the ASR output.

## Context-assisted routing result

| Safe next action | Cases | Meaning |
|---|---:|---|
| `CONFIRM_ENTITIES` | 13 | Show critical content and obtain explicit confirmation |
| `ASK_CLARIFICATION` | 6 | Ask again because alternatives, uncertainty or polarity matter |
| `REFER_TO_HUMAN` | 1 | Stop automation because an expected formal term is missing |

## Interpretation

Context improved domain and code-switch recognition, especially where a small modifier or treatment term changed meaning. It did not improve every formal term. The result supports **context plus human oversight**, not autonomous insurance use.

Context 對專業術語同中英夾雜有幫助，但唔能夠取代人手確認。研究結論唔係「ASR已經安全」，而係「context可以減少部分錯誤，而 guard 必須處理剩餘風險」。

## Scope

The experiment used one consenting speaker, 20 synthetic utterances, clean audio, a Singapore endpoint and the fixed snapshot `qwen3-asr-flash-2026-02-10`. These descriptive results are not confidence intervals, fairness measurements or production benchmarks.

Machine-readable, de-identified outputs are available in [`results/`](../results/).
