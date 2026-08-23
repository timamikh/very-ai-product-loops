---
node_type: sources-index
title: Sources index — Decksmith
updated: 2026-08-23
version: 0.3.0
---

# Sources index

The navigation map read **first** on every task, so an agent opens only the sources a task needs.
Roles: **access** (living — how to reach a source) · **evidence** (dated, immutable — a capture or
report). A source is **dispatched into worklogs** by `source-intake`, never linked from an artifact.
The "Dispatched into" column records which worklog(s) have absorbed each source.

| File <!--c:file--> | Role <!--c:role--> | Type <!--c:type--> | What it contains <!--c:what--> | In scope <!--c:in-scope--> | Out of scope <!--c:out-of-scope--> | Feeds steps <!--c:feeds--> | Dispatched into <!--c:dispatched--> | Confidence / freshness <!--c:conf--> |
|------|------|------|------------------|----------|--------------|-------------|-----------------|------------------------|
| `sources/originals/founder-brief.md` | evidence | kb | The raw idea and the founder's early bets at kickoff: the "editable vs designed" fork, observed pains (templated look, wrong story), lead segment (sales & marketers), riskiest bet (feasibility), and explicit out-of-scope (collaboration, non-slide formats, pricing). | The whole brief — it is the origin the concept is built from. | Nothing excluded; it is the sole product input by design. | 1 (concept) primarily; feasibility bet also informs 3–4; pricing deferral noted for 3. | `1-concept/concept-formation.md`, `1-concept/jtbd-concept.md`, `1-concept/segmentation.md`, `1-concept/segment-pains.md`, `1-concept/concept-expansion.md`, `1-concept/value-definition-concept.md` | Captured 2026-07-16; fictional sample. Founder's bets are `[assumption]`; the observed pains are `[sourced: founder brief]`. |
| `sources/access/product-analytics.md` | access | metrics | Passport for the product analytics panel (fictional): what it is, location, owner, how to verify reach, how to recover access, secret handling. Recorded from the founder's setup answers — not evidence. | How to reach the point. | The values themselves (those arrive as dated snapshots, then land in the metric register). | 4–6 (activation/generation/export metrics) once the prototype ships. | Not dispatched — a passport is reached by the `pull-analytics-weekly` skill, not absorbed into a worklog. | Recorded 2026-08-18; fictional sample. Panel goes live with the prototype. |

## Change log

### 2026-08-23 — column keys + typed slots
- **From → To:** prose-only header → every column carries its `<!--c:key-->`; new `Type` column
  names the slot each source serves for a method's `reads:` (`kb` · `interview` · `research` ·
  `metrics` · `git` — the closed list in `cards.SOURCE_SLOTS`, held by lint check S2)
- **Why:** the index is the machine-checkable evidence map, and prose is not a carrier — an
  untyped row can't be matched against what a method declares it reads
- **Trigger:** run-2 follow-up — the evidence gate needs typed slots to become mechanical

### 2026-08-18 — analytics passport registered
- **From → To:** — → `sources/access/product-analytics.md` added; the `pull-analytics-weekly` skill
  reaches it and lands weekly counts via `metrics-capture`
- **Why:** boundary-layer instrumentation prep — give the weekly analytics pull a reachable,
  human-recorded destination so it never invents a source
- **Trigger:** framework 0.10 boundary layer

### 2026-08-18 — sources layout migrated
- **From → To:** `sources/founder-brief.md` → `sources/originals/founder-brief.md`
- **Why:** reorganized sources into `originals/` · `snapshots/` · `access/` subfolders
- **Trigger:** framework 0.10 boundary layer

### 2026-08-16 — created
- **From → To:** — → index created with the founder brief dispatched to the Step 1 worklogs
- **Why:** instance setup; the founder brief is the sole product input and is routed into the
  Step 1 concept worklogs via `source-intake` so the first Act pass finds its evidence in place
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
