---
node_type: card
kind: method
name: product-baseline
steps: [3]
prerequisites: [something is live to inventory, a source to read it from (walkthrough / analytics / interview / git passport)]
reads: [register:features, register:surfaces, register:metrics, source:interview, source:metrics, source:git, source:kb]
writes: [worklog, section:product-surface, register:features, register:surfaces]
opinionated: false
method_basis: "As-is inventory from sources — every live surface and every live feature landed as `live` register rows with a source; drift against the register is the trigger, not a calendar"
evidence_standard: internal-data
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.0
updated: 2026-08-24
---
# Product Baseline (as-is inventory)

Build or refresh the **as-is state of the product** in the feature register: every surface the
product actually runs (`S-…`, `surfaces.md`) and every feature actually live on it (`F-…`,
`features.md`, `state: live`) — **from sources, never from memory**. The register's `live` rows ARE
the as-is; there is no separate as-is document to drift out of date. Contributes to
`{#product-surface}` (Step 3, second marker): the section keeps the strategic *why*, this method
keeps the ledger under it honest.

**Method basis.** Inventory from sources. A row without evidence does not appear: a product
walkthrough, an analytics read (via `metrics` slot), a team interview, or a bounded codebase
snapshot (via the `git` source passport — structure and services, never content). The unit is a
**feature, not a control**: "autopay" is a row; the checkbox that enables it is not.

## When to apply
- **Any status — the prerequisite gates it, not the status.** The method runs whenever *something*
  is live to inventory; with nothing shipped it skips by its own first prerequisite. A
  `concept-viability` product with a landing page, a waitlist or an MVP demo already has an as-is —
  three rows read from sources beat a register that pretends the product doesn't exist yet.
- **First full pass at `pmf`/`growth`** — the product exists, the register holds no `live` rows yet.
- **On drift** — a pass finds the register disagreeing with the real product (a feature shipped
  outside the loop, a surface retired quietly). Drift is the trigger; there is no calendar cadence.
- **After a major release** or when several sprints of `impact-readout` flips have accumulated and
  a reconciliation sweep is cheap insurance.

## Prerequisites
- **Something live to inventory.** *Nothing shipped yet → skip; this method has no subject.*
- **A source to read it from** — a walkthrough the human narrates, an analytics export, a team
  interview, or the codebase passport (`sources/access/`). *None → obtain access first; an
  inventory from memory is a guess wearing a table.*

## How to do it
0. **Assemble the sources before walking.** Read `sources/INDEX.md` for everything already filed
   under this method's slots (`interview` / `metrics` / `git` / `kb`), show the owner that list,
   and ask what is missing — a walkthrough they can narrate, an export they can pull, an access
   not yet passported. A source named here goes through `source-intake` first; a source that
   cannot be obtained is a declared gap in the worklog, not a silent hole in the inventory.
1. **Walk the surfaces first.** From `3#product-surface`, the channels list, and the source at
   hand: what does the audience actually meet today? Each gets an `S-…` row (`state: live`) with
   its source. A surface planned but not shipped stays `planned`; one quietly killed → `retired`.
2. **Inventory features per surface.** For each live surface, the features actually on it — at
   feature altitude (the row is "autopay", not its checkbox; "the AI content line", not post 123).
   Each `F-…` row: `direction`, `surface`, `serves` (the `M-…`/`R-…`/`H-…` it exists for — unknown
   is a finding, mark `— to clarify —`), `owner`, `[sourced: …]`.
3. **Reconcile, don't re-author.** Diff against the existing register: a `planned` row that turns
   out shipped → flip to `live` with a note (and ask why its readout never ran); a `live` row the
   product no longer has → `retired`; a feature the register never knew → a new `live` row and a
   process question (what shipped outside the loop?).
4. **Refresh the section.** Update `{#product-surface}` where the inventory moved it; the section
   cites `S-…` ids in prose. Deeper detail stays in the worklog and the register.
5. **Bound the codebase read.** When the source is the `git` slot: structure, services,
   integrations — an inventory, never a code review. The passport says where to look; everything
   else is noise this method exists to shield the loop from.

## Anti-patterns
- **Inventory from memory.** A row without a source is a decision the human never made — the
  grammar of evidence applies to the model of the product like to everything else.
- **Control-level rows.** A row per button/screen/post turns the register into a second backlog;
  the altitude is the feature.
- **Re-authoring instead of diffing.** Wiping and rewriting the register loses the ids everything
  links to; the pass edits states and adds rows, never renumbers.
- **Calendar ritual.** Refreshing on schedule when nothing drifted is paid work with no reader.

## Worklog & projection
The working is done in the step's **worklog** `<step-folder>/product-baseline.md` (`node_type:
worklog`, e.g. `3-strategy/product-baseline.md`): the source(s) read, the walkthrough notes, the
surface and feature inventories with their evidence, the reconciliation diff (flips, retirements,
strays), and the open `— to clarify —` serves-links. That worklog is the **source of truth**; the
register rows and the refreshed `{#product-surface}` lines are its projections
(`process/CONVENTIONS.md` → *Step folders & worklogs*).

## Output
`live` rows in `registers/features.md` / `registers/surfaces.md` (each `[sourced: …]`), the
reconciliation diff in the worklog, and a refreshed `{#product-surface}` via the section's primary
method. Downstream: Step-6 items link these `F-…`; Step-5 `impact-readout` flips the `planned` ones
this baseline did not create.
