---
node_type: reference
title: The card — the pinned schema for every instruction an agent acts on
status: draft
version: 0.3.1
updated: 2026-09-02
---

# The card — the pinned schema

*Read this when writing or validating a **card**: a step `README.md`, a library method, an operations
skill, an outputs skill, or an instance's own exchange skill. The one-line pointer stays in*
[`CONVENTIONS.md`](../CONVENTIONS.md) → *Cards*; *the linter enforces this file as checks **X**
(schema) and **Z** (home).*

A **card** is the one entity an agent acts on. Its frontmatter **is the pass plan**: what must exist
before it runs, what it may read, what it may write, and which surfaces move 5 must touch. Five kinds
differ by **field values, not by a second schema** — one questionnaire, filled differently. The
[goal map](../goal-map.md) routes a trigger and a goal to a card; the card supplies the rest.

## The core — every card, every kind

```yaml
node_type: card
kind: step | method | operation | output | exchange
name: <slug>            # = the folder name; for a step card, the folder minus its number (1-concept -> concept)
prerequisites: [...]    # what must exist before the pass runs — prose items, as today
reads: [...]            # the read perimeter of move 2, as atoms (below)
writes: [...]           # the write perimeter of move 4, as atoms
surfaces: [...]         # the surfaces move 5 must touch, as atoms
status: draft|…
version: <semver>
updated: YYYY-MM-DD
```

`title:` is **not** part of the core — a card's heading is its first line and its identity is `name`.
Step cards keep their existing `title:` as an optional field; no card gains one.

## One atom grammar — three fields

`reads`, `writes` and `surfaces` are lists of **atoms** from one grammar. A prefix is mandatory
wherever a bare word would be ambiguous: `metrics` is both a register and a source slot, so
`register:metrics` (the register file) and `source:metrics` (an analytics system) are different atoms.

| Atom | What it names | Legal in |
|---|---|---|
| `register:<name>` | a register **file** — the six names in [`REGISTERS.md`](../REGISTERS.md)'s enumeration (`hypotheses` · `risks` · `metrics` · `metric-tree` · `features` · `surfaces`) | reads · writes · surfaces |
| `source:<slot>` | an external input slot — `kb` · `interview` · `research` · `metrics` · `git` | reads |
| `section:<anchor>` | an artifact section by its `{#anchor}` | reads · writes · surfaces |
| `worklog` | bare: **its own** worklog; the path is resolved by [`worklog-resolution.md`](worklog-resolution.md), never restated here | reads · writes · surfaces |
| `worklog:<step-folder>/<method>` | a **declared foreign worklog input** — the one legal way to read another method's worklog (OPERATING-LOOP move 2; checks X and T); tags carry verbatim. Writing stays with its own method (plus the projection move's *orchestrator's conclusions* block — `projection` step 0) | reads |
| `file:<path>` | a file, path relative to the instance root | reads · writes · surfaces |
| `state:<key>` | a key in `state.yaml` | writes · surfaces |
| `ticks` | the current step gate's checklist items | surfaces |
| `sign-off` | a section confirmation marker | writes · surfaces |
| `change-log` | a change-log entry | surfaces |

**The wildcard `*` is the slot the data fills.** `section:*`, `worklog:*`, `register:*`,
`file:export-files/*` mean *"one this pass resolves from the trigger and the data"* — the law *slots
from the card, instances from the data* written as syntax. A card that names a concrete anchor commits
to it; a card that writes wherever it is pointed (`projection`, `source-intake`, `theses`) says so with
`*`, and the check accepts that as a declaration, not as a blank.

`worklog:*` in **`writes`** is the one narrow case, and it says one thing only: the *orchestrator's
conclusions* block appended before projecting ([`projection`](../../tool-skills/operations/projection/SKILL.md)
step 0), in whichever worklog the pass is projecting from — `step-close` declares it because its
perimeter is a whole step of them. It is never permission to write another method's working: that
stays with the method that owns it.

An empty list is a **declaration that the card touches nothing there** (`orchestration` writes nothing
of its own: `writes: []`), and is different from an absent field, which is an error.

## `reads` is a perimeter, not a hint

For a **method** card, `reads` is closed: the **primary working of the worklog** — the first pass
that drafts the method's reasoning, inline or through a `draft` brief — draws on these atoms and
nothing else. An input the perimeter names but the instance lacks is a **declared gap**
(`— to clarify —` and `[assumption]` marks), never silently replaced by whatever else lay in reach —
the hub run showed exactly this working: `source:interview` declared everywhere, empty everywhere,
and every method honestly wrote assumptions instead of borrowing.

Wider context enters through exactly two doors, both the orchestrator's and both **recorded**:

- the *orchestrator's conclusions* block ([`projection`](../../tool-skills/operations/projection/SKILL.md)
  step 0) — unrestricted, already ⚙️-tagged;
- a **rework order**: sending a worklog back, the orchestrator may supplement the perimeter with
  named inputs the quality of the result needs — the supplement is written into the worklog with
  the rework entry, so an audit can tell a sanctioned widening from a leak.

Four inputs are **ambient** — inside every perimeter, never declared: the card itself, the method's
own worklog and prior section state, the instance's `config.yaml`/`state.yaml`, and the human's
answers to the method's own questions. Declaring them would put the same four lines on every card.

