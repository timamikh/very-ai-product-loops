---
node_type: status
name: growth
order: 3
gate_emphasis: >
  Weigh sustainable, guardrailed scaling over one-off spikes. Check that growth does not erode
  retention, unit economics, or defensibility.
per_step:
  "1":  # Concept
    goals:
      - Keep the concept true to what metrics now show; revise stale assumptions
      - Watch for a segment/pain shift that signals a new opportunity or a pivot
    tools: [segmentation, segment-pains, value-definition-concept]
  "2":  # Analysis
    goals:
      - Re-read the market for expansion arenas and emerging threats (new entrants, commoditization, platform shifts)
      - Track competitor dynamics from live data — who's gaining, whose strategy is working
      - Name the sharpest threat to DURABLE growth (moat erosion) as the "so what"
    tools: [competitor-analysis, competitor-pricing, competitor-dynamics, market-sizing, substitutes]
  "3":  # Strategy
    goals:
      - Sharpen how-to-win around DEFENDING the moats that make growth durable, plus the next expansion segment/market
      - Revisit pricing & packaging for expansion (new tiers/segments) without eroding the core
      - Frame expansion + defense as testable bets; watch for a segment shift signaling a new opportunity
    tools: [where-to-play-how-to-win, value-definition-strategy, pricing-strategy, channels-expansion, uvp-cpv, product-surface, product-baseline, architecture-c4, pre-mortem]
  "4":  # Strategic Plan
    goals:
      - Re-forecast off a working model; optimize the metric tree around the levers with the best marginal return
      - Analyze retention by cohort/segment — protect the retained core as scaling adds lower-intent users
      - Keep unit economics honest at scale (CAC inflation, COGS, capacity caps) in both bases
    tools: [metric-tree, retention-analysis, unit-economics, financial-model, strategic-targets, capabilities-systems, risk-mitigation, hypothesis-thresholds, instrumentation-plan]
  "5":  # Tactical Plan
    goals:
      - Pick the growth levers whose movement compounds this period; set guardrails so scale doesn't erode retention/economics/defensibility
      - Test expansion bundles (new segments/channels) with pre-set decision rules
      - Balance load across directions; surface scaling blockers early
    tools: [prioritization-tactical-plan, goal-targets, guardrails, segment-cvp, hypothesis-test-design, ab-test, experiment-readout, impact-readout, resource-check]
  "6":  # Sprint Plan
    goals:
      - Must-set = scale-and-defend items that move a growth lever or hold a guardrail; instrument before optimizing
      - Every item moves a metric node or defends one; defer nice-to-haves to backlog
      - Delivery includes the guardrail checks the team must watch during rollout
    tools: [prioritization-sprint-plan, feature-spec, activity-spec, task-spec, feature-grooming]
status: draft
version: 0.8.0
updated: 2026-08-23
---

# Status: growth

A working, profitable product. The goal is to **develop and expand** it — scale acquisition and
revenue within guardrails, open new segments/markets, and defend the moats that make growth
durable.

Evidence is dominated by **internal product metrics**. At the concept level (Step 1) the job is
mostly to keep it honest against reality and catch shifts early; the center of gravity is the
**guardrails** — growth that erodes retention, economics, or defensibility is not growth.
