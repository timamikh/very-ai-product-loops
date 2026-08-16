---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.22.2
updated: 2026-08-16
---

# Conventions

Shared notation used by every step template and library tool. Keeps artifacts machine-readable
(for aggregators, output renderers, and the GitMark graph) while staying human-readable.

## Confidence tags

Every non-trivial claim ends with a confidence tag. A claim with no tag is treated as
`assumption`.

- `[assumption]` — stated, not yet backed by a source.
- `[sourced: <where>]` — backed by a document/metric/decision. Name it, e.g. `[sourced: metrics W24]`.
- `[validated: <evidence>]` — confirmed by evidence (an experiment, data, customer signal).
- `[refuted: <why>]` — tested and found false. Kept, not deleted (see change log).

Agent-proposed defaults awaiting human approval are prefixed with **⚙️**.

## Sources

`[sourced: ...]` names the origin. Source slots a tool/step may draw from:
`interview` · `metrics` · `git` · `kb` · `human-decision (dated)`.
Missing data is written literally as `— to clarify —`, never guessed.

## Section IDs

Every artifact section carries a stable ID so tools can fill it and links can target it:

```markdown
## Value & Defensibility {#value-defensibility}
```

IDs are kebab-case and stable across revisions — rename the heading text freely, keep the ID.

## Column keys

A table column is addressed by a **stable key** in a hidden header comment, never by its header text —
the column-level twin of a section `{#anchor}`, the same "mark, don't guess" rule one level down:

```markdown
| Layer <!--c:layer--> | Value <!--c:value--> | Confidence <!--c:conf--> |
```

The comment is invisible in every reader, so the header prose stays whatever the instance's language
makes it (`Уровень`, `Nivel`) while a tool still finds the column. Keys are kebab-case, unique within
their table, stable across revisions and translations. A table is **all-keyed or none** (linter check
O); a filled instance section carries its template's keys (check O2). A column nothing reads by key
carries none — "no consumer, no key".

**The authoring rule — the three homes of a key, and the one place it must never be (a method
template) — is** [`reference/column-keys.md`](reference/column-keys.md). Read it when editing a step
template or a register.

## Links & register item IDs

Register items have stable IDs — hypotheses `H-001`, risks `R-001`, metric nodes `M-northstar`,
`M-activation`. Their **type/category taxonomy, the one-type rule, and the split-in-two lifecycle are
defined in** [`REGISTERS.md`](REGISTERS.md); this file carries only the link form that references them.
Reference an item inline in brackets, e.g. "drives `M-activation`" or "tests `H-003`".

**Cross-artifact links use a relative file path + the target's stable `{#anchor}`** — e.g.
`2-analysis.md#opportunity`, `3-strategy.md#bets` (from a register or other subdirectory, prefix the
path: `../2-analysis.md#opportunity`). This is the one canon: standard markdown, clickable without a
custom resolver, parseable by any tool. **Never** a wiki-style double-bracket link. Point at the
stable `{#anchor}`, never a heading's changeable text; keep anchors stable across revisions. A gate
checklist may use the shorthand `artifact#section` (e.g. `concept#idea`) to name the section it
validates.

## Artifact filenames

A step's output artifact is named **`<step-number>-<slug>.md`** — `1-concept.md`, `2-analysis.md`,
`3-strategy.md`, `4-strategic-plan.md`, `5-tactical-plan.md`, `6-sprint-plan.md`. The numeric prefix
exists only so a directory listing sorts in step order. Links use the real filename, prefix
included (`3-strategy.md#bets`, `../1-concept.md#idea`) — there is no logical id to resolve.
Registers and deliverables are not step outputs and take no prefix.

## Step folders & worklogs

The artifact `<step-number>-<slug>.md` is a **projection**; the working documents it is assembled from
live in a sibling folder of the same stem — `2-analysis/` beside `2-analysis.md` (file and folder
coexist; the artifact is **not** moved inside). The stem is the **artifact's** (`<step-number>-<slug>`),
which matches the step directory `steps/<step-number>-<slug>/` for every step — the console and check P
both resolve the worklog folder from the artifact stem. The folder holds one **worklog** per method that fills
a section: `<step-folder>/<tool>.md`, where `<tool>` is the id in the section's `<!-- tool: <tool> -->`
marker. `<!-- synthesis -->` sections — no method, the orchestrator's own reasoning — share the
reserved `<step-folder>/synthesis.md`.

