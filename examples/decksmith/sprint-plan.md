---
node_type: artifact
artifact: sprint-plan
product: Decksmith (fictional sample)
step: 6
status_stage: concept-viability
owner: sample
updated: 2026-07-21
version: 0.1.0
---

# Sprint Plan — Decksmith (fictional sample) · Sprint 1 (2026-07-21 → 2026-08-01, ~2 wk)

> Status: `concept-viability` · Owner: sample · Capacity: 1 feature · 1 activity · 2 tasks
> Inputs: `tactical-plan.md` · registers. Hands off to: the team's development process.
> **Every item this sprint must produce a learning signal toward the period gate `H-001`**
> (`M-edit-fidelity` ≥ 90%). Anything that tests no hypothesis is cut (status goal).

## Must {#must}
_Minimal mandatory items — without which the period goal is unreachable. Grouped by direction._
_Ranked by contribution to the gate: the export slice + its measurement harness are the concept-killer; the demand probe is cheap and parallel._

### Development — Features
<!-- tool: feature-spec, prioritization -->

**F-1 · Native `.pptx` export slice (generate → export one deck)** — links: `H-001` / `M-edit-fidelity`
- **Description:** The thinnest end-to-end path that proves feasibility — prompt in, one generated deck out as a real `.pptx` where shapes, text, and charts are **native objects**, not flattened images. No editor UI, no accounts; a single happy path.
- **Scope:**
  - Generate a deck structure from a prompt (reuse the existing LLM call).
  - Map generated content to native PPTX objects (text frames, shapes, one chart type, one image placeholder).
  - Export a downloadable `.pptx`.
  - Run it against the 20-deck test set (see `T-2` backlog) and log the fidelity read.
- **Business value:** Directly tests `H-001`, the concept-killer — nothing else matters if native fidelity fails. Feeds `M-edit-fidelity`.
- **User value:** A deck the user can actually open and edit in PowerPoint/Keynote without redoing it — the core wedge.
- **User stories:** _As a salesperson, I want to export a generated deck and edit every element in PowerPoint, so that I don't have to rebuild it by hand._

### Go-to-market — Activities
<!-- tool: activity-spec, prioritization -->

**A-1 · Seed the demand probe in one sales-enablement community (B-01)** — links: `H-005` / `M-activation`
- **Description:** A single, honest post in one revenue-ops / sales-enablement Slack describing the "editable designed deck you can actually edit in PowerPoint" wedge, offering an early trial slot — the first cheap read on demand, run in parallel with the build.
- **Scope:** draft copy → get community entry (see `R-009` blocker) → post → collect trial sign-ups in a simple form → tag each as qualified/not.
- **Business value:** First signal for `H-005` (wedge demand); builds the qualified-trial pool that `M-activation` will later read against.
- **Audience value:** Salespeople prepping client decks under time pressure get an early fix for "AI decks look templated and I can't edit them" — a real pain, not spam.
- **Links:** tests `H-005`, moves proxy for `M-activation`; runs on the community channel from bundle `B-01` (`tactical-plan.md#market-bundles`).

### Back-office — Tasks
<!-- tool: prioritization -->

**T-1 · Edit-fidelity measurement harness + export event capture** — links: `M-edit-fidelity` / `M-activation` · `R-007`
- **Description:** The instrument that reads the concept-killer: a repeatable way to score what fraction of objects in an exported deck are natively editable, plus event capture on generate/export/keep.
- **Definition of Done:** given a `.pptx`, the harness outputs an objects-editable % (native vs flattened) that a human can spot-check; `generate` / `export` / `keep` events land in analytics against `M-edit-fidelity` and `M-activation`.
- **Why:** Without an honest, repeatable fidelity read there is no `H-001` verdict — and no defence against the "flatten-to-image" shortcut the guardrail forbids.

## Backlog {#backlog}
_The rest, prioritized (not a flat list), grouped by direction. Same item formats as above._

| Rank | Direction | Item | Format | Links (`H-…`/`M-…`) | Est. | Confidence |
|------|-----------|------|--------|---------------------|------|------------|
| 1 | back-office | **T-2 · Assemble the 20 representative test decks** (layouts, charts, images that fairly stress fidelity) — DoD: 20 decks agreed as representative, versioned | Task+DoD | `M-edit-fidelity` · `R-007` | S | [assumption] |
| 2 | back-office | **T-3 · Abstract the LLM provider** behind one interface (swap without rewrite) — DoD: provider swappable via config; one alt tested | Task+DoD | `M-cogs-per-deck` · `R-004` | M | [assumption] |
| 3 | go-to-market | **A-2 · Intent SEO page "fix Gamma PPT export"** (B-03) — capture the Gamma-frustrated intent, route to trial | Activity | `H-005` / `M-activation` | M | [assumption] |
| 4 | development | **F-2 · Brand-kit intake** (upload colors/fonts → applied to export) for the marketer bundle B-02 | Feature | `H-007` / `M-activation` | M | [assumption] |
| 5 | development | **F-3 · Chart-fidelity hardening** (native editable charts beyond the one type in F-1) | Feature | `H-001` / `M-edit-fidelity` | M | [assumption] |

_Line drawn by capacity: the must-set (F-1 + A-1 + T-1) is the minimum that yields a Sprint-1 signal on the gate and fits 1 feature + 1 activity + 2 hands. T-2 is ranked #1 backlog because F-1's fidelity read depends on it — if the deck set slips, it gets pulled into must._

## Handoff {#handoff}
_What goes to the development process, and how (the framework ends here; work proceeds in the team's own flow)._

- **Handed off:** `F-1` and `T-1` to the eng pair's board; `A-1` to the founder. Items carry their `H-`/`M-` links so the reason each exists travels with it.
- **Acceptance / how results flow back:**
  - `F-1` + `T-1` produce the first `M-edit-fidelity` read → recorded in `registers/metrics.csv` against `M-edit-fidelity`.
  - A fidelity read **< 70%** refutes `H-001` → bubbles up to `tactical-plan.md#hypotheses-to-test` (rethink engine or pivot); **70–90%** → iterate the slice next sprint; **≥ 90%** → `H-001` toward `validated`, proceed.
  - `A-1` qualified-trial count feeds the `H-005` probe read in the Tactical Plan; a weak signal (≤ 2) reframes positioning, not the build.

## To clarify {#to-clarify}
- **"Objects-editable %" scoring rule** — which object types count, and does a partially-editable object count as pass or fail? (sharpens the `M-edit-fidelity` definition)
- **"Keep" event** — is export enough to count a qualified trial, or is an edit event required? (mirrors the open question in `tactical-plan.md` / Step 4)
