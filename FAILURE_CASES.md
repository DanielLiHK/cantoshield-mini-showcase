# 失敗案例｜Failure cases

## 點解展示失敗比只展示分數重要

一個高平均分可以遮住少量但嚴重嘅語意錯誤。以下案例使用合成測試內容，展示 context 有效同無效嘅邊界。

A high average score can hide rare but consequential meaning changes. These synthetic cases show both the value and the limit of context.

| ID | Baseline | Context-assisted | User impact / 用家風險 |
|---|---|---|---|
| U15 | `定名診斷成像檢測` | `定明診斷成像檢測` | Both miss `訂明診斷成像檢測`; stop and refer to a human / 兩邊同錯，必須人手覆核 |
| U18 | Drops `pre-` from `pre-existing condition` | Restores full phrase | Missing scope can change medical-history meaning / 遺漏範圍字會改變已有病語意 |
| U19 | `chemo` becomes unrelated `劇霧` | Recovers `化療` | A treatment entity is lost in Baseline / Baseline 遺失治療項目 |

## Presentation improvements, not safety gains

U10 (`復診` → `覆診`) and U17 (`co insurance` → `coinsurance`) are clearer Hong Kong/domain forms, but the semantic alias scorer treats both Baseline forms as meaning-preserving. They are not counted as safety improvements.

## Main lesson / 主要結論

如果 Baseline 同 Context 一齊聽錯，單靠比較兩者會產生假安全感。Shared errors require an offline gold-aware benchmark plus human audio review.
