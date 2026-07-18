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
    tools: [segmentation, value-definition, segment-cvp]
  "2":  # Analysis
    goals:
      - Re-read the market for expansion arenas and emerging threats (new entrants, commoditization, platform shifts)
      - Track competitor dynamics from live data — who's gaining, whose strategy is working
      - Name the sharpest threat to DURABLE growth (moat erosion) as the "so what"
    tools: [analytics-search, competitor-analysis, market-sizing, substitutes]
  "3":  # Strategy
    goals:
      - Sharpen how-to-win around DEFENDING the moats that make growth durable, plus the next expansion segment/market
      - Revisit pricing & packaging for expansion (new tiers/segments) without eroding the core
      - Frame expansion + defense as testable bets; watch for a segment shift signaling a new opportunity
    tools: [where-to-play-how-to-win, value-definition, pricing, channels-expansion, uvp-cpv, segment-cvp, risk-mitigation]
  "4":  # Strategic Plan
    goals:
      - Re-forecast off a working model; optimize the metric tree around the levers with the best marginal return
      - Analyze retention by cohort/segment — protect the retained core as scaling adds lower-intent users
      - Keep unit economics honest at scale (CAC inflation, COGS, capacity caps) in both bases
    tools: [metric-tree, retention-analysis, unit-economics, financial-model, risk-mitigation, hypothesis-test-design]
  "5":  # Tactical Plan
    goals:
      - Pick the growth levers whose movement compounds this period; set guardrails so scale doesn't erode retention/economics/defensibility
      - Test expansion bundles (new segments/channels) with pre-set decision rules
      - Balance load across directions; surface scaling blockers early
    tools: [prioritization, metric-tree, guardrails, segment-cvp, hypothesis-test-design, resource-check]
  "6":  # Sprint Plan
    goals:
      - Must-set = scale-and-defend items that move a growth lever or hold a guardrail; instrument before optimizing
      - Every item moves a metric node or defends one; defer nice-to-haves to backlog
      - Handoff includes the guardrail checks the team must watch during rollout
    tools: [prioritization, feature-spec, activity-spec]
status: draft
version: 0.3.0
updated: 2026-07-18
---

# Status: growth

A working, profitable product. The goal is to **develop and expand** it — scale acquisition and
revenue within guardrails, open new segments/markets, and defend the moats that make growth
durable.

Evidence is dominated by **internal product metrics**. At the passport level the job is mostly
to keep it honest against reality and catch shifts early.

## Change log

### 2026-07-18 — filled per_step for steps 2–6
- **From → To:** steps 2–6 were `— to define —` stubs → concrete growth-stage goals + tools:
  expansion-arena + threat re-read (2); defend-the-moat how-to-win + expansion pricing (3);
  re-forecast + cohort retention + honest-at-scale economics (4); compounding levers within
  guardrails + expansion-bundle tests (5); scale-and-defend must-set (6). Added the new tools
  (`pricing`, `retention-analysis`, `segment-cvp`) where they fit, and `segment-cvp` to step 1.
- **Why:** an empty per_step parameterized only step 1; the framework nears release and the growth
  stage needed its full guidance. Filled by design (goals lean scale + defense on internal metrics)
  ahead of a live growth run, per the user's release push — to be sharpened on the first real run.
- **Trigger:** per_step fill pass, 2026-07-18.

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
