---
node_type: deliverables-index
title: Decksmith — deliverables (rendered views)
status: draft
version: 0.4.0
updated: 2026-07-21
---

# Deliverables — Decksmith

Rendered **views** of the instance, produced by the [adapters](../../../tool-skills/adapters/).
These are **projections**, not sources: the source of truth stays in the artifacts and registers
one level up. **This folder holds results only** — the render logic is the **generic, instance-
agnostic** renderer that ships *with each adapter* (no decksmith-specific script anywhere). Change an
artifact/register and re-render; never hand-edit a deliverable as if it were the source.

| File | Adapter · profile | Rendered from |
|------|-------------------|---------------|
| [`concept-pitch-deck.html`](concept-pitch-deck.html) | `to-deck` · **concept-pitch** | all six step artifacts + registers (agent-authored HTML per `ADAPTER.md`) |
| [`concept-brief.docx`](concept-brief.docx) | `to-document` · **one-pager** | agent-authored brief markdown → styled by the generic renderer |
| [`decksmith-registers-and-plan.xlsx`](decksmith-registers-and-plan.xlsx) | `to-table` · **one workbook, a tab per dataset** | `registers/{hypotheses,risks,metric-tree}` + `strategic-plan#global-hypotheses` + `sprint-plan#backlog` |

## Regenerate (run from the repo root)
Only `.docx`/`.xlsx` use a shipped renderer (a library is required); HTML/CSV/markdown the agent authors directly per `ADAPTER.md`.

```sh
# tables — fully mechanical (parses the markdown tables from the instance)
python3 tool-skills/adapters/to-table/render.py examples/decksmith \
  --section "strategic-plan.md#global-hypotheses:Strategic plan" \
  --section "sprint-plan.md#backlog:Sprint plan" \
  --stamp 2026-07-21 \
  --out examples/decksmith/deliverables/decksmith-registers-and-plan.xlsx

# document — agent authors the brief content (per to-document ADAPTER.md), then style it:
python3 tool-skills/adapters/to-document/render.py <brief-content>.md \
  --out examples/decksmith/deliverables/concept-brief.docx
```

Notes: the workbook's **Sprint plan** tab is the backlog *table*; the three `must` items are
feature/activity/task specs (prose), so they live in `sprint-plan.md` and the deck/doc, not this
table. A **company adapter** would re-skin any output with a brand system without changing structure
or source data.
