---
node_type: registers
title: Registers — metrics, hypotheses, risks
status: draft
version: 0.8.0
updated: 2026-08-15
---

# Registers

Three living, vertical objects, shared across all steps. Born once, refined downward, results
flowing back up — **not re-authored per step**. In an instance they live in `product-loops/registers/`.
Follow [`CONVENTIONS.md`](CONVENTIONS.md) for IDs, confidence, and dated change logs.

| Register | Born at | Refined at |
|----------|---------|------------|
| Hypotheses | Step 1/3 | 4 (quantify) → 5 (test design) → 6 (experiment tasks) |
| Risks | Step 2 | 3 (product) → 4 (mitigation) → 5 (period blockers) |
| Metric tree | Step 4 | 5 (select nodes) → 6 (task ↔ metric) |

## What earns a register — the four-sign test

A fourth register is a change to the load-bearing core, so a candidate is **tested, not argued**, on
all four signs: a stable cross-step id · an enumerable lifecycle (`status`) · a life outlasting the step
that bore it · state that flows both ways. Fail one and the home is a step artifact section instead. The
full test, its two guards, and the open `segments` candidate are in [`EXTENDING.md`](../EXTENDING.md) →
*What earns a register*.

## Hypothesis register (`hypotheses.md`)

Every bet/assumption becomes an entry. Fields:

| Field | Values / notes |
|-------|----------------|
| `id` | `H-001`, … (stable) |
| `statement` | the hypothesis, falsifiable |
| `type` | `desirability` · `feasibility` · `viability` · `usability` |
| `tags` | free cross-cutting themes (*moat*, *pricing*) — never compounded into `type`, never load-bearing |
| `status` | `open` · `testing` · `validated` · `refuted` · `superseded` (never delete — refuted stays; `superseded` = split in two, not disproved) |
| `born` | step it originated in |
| `source` | where it came from |
| `test` | link to the test design (Step 5) / experiment (Step 6) |
| `confidence` | `assumption` · `sourced` · `validated` · `refuted` |
| `signal` | *post-test* — the observed market response, graded: `weak` (click · like · page-view — channel diagnostics, not a result) · `medium` (lead · sign-up · reply · details request) · `strong` (meeting with a real DM · trial access · price talk · pilot · pre-pay · sale). Empty until read. |
| `decision` | *post-test* — the call the readout drives: `scale` · `iterate` · `reject` · `research` (return to discovery). Distinct from `status`: a bet can be `validated`/`scale` or `refuted`/`reject` or partially-true/`iterate`. Empty until read. |

**One `type` per hypothesis** (`desirability` · `feasibility` · `viability` · `usability` — the classic
product-risk taxonomy). A cross-cutting theme (*moat*, *pricing*) is **not** a fifth type — it goes in
the free `tags` column, never compounded into `type` (`viability/moat` is wrong — write `type:
viability`, `tags: moat`). A hypothesis needing **two verdicts** is **split in two at the first attempt
to test it** (Step 4, when a metric is attached): the halves name the original, and the original closes
as `superseded` — not `refuted`; it was divided, not disproved. Risks follow the same shape below:
**exactly one `category`**, extra themes in `tags`. This id/type taxonomy is defined **here**;
`CONVENTIONS.md` only carries the link form that references it.

`signal` and `decision` are **gradations** (ordinal, in the row), orthogonal to the confirmation
marker a human signs — see [`CONVENTIONS.md`](CONVENTIONS.md) *Gradation vs confirmation*. A
**refuted** bet, or a `reject`/`research` decision, is a signal: it can trigger an upward revisit
(see step cadence/invalidation). Which bets enter a test is a **priority score** (1/3/5 on pain
acuteness · segment reach · product fit · pay potential · test speed) — a selection scale owned by
[`hypothesis-test-design`](../tool-skills/library/hypothesis-test-design/SKILL.md), not a register
column.

## Risk register (`risks.md`)

