# 失敗案例｜Failure cases

## 點解要展示失敗｜Why failures are shown

高平均分可以遮住少量但嚴重嘅語意錯誤。以下合成案例同時展示 context 有效同無效嘅邊界。

A high average score can hide rare but consequential meaning changes. These synthetic cases show both the value and the limit of context.

| ID | Baseline 結果 | Context-assisted 結果 | 用家風險 User impact |
|---|---|---|---|
| U15 | `定名診斷成像檢測` | `定明診斷成像檢測` | 兩邊都錯過 `訂明診斷成像檢測`，必須停止並轉交人手。 / Both miss the expected formal term, so automation must stop for human review. |
| U18 | 遺漏 `pre-existing condition` 嘅 `pre-` / Drops `pre-` | 恢復完整詞語 / Restores the full phrase | 遺漏範圍字可能改變已有病相關意思。 / Missing the scope modifier can change the medical-history meaning. |
| U19 | `chemo` 變成無關詞語 `劇霧` / Becomes unrelated `劇霧` | 恢復為 `化療` / Recovers `化療` | Baseline 遺失咗治療項目。 / Baseline loses a treatment entity. |

## 表達改善而非安全增益｜Presentation improvements, not safety gains

U10（`復診` → `覆診`）同 U17（`co insurance` → `coinsurance`）更符合香港或專業寫法，但兩組 Baseline 用語都冇改變意思，所以唔計作安全增益。

U10 (`復診` → `覆診`) and U17 (`co insurance` → `coinsurance`) improve Hong Kong or domain presentation, but the Baseline forms preserve meaning and therefore do not count as safety gains.

## 主要結論｜Main lesson

如果 Baseline 同 Context 一齊聽錯，單靠比較兩者會產生假安全感，因此需要預先定義答案嘅離線 benchmark 配合人手聽音覆核。

If Baseline and Context are both wrong, comparing them can create false confidence. A pre-declared offline benchmark and human audio review are both required.