`prerequisites` names, in prose, the subset of the perimeter that must already exist for the pass
to **start**; it never names an input `reads` does not carry — a prerequisite the atoms cannot
express is the signal the `reads` list is incomplete, not a license to keep it in prose only.

Two cases the prose used to carry, settled here so no card has to re-decide them: a **renderer**
writes `file:export-files/*` and names its extensions in `formats:`; a **pull** writes
`file:sources/snapshots/*` and never a register — landing a value is a separate pass
([`boundary-layout.md`](boundary-layout.md), rule 1).

## Fields by kind — the mutual exclusions the check holds

| Kind | Lives in | Adds | Must not carry |
|---|---|---|---|
| `step` | `steps/<n>-<slug>/README.md` | `step: <n>` · `output: <artifact>.md` · `cadence:` · `method_basis:` | `steps:` |
| `method` | `tool-skills/library/<name>/SKILL.md` | `steps: [<n>]` (exactly one — check U) · `opinionated:` · `method_basis:` · the quality block: `evidence_standard` · `volume_rule` · `selection_rule` · `rejects_shown` (check L) | `surfaces:` — **a method is never a routing target** |
| `operation` | `tool-skills/operations/<name>/SKILL.md` | `opinionated:` · `method_basis:` | `steps:` — it is routed, not step-bound |
| `output` | `tool-skills/outputs/<name>/SKILL.md` | `output_kind: rendered \| authored` · `opinionated:` · `formats:` (what a renderer emits); `authored` may carry the quality block | `steps:` |
| `exchange` | `<instance>/skills/<slug>/SKILL.md` | `direction: pull \| push` · `cadence:` · `reaches:` (its passport) · `lands_via:` (the landing card) | `steps:` |

**The law of ranks, as fields.** A `method` has `steps` and **no** `surfaces`: it is reached from
inside a pass, through its section's marker, and is never routed to. A routed kind is the reverse — no
`steps`, and `surfaces` naming what move 5 owes.

**Who must carry `surfaces` is resolved against the router, not against a list here.** Every `step`
card, plus every card the [goal map](../goal-map.md) actually routes to, must declare a non-empty
`surfaces` — a pass that owes no surface has no reason to be a pass (check X reads goal-map.md; a
second list of routed cards would drift from the first). An operations card that is a **move** rather
than a pass — `projection` and `orchestration`, invoked from inside moves 2–5 and never routed to —
declares `surfaces: []`, and that empty list is the honest statement of its rank.

**The law of two homes.** A card ships with the framework → `tool-skills/`. A card is written for one
product → `<instance>/skills/`. The discriminator is **who authored it**, as objective as the delivery
channel in `sources/`. `kind: exchange` outside an instance is an error; a framework kind inside an
instance is an error (check Z).

## Migration map — old field to new

| Old | New |
|---|---|
| `produces` (a section noun, e.g. `segments`) | `writes: [worklog, section:segments]` |
| `produces` (a path) | `writes: [file:<path>]` |
| `produces` (prose "none of its own") | `writes: [section:*]` or `writes: []` — say which, in atoms |
| `writes_registers: [hypotheses]` | `writes: [… register:hypotheses]` |
| `reads_registers: [metrics]` | `reads: [… register:metrics]` |
| `inputs: [kb, metrics]` | `reads: [source:kb, source:metrics]` |
| `used_by_steps: [3]` | `steps: [3]` |
| `used_by_steps: [any]` (operations) | dropped — an operation is routed, not step-bound |
| `kind: method \| template \| research` | dropped — see rule 4 below |
| `kind: adapter` / `kind: deliverable` (outputs) | `output_kind: rendered` / `authored`, and `ADAPTER.md` is renamed `SKILL.md` |
| `node_type: step` · `node_type: instance-exchange-skill` · no `node_type` at all | `node_type: card` + its `kind` |
| the goal map's *Move-5 surfaces* column | `surfaces:` on the card that row routes to — the column is deleted; a fact about a card lives in the card |

## Rules

1. **One questionnaire.** A role that needs a field the table above does not give it is a change to
   this file, never a second schema. A field outside this file is a warning — *unknown card field* —
   so a private key cannot quietly become de-facto schema.
2. **Values are canon, not free text.** The check validates the **atoms**, not merely that the field
   exists. A `reads` list of prose is the failure this schema exists to prevent: 62 cards would
   describe their inputs 62 ways and the single structure would be nominal.
3. **The card declares types; the pass resolves instances.** Frontmatter never carries a row id, a
   date, or a resolved path where a slot will do. `worklog` is the standing example: the atom names
   it, `worklog-resolution.md` alone says how the path is built.
4. **`kind: method | template | research` is dropped, not renamed.** It was required by check M but
   never validated and never branched on — no reader consumes it (⚙️ proposed; see В-3 in the wave
   plan). *Its former slot is now the card's own kind.* If the author keeps it, it returns as
   `task_kind:` with a declared vocabulary and a named consumer — a key with neither is the thing
   *Column keys* already forbids.
5. **Readers stay tolerant, the linter stays strict.** A reader meeting an off-canon card still shows
   it *and* surfaces the drift. Tolerance is for the human's benefit, never permission.