**One id threads the chain.** The same `<tool>` names the section's marker, the skill folder
(`tool-skills/.../<tool>/`), and the worklog file — so a reader resolves a section's worklog with no
guessing and no per-instance link. The flow runs along it: subagents gather into `<tool>.md`, then the
skill `<tool>` **projects** the artifact section from it. The **worklog is the source of truth; the
artifact section is its projection** — which is also why that step's change-log history lives in the
worklog, not the artifact. Every section that a method fills has a worklog; this is not optional —
a projected section with no worklog behind it is the source of truth gone missing (the linter's
check P holds it).

**One method → several sections: one worklog.** A method that fills several sections keeps **one**
worklog; every one of its markers points at it (e.g. `competitor-analysis` fills `{#competitors}` and
`{#competitor-strategy}`, both projected from `2-analysis/competitor-analysis.md`).

**Several methods → one section: the first is primary.** When a section's marker lists more than one
tool (`<!-- tool: where-to-play-how-to-win, value-definition-strategy -->`), the **first** tool is the section's
**primary**: its worklog `<step-folder>/<first-tool>.md` backs the section, carries the id-thread, and
is what the section projects from. The others are **contributing methods** — their working for *this*
section lands in the primary's worklog, not a file of their own (a contributing method still owns its
own worklog for any section where *it* is primary). So every section resolves to exactly one worklog,
whether its marker names one method or several — the rule a reader and the linter both apply is *the
first tool in the marker owns the section's worklog*.

Raw external inputs are **not** worked here directly: they live in `sources/` and are dispatched into
these worklogs by the `source-intake` skill (see *Raw data & access*).

## Section confirmation

An artifact section is a **thesis** — the step's conclusion projected from the worklog. The linter holds
its *structure*; a **human** holds its *meaning* by signing it off with a marker:

```markdown
## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
<!-- confirmed: 2026-08-13 -->
```

The marker syntax is the contract (the console and linter read it); the **procedure** — walking the
human through each thesis and stamping the marker, never self-issued — is the
[`theses`](../tool-skills/operations/theses/SKILL.md) operations skill (OPERATING-LOOP step 7).

- **`confirmed: YYYY-MM-DD`** — approval of *this* version. **Absence = pending** (a section with nothing
  written is not pending — there is no result to sign). Re-projection from a changed worklog **drops** the
  marker, so a stale sign-off never outlives its thesis. Optional `by:<who>` attributes it.
- **`contested: YYYY-MM-DD`** — a human reviewed the section and pushed it back (distinct from *pending*:
  someone looked). **Confirmed or contested, never both** (check R); the reason goes in the change log.
- **`rests-on: <step>#<section-id>, …`** — a **schema** marker (lives in the step template): the upstream
  sections a conclusion depends on. A section confirmed while a foundation it rests on is not shows as
  *foundation unconfirmed* (console) and warns (check S); every target must be a real section id.
- **`open`** — marks an agent→human inbox (`to-clarify`, `open-questions`, `blockers`), resolved by
  *removing* an item, never confirming it. **Left out** of the step's "N of M confirmed" count, and it
  **must never carry a `confirmed:` marker** (check R).

## Gradation vs confirmation — two orthogonal axes

**Confirmation** answers *has a human signed this?* — a binary marker (above), set by `theses`, dropped
on re-projection. **Gradation** answers *how good is it?* — an ordinal scale carried **inside the row**:
a hypothesis's `signal`/`decision` and priority score, a risk's likelihood × impact and lifecycle. The
scales are defined once (enums in [`REGISTERS.md`](REGISTERS.md), the readout in the owning library
skill), never per step.

The axes are **independent** — a section can be confirmed at a low grade, or unconfirmed at a high one.
A high grade is **not** a sign-off, and confirming does not raise a grade; a console renders **two
chips**, never folding one into the other (that would relabel "nobody checked" as "checked and weak").

## Instance config (`config.yaml`)

`config.yaml` is the **human's decisions** about the instance; the cycle's position lives in
`state.yaml` (see OPERATING-LOOP). Its keys are canon, spelled exactly one way — a second spelling is a
place two readers diverge, so the linter enforces the schema (check **H**). The **pinned schema — every
key, its shape, and the no-alias rule — is** [`reference/config-schema.md`](reference/config-schema.md);
read it when writing or validating a `config.yaml`.

## One mechanism, one way

Product decisions fork; **framework mechanics must not**. For anything the framework itself does —
where values live, file formats, ID schemes, section anchors — there is exactly **one canonical
way**. No dual formats, no "start in X then migrate to Y" thresholds, no documented alternatives:
every mechanical variation point is a place where two agents (or an agent and an aggregator)
diverge and break. If two ways exist, pick one and eliminate the other in the same change.

