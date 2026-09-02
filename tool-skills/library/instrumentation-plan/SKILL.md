---
node_type: card
kind: method
name: instrumentation-plan
steps: [4]
prerequisites: [the step-3 architecture sketch, the step-3 product-surface map]
reads: [section:architecture, section:product-surface, section:unit-economics, register:metric-tree, register:metrics, source:kb, source:git]
writes: [worklog, section:architecture-instrumentation]
opinionated: false
method_basis: "Instrumentation mapping: component → instrumented/proxy/not-instrumented → data yielded → infra cost driven; every metric node needs a data source or an explicit gap"
evidence_standard: decision
volume_rule: n/a
selection_rule: n/a
rejects_shown: n/a
status: draft
version: 0.1.2
updated: 2026-09-02
---
# Instrumentation Plan

Refine Step 3's `#architecture` and `#product-surface` into one measurability map: for every
**component**, its instrumentation state (**instrumented / proxy / not-instrumented**), the **data
it yields**, and the **infra cost it drives**. Every future metric-tree node needs a data source
here or an explicit gap; the not-instrumented list feeds Steps 5–6 as work items. Fills
`{#architecture-instrumentation}` — this method is that section's single owner (one section — one
method).

**Method basis.** Instrumentation mapping: strategy becomes measurable only where a component
actually emits data. The map crosses the architecture (what exists) with the surface (where users
touch it) and answers, per component: can we measure it, with what fidelity, at what infra cost.

> **Relation to neighbours (one mechanism, one way).**
> - `architecture-c4` (Step 3) sketches the system and its dependencies; `product-surface` (Step 3)
>   maps the touchpoints. This method **refines both into the Step-4 instrumentation map** — it does
>   not redraw the architecture or re-list the surfaces.
> - This method **owns the per-surface instrumentation status** (`instrumented | proxy |
>   not-instrumented`) and the **not-instrumented work list at surface level**. `metric-tree`
>   projects that status onto its nodes — a node carries the mark of the surface its data comes
>   from, or an explicit gap — and never re-marks a surface.
> - The infra cost drivers named here must **reconcile with `unit-economics`' COGS lines** — a cost
>   driver with no COGS line (or vice versa) is a hole in one of the two.

## When to apply
- **Step 4**, before (or alongside) `metric-tree` — the tree's instrumentation column reads off
  this map.
- When a new component or surface ships, or a proxy is upgraded to real instrumentation — update
  the map, then the affected `M-…` nodes.

## Prerequisites
- **The Step-3 architecture sketch** (`3-strategy.md#architecture`). *Missing → run
  `architecture-c4` first.*
- **The Step-3 product-surface map** (`3-strategy.md#product-surface`). *Missing → run
  `product-surface` first.*

## How to do it
1. **List the components.** Union of the architecture's boxes and the surface's touchpoints —
   channels, landings, in-product UI, admin, integrations, external systems (LLM providers,
   analytics, email). One row per component.
2. **Mark each: `instrumented` / `proxy` / `not-instrumented`.** Exactly these three.
   `instrumented` = the event/measure exists and lands somewhere queryable; `proxy` = an indirect
   stand-in exists (name what it actually measures and where it lies); `not-instrumented` = no
   signal today. The mark comes from the analytics configuration or filed instrumentation docs
   (`source:kb`) or the codebase passport (`source:git`) — never from memory.
3. **Name the data each yields.** What events/measures the component produces (or would). This is
   the supply side of the metric tree: every `M-…` node already defined (`registers/metric-tree.md`,
   readings in `metrics.csv`) and every future one must trace to a row here — a node with no source
   row is an **explicit gap**, written down, not glossed.
4. **Name the infra cost each drives.** What the component costs to run and to instrument (LLM
   inference, analytics stack, session capture, email provider…). These drivers must reconcile with
   `unit-economics`' COGS lines (`{#unit-economics}`, when it already exists — on the first pass
   the check runs from that side) — flag any driver missing there, and any COGS line with no
   component here.
5. **Emit the not-instrumented list as work.** The `not-instrumented` rows (and the proxies worth
   upgrading) are a first-class output — they feed Steps 5–6 as instrumentation work items, sized
   and scheduled there.

## Anti-patterns
- **Redrawing the architecture.** Re-deriving boxes or dependencies here — that is Step 3's
  `architecture-c4`; this map refines, it does not redraw.
- **A proxy sold as instrumented.** Counting an indirect stand-in as real measurement without
  naming what it actually measures — the tree then steers by a lie.
- **Orphan metrics.** A metric-tree node with no component row and no explicit gap — wanting a
  number nowhere collected.
- **Silent gaps.** `not-instrumented` rows that never become Steps 5–6 work items — the gap list is
  an output, not a confession.
- **Cost drivers off the books.** An infra cost named here that appears in no `unit-economics` COGS
  line (or a COGS line with no component driving it) — the two must reconcile.

## Worklog & projection
Worklog: `4-strategic-plan/instrumentation-plan.md` — the component union from `3#architecture` + `3#product-surface`, each mark with what a proxy measures, the data yielded, the cost drivers with their COGS reconciliation, the not-instrumented work list. Projects `{#architecture-instrumentation}`; face: the **Measurability read** line, via [`template-fragment.md`](template-fragment.md). Path form, primary/contributing and revisit rules: [`worklog-resolution.md`](../../../process/reference/worklog-resolution.md).

## Output
Projects `{#architecture-instrumentation}` via [`template-fragment.md`](template-fragment.md) from
the worklog; inputs via [`questions.yaml`](questions.yaml). Supplies the instrumentation marks
`metric-tree` reads, the not-instrumented work list for Steps 5–6, and the infra cost drivers that
reconcile with `unit-economics`' COGS lines.
