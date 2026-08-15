---
node_type: extending
title: Extending — how to adapt the framework without forking it
status: draft
version: 0.4.0
updated: 2026-08-15
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
| **change what a delegated subagent may do** (its tools, its instructions) | `.claude/agents/loops-*.md` on Claude Code; the brief itself on any other runtime | your fork / your setup | [`tool-skills/operations/orchestration/SKILL.md`](tool-skills/operations/orchestration/SKILL.md) → *On the runtime*. The **rule** is canon and not a dial: only the orchestrator writes ([`process/OPERATING-LOOP.md`](process/OPERATING-LOOP.md) → *Delegation*) |
| **add or rename a product stage** | `statuses/<order>-<name>.md` | upstream / your fork of the core | [`statuses/README.md`](statuses/README.md) → *Add or change a status* |
| **change what a stage asks per step** (its goals and recommended tools) | the active status file, `per_step` | upstream / your fork | [`statuses/README.md`](statuses/README.md) → *Anatomy of a status* |
| **change the work directions** (execution streams in Steps 5–6) | `product/config.yaml` → `directions` | your product | *below* |
| **change the documentation language** | `product/config.yaml` → `language` | your product | edit the key; artifacts already written stay in their language until rewritten |
| **contribute a method to the framework itself** | `tool-skills/library/<name>/` upstream | upstream | [`tool-skills/library/README.md`](tool-skills/library/README.md) → *How to add a tool* + [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **change a section or its columns in a step artifact** (add a field, key a column, reshape a table) | `steps/<n>/template.md` — the schema *is* the template | upstream / your fork | *below — "Changing a section or its columns"* |
| **add, remove or reorder a step** | `steps/` — the fixed core | **almost never** | *below — read it before trying* |
| **the register schemas** (hypotheses / risks / metric tree) | `process/REGISTERS.md` | canon | not a dial: the schemas are the contract every tool reads. What an instance may use instead: `tags` for a cross-cutting theme, `note` for a qualifier an enum cell cannot hold |

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

## Changing a section or its columns

A step artifact's shape is a contract, and its one home is the step template `steps/<n>/template.md`:
the chistovik an instance fills and the console that renders it are the *same form*, read from there.
So changing a section means changing that schema — everything else follows it, nothing is a second edit.

A section is three marks (the column half is specified in
[`process/CONVENTIONS.md`](process/CONVENTIONS.md) → *Column keys*):

- `## Title {#anchor}` — the section's stable handle; the language of the prose is free, the anchor is not;
- `<!-- tool: X -->` — the method that fills it. The same `X` names the skill folder
  `tool-skills/library/X/` and the worklog `<step-folder>/X.md` — one id threads method, worklog and section;
- on a table, `<!--c:key-->` on each column a consumer reads — a column is addressed by its key, never
  by header prose. A column nothing reads by key carries none ("no consumer, no key").

What a section change drags with it:

- the **gate item is derived, not maintained** — every `{#anchor}` becomes `artifact#section` in
  `state.yaml` on its own (`tools/loops/framework.py`), so a renamed anchor renames its gate id and
  orphans its ticks; keep anchors stable;
- the **linter holds the shape**: check **O** (keys well-formed on the template — all-keyed-or-none,
  unique; a key in a *method* template is an error), check **O2** (a filled instance section carries its
  template's keys), check **P** (the `<!-- tool: X -->` has its worklog);
- the **console follows the keys by itself** — it reads by anchor + key, so a new or reshaped section
  renders generically with **no console edit**; a *bespoke* board for it is opt-in (`COL_SCHEMA` + a
  renderer in [`tools/ui/app/app.js`](tools/ui/app/app.js));
- **cross-section references go by words, not row codes** — a code like `P1` that lives only in a
  worklog does not survive into another section's prose (a reader-not-in-the-room can't resolve it).

The guard, and the one failure mode: **change the shape = change the keys, then run the linter.**
Editing the template's prose while leaving the keys is the one bypass the console cannot see; checks
O/O2 are what catch it. Then `python3 tools/lint.py <instance>` to zero, bump the template `version`,
and record it in [`CHANGELOG.md`](CHANGELOG.md).

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
- **Classify before you write it.** A rule that a machine can verify belongs in the linter; a procedure
  belongs in a skill; only a contract two readers must agree on belongs in `process/` — see CONVENTIONS
  → *Where a new rule goes*. This is what keeps the always-loaded rule set from thickening with every
  lesson learned.
- **A fourth register is a core change**, decided by the four-sign test in
  [`process/REGISTERS.md`](process/REGISTERS.md) — not by how much the need itches.
- **The agent never invents the method.** If you have not said what a new method *does*, its content
  lines stay `— to clarify —`. A plausible-looking method nobody chose is worse than a blank one.
- **The linter is the gate.** `python3 tools/lint.py <instance>` reports 0 errors before a change is
  done — name the instance, and check the line it prints (`instances checked: …`): a run that found
  nothing to check is a failure wearing a success message. It checks wiring and enums — not whether
  your method is any good.
- **History is recorded where the file lives:** instance files (artifacts, registers, sources, handoff)
  carry a dated change log; framework files carry a `version` bump and a line in `CHANGELOG.md`.
