---
node_type: worklog
tool: feature-spec
step: 6
title: "feature specs — Sprint 1"
updated: 2026-08-16
version: 0.1.0
---

# feature specs — the working (Sprint 1)

_Source of truth for the **Development → Features** blocks of `6-sprint-plan.md#must` / `#backlog`.
Each dev item at grooming altitude (a feature, not sub-tasks): Description · Scope · Acceptance
criteria (binary) · Business value (the `M-…`/`H-…` it serves) · User value · User stories. The
ranking/line comes from `prioritization-sprint-plan`; this owns the feature rows._

## Must

### F-1 · Native-export engine — first vertical slice (`.pptx`) — links `H-001` · `M-design-acceptance`
- **Description:** the core generator → **valid, natively-editable `.pptx`** on the primary template
  families (title, agenda, content, chart, closing) — the "editable" half of the wedge, first slice.
- **Scope:** brief→outline→layout mapping; native `.pptx` shape/text/theme emission; theme-token
  application; a smoke set of ~10 briefs across the primary verticals.
- **Acceptance criteria (binary):** (1) exported `.pptx` opens clean in PowerPoint **and** Google
  Slides with **no repair prompt**; (2) every text box and shape is **natively editable** (no
  flattened images); (3) every slide renders the single applied theme's tokens — **no off-theme
  colour**; (4) the ~10-brief smoke set exports without a hard failure.
- **Business value:** the enabler bet `H-001`; moves `M-design-acceptance` (and unblocks the whole
  metric tree). Without this slice the period gate (A) is unreachable.
- **User value:** a client-ready deck the maker can edit in their own tool — zero rebuild.
- **User stories:** *As an agency deck-maker, I want the AI's deck as a real editable `.pptx`, so that
  I can tweak a slide without rebuilding it from a screenshot.*
- **Owner:** founder-engineer ⚙️ · **Estimate:** the sprint's heavy build (~1.3 dev-FTE).

### F-2 · Design-acceptance / edit-behaviour instrumentation — links `M-design-acceptance`/`M-northstar` · `R-012`
- **Description:** capture the **proxy** signal behind the North Star's "kept" clause — did the maker
  export without a full in-app restyle — so F-1 can be *read*, not eyeballed.
- **Scope:** instrument export events, in-app restyle-before-export events, per-vertical tagging; a
  minimal internal dashboard for the eval read.
- **Acceptance criteria (binary):** (1) every native export emits an event with vertical + a
  restyle-before-export flag; (2) `M-design-acceptance` is computable from instrumented data for the
  F-1 smoke set; (3) events land in the store the eval harness (F-3) will read.
- **Business value:** closes the `R-012` instrumentation gap early; makes `M-design-acceptance` /
  `M-northstar` readable. Gate (A) is unmeasurable without it.
- **User value:** indirect — it's the measurement that keeps the "designed" promise honest.
- **User stories:** *(internal)* *As the PO, I want each export's acceptance captured, so that the
  H-001 eval reads itself instead of being argued.*
- **Owner:** engineer ⚙️ · **Estimate:** ~0.5 dev-FTE (scoped lean).

## Backlog

### F-3 · Eval harness (≥50 briefs × ≥5 verticals) — links `H-001` · `M-design-acceptance`
- **Description:** the standing test set + runner that executes the `H-001` design-acceptance eval
  (the Step-5 test design) against F-1's output.
- **Scope:** curate ≥50 briefs across ≥5 verticals; batch-run through F-1; score via F-2's instrumented
  acceptance; report per-vertical.
- **Acceptance criteria (binary):** (1) ≥50 briefs across ≥5 verticals run end-to-end; (2) a
  per-vertical `M-design-acceptance` number is produced; (3) the run is repeatable on a new engine
  build.
- **Business value:** the instrument that reads `H-001` against its ≥70%/<40% bar (`5#hypotheses-to-test`).
- **User value:** indirect (quality assurance of the designed promise).
- **User stories:** *(internal)*.
- **Owner:** engineer ⚙️ · **Estimate:** ~0.4 dev-FTE (backlog — fires once F-1 emits).

### F-4 · Second export format (`.key` / Keynote) — links `H-001` · `R-006`
- **Description:** extend native export to Keynote `.key` for the macOS-heavy S1 slice.
- **Scope:** `.key` emission from the same layout model; fidelity tests across Keynote versions.
- **Acceptance criteria (binary):** (1) `.key` opens clean in Keynote with no repair; (2) shapes/text
  natively editable; (3) fidelity test suite passes on the current Keynote version.
- **Business value:** widens `H-001` coverage; touches `R-006` (format dependency).
- **User value:** Keynote-native makers get the same zero-rebuild deck.
- **User stories:** *As a Mac-based consultant, I want a real `.key` file, so that I edit in Keynote,
  not a converter.*
- **Owner:** engineer ⚙️ · **Estimate:** ~0.6 dev-FTE (backlog — after the `.pptx` slice proves out).

## Change log

### 2026-08-16 — Sprint-1 feature specs written
- **From → To:** — → F-1/F-2 (must) + F-3/F-4 (backlog) specced at grooming altitude, each with
  binary acceptance criteria and an `H-…`/`M-…` link
- **Why:** Step 6 hands development items to the team's process at feature altitude; a feature with no
  link or no checkable "done" is a candidate to cut
- **Trigger:** Step 6 pass, Development subsections of `#must`/`#backlog`
