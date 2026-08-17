---
node_type: register
register: metric-tree
title: Metric tree — Decksmith
updated: 2026-08-16
version: 0.1.0
---

# Metric tree

Node **definitions** only (North Star → drivers → input metrics); dated **values** live in
`metrics.csv`, append-only. The tree is born at Step 4. Schema:
[`process/REGISTERS.md`](../../../process/REGISTERS.md). Exactly one id per row; a changed
definition mints a NEW id, never reuses the old one.

| ID <!--c:id--> | Name <!--c:name--> | Definition <!--c:definition--> | Unit <!--c:unit--> | Kind <!--c:kind--> | Parent <!--c:parent--> | Population <!--c:population--> | Instrumentation <!--c:instrumentation--> | Target <!--c:target--> | Owner <!--c:owner--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|------------|------|------|--------|------------|-----------------|--------|-------|--------|------|
| M-northstar | Weekly Native Value-Exports (WNVE) | on-brand decks natively exported (`.pptx`/`.key`) per week, counting only exports the maker *kept* (design-accepted) | exports/wk | measured | — | active accounts | proxy | ⚙️ see `#strategic-targets` | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | North Star; "kept" clause is a proxy (edit-behaviour gap) |
| M-activated | Activated accounts | new accounts reaching their first native value-export | accounts | measured | M-northstar | new signups | instrumented | ⚙️ see `#strategic-targets` | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | driver: acquisition/activation |
| M-paid-conv | Trial→paid conversion | share of trials that convert to a paid seat | % | derived | M-northstar | trials | instrumented | ⚙️ | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | driver: conversion; = paid starts ÷ trial starts |
| M-exports-per-acct | Value-exports per active account | native value-exports per active account per week | exports/acct/wk | derived | M-northstar | active accounts | proxy | ⚙️ | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | driver: deepening (engagement axis) |
| M-w4-retention | Week-4 value-export retention | % of activated accounts still doing a value-export at week 4 (cohort) | % | derived | M-northstar | activated cohort | not-instrumented | ⚙️ see `#strategic-targets` | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | driver: retention; unobservable pre-launch (censored) |
| M-design-acceptance | Design-acceptance rate | % of native exports the maker keeps without a full restyle | % | derived | M-northstar | exports | proxy | ⚙️ | acting PO ⚙️ | `4-strategic-plan/metric-tree.md` | guardrail: quality (the "designed enough" floor) |
| M-contribution | Contribution per payer | revenue − COGS (incl. LLM inference) per payer per month, honest basis | $/payer/mo | derived | M-northstar | payers | instrumented | ⚙️ | acting PO ⚙️ | `4-strategic-plan/unit-economics.md` | guardrail: finance; = M-arppu − allocated COGS |
| M-cogs-per-export | Inference COGS per value-export | LLM inference $ per native value-export | $/export | derived | M-contribution | value-exports | instrumented | ⚙️ | acting PO ⚙️ | `4-strategic-plan/unit-economics.md` | guardrail: cost; token metering × provider price |
| M-arppu | Revenue per payer | blended revenue per paying account per month | $/payer/mo | derived | M-contribution | payers | instrumented | ⚙️ | acting PO ⚙️ | `4-strategic-plan/unit-economics.md` | unit-economics input |
| M-cac | CAC per paying account | acquisition cost per new paying account, by channel | $/payer | derived | M-northstar | new payers | proxy | ⚙️ | acting PO ⚙️ | `4-strategic-plan/unit-economics.md` | community/organic attribution is a proxy |

## Change log

### 2026-08-16 — metric tree born (Step 4): 10 nodes
- **From → To:** empty → `M-northstar` (Weekly Native Value-Exports) + 4 drivers (`M-activated`,
  `M-paid-conv`, `M-exports-per-acct`, `M-w4-retention`) + 3 guardrails (`M-design-acceptance`,
  `M-contribution`, `M-cogs-per-export`) + 2 unit-econ inputs (`M-arppu`, `M-cac`)
- **Why:** the North-Star tree the whole lower ladder references, born at Step 4; encodes the
  editable-AND-designed how-to-win (North Star = *kept* native exports, not decks generated)
- **Trigger:** Step 4 pass, `#metric-tree` (`metric-tree`) + `#unit-economics` (`unit-economics`).
  Values in `metrics.csv` stay empty — the product is pre-launch, no readings exist yet.

### 2026-08-16 — created
- **From → To:** — → empty metric tree scaffolded
- **Why:** instance setup; the metric tree is born at Step 4, not at scaffold time
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
