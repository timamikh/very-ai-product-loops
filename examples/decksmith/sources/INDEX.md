---
node_type: sources-index
title: Sources index — Decksmith
updated: 2026-08-16
version: 0.1.0
---

# Sources index

The navigation map read **first** on every task, so an agent opens only the sources a task needs.
Roles: **access** (living — how to reach a source) · **evidence** (dated, immutable — a capture or
report). A source is **dispatched into worklogs** by `source-intake`, never linked from an artifact.
The "Dispatched into" column records which worklog(s) have absorbed each source.

| File | Role | What it contains | In scope | Out of scope | Feeds steps | Dispatched into | Confidence / freshness |
|------|------|------------------|----------|--------------|-------------|-----------------|------------------------|
| `sources/founder-brief.md` | evidence | The raw idea and the founder's early bets at kickoff: the "editable vs designed" fork, observed pains (templated look, wrong story), lead segment (sales & marketers), riskiest bet (feasibility), and explicit out-of-scope (collaboration, non-slide formats, pricing). | The whole brief — it is the origin the concept is built from. | Nothing excluded; it is the sole product input by design. | 1 (concept) primarily; feasibility bet also informs 3–4; pricing deferral noted for 3. | `1-concept/concept-formation.md`, `1-concept/jtbd-concept.md`, `1-concept/segmentation.md`, `1-concept/segment-pains.md`, `1-concept/concept-expansion.md`, `1-concept/value-definition-concept.md` | Captured 2026-07-16; fictional sample. Founder's bets are `[assumption]`; the observed pains are `[sourced: founder brief]`. |

## Change log

### 2026-08-16 — created
- **From → To:** — → index created with the founder brief dispatched to the Step 1 worklogs
- **Why:** instance setup; the founder brief is the sole product input and is routed into the
  Step 1 concept worklogs via `source-intake` so the first Act pass finds its evidence in place
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
