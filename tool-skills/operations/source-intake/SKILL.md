---
name: source-intake
kind: template
produces: product/<step-folder>/<tool>.md
reads_registers: []
writes_registers: []
inputs: [kb]
prerequisites:
  - a raw file in `sources/` (or a new one just added) with a role in `sources/INDEX.md`
  - the target step's artifact exists, so its `<!-- tool: X -->` markers name the worklogs a source may feed
  - a decision, when a source could feed more than one step, on which it primarily informs — proposed by the agent, confirmed by the human
used_by_steps: [any]
opinionated: true
method_basis: "Route, don't reason: every external source is dispatched into the step worklog(s) it informs and cited there, so no artifact ever reaches around a worklog to a raw file"
status: draft
version: 0.1.0
updated: 2026-08-13
---

# Source intake — dispatch a raw source into the step worklogs it feeds

**What it is.** The pass that takes an **external source** in `sources/` — legacy material brought in at
setup, or a file just added — and **dispatches its content into the step worklogs it informs**. A source
is evidence, not analysis: this skill routes each fact to the worklog whose method works from it
(`<step-folder>/<tool>.md`, e.g. `2-analysis/market-sizing.md`), cites the source there, and records the
routing in `sources/INDEX.md`. It does **not** analyse and it never touches an artifact.

**Why it is an operations skill, not a library method.** It fills no section of any step artifact and
belongs to no step — one source can feed several. It is triggered by an event (setup, a new file) and
acts on the instance's worklogs and source index. What it contributes is *where each fact belongs*, not
what the fact means; the meaning is worked later, by the library method's *Act* pass, from the worklog
this skill seeded.

**The one thing it exists to prevent.** A source that an artifact cites **directly**. The moment a
`1-6` artifact links `sources/foo.md`, the layering is broken: the worklog is no longer the source of
truth, the console can no longer drill from a board into where a claim was worked, and `check P` warns.
Every external fact must land in a worklog first; the artifact section then projects from the worklog,
and the worklog — never the artifact — points back to the raw file (reachable in the console only under
*Sources*). See [`CONVENTIONS.md`](../../../process/CONVENTIONS.md) → *Raw data & access* and *Step
folders & worklogs*.

## When to apply

Triggered by events, not by a step:

1. **At product setup** — the instance arrives with legacy material in `sources/`. Before any step is
   worked, each source is routed into the worklog(s) it will inform, so the first *Act* pass on a step
   already finds its evidence dispatched and cited.
2. **A new file lands in `sources/`** — an export, a report, an interview transcript. It is routed the
   same way before any artifact section leans on it.
3. **A source changed** — re-dispatch the affected worklogs and re-date the intake rows; a superseded
   value is struck, not silently overwritten.
4. **On request** — the human points at a source and asks where it belongs.

This is a pass of the [operating loop](../../../process/OPERATING-LOOP.md): it ends with the worklogs
written, `sources/INDEX.md` updated, and a change-log entry. Routing evidence is still *Update state* —
"I only filed a source" does not skip it.

> **Metric values are not routed as prose.** A number that belongs in `registers/metrics.csv` is captured
> by [`metrics-capture`](../metrics-capture/SKILL.md), not dispatched as an intake row. Source-intake
> routes qualitative and contextual evidence; a metric reading's home is the register, and the worklog
> cites the register id.

## Prerequisites

- **A source with a role.** The file is in `sources/` and `sources/INDEX.md` records what it is. An
  unindexed file is indexed as part of this pass — role first, then routing.
- **The target artifact exists.** A worklog may only be created for a `<tool>` the step's artifact
  actually declares (`<!-- tool: X -->`). Material that fits no declared tool is a **routing question for
  the human**, not a licence to invent a worklog — an orphan worklog is exactly what `check P` flags.
- **A primary step, when a source spans several.** The agent proposes which step a source primarily
  informs (⚙️) and the human confirms; a source may be cited from more than one worklog, but each fact is
  dispatched to the one method that works from it, never copied wholesale into all of them.

## How to do it

**1 · Read the source and its role.** Open the file and its `sources/INDEX.md` row. Name, in a sentence,
what decision or method this material serves. If nothing in the six steps consumes it, it is a source
worth removing rather than routing.

**2 · Route each fact to a tool, not a step.** Read the target step's artifact for its section markers
(`<!-- tool: X -->`, and `<!-- synthesis -->` → `synthesis`). Map each fact in the source to the worklog
whose method works from it: market figures → `market-sizing`, competitor prices → `competitor-analysis`,
a cross-cutting read → `synthesis`. A fact that maps to no declared tool goes to the human as a routing
question; it does not conjure a new worklog.

**3 · Dispatch into the worklog, dated and tagged.** For each target `<step-folder>/<tool>.md`:

- if the worklog does not exist yet, create it with `node_type: worklog` frontmatter (`tool`, `step`,
  `title`, `updated`, `version`) per [`CONVENTIONS.md`](../../../process/CONVENTIONS.md) → *Step folders
  & worklogs*;
- add the fact to the worklog's **intake block** via [`template-fragment.md`](template-fragment.md): the
  source (a relative `../sources/<file>` link), what it gives this method, the value or claim, the date,
  and a confidence tag — `[sourced: <slug>]` for a fact the source states, never `[sourced]` for
  something you inferred from it.

**4 · Cite the source from the worklog, never from the artifact.** The link to the raw file lives in the
worklog only. If the artifact already links `sources/…` directly (a pre-migration instance), move that
citation down into the worklog as part of this pass and leave the artifact pointing at the worklog — this
is what clears the `check P` warning.

**5 · Record the routing in the index.** Update the source's `sources/INDEX.md` row to name the
worklog(s) it was dispatched into, so the next agent can see at a glance which evidence has been absorbed
and which is still sitting unrouted.

**6 · Land it, then close the pass.** In one pass: the worklog(s) written, `sources/INDEX.md` updated, a
dated **change-log entry** in each worklog touched (from → to · why · trigger), and
**`python3 tools/lint.py <instance>` reporting 0 errors** — `check P` is the guard that every worklog is
well-formed and no artifact still links a source directly. Then tell the human what was routed where,
decoding each id and file in the same sentence, and name any source left unrouted and why.

## Anti-patterns

- **The artifact citing a source.** The failure this skill exists to prevent — a `1-6` artifact linking
  `sources/…`. Evidence goes into a worklog; the artifact points at the worklog.
- **The invented worklog.** Creating `<step>/<tool>.md` for a tool the artifact does not declare, to give
  a stray fact a home. That is an orphan; the fact is a routing question instead.
- **Routing as analysis.** Drawing a conclusion while dispatching. Source-intake places evidence; the
  reasoning is the method's *Act* pass, from the worklog this skill seeded.
- **The blended copy.** Pasting a whole source into every worklog that might touch it. Each fact is
  dispatched once, to the method that works from it; other worklogs cite it by reference.
- **A metric as prose.** Filing a number that belongs in `metrics.csv` as an intake row — its home is the
  register (`metrics-capture`); the worklog cites the register id.
- **The silent overwrite.** A changed source overwriting an intake row with no strike and no new date, so
  a superseded value looks current.
- **Filing without Update state.** Evidence moved, index and change log untouched — the pass did not
  happen as far as the next agent is concerned.

## Output

- Dated intake rows in the step worklogs (`product/<step-folder>/<tool>.md`) via
  [`template-fragment.md`](template-fragment.md), each citing its `../sources/` file.
- A `sources/INDEX.md` that records, per source, which worklog(s) absorbed it.
- No artifact edit and no register write — those are the *Act* pass and `metrics-capture`, respectively.
