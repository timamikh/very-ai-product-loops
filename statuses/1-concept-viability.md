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
    tools: [interview, analytics-search, segmentation, segment-pains, value-definition, concept-formation]
  "2": { goals: ["— to define alongside step 2 —"], tools: [] }
  "3": { goals: ["— to define alongside step 3 —"], tools: [] }
  "4": { goals: ["— to define alongside step 4 —"], tools: [] }
  "5": { goals: ["— to define alongside step 5 —"], tools: [] }
  "6": { goals: ["— to define alongside step 6 —"], tools: [] }
status: draft
version: 0.2.0
updated: 2026-07-16
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

### 2026-07-16 — per-step structure
- **From → To:** flat priority_goals/recommended_tools → per_step goals + tools (step 1 filled)
- **Why:** keep the agent focused per step, not abstract (see OPERATING-LOOP.md)
- **Trigger:** review feedback on PR #2

### 2026-07-16 — created
- **From → To:** — → initial default status definition
- **Trigger:** Phase 1 (golden exemplar)
