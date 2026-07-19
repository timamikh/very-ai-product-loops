---
node_type: status
name: concept-viability
order: 1
gate_emphasis: >
  Weigh whether the concept is testable and the demand signal is real over completeness of
  metrics or financials. Do not block on product data that cannot exist yet.
per_step:
  "1":  # Idea / Concept
    goals:
      - Name the riskiest assumption the concept rests on
      - Frame segments and pains as testable hypotheses, not facts
      - State the value bet (lead moat) to validate
    tools: [interview, concept-formation, segmentation, segment-pains, value-definition, jtbd, segment-cvp]
  "2":  # Analysis
    goals:
      - Size the prize roughly (bottom-up, few sources, wide error bars OK) — just enough to know it's worth chasing
      - Map who already solves this pain (competitors + substitutes incl. do-nothing) to find the white space
      - State ONE sharpest opportunity/threat as the "so what" — a conclusion, not a survey
    tools: [analytics-search, market-sizing, competitor-analysis, substitutes]
  "3":  # Strategy
    goals:
      - Choose ONE beachhead arena to win first (resist "for everyone")
      - State how-to-win as a testable positioning bet, not a finished position
      - Compose the first market-entry bundles so the bet is concrete enough to test (WTP stays an open hypothesis, not a set price)
    tools: [where-to-play-how-to-win, uvp-cpv, segment-cvp, jtbd, value-definition]
  "4":  # Strategic Plan
    goals:
      - Keep the metric tree light — name the ONE activation/value metric that proves the concept works; defer the rest
      - Sketch unit economics with placeholders; treat willingness-to-pay and cost as explicit hypotheses, not facts (retention has no cohorts yet)
      - Pre-mortem the 2–3 risks that would kill the concept
    tools: [metric-tree, unit-economics, risk-mitigation, hypothesis-test-design]
  "5":  # Tactical Plan
    goals:
      - Set the period's ONE learning goal — the concept-killing assumption we test now
      - Stage 3–5 ready market-entry bundles; design the smallest test with a pre-set decision rule
      - Guard the little you have (runway, founder time) — don't over-invest before signal
    tools: [prioritization, segment-cvp, hypothesis-test-design, resource-check, guardrails]
  "6":  # Sprint Plan
    goals:
      - Must-set = only what produces a learning signal this sprint (a prototype slice or a test launch)
      - Every item tests a hypothesis; cut anything that doesn't move the bet
      - Keep the handoff lightweight — optimize for cycle speed with a small team
    tools: [prioritization, feature-spec, activity-spec]
status: draft
version: 0.3.0
updated: 2026-07-18
---

# Status: concept-viability

The earliest stage. There is no product in market and often no users yet. The goal is a
prototype/MVP that tests two things: **can this be built**, and **is there some demand** worth
pursuing toward PMF.

With no usage data, this stage's goals lean **technical and discovery** — expressed by the
per-step goals above, not a fixed flag. Data comes from **interviews and analytics search**,
not internal product metrics (there aren't any yet). The hypothesis register is the center of
gravity.

## Change log

### 2026-07-18 — filled per_step for steps 2–6
- **From → To:** steps 2–6 were `— to define —` stubs → concrete discovery-stage goals + tools:
  rough sizing + white-space (2); one beachhead + testable positioning bet composed as bundles (3);
  light metric tree + WTP/cost-as-hypotheses (4); one learning goal + smallest test (5);
  learning-signal-only must-set (6). Added `segment-cvp` to step-1 tools (compose market-entry
  bundles from segments/pains) and to steps 3 & 5.
- **Why:** an empty per_step parameterized only step 1; the framework nears release and the concept
  stage needed its full guidance filled (goals lean discovery/learning, no product data yet). Done
  by design rather than waiting for a live concept-viability run, per the user's release push.
- **Trigger:** per_step fill pass, 2026-07-18.

### 2026-07-18 — interview re-added as a tool
- **From → To:** step-1 `tools` gained `interview` — now that it's an authored **research tool**
  (`kind: research`, prepares goal/portrait/questions/interviewer-guide → `sources/`), it's the
  primary discovery method for this stage, not just an input slot.
- **Why:** the earlier cleanup dropped it because it was an unauthored source-slot; that premise
  changed when `tool-skills/library/interview/` was written. A discovery stage without interview in its tool
  list read as a gap.
- **Trigger:** interview/analytics-search authored as tools, 2026-07-18.

### 2026-07-18 — step-1 tools cleanup (audit)
- **From → To:** step-1 `tools` dropped `interview` and `analytics-search` (those are **source
  slots** / inputs, not library tools) and added `jtbd` (a step-1 job lens). Steps 2–6 stay
  stubbed until a run on this stage fills them.
- **Why:** `tools` should list library methods that fill sections; gathering is expressed via a
  tool's `inputs`. Interviews/analytics as inputs are still described in the body below.
- **Trigger:** framework audit, 2026-07-18.

### 2026-07-16 — per-step structure
- **From → To:** flat priority_goals/recommended_tools → per_step goals + tools (step 1 filled)
- **Why:** keep the agent focused per step, not abstract (see OPERATING-LOOP.md)
- **Trigger:** review feedback on PR #2

### 2026-07-16 — created
- **From → To:** — → initial default status definition
- **Trigger:** Phase 1 (golden exemplar)
