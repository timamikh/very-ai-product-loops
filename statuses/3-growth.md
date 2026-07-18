---
node_type: status
name: growth
order: 3
gate_emphasis: >
  Weigh sustainable, guardrailed scaling over one-off spikes. Check that growth does not erode
  retention, unit economics, or defensibility.
per_step:
  "1":  # Idea / Concept
    goals:
      - Keep the passport true to what metrics now show; revise stale assumptions
      - Watch for a segment/pain shift that signals a new opportunity or a pivot
    tools: [segmentation, value-definition]
  "2": { goals: ["— to define alongside step 2 —"], tools: [] }
  "3": { goals: ["— to define alongside step 3 —"], tools: [] }
  "4": { goals: ["— to define alongside step 4 —"], tools: [] }
  "5": { goals: ["— to define alongside step 5 —"], tools: [] }
  "6": { goals: ["— to define alongside step 6 —"], tools: [] }
status: draft
version: 0.2.1
updated: 2026-07-18
---

# Status: growth

A working, profitable product. The goal is to **develop and expand** it — scale acquisition and
revenue within guardrails, open new segments/markets, and defend the moats that make growth
durable.

Evidence is dominated by **internal product metrics**. At the passport level the job is mostly
to keep it honest against reality and catch shifts early.

## Change log

### 2026-07-18 — step-1 tools cleanup (audit)
- **From → To:** step-1 `tools` dropped `analytics-search` (a source slot / input, not a library
  tool). Steps 2–6 stay stubbed until a run on this stage fills them.
- **Why:** `tools` should list library methods; gathering is expressed via a tool's `inputs`
  (analytics as an input is still described in the body).
- **Trigger:** framework audit, 2026-07-18.

### 2026-07-16 — per-step structure
- **From → To:** flat lists → per_step goals + tools (step 1 filled)
- **Why:** per-step focus (see OPERATING-LOOP.md)
- **Trigger:** review feedback on PR #2

### 2026-07-16 — created
- **From → To:** — → initial default status definition
- **Trigger:** Phase 1 (golden exemplar)
