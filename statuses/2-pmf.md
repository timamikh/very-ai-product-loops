---
node_type: status
name: pmf
order: 2
gate_emphasis: >
  Weigh evidence of repeatable value and a credible path to profit over breadth of growth
  activity. Guard against scaling spend before the economics work.
per_step:
  "1":  # Concept
    goals:
      - Sharpen segments/pains with real usage evidence, not just interviews
      - Confirm the value bet against how first clients actually behave
    tools: [segment-pains, segmentation, value-definition, segment-cvp]
  "2":  # Analysis
    goals:
      - Refresh the market read with LIVE data — prices and competitors move; a stale read misleads pricing
      - State the sharpest threat to repeatable monetization (commoditization, a direct competitor) as the "so what"
    tools: [competitor-analysis, market-sizing, substitutes]
  "3":  # Strategy
    goals:
      - Sharpen how-to-win around what actually RETAINS paying users, not just what attracts them
      - Turn the retention logic into a testable bet and name the moats it leverages
      - Set pricing & packaging that captures the repeatable value (value metric + fences), tested not assumed
    tools: [where-to-play-how-to-win, uvp-cpv, value-definition, pricing, channels-expansion, jtbd, risk-mitigation]
  "4":  # Strategic Plan
    goals:
      - Build the metric tree with a North Star that ENCODES the strategy, not a vanity/lag metric
      - Prove unit economics in BOTH bases (operational and honest own-compute) — profit must survive the honest one
      - Read retention by cohort — the flattening curve is the PMF signal and the real churn input to LTV, not an assumed %
      - Model off drivers, treat churn as a scenario axis, and surface capacity caps as a first-class ceiling
    tools: [metric-tree, retention-analysis, unit-economics, financial-model, risk-mitigation, hypothesis-test-design]
  "5":  # Tactical Plan
    goals:
      - Pick the few metric nodes whose movement would prove repeatable value this period
      - Design the smallest tests for the live bets; set guardrails so growth doesn't erode the economics
      - Compose & stage market-entry bundles for the go-to-market direction; test the strongest with pre-set decision rules
    tools: [prioritization, segment-cvp, metric-tree, hypothesis-test-design, guardrails, resource-check]
  "6":  # Sprint Plan
    goals:
      - Must-set = only what proves value/monetization or unblocks its measurement (instrumentation first if it's missing)
      - Every item moves a metric node or tests a hypothesis; defer scale-spend items to the backlog
    tools: [prioritization, feature-spec, activity-spec]
status: draft
version: 0.3.1
updated: 2026-07-18
---

# Status: pmf

First clients are here and the product has a plausible path to profit. The goal is to
**validate repeatable value and monetization** so the product can be scaled with confidence.

Product/usage data now exists, so evidence shifts from interviews toward **internal product
metrics** (with a few interviews for the "why"). Hypotheses move from "is there demand" to
"does value repeat and can we charge".
