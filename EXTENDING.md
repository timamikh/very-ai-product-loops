---
node_type: extending
title: Extending — how to adapt the framework without forking it
status: draft
version: 0.1.0
updated: 2026-08-03
---

# Extending the framework

The framework is built to be adapted: a company brings its own methods, its own stages, its own
execution streams. This file is the **map of the dials** — which one to turn for what you want, who
owns it, and where its procedure is written. It does not restate those procedures (that would be a
second source of truth); it routes you to the one place each lives, and it fills in the two dials that
had no home.

**How a change happens: you ask the agent.** Every dial below is a file in the repo, and every file in
the repo is written by an agent running the loop — describe what you want, or point at an existing
skill to adapt. There is no settings screen: the local console
([`tools/ui/`](tools/ui/README.md)) *shows* what you have and never changes it, on purpose (a form
that fills a method is the failure this framework exists to prevent).

## The dials

| You want to change | It lives in | Owner | Procedure |
|---|---|---|---|
| **add a product method** (segmentation, pricing, your own framework) | `product/tool-skills/library/<name>/` | your product | [`tool-skills/README.md`](tool-skills/README.md) → *Where a product's OWN skills live* |
| **change a shipped method** to how you work | `product/tool-skills/library/<same-name>/` — a local skill wins over the vendored one | your product | same as above; copy the vendored skill as the starting point |
| **add a runtime skill** (how the agent works across sessions) | `product/tool-skills/operations/<name>/` | your product | same as above |
| **add a deliverable format** (a branded deck, a board card) | an adapter | your product or upstream | [`tool-skills/adapters/README.md`](tool-skills/adapters/README.md) → *How to add an adapter* |
| **add or rename a product stage** | `statuses/<order>-<name>.md` | upstream / your fork of the core | [`statuses/README.md`](statuses/README.md) → *Add or change a status* |
| **change what a stage asks per step** (its goals and recommended tools) | the active status file, `per_step` | upstream / your fork | [`statuses/README.md`](statuses/README.md) → *Anatomy of a status* |
| **change the work directions** (execution streams in Steps 5–6) | `product/config.yaml` → `directions` | your product | *below* |
| **change the documentation language** | `product/config.yaml` → `language` | your product | edit the key; artifacts already written stay in their language until rewritten |
| **contribute a method to the framework itself** | `tool-skills/library/<name>/` upstream | upstream | [`tool-skills/library/README.md`](tool-skills/library/README.md) → *How to add a tool* + [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **add, remove or reorder a step** | `steps/` — the fixed core | **almost never** | *below — read it before trying* |
| **the register schemas** (hypotheses / risks / metric tree) | `process/REGISTERS.md` | canon | not a dial: the schemas are the contract every tool reads. Add a free `tags` column instead |

Everything in the vendored framework is **read-only**: updating means re-vendoring at a newer tag,
which overwrites it. That is why your own skills live under `product/` — they survive the update, and
a local skill of the same name wins.

## Changing the work directions

**Directions** are the execution streams that Steps 5–6 are organized around. The default is
`development` · `go-to-market` · `back-office`; the count and the names are an instance decision, not
a framework constant (see [`process/OVERVIEW.md`](process/OVERVIEW.md) §4, where directions are called
out as an editable instance config).

What depends on them, so you know what a change touches:

- **Steps 5–6 artifacts** (`5-tactical-plan.md`, `6-sprint-plan.md`) group their content by direction.
- **A status may split its per-step goals by direction** — a direction you remove leaves goals with
  nothing to attach to; a direction you add has no goals until the status file names them.
- **`directions` is a required key** in `config.yaml` (see [`process/CONVENTIONS.md`](process/CONVENTIONS.md)
  → *Instance config*), so the linter fails if it goes missing.

The procedure, run by the agent as one pass of the loop:

1. Decide the streams from how the work is actually divided — a direction is a stream someone owns,
   not a category of thought. Fewer and real beats many and tidy.
2. Edit `directions` in `product/config.yaml`.
3. Re-read the active status's `per_step` goals for Steps 5–6. If they are split by direction, the
   agent proposes goals for a new stream (marked ⚙️) and flags orphaned ones for a removed stream.
4. Re-organize the existing Step 5–6 artifacts to the new streams. This is a normal pass: content
   moves, nothing is invented, anything with no home becomes `— to clarify —`.
5. Dated change-log entry in each artifact touched — with the *why*, not just the diff — then
   `python3 tools/lint.py` must report **0 errors**.

## Adding, removing or reordering a step

**Start from the assumption that you don't need to.** The six steps are the fixed core: the thing that
makes two instances comparable and every tool able to read them. Nearly every "we need a different
step" turns out to be one of these, and each is a dial that costs nothing:

| What you actually want | The dial |
|---|---|
| this stage should focus elsewhere | the status's `per_step` goals and tools |
| we need content the artifacts don't hold | a library method whose `produces` section is homed in an existing step artifact |
| we need a different output | an adapter |
| we need another execution stream | `directions` |
| our stage isn't concept-viability / PMF / growth | a new status |

If it is genuinely none of those, then a step change is a **change to the framework core** — a fork or
an upstream contribution, never an instance-level edit. What it drags with it:

- every **gate checklist** item is keyed to `artifact#section`, and section anchors must stay stable;
- **cross-artifact links** are real relative paths, so a renamed or renumbered artifact breaks them;
- the linter's check that every method's output has a **home** in some step template (check B) will
  fail for methods that pointed at what you removed;
- **every status file** must gain a `per_step` block for a new step, or it silently has no goals there;
- the artifact filename prefix is a **sort order** (`1-…` … `6-…`), so inserting in the middle
  renumbers the neighbours — and renumbering is a rename, with the link consequences above.

The procedure, if you accept all that: change `steps/`, update every status's `per_step`, re-home the
affected methods, fix the links, run the linter to zero, bump the version and record it in
[`CHANGELOG.md`](CHANGELOG.md) — and keep it in a fork or a pull request, not in a product folder.

## Rules that hold for any change

- **One mechanism, one way.** If your change introduces a second format or a second path for something
  the framework already does one way, it is the wrong change — see
  [`process/CONVENTIONS.md`](process/CONVENTIONS.md).
- **The agent never invents the method.** If you have not said what a new method *does*, its content
  lines stay `— to clarify —`. A plausible-looking method nobody chose is worse than a blank one.
- **The linter is the gate.** `python3 tools/lint.py` reports 0 errors before a change is done. It
  checks wiring and enums — not whether your method is any good.
- **History is recorded where the file lives:** instance files (artifacts, registers, sources, handoff)
  carry a dated change log; framework files carry a `version` bump and a line in `CHANGELOG.md`.
