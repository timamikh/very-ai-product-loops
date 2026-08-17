---
node_type: worklog
tool: metric-tree
step: 4
title: "metric tree — the working"
updated: 2026-08-16
version: 0.1.0
---

# metric tree — the working

_Source of truth for `4-strategic-plan.md#metric-tree`. Lens: North Star Framework (Amplitude) —
one metric the team steers by, 3–5 drivers, guardrails; anti-lamppost (the right metric over the
measured one). Node **definitions** are minted into `registers/metric-tree.md`; **values** would live
in `metrics.csv` (empty — the product is pre-launch, no readings exist). Status `concept-viability` →
the tree is kept light and few nodes are instrumented today._

## 1 · Candidate North Stars (2–4, each through all three filters)

Filters: **leading** (moves before revenue) · **value-repeating** (counts value recurring, not once)
· **strategy-encoding** (optimising it strengthens *our* how-to-win — editable-AND-designed).

| Candidate | Leading? | Value-repeating? | Strategy-encoding? | Verdict |
|-----------|----------|------------------|--------------------|---------|
| **A — Weekly Native Value-Exports** (on-brand decks natively exported and *kept* — no full restyle before export) | yes | **yes** — each kept native export is the value delivered, and it recurs per client deck | **yes** — it *is* the editable-AND-designed promise delivered | **chosen** |
| B — Decks generated / week | yes | **no** — a generated deck the maker then rebuilds delivers no value (that's the competitors' trap); generation ≠ value | **no** — it's the metric a *design-led rival* would pick | reject (fails value-repeating + strategy-encoding) |
| C — Retained paying seats | **no** — lags revenue | yes | partly | reject (fails *leading* — it's downstream of the value) |
| D — Weekly active "design-accepted" makers | yes | yes | yes (sharper than A on the "kept" axis) | folded **into** A as its acceptance qualifier (the "kept" clause) rather than a separate NS |

**Chosen North Star — `M-northstar` Weekly Native Value-Exports (WNVE):** count of on-brand decks
natively exported (`.pptx`/`.key`) per week across active accounts, **counting only exports the maker
kept** (design-accepted — proxy: no full in-app restyle-and-re-export in the session). Revenue is the
*outcome*, never the NS.

> **Anti-lamppost, stated on purpose:** the NS's "kept/accepted" clause is only **proxy**-instrumentable
> today — the edit-behaviour + post-export fidelity gap flagged at Step 3 (`product-surface.md`). We
> pick the right metric and carry the instrumentation gap as work (→ Steps 5–6), rather than steer by
> raw export count (candidate B, the wrong-but-measurable metric).

## 2 · Drivers (3–5) and inputs

| Driver (role) | Node | Definition | Inputs |
|---------------|------|------------|--------|
| Acquisition / activation | `M-activated` | new accounts reaching **first** native value-export | signup→first-export funnel |
| Conversion | `M-paid-conv` | trial → paid conversion rate | trial starts, paid starts |
| Deepening (the strategy's engagement axis) | `M-exports-per-acct` | native value-exports per **active account** per week | export events × design-acceptance |
| Retention | `M-w4-retention` | % of activated accounts still doing a value-export at week 4 (cohort) | cohort export recurrence |

## 3 · Guardrails (must not degrade while chasing the NS)

| Guardrail (role) | Node | Definition |
|------------------|------|------------|
| Quality | `M-design-acceptance` | % of native exports the maker **keeps** without a full restyle (the "designed enough" proxy; the NS's own quality floor) |
| Finance | `M-contribution` | contribution $/payer/mo on the **honest** basis (revenue − COGS incl. LLM inference) |
| Cost | `M-cogs-per-export` | LLM inference $ per native value-export (the COGS unit that scales with usage) |

Plus the two unit-economics nodes `metric-tree` shares with `unit-economics`: `M-arppu` (revenue per
payer/mo) and `M-cac` (CAC per paying account, by channel).

## 4 · Instrumentation status per node (feeds the not-instrumented work list → Steps 5–6)

| Node | Instrumentation | Why |
|------|-----------------|-----|
| M-northstar | **proxy** | export is instrumented; the "kept/accepted" clause is a proxy (edit-behaviour gap) |
| M-activated | instrumented | standard funnel event |
| M-paid-conv | instrumented | billing |
| M-exports-per-acct | proxy | inherits the design-acceptance proxy |
| M-w4-retention | not-instrumented | **no usage history — pre-launch**; cohort unobservable yet (all censored) |
| M-design-acceptance | proxy | in-app restyle-before-export as a stand-in for "off-brand" |
| M-contribution | instrumented | billing + usage metering |
| M-cogs-per-export | instrumented | token metering × provider price |
| M-arppu | instrumented | billing |
| M-cac | proxy | paid channels attributable; community/organic CAC attribution is a proxy |

**Not-instrumented / proxy-to-upgrade (→ Steps 5–6 work):** the design-acceptance / post-export
fidelity signal behind `M-northstar`, `M-exports-per-acct`, `M-design-acceptance` (the load-bearing
gap — it measures the promise itself); and `M-w4-retention`, unobservable until usage history exists.

## 5 · Why this tree smells of *this* strategy (not generic SaaS)

The North Star is not "active users" or "decks made" — it is **kept native exports**, which is exactly
the editable-AND-designed wedge. The quality guardrail (`M-design-acceptance`) is the "designed"
half; the North Star's native-export count is the "editable" half; the cost guardrail
(`M-cogs-per-export`) guards the `H-010` margin bet. A design-led competitor's tree would top out at
candidate B (decks generated) — the very metric this one rejects.

## Change log

### 2026-08-16 — metric tree built and projected
- **From → To:** empty register → 10 nodes minted (`M-northstar` + 4 drivers + 3 guardrails +
  `M-arppu`/`M-cac`), each with kind/parent/instrumentation; 4 candidate North Stars with the losers
  and the filter each failed
- **Why:** Step 4 builds the North-Star tree the whole lower ladder references; it must encode the
  how-to-win, not generic SaaS
- **Trigger:** Step 4 operating-loop pass, section `#metric-tree`; nodes minted into
  `registers/metric-tree.md` by the orchestrator
