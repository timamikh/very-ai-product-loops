---
node_type: worklog
tool: experiment-readout
step: 5
title: "experiment readout — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# experiment readout — the working (Period 1)

_Source of truth for `5-tactical-plan.md#readouts`. Reads every test that **finished** this period
strictly against its pre-registered rule, grades the signal, records the decision, writes back to the
register. **No post-hoc re-thresholding, no peeking.**_

## Period 1 has no finished tests — stated, not skipped

Period 1 **launches** the first three tests (`H-001`, `H-011`, `H-010`, designed in
`hypothesis-test-design.md`); none has reached its pre-registered sample/duration yet, and the product
is pre-launch, so **`registers/metrics.csv` holds no result to read**. Per the method, reading now
would be **peeking** — the read would be void, not an "early signal."

Therefore there is **nothing to read out this period**, and nothing is written back to the register as
a verdict. This is the honest first-period state, recorded so the next period knows exactly which three
readouts are pending at the Period-1 boundary — not an omission.

| Pending test | Reads out when | Against the rule in |
|--------------|----------------|---------------------|
| `H-001` design-acceptance eval | the ≥50-brief eval batch completes (end of build) | `#hypotheses-to-test` |
| `H-011` recruit push | the ~2-week push completes | `#hypotheses-to-test` |
| `H-010` partner price-talk | after the ~8 price-talks | `#hypotheses-to-test` |

## Change log

### 2026-08-16 — Period-1 readout: none finished (recorded)
- **From → To:** — → explicit "no finished tests this period"; the three launched tests listed with
  when each reads out; no register verdict written (reading now would be peeking)
- **Why:** every finished test gets a readout and every unfinished one is *not* read early — the first
  period finishes none, and that is stated rather than left blank
- **Trigger:** Step 5 pass, section `#readouts`
