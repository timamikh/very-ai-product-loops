---
node_type: reference
title: Which conventions apply where — the node_type matrix
status: draft
version: 0.2.0
updated: 2026-08-16
---

# Which conventions apply where

*Read this when in doubt **which conventions apply** to a file. The one-line pointer stays in*
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Which conventions apply where*.

Conventions are **not** uniform across file types — applying all of them everywhere creates the
same on-the-fly ambiguity "one mechanism, one way" is meant to kill (does a source file need a
change log? does a register need inline confidence tags when confidence is already a column?).
The matrix below is authoritative; a file's `node_type` (frontmatter) selects its row.

| `node_type` | Confidence tags | Section IDs | Register/item IDs | Change log | Notes |
|-------------|-----------------|-------------|-------------------|------------|-------|
| `artifact` (step outputs) | **yes** — on every non-trivial claim | **yes** | reference by ID | **yes** | the full convention set; a **projection** of its worklogs (see CONVENTIONS *Step folders & worklogs*) |
| `worklog` (a method's working doc in a step folder) | **yes** — on every non-trivial claim | optional | reference by ID | **yes** — the step's history lives here | source of truth the artifact section projects from; one per `<tool>`, named `<step-folder>/<tool>.md` |
| `register` (hypotheses/risks/metric-tree) | **no** in prose — `confidence` is a table column instead | n/a | **defines** the IDs | **yes** | values obey the metric-register split (see REGISTERS.md) |
| `source` (external-data notes) | **yes** — tag each captured fact | optional | reference by ID | **yes** | secrets/raw-data rules apply (see CONVENTIONS *Raw data & access*); only what comes from outside — a derivation is a `worklog` (`metrics-capture`) |
| `sources-index` | n/a | n/a | reference by ID | **yes** | navigation only; no captured values |
| `deliverable` (an authored export file in `export-files/` — a brief, an interview guide) | **yes** — on every non-trivial claim | n/a (a standalone file, no `{#anchors}`) | reference by ID | **yes** | authored by an outputs skill, signed by the human; itself the source of truth (unlike a rendered view, which regenerates) |
| `handoff` | tag any state that is an assumption | n/a | reference by ID | **yes** | never the home of rules or truth |
| framework files (`step`, `status`, `conventions`, `operating-loop`, `goal-map`, `library-*`, `template-fragment`, `reference`, …) | n/a | **yes** where sectioned | n/a | **no** — see root `CHANGELOG.md` | authored by maintainers; `version`-bumped, history in the central changelog |
| **instance exchange skill** (`<instance>/skills/<slug>/SKILL.md` — a pull/push procedure) | n/a — a procedure, not claims | **yes** where sectioned | reference by ID | **yes** — its own dated change log (it lives in the instance, not the repo CHANGELOG) | authored by the orchestrator, material choices human-confirmed; `cadence` in frontmatter, `last_run` in `state.yaml` — see [`boundary-layout.md`](boundary-layout.md) |

If a convention is marked n/a / no for a node_type, **omitting it is correct** — not a lapse.
A convention not listed here (e.g. "Talking to the human") is behavioral and applies always.
