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
    tools: [interview, concept-formation, segmentation, segment-pains, value-definition, jtbd]
  "2": { goals: ["— to define alongside step 2 —"], tools: [] }
  "3": { goals: ["— to define alongside step 3 —"], tools: [] }
  "4": { goals: ["— to define alongside step 4 —"], tools: [] }
  "5": { goals: ["— to define alongside step 5 —"], tools: [] }
  "6": { goals: ["— to define alongside step 6 —"], tools: [] }
status: draft
version: 0.2.1
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

### 2026-07-18 — interview re-added as a tool
- **From → To:** step-1 `tools` gained `interview` — now that it's an authored **research tool**
  (`kind: research`, prepares goal/portrait/questions/interviewer-guide → `sources/`), it's the
  primary discovery method for this stage, not just an input slot.
- **Why:** the earlier cleanup dropped it because it was an unauthored source-slot; that premise
  changed when `library/interview/` was written. A discovery stage without interview in its tool
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
