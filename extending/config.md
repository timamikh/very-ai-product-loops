---
node_type: extending
title: Change an instance decision — config.yaml
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Change an instance decision

*Read this when what changes is a decision the product made, not a piece of the framework. The dial
table is in* [`../EXTENDING.md`](../EXTENDING.md); *the schema of every key is in*
[`../process/reference/config-schema.md`](../process/reference/config-schema.md).

`product-loops/config.yaml` holds the decisions the framework reads and never makes: the product's name,
the documentation language, the active stage, the execution streams, whether delegation is allowed. They
change by being said to the agent, and each change is a dated change-log entry with the **why**.

## Which key, and does it drag anything

| You want to change | Key | What it drags |
|---|---|---|
| the documentation language | `language` | nothing automatic — artifacts already written stay in their language until rewritten. The console's chrome follows it; product text never does |
| the active stage | `active_status` | the goals and recommended methods of every step change from the next pass on. Adding or renaming a stage is [`status.md`](status.md) |
| the execution streams of Steps 5–6 | `directions` | a real procedure — below |
| whether the orchestrator may spawn subagents | `delegation` | `off` means the orchestrator runs every pass itself and writes every worklog directly. Nothing else changes |
| what is in and out of scope | `scope_note` | prose the agent reads; no wiring |
| where a metric comes from | `metric_source_slots` | the *how to reach it* lives in its passport under `sources/access/<slug>.md` — **never a secret value in config** |

## Changing the work directions

**Directions** are the execution streams Steps 5–6 are organized around. The default is
`development` · `go-to-market` · `back-office`; the count and the names are an instance decision, not a
framework constant.

What depends on them, so you know what a change touches:

- **Steps 5–6 artifacts** (`5-tactical-plan.md`, `6-sprint-plan.md`) group their content by direction.
- **A status may split its per-step goals by direction** — a direction you remove leaves goals with
  nothing to attach to; a direction you add has no goals until the status file names them.
- **`directions` is a required key**, so the linter fails if it goes missing.

The procedure, run by the agent as one pass of the loop:

1. **Decide the streams from how the work is actually divided** — a direction is a stream someone owns,
   not a category of thought. Fewer and real beats many and tidy.
2. **Edit `directions`** in `product-loops/config.yaml`.
3. **Re-read the active status's `per_step` goals for Steps 5–6.** If they are split by direction, the
   agent proposes goals for a new stream (marked ⚙️) and flags orphaned ones for a removed stream.
4. **Re-organize the existing Step 5–6 artifacts** to the new streams. This is a normal pass: content
   moves, nothing is invented, anything with no home becomes `— to clarify —`.
5. **Dated change-log entry in each artifact touched** — with the *why*, not just the diff.
6. **`python3 tools/lint.py <instance>` — 0 errors.**

## Checklist

- [ ] The change is a decision the product made, not a piece of the framework bent to fit it.
- [ ] Every direction is a stream a person owns.
- [ ] No goal in the active status is left attached to a stream that no longer exists.
- [ ] Nothing moved into a Step 5–6 artifact that was not already there; every homeless item reads
      `— to clarify —`.
- [ ] No secret value written into `config.yaml`.
- [ ] A dated change-log entry with the **why** in every artifact touched.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
