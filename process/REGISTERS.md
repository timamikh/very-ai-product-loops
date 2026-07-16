---
node_type: registers
title: Registers — metrics, hypotheses, risks
status: draft
version: 0.1.0
updated: 2026-07-16
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

## Metric tree (`metric-tree.md`)

A decomposition, not a flat list: **North Star → drivers → input metrics**.

| Field | Values / notes |
|-------|----------------|
| `id` | `M-northstar`, `M-activation`, … |
| `name` / `definition` | what it is, precisely |
| `parent` | the node it feeds (builds the tree) |
| `values` | **time series** — dated entries appended, never overwritten (`2026-07-16: 12.3%`) |
| `target` | the goal + horizon |
| `owner` | who owns it |
| `source` | metric source slot |

Time-series values follow "everything is dated, nothing is overwritten": each reading is a new
dated line, so the trend is visible, not just the latest number.
