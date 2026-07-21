---
node_type: renderers-index
title: Decksmith — renderer scripts
status: draft
version: 0.1.0
updated: 2026-07-21
---

# Renderers — Decksmith

The scripts that render this instance's [deliverables](../deliverables/). Kept **here, with the
instance** — not in `deliverables/` (results only) and not in the base
[`tool-skills/adapters/`](../../../tool-skills/adapters/) folder (which stays instance-agnostic).
Each is a concrete, one-off implementation of a base adapter for the decksmith data.

| Script | Adapter | Output | Requires |
|--------|---------|--------|----------|
| [`render_brief.py`](render_brief.py) | `to-document` | `../deliverables/concept-brief.docx` | `python-docx` |
| [`render_tables.py`](render_tables.py) | `to-table` | `../deliverables/decksmith-registers-and-plan.xlsx` | `openpyxl` |

Run from this folder: `python3 render_brief.py && python3 render_tables.py`. Both read the instance
as the source of truth and overwrite the deliverable — re-run after any artifact/register change.
