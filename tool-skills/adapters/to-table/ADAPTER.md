---
name: to-table
kind: adapter
mode: table
consumes: [registers, artifacts]
reads_ids: [hypotheses, risks, metric-tree, metrics.csv, "<any artifact section with a table>"]
produces: A shareable table from a register or artifact section — CSV by default; a single multi-tab .xlsx when several datasets are asked for together
formats: [csv, xlsx, markdown, tsv]
opinionated: false
status: draft
version: 0.2.0
updated: 2026-07-21
---

# to-table

Render a **register or an artifact section** into a **flat, shareable table** — a hypothesis
scoreboard, the metric series, the market-bundle registry, a sprint backlog — in CSV (for
Sheets/Excel), markdown (for a doc/PR), or TSV.

Unlike a deck, a table is **already human-consumable in these formats**: a **CSV opens directly in
Excel/Sheets** and a markdown table drops straight into a doc or PR. So the emitted CSV (or markdown)
file *is* the finished deliverable — not an intermediate step.

> **One-table rule.** If the human asks for "a table" and enumerates what should be in it, that is
> **one deliverable** unless they say otherwise. For a single dataset → one CSV. For several
> **heterogeneous** datasets asked for together (e.g. hypotheses + risks + metrics + a plan) → **one
> `.xlsx` workbook with a tab per dataset**, not a scatter of separate CSV files. Only split into
> multiple files when explicitly asked, or when the consumer needs raw CSV per source.

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
2. **Plan the columns first (write them down).** Before emitting a single row, state the schema
   explicitly: list each column, and for each one where its value comes from in the source. This is a
   required planning step — it prevents the classic failure where every field lands in one cell
   because the delimiter/structure wasn't planned. One field = one column; a row = one record.
3. **Select & order columns.** Keep only planned columns; preserve register IDs (`H-…`/`R-…`/`M-…`)
   as the first column so the table stays linkable back to source.
4. **Filter & sort** as asked. State the filter/sort applied in the provenance so the view is reproducible.
5. **Compute derived columns explicitly.** If asked for a score/ratio, show the formula in the
   provenance; mark any input that was `[assumption]` so a soft number isn't read as hard.
6. **Emit in the right format.** One dataset → **CSV** (header row first; do **not** put a comma-less
   caption on line 1 — a single-field line makes spreadsheets collapse everything into one column;
   put provenance in a trailing row or a sidecar). Several datasets asked for together → **one `.xlsx`**
   with a tab per dataset (header row bold/shaded, freeze the header, size columns to content).
   Markdown table for docs/PRs; TSV on request. Keep confidence tags in a column (don't drop them).
7. **Stamp provenance.** Record source id(s), filter/sort, and date rendered — in a `.docx`/`.xlsx`
   this is a caption cell or footer; for CSV, a sidecar or a clearly-marked trailing row (never a
   header-breaking first line).

## The renderer (shipped, generic)
Because `.xlsx` needs a library, this adapter ships a **generic, instance-agnostic** renderer here:
[`render.py`](render.py) — parses markdown tables from *any* instance and emits one styled `.xlsx`
(a tab per source) or CSVs (requires `openpyxl`). It holds **no product data**, so it travels with
the framework. Defaults to the three registers as tabs; add artifact-section tables with `--section`:

```sh
python3 render.py <INSTANCE_DIR> \
  --section "4-strategic-plan.md#global-hypotheses:Strategic plan" \
  --section "6-sprint-plan.md#backlog:Sprint plan" \
  --out <INSTANCE_DIR>/deliverables/tables.xlsx
```

(CSV and markdown output need no library — the agent can author those directly from this ADAPTER.)

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
fixed column order) or a single multi-tab `.xlsx` workbook. It re-skins the output; the
selection/flattening logic stays here.

## Change log

### 2026-07-21 — one-table rule, .xlsx for multi-dataset, column-planning step
- **From → To:** (1) added the **one-table rule** — "give me a table with X, Y, Z" means one
  deliverable, so several datasets → **one `.xlsx` workbook with tabs**, not scattered CSVs (`xlsx`
  added to `formats`). (2) Added a required **plan-the-columns-first** step (write the schema before
  filling) to stop fields collapsing into one cell. (3) Fixed the CSV provenance guidance — a
  comma-less caption on line 1 makes spreadsheets collapse to one column; use a trailing row/sidecar.
  (4) Affirmed CSV/markdown are finished deliverables (agent-readable → human-consumable).
- **Why:** decksmith live run — the user wanted one tabbed workbook, and a `#`-caption CSV rendered
  as a single column in the spreadsheet.
- **Trigger:** feedback on the first CSV render.
