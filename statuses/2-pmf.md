---
node_type: status
name: pmf
order: 2
gate_emphasis: >
  Weigh evidence of repeatable value and a credible path to profit over breadth of growth
  activity. Guard against scaling spend before the economics work.
per_step:
  "1":  # Idea / Concept
    goals:
      - Sharpen segments/pains with real usage evidence, not just interviews
      - Confirm the value bet against how first clients actually behave
    tools: [segment-pains, segmentation, value-definition]
  "2":  # Analysis
    goals:
      - Refresh the market read with LIVE data — prices and competitors move; a stale read misleads pricing
      - State the sharpest threat to repeatable monetization (commoditization, a direct competitor) as the "so what"
    tools: [competitor-analysis, market-sizing, substitutes]
  "3":  # Strategy
    goals:
      - Sharpen how-to-win around what actually RETAINS paying users, not just what attracts them
      - Turn the retention logic into a testable bet and name the moats it leverages
    tools: [where-to-play-how-to-win, uvp-cpv, value-definition, channels-expansion, jtbd, risk-mitigation]
  "4":  # Strategic Plan
    goals:
      - Build the metric tree with a North Star that ENCODES the strategy, not a vanity/lag metric
      - Prove unit economics in BOTH bases (operational and honest own-compute) — profit must survive the honest one
      - Model off drivers, treat churn as a scenario axis, and surface capacity caps as a first-class ceiling
    tools: [metric-tree, unit-economics, financial-model, risk-mitigation, hypothesis-test-design]
  "5":  # Tactical Plan
    goals:
      - Pick the few metric nodes whose movement would prove repeatable value this period
      - Design the smallest tests for the live bets; set guardrails so growth doesn't erode the economics
    tools: [prioritization, metric-tree, hypothesis-test-design, guardrails, resource-check]
  "6":  # Sprint Plan
    goals:
      - Must-set = only what proves value/monetization or unblocks its measurement (instrumentation first if it's missing)
      - Every item moves a metric node or tests a hypothesis; defer scale-spend items to the backlog
    tools: [prioritization, feature-spec, activity-spec]
status: draft
version: 0.3.0
updated: 2026-07-18
---

# Status: pmf

First clients are here and the product has a plausible path to profit. The goal is to
**validate repeatable value and monetization** so the product can be scaled with confidence.

Product/usage data now exists, so evidence shifts from interviews toward **internal product
metrics** (with a few interviews for the "why"). Hypotheses move from "is there demand" to
"does value repeat and can we charge".

## Change log

### 2026-07-18 — filled per_step for steps 2–6 (from the first full pmf run)
- **From → To:** steps 2–6 were `— to define —` stubs → concrete goals + existing tools, drawn
  from the ai-hub-service run (live-data re-analysis; strategy around retention; dual-basis
  economics + capacity-cap ceiling; smallest-test period goals with guardrails; instrumentation-
  first must-set). Step-1 tools dropped the `analytics-search` source-slot (it's an input, not a
  library tool). `concept-viability` and `growth` stay stubbed until a run on those stages.
- **Why:** empty per_step meant the status parameterized only 1 of 6 steps; the pmf run gave the
  evidence to fill the rest (per OPERATING-LOOP: statuses complete as a by-product of a run).
- **Trigger:** framework audit + per_step decision, 2026-07-18.

### 2026-07-16 — per-step structure
- **From → To:** flat lists → per_step goals + tools (step 1 filled)
- **Why:** per-step focus (see OPERATING-LOOP.md)
- **Trigger:** review feedback on PR #2

### 2026-07-16 — created
- **From → To:** — → initial default status definition
- **Trigger:** Phase 1 (golden exemplar)
