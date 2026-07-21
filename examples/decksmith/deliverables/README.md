---
node_type: deliverables-index
title: Decksmith — deliverables (rendered views)
status: draft
version: 0.1.0
updated: 2026-07-21
---

# Deliverables — Decksmith

Rendered **views** of the instance, produced by the [adapters](../../../tool-skills/adapters/).
These are **projections**, not sources: the source of truth stays in the artifacts and registers
one level up. Change an artifact/register and **re-render** — never hand-edit a deliverable as if
it were the source.

| File | Adapter · profile | Rendered from |
|------|-------------------|---------------|
| [`concept-pitch-deck.html`](concept-pitch-deck.html) | `to-deck` · **concept-pitch** | `passport.md` · `analysis.md` · `strategy.md` · `strategic-plan.md` · `tactical-plan.md` · `sprint-plan.md` + registers |

**`concept-pitch-deck.html`** — a self-contained, presentable HTML deck (open it in any browser;
arrow/space/click to navigate). Neutral, house-agnostic styling per the base `to-deck` adapter; a
company adapter would re-skin it with a brand system without changing the structure or messaging.
