---
name: to-table
kind: adapter
mode: table
consumes: [registers, artifacts]
reads_ids: [hypotheses, risks, metric-tree, metrics.csv, "<any artifact section with a table>"]
produces: A flat, shareable table (CSV / markdown / spreadsheet-ready) from a register or artifact section
formats: [csv, markdown, tsv]
opinionated: false
status: draft
version: 0.1.0
updated: 2026-07-18
---

# to-table

Render a **register or an artifact section** into a **flat, shareable table** — a hypothesis
scoreboard, the metric series, the market-bundle registry, a sprint backlog — in CSV (for
Sheets/Excel), markdown (for a doc/PR), or TSV.

**What it is for.** The instance already holds tables (registers, skeleton sections). `to-table`
*selects*, *flattens*, *filters*, and *reshapes* them into the exact table a human wants to paste
into a spreadsheet or a report — without hand-copying, and re-runnable when the source changes.

## What it consumes
- A **named source**: a register (`hypotheses` · `risks` · `metric-tree` + `metrics.csv`) or an
  artifact section by its stable id (e.g. `tactical-plan#market-bundles`, `sprint-plan#backlog`).
- The **columns** to keep and their order (defaults to the source's own columns).
- Optional **filter** (e.g. `status = testing`), **sort** (e.g. by score), and **derived columns**
  (e.g. a RICE score computed from existing fields — state the formula).

## How to render
1. **Resolve the source.** Read the register / section by id. If it's the metric register, join
   `metric-tree.md` (definitions) with `metrics.csv` (values) on `id` — never invent values; use the
   latest reading per `measured_at`, or emit the full series if a time table is asked for.
2. **Select & order columns.** Keep only requested columns; preserve register IDs (`H-…`/`R-…`/`M-…`)
   as the first column so the table stays linkable back to source.
3. **Filter & sort** as asked. State the filter/sort applied in a caption so the view is reproducible.
4. **Compute derived columns explicitly.** If asked for a score/ratio, show the formula in the
   caption; mark any input that was `[assumption]` so a soft number isn't read as hard.
5. **Emit in the requested format.** CSV with a header row for spreadsheets; a markdown table for
   docs/PRs; TSV on request. Keep confidence tags in a column (don't drop them silently).
6. **Stamp provenance.** Add a caption line: source id(s), filter/sort, and the date rendered — so a
   pasted table says what it is and when it was true.

## Output shape

```
# Hypotheses — status=testing, sorted by born  (source: registers/hypotheses.md · 2026-07-18)
id,statement,type,status,born,test,confidence
H-007,"pain A blocks payment",viability,testing,step1,tactical-plan#hypotheses-to-test,assumption
```

or markdown:

```markdown
_Source: `tactical-plan#market-bundles`, readiness=ready, sorted by signal tier · 2026-07-18_

| ID | Segment | CVP | Offer | Channel | Signal · tier | H-… |
|----|---------|-----|-------|---------|---------------|-----|
| B-01 | … | … | … | … | trial · strong | H-012 |
```

## Anti-patterns
- **Editing the rendered table as the source.** It's a view; change the register/section and re-run.
- **Dropping IDs or confidence.** A table with no `H-…`/`M-…` can't be linked back; a table with no
  confidence tag reads assumptions as facts.
- **Inventing values.** If a metric has no reading in `metrics.csv`, show `—`, don't fabricate.
- **Silent filters.** A filtered view with no caption misleads — always state what was included.

## Company specialization
A company adapter can wrap `to-table` to emit a specific internal form (e.g. a scoring sheet in a
fixed column order). It re-skins the output; the selection/flattening logic stays here.
