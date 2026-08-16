---
node_type: status
name: concept-viability
order: 1
gate_emphasis: >
  Weigh whether the concept is testable and the demand signal is real over completeness of
  metrics or financials. Do not block on product data that cannot exist yet.
per_step:
  "1":  # Concept
    goals:
      - Name the riskiest assumption the concept rests on
      - Frame segments and pains as testable hypotheses, not facts
      - State the value bet (lead moat) to validate
    tools: [interview, concept-formation, segmentation, segment-pains, value-definition-concept, jtbd-concept]
  "2":  # Analysis
    goals:
      - Size the prize roughly (bottom-up, few sources, wide error bars OK) — just enough to know it's worth chasing
      - Map who already solves this pain (competitors + substitutes incl. do-nothing) to find the white space
      - State ONE sharpest opportunity/threat as the "so what" — a conclusion, not a survey
    tools: [market-sizing, competitor-analysis, substitutes]
  "3":  # Strategy
    goals:
      - Choose ONE beachhead arena to win first (resist "for everyone")
      - State how-to-win as a testable positioning bet, not a finished position
      - Formulate the CVP per situation for the lead segment so the bet is concrete enough to test (bundles are composed at Step 5; WTP stays an open hypothesis, not a set price)
    tools: [where-to-play-how-to-win, uvp-cpv, bets, value-definition-strategy]
  "4":  # Strategic Plan
    goals:
      - Keep the metric tree light — name the ONE activation/value metric that proves the concept works; defer the rest
      - Sketch unit economics with placeholders; treat willingness-to-pay and cost as explicit hypotheses, not facts (retention has no cohorts yet)
      - Pre-mortem the 2–3 risks that would kill the concept
    tools: [metric-tree, unit-economics, risk-mitigation, hypothesis-thresholds, instrumentation-plan]
  "5":  # Tactical Plan
    goals:
      - Set the period's ONE learning goal — the concept-killing assumption we test now
      - Stage 3–5 ready market-entry bundles; design the smallest test with a pre-set decision rule
      - Guard the little you have (runway, founder time) — don't over-invest before signal
    tools: [prioritization-tactical-plan, goal-targets, segment-cvp, hypothesis-test-design, experiment-readout, resource-check, guardrails]
  "6":  # Sprint Plan
    goals:
      - Must-set = only what produces a learning signal this sprint (a prototype slice or a test launch)
      - Every item tests a hypothesis; cut anything that doesn't move the bet
      - Keep the delivery lightweight — optimize for cycle speed with a small team
    tools: [prioritization-sprint-plan, feature-spec, activity-spec, task-spec]
status: draft
version: 0.4.0
updated: 2026-08-16
---

# Status: concept-viability

The earliest stage. There is no product in market and often no users yet. The goal is a
prototype/MVP that tests two things: **can this be built**, and **is there some demand** worth
pursuing toward PMF.

With no usage data, this stage's goals lean **technical and discovery** — expressed by the
per-step goals above, not a fixed flag. Data comes from **interviews and analytics search**,
not internal product metrics (there aren't any yet). The hypothesis register is the center of
gravity.
