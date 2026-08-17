---
node_type: worklog
tool: instrumentation-plan
step: 4
title: "instrumentation plan — the working"
updated: 2026-08-16
version: 0.1.0
---

# instrumentation plan — the working

_Source of truth for `4-strategic-plan.md#architecture-instrumentation`. Refines Step-3
`#architecture` + `#product-surface` into one measurability map: per component →
instrumented/proxy/not-instrumented → data yielded → infra cost driven. Every metric-tree node
traces to a row here or carries an explicit gap. Cost drivers reconcile with `unit-economics` COGS._

## Component map (union of `3#architecture` boxes + `3#product-surface` touchpoints)

| Component | Instrumentation | Data it yields | Infra cost driver | Feeds node |
|-----------|-----------------|----------------|-------------------|------------|
| Landing + comparison pages | instrumented | visits, source, signup CVR | analytics (small) | (acquisition) |
| Signup / onboarding | instrumented | signup→first-export funnel, drop-off | analytics | `M-activated` |
| Generation UI + LLM provider | instrumented | generations, tokens/deck, time-to-deck | **LLM inference — the COGS line** | `M-cogs-per-export` |
| Native export action | instrumented | export count, format | export/render service | `M-northstar` (count half) |
| **Design-acceptance / edit-behaviour** | **proxy** | in-app restyle-before-export as stand-in for "off-brand" | analytics | `M-design-acceptance`, `M-northstar` ("kept" half), `M-exports-per-acct` |
| **Post-export fidelity** (client opens file) | **not-instrumented** | did the file open clean / stay edited (off our surface) | — | (quality — no node yet; gap) |
| Brand-kit manager | instrumented | kits created, reuse rate | storage (small) | (lock-in/retention) |
| Billing / admin | instrumented | seats, plan, MRR, churn | — | `M-arppu`, `M-paid-conv`, `M-contribution` |
| Cohort store | not-instrumented | value-export recurrence by cohort | analytics | `M-w4-retention` (no data pre-launch) |
| Paid-channel attribution | instrumented | CAC by paid channel | ad spend | `M-cac` (paid) |
| Community/organic attribution | proxy | self-report / coarse UTM | — | `M-cac` (community — a proxy) |

## The two load-bearing gaps (→ Steps 5–6 work; carried as `R-012`)

1. **Design-acceptance / edit-behaviour (proxy).** The "kept" clause of the North Star and the whole
   quality guardrail ride on an in-app restyle proxy — because true acceptance is judged *after*
   native export, off our surface. Upgrade candidates: pre-export design-lint, an opt-in "opened
   successfully?" ping, agency-panel interviews.
2. **Post-export fidelity (not-instrumented).** No signal today; the differentiation itself
   (native file leaves us) is what makes it unmeasurable — the irony noted at Step 3.

**Both are the reason `capabilities-systems` mints `R-012` (execution: instrumentation gap blocks
both the North-Star measurement and the data-loop moat).**

## COGS reconciliation with `unit-economics`

Every cost driver here has a COGS line there and vice-versa: **LLM inference** (the big one, →
`M-cogs-per-export`), export/render service, analytics, email, storage. No orphan driver, no orphan
COGS line.

## Change log

### 2026-08-16 — instrumentation map built and projected
- **From → To:** — → component map crossing `3#architecture` × `3#product-surface`, each with
  instrumented/proxy/not-instrumented mark, data yielded, cost driver, node fed; the two gaps emitted
  as Steps 5–6 work (→ `R-012`); COGS reconciled with `unit-economics`
- **Why:** Step 4 makes the tree measurable — every `M-…` node needs a source row or an explicit gap
- **Trigger:** Step 4 pass, section `#architecture-instrumentation`
