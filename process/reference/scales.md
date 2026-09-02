---
node_type: reference
title: Scales — the shared gradations a hypothesis and a risk travel with
status: draft
version: 0.1.0
updated: 2026-09-02
---

# Scales

*Read this when a method rates, gates, scores or grades something on an ordinal scale — before
inventing a tier. Every scale below is defined **once, here**; the methods that use it **operate**
it and point here. A scale is a **gradation** (a value in a row), orthogonal to the confirmation
marker a human signs* ([`CONVENTIONS.md`](../CONVENTIONS.md) → *Gradation vs confirmation*). *The
register columns that carry a gradation as an enum are in* [`REGISTERS.md`](../REGISTERS.md);
*the linter validates those (check D) — this file is the meaning behind the tokens.*

Until 2026-09-02 these lived inside `hypothesis-test-design` and were read by five other methods —
canon in a neighbour's house. One home, six readers.

## Hypothesis scales

### Readiness gate — 6 filters, pass / fail

A hypothesis (or a market-entry bundle) is **test-ready** only if every filter has a concrete
answer, not a hand-wave. A failing filter is named on the row (`not-ready: <filter>`).

| Filter | Question it must answer | Fails on |
|--------|-------------------------|----------|
| Find | Where exactly do we reach this segment? | "somewhere in small business" |
| Recognize | Would the person recognize themselves in the wording? | "everyone who wants AI" |
| Pain | Is there a cost of inaction? | "would be nice" |
| Alternative | How do they solve it today? | "no idea / they don't" |
| CVP | Do we promise a concrete result? | "gets more efficient" |
| Action | What signal will we get? | "interest / reactions" |

Operated by `segment-cvp` (Step 5) over bundles; applied by `hypothesis-test-design` before a test
is designed.

### Priority score — 1 · 3 · 5 on five criteria, sum 5–25

Which bet is worth learning about first. Ready candidates only; the top few are staged. A
criterion that cannot be judged is `— to clarify —`, never a 3; a score is ⚙️ until confirmed.

| Criterion | 1 | 3 | 5 |
|-----------|---|---|---|
| **Pain acuteness** — the cost of inaction | nice-to-have | recurring irritation | already paying or improvising to avoid it |
| **Reachability** | no named place | a place we could get into | a named community / base / partner reachable this week |
| **Deliverability** | needs a product we don't have | needs work we could do | deliverable today, even manually |
| **Evidence of willingness to pay** | none | they pay for something adjacent | they pay for this problem today |
| **Speed to a signal** | > 2 weeks | about a week | 1–2 days |

Operated by `segment-cvp` (Step 5). The **pain acuteness** row is the same gradation Step 1's
`segment-pains` writes into the *Cost of inaction* column (`nice-to-have` / `recurring irritation`
/ `already paying or improvising` — the step template declares it as a column vocabulary), so the
column feeds the Step-3 CVP and this score without translation. Not a RICE axis and never merged
with one: `prioritization-tactical-plan` decides what fits the period's capacity, this score
decides what is worth a test slot — one object, one scale each.

### Signal strength — `weak` / `medium` / `strong`

The observed market response after a test. `weak` = click · like · page-view — **channel
diagnostics, not a result**; `medium` = lead · sign-up · reply · details request · diagnostic
completed; `strong` = meeting with a real decision-maker · trial access · price talk · pilot ·
pre-pay · sale. Success means a qualified action: a decision rule reads against the signal grade,
never against raw clicks. Register column `signal`; graded by `experiment-readout`.

### Decision — `scale` / `iterate` / `reject` / `research`

The call a readout drives, written to the register's `decision` column by `experiment-readout`. A
test with no decision recorded is not finished; `research` must name a learning item that enters
the next period's goals — it is not a shrug.

## Risk scales

### Likelihood × impact — H / M / L, backed 5 / 3 / 1

The tiers stay human-readable (`H` / `M` / `L`, one letter per cell); the triage **ranks by the
product on the numeric backing** (H = 5 · M = 3 · L = 1) — five "high"s with no numbers behind them
is not an ordering. Set once at triage by `pre-mortem` (Step 3); the score travels on the register
row and is **not re-derived** by `risk-mitigation`.

### Lifecycle — `open` → `mitigating` → `contained` → `realized` → `closed`, plus `accepted`

`open` = carried, unmanaged (every risk leaves Step 3 like this) · `mitigating` = a mitigation is
being put in place · `contained` = a live risk whose mitigation is in place · `realized` = it fired;
the mitigation and the fallout are now the story · `closed` = no longer credible. `accepted` is
**off-cycle** — a decision to carry the risk un-mitigated on purpose, not a stage. Written to the
register's `status` by `risk-mitigation` (Step 4).

## Who points here

`hypothesis-test-design` · `segment-cvp` · `segment-pains` · `experiment-readout` · `pre-mortem` ·
`risk-mitigation` — and `REGISTERS.md` for the enum columns. A method that needs a scale not on
this page adds it **here**, then operates it; a second definition anywhere else is the drift this
file exists to prevent (`CONVENTIONS.md` → *One mechanism, one way*).
