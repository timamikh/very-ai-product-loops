---
node_type: deliverables-index
title: Decksmith — deliverables (rendered views)
status: draft
version: 0.3.0
updated: 2026-07-21
---

# Deliverables — Decksmith

Rendered **views** of the instance, produced by the [adapters](../../../tool-skills/adapters/).
These are **projections**, not sources: the source of truth stays in the artifacts and registers
one level up. **This folder holds results only** — the small renderer scripts live in
[`../renderers/`](../renderers/). Change an artifact/register and re-render; never hand-edit a
deliverable as if it were the source.

| File | Adapter · profile | Rendered from | Regenerate |
|------|-------------------|---------------|------------|
| [`concept-pitch-deck.html`](concept-pitch-deck.html) | `to-deck` · **concept-pitch** | `passport` · `analysis` · `strategy` · `strategic-plan` · `tactical-plan` · `sprint-plan` + registers | (authored HTML) |
| [`concept-brief.docx`](concept-brief.docx) | `to-document` · **one-pager** | `passport` · `analysis` · `strategy` · `strategic-plan` · `sprint-plan` + registers | `python3 ../renderers/render_brief.py` |
| [`decksmith-registers-and-plan.xlsx`](decksmith-registers-and-plan.xlsx) | `to-table` · **one workbook, a tab per dataset** | `registers/hypotheses` · `registers/risks` · `registers/metric-tree` · `strategic-plan#global-hypotheses` · `sprint-plan#must`/`#backlog` | `python3 ../renderers/render_tables.py` |

**Formats by adapter (base, house-agnostic):**
- **`to-deck` → HTML** — a self-contained, presentable deck (open in any browser; arrow/space/click to navigate).
- **`to-document` → `.docx`** — a formatted, stakeholder-ready document (opens in Word/Pages/Docs). Requires `python-docx`.
- **`to-table` → `.xlsx`** — one workbook, a tab per dataset (per the one-table rule); opens in Excel/Sheets. Requires `openpyxl`.

A **company adapter** would re-skin any of these with a brand system (deck theme, doc template,
branded workbook) without changing the structure or the source data.
