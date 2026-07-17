---
node_type: registers
title: Registers — metrics, hypotheses, risks
status: draft
version: 0.3.0
updated: 2026-07-17
---

# Registers

Three living, vertical objects, shared across all steps. Born once, refined downward, results
flowing back up — **not re-authored per step**. In an instance they live in `product/registers/`.
Follow [`CONVENTIONS.md`](CONVENTIONS.md) for IDs, confidence, and dated change logs.

| Register | Born at | Refined at |
|----------|---------|------------|
| Hypotheses | Step 1/3 | 4 (quantify) → 5 (test design) → 6 (experiment tasks) |
| Risks | Step 2 | 3 (product) → 4 (mitigation) → 5 (period blockers) |
| Metric tree | Step 4 | 5 (select nodes) → 6 (task ↔ metric) |

## Hypothesis register (`hypotheses.md`)

Every bet/assumption becomes an entry. Fields:

| Field | Values / notes |
|-------|----------------|
| `id` | `H-001`, … (stable) |
| `statement` | the hypothesis, falsifiable |
| `type` | `desirability` · `feasibility` · `viability` · `usability` |
| `status` | `open` · `testing` · `validated` · `refuted` (never delete — refuted stays) |
| `born` | step it originated in |
| `source` | where it came from |
| `test` | link to the test design (Step 5) / experiment (Step 6) |
| `confidence` | `assumption` · `sourced` · `validated` · `refuted` |

A **refuted** hypothesis is a signal: it can trigger an upward revisit (see step cadence/invalidation).

## Risk register (`risks.md`)

| Field | Values / notes |
|-------|----------------|
| `id` | `R-001`, … |
| `description` | the risk |
| `category` | market · product · execution · legal · financial · dependency |
| `likelihood` | H/M/L |
| `impact` | H/M/L |
| `mitigation` | the plan (added Step 4) |
| `owner` / `due` | who, by when (added Step 4/5) |
| `status` | `open` · `mitigating` · `closed` · `accepted` |
| `source` | where it surfaced |

## Metric register (`metric-tree.md` + `metrics.csv`)

A decomposition, not a flat list: **North Star → drivers → input metrics**. One canonical split
(per CONVENTIONS "One mechanism, one way"): **definitions in markdown, values in CSV** — always,
from the first capture; no md-cell time series, no transition thresholds.

**`metric-tree.md` — node definitions only:**

| Field | Values / notes |
|-------|----------------|
| `id` | `M-northstar`, `M-activation`, … — **a changed definition mints a NEW id**, never reuses the old one (else the series silently compares incomparables) |
| `name` / `definition` | what it is, precisely — incl. what it excludes |
| `unit` | ₽ · $ · % · count · … (a property of the node, not of a reading) |
| `kind` | `measured` (captured) · `derived` (computed — state the formula) |
| `parent` | the node it feeds (builds the tree); `— to clarify —` before Step 4 |
| `instrumentation` | `instrumented` · `proxy` · `not-instrumented` — where the data comes from, or why it can't yet |
| `target` | the goal + horizon |
| `owner` | who owns it |
| `source` | metric source slot |

**`metrics.csv` — append-only dated readings**, one row per reading:

```csv
id,period_start,period_end,measured_at,value,basis,source,note
```

- `measured_at` = when the reading was taken; `period_start/period_end` = what interval the value
  describes (empty for point-in-time values). Collapsing these into one date makes every
  trailing-window metric ("last 30d") lie to trend readers.
- `basis` = the value's qualifier when one node legitimately carries variants
  (`operational` · `with_depreciation` · `metered` · `fact` …) — a parseable column, never prose
  in `note`.
- Rows are appended, never edited or deleted. Every `id` in the csv must exist in
  `metric-tree.md` (the md file is the authority on which ids exist and what they mean).

**Where metric readings live (hard rule).** Any captured metric value — from an admin panel, an
export, an analytics query — goes into **`metrics.csv` as a dated row at capture time**, even
before Step 4 builds the tree. A raw capture (a snapshot file in `sources/`) is *evidence of the
reading*, not its home: the csv holds the series, the source holds the how/where/context, and
they link to each other. A metrics snapshot that lives only in `sources/` breaks the register's
whole purpose — the visible trend.
