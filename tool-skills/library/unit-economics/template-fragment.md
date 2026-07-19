<!--
  template-fragment: unit-economics → fills {#unit-economics} (Step 4)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Unit economics {#unit-economics}
_Method: contribution margin, LLM inference as an explicit COGS line. Two bases: operational / honest.
LTV uses the retention curve from `{#retention}`, not an assumed churn %._

| Metric | Operational | Honest (+depreciation / market compute) | Assumptions |
|--------|-------------|------------------------------------------|-------------|
| Revenue per payer (blended, ₽/mo) | | | |
| COGS per payer (₽/mo) | | | [assumption: allocation rule] |
| Contribution (₽/mo · %) | | | |
| CAC (by channel) | | | [sourced / ⚙️] |
| Payback | | | |
| LTV | — churn scenarios X/Y/Z% ⚙️ — | | from the `{#retention}` curve once instrumented |

**By tariff:** <one row per tariff: price · actual ARPPU · contribution in both bases>
**Who bears free / grant consumption:** <explicit decision>
**Excluded segments:** <e.g. polygon accounts — contribution in the honest basis>
