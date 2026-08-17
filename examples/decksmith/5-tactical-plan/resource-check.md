---
node_type: worklog
tool: resource-check
step: 5
title: "resource check — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# resource check — the working (Period 1)

_Source of truth for `5-tactical-plan.md#resources`. A **lightweight capacity survey** — people ·
budget · time — stated (not measured) by whoever owns each figure, so the period goals fit real
capacity. **This is a fictional reference run: there is no real human to survey**, so every figure is
an acting-PO ⚙️ commitment and the whole survey is flagged `— to clarify —` for the founder to
confirm before Period 1 is drawn. Fake precision is refused; the numbers are round on purpose._

## 0 · Period frame

- **Period 1 — "Prototype-to-first-signal."** Length **⚙️ ~8 weeks** (no calendar dates — the strategy
  horizon has no date yet, `4#open-questions`; a period *length* is set so the plan is boundable, a
  period *date* is not invented).
- **Status `concept-viability`** → the period's job is **evidence, not traction**: a working
  native-export engine that proves `H-001` far enough to continue, and the first qualified S1 signals.

## 1 · People (per direction) ⚙️

| Direction | Available ⚙️ | Declined alternative (named, per the method) |
|-----------|-------------|----------------------------------------------|
| development | founder-engineer (~0.7 FTE) + 1 full-time engineer + 0.5 contract engineer ≈ **~2.2 dev-FTE** | not 3 full-timers — the 3rd headcount is post-signal, not pre- |
| go-to-market | founder (~0.3 FTE) — the **warm-audience owner**, the whole `H-011` channel bet | not a hired growth marketer this period — founder-led is the bet under test |
| back-office | ~0.2 FTE contractor (billing + legal/ToS setup) | not a full-time ops hire — back-office is DoD plumbing this period |

## 2 · Budget ⚙️

- **~$15k for the period** ⚙️: LLM inference for the design-acceptance eval (the biggest line, still
  small — `unit-economics` §6), tooling/hosting, and a **minimal** paid-ad probe (secondary to the
  founder channel, kept small on purpose — paid CAC is thin, `unit-economics` §4).
- Earmark: inference eval > infra > a small paid probe. No sales/marketing headcount spend.

## 3 · Time ⚙️

- ~8 weeks; no fixed external dates. One internal stage-gate at the period boundary (the readout).

## 4 · Binding constraint (the flag)

**Two human ceilings bind — not money, not compute:**
1. **Engineering throughput on the native-export engine** — the core feasibility build (`H-001`) is
   the long pole; everything else waits on a prototype that emits valid, on-brand native files.
2. **Founder taste / curation bandwidth** — the corpus + design-acceptance labelling depends on the
   founder (twin of `R-010`, key-person). It caps how fast the "designed" half can be judged.

Compute scales elastically (`financial-model` §4), so it is **not** the cap. The plan below is bounded
by dev-FTE and founder bandwidth, not by budget.

## Register

No register writes (this method reads none). The binding constraint feeds
`prioritization-tactical-plan` (capacity line) and echoes `R-010` (key-person) — not re-minted.

## Change log

### 2026-08-16 — Period-1 capacity surveyed (⚙️, fictional — to clarify)
- **From → To:** — → people/budget/time for Period 1, each an acting-PO ⚙️ commitment with the
  declined alternative named; binding constraint flagged (dev throughput + founder taste bandwidth)
- **Why:** capacity must bound the period goals before they're drawn; stated honestly as ⚙️/`— to
  clarify —` because there is no real human to survey in a reference run
- **Trigger:** Step 5 pass, section `#resources`; feeds `prioritization-tactical-plan`
