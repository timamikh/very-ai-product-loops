---
node_type: register
register: surfaces
title: Surface register — Decksmith (fictional sample)
updated: 2026-08-23
version: 0.1.0
---

# Surface register

Every surface through which Decksmith meets its audience. Few and long-lived; features
(`features.md`) reference them by `S-…`. Born from `3#product-surface` (the strategic *why* stays
there — this file is the ledger). All rows are `planned`: the product is pre-build at
`concept-viability`, so no `product-baseline` pass has run — the first pmf-status baseline will
reconcile these rows against what actually shipped.

| ID <!--c:id--> | Name <!--c:name--> | Type <!--c:type--> | Purpose <!--c:purpose--> | State <!--c:state--> | Source <!--c:source--> | Note <!--c:note--> |
|----|------|------|---------|-------|--------|------|
| S-01 | Landing + comparison pages | landing | acquisition | planned | `3#product-surface` | Sprint-1 lean build (item T 1) |
| S-02 | Signup / onboarding | in-product | activation | planned | `3#product-surface` | |
| S-03 | Generation UI | in-product | core value | planned | `3#product-surface` | |
| S-04 | Native export action | in-product | the promise (`H-001`) | planned | `3#product-surface` | open-success off our surface — proxy needed |
| S-05 | Edit-behaviour capture | internal | moat + `H-001` proof | planned | `3#product-surface` | instrumentation surface, not user-facing |
| S-06 | Brand-kit manager | in-product | retention / lock-in | planned | `3#product-surface` | build deferred (`H-012` trajectory) |
| S-07 | Admin / billing | admin | ops + revenue | planned | `3#product-surface` | |
| S-08 | Lifecycle emails | mailing | activation / retention | planned | `3#product-surface` | |
| S-09 | Founder design community | channel | acquisition — the `H-011` warm channel | planned | `6#must` (activity spec) | go-to-market surface; not in `3#product-surface` (interaction surfaces only) |

## Change log

### 2026-08-23 — register born (`3#product-surface` + one g2m surface from Step 6)
- **From → To:** — → `S-01`…`S-09`, all `planned`
- **Why:** `S-01`…`S-08` ledger the interaction surfaces the strategy mapped in `3#product-surface`; `S-09` was declared by the Sprint-1 activity spec (`6#must`) — a go-to-market surface the strategy pass did not carry.