| Field | Values / notes |
|-------|----------------|
| `id` | `R-001`, … |
| `description` | the risk |
| `category` | market · product · execution · legal · financial · dependency |
| `tags` | free cross-cutting themes — same rule as hypotheses: never compounded into `category` |
| `likelihood` | H/M/L — tiers backed by 5/3/1 for ranking (H=5 · M=3 · L=1) |
| `impact` | H/M/L — same 5/3/1 backing |
| `mitigation` | the plan (added Step 4) |
| `owner` / `due` | who, by when (added Step 4/5) |
| `status` | `open` · `mitigating` · `contained` (mitigated but still live) · `realized` (it fired) · `closed` · `accepted` (carried un-mitigated on purpose) |
| `source` | where it surfaced |

Carried risks are **ranked by likelihood × impact** on the 5/3/1 tiers — the numeric backing is
what makes the product a real ordering rather than a pile of "high"s. The scale and the pre-mortem
that feeds it are owned by
[`risk-mitigation`](../tool-skills/library/risk-mitigation/SKILL.md).

## Metric register (`metric-tree.md` + `metrics.csv`)

A decomposition, not a flat list: **North Star → drivers → input metrics**. One canonical split
(per CONVENTIONS "One mechanism, one way"): **definitions in markdown, values in CSV** — always,
from the first capture; no md-cell time series, no transition thresholds.

**`metric-tree.md` — node definitions only:**

| Field | Values / notes |
|-------|----------------|
| `id` | `M-northstar`, … — **exactly one id per row** (ids sharing a definition are separate nodes, else their csv series point at nothing), and **a changed definition mints a NEW id**, never reuses the old one (else the series silently compares incomparables) |
| `name` / `definition` | what it is, precisely — incl. what it excludes and, for an outcome/cohort node, **the observation window** (the outcome is countable only once that window has elapsed) |
| `unit` | $ · € · % · count · … (a property of the node, not of a reading) |
| `kind` | `measured` (captured) · `derived` (computed — state the formula) |
| `parent` | the node it feeds (builds the tree); `— to clarify —` before Step 4 |
| `population` | who is counted **by default** — all accounts · paying · a named cohort. An empty `population` in the csv means *this* value; never a sentence standing nearby |
| `instrumentation` | `instrumented` · `proxy` · `not-instrumented` — where the data comes from, or why it can't yet |
| `target` | the goal + horizon |
| `owner` | who owns it |
| `source` | metric source slot |
| `note` | what an enum cell may not carry (`since 2026-05`, `manual pass`, a caveat). **An enum cell holds the bare value** — the qualifier goes here, the theme in `tags` |

**`metrics.csv` — append-only dated readings**, one row per reading:

```csv
id,period_start,period_end,measured_at,value,observed_n,population,basis,source,note
```

- `measured_at` = when the reading was taken; `period_start/period_end` = what interval the value
  describes (empty for point-in-time values). Collapsing these into one date makes every
  trailing-window metric ("last 30d") lie to trend readers.
- `observed_n` = how many of the population **could already have shown the outcome** — the
  denominator of a rate. A cohort metric divides by the observed, never by the whole cohort: the
  un-observed produce a plausible number that is simply false, and the error survives into every
  comparison (two groups then "differ" by their age, not their behaviour). **An empty `value` means
  the outcome was not observable yet** — never a word inside a numeric column.
- `basis` = **how the value was computed**, and nothing else (`operational` · `with_depreciation` ·
  `metered` · `fact` …). *Who* was counted is `population`; *which slice* is a node of its own. One
  column cannot mean three things: rows are comparable across `basis`, and are not across
  `population`.
- Rows are appended, never edited or deleted. Every `id` in the csv must exist in
  `metric-tree.md` (the md file is the authority on which ids exist and what they mean).
- **Checked after every csv write** — `python3 tools/lint.py <instance>` (check E): every id in
  `metrics.csv` must be defined in `metric-tree.md`. A csv id with no definition is a typo or an
  orphan reading — fix it before moving on.

**Where metric readings live (hard rule).** Any captured metric value — from an admin panel, an
export, an analytics query — goes into **`metrics.csv` as a dated row at capture time**, even
before Step 4 builds the tree. A raw capture (a snapshot file in `sources/`) is *evidence of the
reading*, not its home: the csv holds the series, the source holds the how/where/context, and
they link to each other. A metrics snapshot that lives only in `sources/` breaks the register's
whole purpose — the visible trend.
