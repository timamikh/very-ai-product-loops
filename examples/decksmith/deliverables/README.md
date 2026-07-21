---
node_type: deliverables-index
title: Decksmith — deliverables (rendered views)
status: draft
version: 0.2.0
updated: 2026-07-21
---

# Deliverables — Decksmith

Rendered **views** of the instance, produced by the [adapters](../../../tool-skills/adapters/).
These are **projections**, not sources: the source of truth stays in the artifacts and registers
one level up. Change an artifact/register and **re-render** (each output ships its small renderer
script) — never hand-edit a deliverable as if it were the source.

| File | Adapter · profile | Rendered from | Regenerate |
|------|-------------------|---------------|------------|
| [`concept-pitch-deck.html`](concept-pitch-deck.html) | `to-deck` · **concept-pitch** | `passport` · `analysis` · `strategy` · `strategic-plan` · `tactical-plan` · `sprint-plan` + registers | (authored HTML) |
| [`concept-brief.docx`](concept-brief.docx) | `to-document` · **one-pager** | `passport` · `analysis` · `strategy` · `strategic-plan` · `sprint-plan` + registers | `python3 render_brief.py` |
| [`hypotheses.csv`](hypotheses.csv) | `to-table` | `registers/hypotheses.md` | `python3 render_tables.py` |
| [`risks.csv`](risks.csv) | `to-table` | `registers/risks.md` | `python3 render_tables.py` |
| [`metric-tree.csv`](metric-tree.csv) | `to-table` | `registers/metric-tree.md` | `python3 render_tables.py` |
| [`strategic-plan-global-hypotheses.csv`](strategic-plan-global-hypotheses.csv) | `to-table` | `strategic-plan.md#global-hypotheses` | `python3 render_tables.py` |
| [`sprint-plan.csv`](sprint-plan.csv) | `to-table` | `sprint-plan.md#must` / `#backlog` | `python3 render_tables.py` |

**Formats by adapter (base, house-agnostic):**
- **`to-deck` → HTML** — a self-contained, presentable deck (open in any browser; arrow/space/click to navigate).
- **`to-document` → `.docx`** — a formatted, stakeholder-ready document (opens in Word/Pages/Docs). Requires `python-docx`.
- **`to-table` → CSV** — one table per file, opens directly in Excel/Sheets; first line is a provenance caption.

A **company adapter** would re-skin any of these with a brand system (deck theme, doc template, xlsx
workbook) without changing the structure or the source data.
