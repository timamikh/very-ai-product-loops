---
node_type: worklog
tool: retention-analysis
step: 4
title: "retention analysis — the working"
updated: 2026-08-16
version: 0.1.0
---

# retention analysis — the working

_Source of truth for `4-strategic-plan.md#retention`. Supplies the real churn/retention input that
`unit-economics` (LTV) and `financial-model` (churn scenario) otherwise only assume. **Status
`concept-viability`, product pre-launch → there is no usage history; no cohort can be formed yet.**
Per the skill's own concept-viability note, the curve is unobservable and the "why-they'd-return"
signal comes from `segment-pains`/`jtbd`, not data._

## 1 · "Active" definition + natural frequency (set now, so the curve is meaningful later)

- **Retained active action:** a **native value-export** (the North Star action — an on-brand deck
  exported and kept), not a login. Vanity "active" (opens) is explicitly rejected.
- **Natural frequency:** **weekly** for the S1 power user (agencies/consultants ship client decks
  continuously); a monthly-frequency read would understate a weekly product. `M-w4-retention` is read
  at **week 4** on this weekly cadence.

## 2 · Cohort curve — unobservable pre-launch (all censored)

No accounts exist; every cohort cell is **censored** (window not elapsed) → `value` empty in
`metrics.csv`, never a zero (the divide-by-un-observed anti-pattern). `M-w4-retention` is marked
**not-instrumented** in the tree for exactly this reason. Nothing is written to `metrics.csv`.

## 3 · The "why value would repeat" signal (from Step-1 evidence, not data)

The engagement loop for the retained core, mapped from `1-concept/jtbd-concept.md` + `segment-pains`:
**trigger** (a new client deck is due) → **action** (generate → native value-export) → **reward**
(client-ready, on-brand, no rebuild — the restyle tax removed) → **investment** (brand kit saved,
reused next time — the lock-in derivative). The recurring *circumstance* (client decks are a
continuous, budgeted job for S1, `H-006`) is why value should repeat; whether it *does* is `H-003`,
untested until launch.

## 4 · Churn as a scenario axis (handed to economics, not guessed as a constant)

No instrumented churn → the economics use a **scenario axis**, anchored to the researched benchmark:
- **Base 5%/mo** logo churn (self-serve prosumer at $15–50/mo; `[sourced: Recurly ~3.2% SaaS floor +
  ChartMogul ~2.3% net MRR, as_of 2026-08-16]`, adjusted up for monthly-billed self-serve).
- **Best 3%/mo** (strong onboarding) · **Worst 7%/mo**.
- Survivor cohorts typically **flatten around month 3–4** `[estimate, benchmark]` — so the LTV lifetime
  is not "1/churn forever" but a flattening core; kept simple at concept-viability.

## 5 · Drop-off / resurrection (hypothesised, pre-launch)

Expected drop-off: **first ~90 days** (benchmark: ~70% of churn is early, wrong-fit trials). The
mitigation is activation quality (reaching first *value-export* fast), which is why `M-activated` is a
driver. Resurrection path: lifecycle email on a new-client-deck trigger. Both `[assumption]`.

## Seeded hypotheses

No new `H-…` minted — retention drivers to act on are already carried (`H-003` switch/return,
`H-005` editability). Revisit this tool once usage history exists (per its cadence rule).

## Change log

### 2026-08-16 — retention (pre-launch) worked and projected
- **From → To:** — → "active"/frequency defined, cohort declared unobservable (censored, no csv
  write), engagement loop from Step-1 evidence, churn scenario axis (5%/mo base, 3–7% band) anchored
  to benchmark and handed to `unit-economics`/`financial-model`
- **Why:** Step 4 needs a churn input for LTV; at concept-viability it is a benchmarked scenario, not
  a measured curve — stated honestly rather than faked
- **Trigger:** Step 4 pass, section `#retention`
