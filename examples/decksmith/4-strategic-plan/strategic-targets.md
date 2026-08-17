---
node_type: worklog
tool: strategic-targets
step: 4
title: "strategic targets — the working"
updated: 2026-08-17
version: 0.1.1
---

# strategic targets — the working

_Source of truth for `4-strategic-plan.md#strategic-targets`. Commits what 3–5 key `M-…` nodes must
reach by the strategy horizon, anchored to the `financial-model` base scenario — **read off it where
it outputs the number, derived or committed as a driver bar where it doesn't** (provenance stated per
node below). `metric-tree` **defines**
the node, this **commits its horizon value**, Step-5 `goal-targets` sets the **period value** — three
values, three owners. Commitments, not readings (they live here, not in `metrics.csv`)._

## 0 · Horizon — an upstream gap, flagged not invented

`3#winning-aspiration` says "**this horizon**" with **no explicit date** (`concept-viability` framed it
as "prove repeatable fit," not a dated number). Per the method, a missing horizon is a gap in the
aspiration — **sent upstream** (→ `#open-questions`), **not minted here**. The targets below are set
against a **⚙️ proposed horizon of "+12 months from launch"** and are explicitly *provisional* until
the human fixes the aspiration's date. They rest on a model with **no actuals** — doubly ⚙️.

## 1 · Nodes chosen (3–5) — the North Star + the drivers the winning logic leans on

| Node | Target @ +12mo (base scenario) ⚙️ | Why this node carries a commitment |
|------|-----------------------------------|-----------------------------------|
| `M-northstar` (Weekly Native Value-Exports) | **~600 WNVE/wk** | the value delivered — the whole strategy in one number |
| `M-paid-conv` (trial→paid) | **≥ 8%** | the WTP/monetisation bet `H-010` made visible |
| `M-w4-retention` (week-4 value-export retention) | **≥ 30%** floor | the switch *sticking* — `H-003`; a flattening core is the fit signal |
| `M-contribution` (per payer, honest) | **≥ $25/mo (~80%)** | the margin guardrail — the model must stay economic while chasing volume |

Four nodes (within 3–5). **Provenance per node — the model outputs accounts and MRR, not all four
numbers, so "read off the base scenario" is only literally true for one of them:**

- `M-contribution` ≥ $25/mo — **read off the model** (§5: ARPPU ~$33 − COGS ~$3.5 ≈ $29.5/payer; $25
  is the committed floor under it).
- `M-northstar` ~600 WNVE/wk — **derived, not read**: base scenario ~600 paying accounts @ mo-12
  (§3) × ~1 value-export/acct/wk (`M-exports-per-acct` — an `[assumption]`, no usage data exists)
  ≈ 600 ⚙️. The multiplier is the honest weak link.
- `M-paid-conv` ≥ 8% and `M-w4-retention` ≥ 30% — **driver bars, not scenario outputs**: the model
  *assumes* conversion feeding the ramp and a churn axis consistent with a retained core; these two
  targets commit to the bars the base scenario needs to be real (quantified into test thresholds by
  `hypothesis-thresholds`, `H-010`/`H-003`). If the bars fail, the scenario fails with them.

## 2 · Nodes considered and left untargeted (kept with why)

| Node | Why not a horizon commitment |
|------|------------------------------|
| `M-cogs-per-export` | a guardrail to *watch*, but COGS is trivial (`unit-economics` §3) — committing a target would be steering by a non-constraint |
| `M-cac` | directional-only inputs (report-mill sourced); committing a CAC target on unsourced data would be bravado — revisit once a primary/own-funnel read exists |
| `M-activated` | upstream of `M-northstar`; steered via the North Star, not double-committed |
| `M-design-acceptance` | proxy-only today (instrumentation gap `R-012`); target it once the signal is real, not while it's a stand-in |

## 3 · Decision lines (⚙️ — unconfirmed; the ladder rule downward)

Each target: **Decided 2026-08-16 · by acting PO ⚙️ (awaiting human) · alternatives considered:** the
conservative/stretch scenario values (e.g. WNVE ~400 conservative / ~850 stretch) — base chosen as the
honest middle. **Ladder rule:** Step-5 `goal-targets` sets each period target as a step toward these;
a period moving no horizon target is drift, visible at the Step-5 gate.

## Change log

### 2026-08-17 — human review pass: per-node provenance made honest
- **From → To:** "each value is read off the base scenario" → provenance stated per node: only
  `M-contribution` is literally read off the model; `M-northstar` is derived (accounts × an assumed
  exports-per-account multiplier); `M-paid-conv`/`M-w4-retention` are driver bars the scenario
  assumes, not outputs it produces
- **Why:** the model outputs accounts and MRR — claiming all four targets were "read off" it
  laundered two hypothesis bars and one derivation into scenario outputs; review returned it
- **Trigger:** human review of the finished run (strategy lens)

### 2026-08-16 — strategic targets worked and projected
- **From → To:** — → 4 horizon targets (`M-northstar`, `M-paid-conv`, `M-w4-retention`,
  `M-contribution`) read off the base scenario, 4 nodes left untargeted with why; horizon-date gap
  flagged upstream (not invented); all ⚙️ pending the human
- **Why:** Step 4 puts a top on the target ladder Step-5 climbs; without it period targets check
  against nothing
- **Trigger:** Step 4 pass, section `#strategic-targets`