## Where a new rule goes — contract · method · check

Before adding a rule to this canon, classify it: a **check** (the linter) costs nothing at read time; a
**method** (a skill) is read only when used; a **contract** (`process/`) is paid on every pass, by every
agent. Only a contract two independent readers must agree on — field names, enum values, id shapes,
file roles, path/link form — earns a place here; try the cheaper classes first. The full test, the
always-loaded budget, and the subtraction rule are in [`EXTENDING.md`](../EXTENDING.md) → *Where a new
rule goes*.

## Forks & options

**Triage first — fewer forks, higher quality each.** Escalate a decision to the human only if it
is (a) consequential — changes strategy, is irreversible or expensive — AND (b) not closable from
evidence with a confident default. Everything reversible and cheap the agent decides itself,
marks **⚙️**, and logs with its rationale — it does not ask. An open fork is an unresolved risk:
close it, or escalate it with an owner — never let `— to clarify —` become standing debt.

For the forks that survive triage, present **2–4 concrete options with their trade-offs**, then
a recommendation — never a single option with the alternatives hidden. A lone recommendation
removes the human's choice and buries the risk in the paths not shown.

- Each option gets a one-line pro/con; the recommended one is marked **⚙️** and stated as the lead.
- This applies in prose forks and in the operating loop's *Clarify* step alike.
- Technical/implementation gaps are still noted as forks in the artifact, not asked — this rule is
  about the *product decisions* the human owns.

## Talking to the human

In chat, never send a bare register ID, section anchor, or link: decode what stands behind it in
the same sentence ("`H-009` — the bet that tech leads stay for the frontier stream"), so the human
never has to open the repo just to follow the conversation. IDs stay bare only inside artifacts,
where the register is one click away.

## Raw data & access

**A source is what comes from outside** — material the user (or the world) brings in; **no skill
produces a source from inside the framework**. Agent reasoning is a worklog; a file produced for use
outside is an export file (`export-files/`, the mirror of `sources/`: in ↔ out). When something fits
none of the entities, the *skill* is recut along these seams — a new entity or a hybrid home is never
minted.

`sources/` holds **two roles**, kept apart because they age differently, both indexed in
`sources/INDEX.md`: **access** (`node_type: source`, living — what an external source is, how to
connect/verify/recover) and **evidence** (`node_type: source`, dated, immutable — a capture, a
report, returned interview notes). How raw rows become register values is agent reasoning and lives
in a **worklog** (`metrics-capture`), citing the access file. A source is **dispatched into
worklogs, never linked from an artifact** (a worklog cites `../sources/<file>`, an artifact links
only the worklog). **Captured values** go to the registers as dated rows; the source records the
context.

The hard rules (also in [`AGENTS.md`](../AGENTS.md)): **raw captures are never committed** and are
deleted once their values land; where the instance's `origin` may be public, raw data and its analysis
code live **outside** the repo, only a reference goes in. **Secrets** are never written anywhere — only
*where* they live and how to rotate them. The routing procedure is the
[`source-intake`](../tool-skills/operations/source-intake/SKILL.md) operations skill.

## Which conventions apply where

Conventions are **not** uniform across file types — a file's `node_type` selects which apply (an
artifact carries the full set; a register uses a `confidence` column instead of inline tags; a source
obeys the raw-data rules). The authoritative by-`node_type` matrix is
[`reference/node-type-matrix.md`](reference/node-type-matrix.md); consult it when in doubt. Omitting a
convention the matrix marks n/a is **correct**, not a lapse. A convention not in the matrix
(e.g. "Talking to the human") is behavioral and applies always.

## Change logs

Every **instance artifact** ends with a change log — the `artifact`, `register`, `source`,
`sources-index`, and `handoff` rows in the matrix above. Narrative artifacts included: the log
carries the *motivation*, not just the diff. Newest entry first.

```markdown
## Change log

### 2026-07-16 — <one-line summary>
- **From → To:** <what the state was> → <what it is now>
- **Why:** <reasoning>
- **Trigger:** <what prompted it — a metric shift, a refuted hypothesis, a decision, …>
```

A **register** entry names the ids it moved (`H-004`, `M-activation`) inside its From → To. That one
habit is what makes a single item's history retrievable — the console assembles the trail of one
hypothesis from these entries instead of anyone storing it a second time.

Framework files (this one included) do **not** carry an inline change log — their history lives in
the repository's root [`CHANGELOG.md`](../CHANGELOG.md), keyed to git version tags.
