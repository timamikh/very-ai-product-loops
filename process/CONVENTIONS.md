---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.31.0
updated: 2026-08-23
---

# Conventions

The shared notation every step template, library tool and instance file uses — each section a
**contract** two independent readers (an agent and a tool, or two agents) must agree on. The
*procedures* that use these forms live in the operations skills; the *authoring detail* lives in
[`reference/`](reference/README.md) — every pointer below names the moment to read it.

## Confidence tags

Every non-trivial claim ends with a tag; **no tag = `assumption`**:
`[assumption]` · `[sourced: <where>]` (name it, e.g. `[sourced: metrics W24]`) ·
`[validated: <evidence>]` · `[refuted: <why>]` (kept, never deleted — see change log).
Agent-proposed defaults awaiting human approval are prefixed **⚙️**.

## Sources

`[sourced: ...]` names the origin. Source slots a tool/step may draw from:
`interview` · `metrics` · `git` · `kb` · `human-decision (dated)`.
Missing data is written literally as `— to clarify —`, never guessed.

## Section IDs

Every artifact section carries a stable, kebab-case ID so tools can fill it and links can target it:
`## Value & Defensibility {#value-defensibility}`. Rename the heading text freely; keep the ID.

## Column keys

A table column is addressed by a **stable key** in a hidden header comment (`| Layer <!--c:layer--> |`),
never by its header text — so it is found in any language. A table is **all-keyed or none** (check O);
a filled instance section carries its template's keys (check O2); **no consumer, no key**. Key form,
the three homes of a key, and the one place it must never be —
[`reference/column-keys.md`](reference/column-keys.md), read when authoring a template or a register.

## The decision line

A section filled by a method whose evidence rests on **a choice** ends in one canonical line, and its
three fields carry **field keys** so a tool reads them in any language:

```markdown
**Decided:** <!--d:date--> 2026-08-20 · **by:** <!--d:by--> ⚙️ acting PO · **alternatives considered:**
<!--d:alts--> leading on demand rather than feasibility (rejected — the concept lives or dies on the engine)
```

Label prose is free and translatable, the keys are not. `·` separates the fields, so no value
*before* the last may hold one; `d:alts` is last and runs to the end of the block — it may list
several alternatives with `·` freely, and the line is its section's last. **All three keys or
none** (check O4), and the alternatives field is never a bare *none* — it names one alternative that
was weighed and why it lost, or what makes the choice forced
([`../tool-skills/library/README.md`](../tool-skills/library/README.md) → *The rejected alternative*).
Unlike a column key, a decision-field key **does** live in a method's `template-fragment.md`: this
line is copied verbatim rather than adapted by meaning, so its keys travel with it.

## Card line

A section may mark **one of its own lines** as its headline — the line a board card shows collapsed:
`<!-- card -->` **trailing a line** points at that line; **alone on a line**, at the paragraph below.
The console shows the marked line verbatim — it never summarises; no mark = title + status. Who
places it, how the line is chosen, and why a section may honestly stay unmarked — the
[`projection`](../tool-skills/operations/projection/SKILL.md) operations skill.

## Links & register item IDs

Register items have stable IDs — hypotheses `H-001`, risks `R-001`, metric nodes `M-northstar`,
features `F-001`, surfaces `S-01` (taxonomy and lifecycle — [`REGISTERS.md`](REGISTERS.md)).
Numbered ids count **sequentially and are never reused**; the digit width is free — zero-padding
is a style choice, not grammar (`F-01`, `F-001` and `F-1000` are all valid, a long-lived product
outgrows any fixed width). Reference one inline in brackets: "drives `M-activation`".

**Cross-artifact links are a relative file path + the target's stable `{#anchor}`** —
`2-analysis.md#opportunity` (from a subdirectory: `../2-analysis.md#opportunity`). **Never** a
wiki-style double-bracket link; point at the `{#anchor}`, never a heading's changeable text. A gate
checklist may use the shorthand `artifact#section` (e.g. `concept#idea`).

## Artifact filenames

A step's artifact is **`<step-number>-<slug>.md`** (`2-analysis.md`); the numeric prefix only sorts
the listing, and links use the real filename, prefix included. Registers and deliverables take no
prefix. The six names are the step list in [`OVERVIEW.md`](OVERVIEW.md).

## Step folders & worklogs

The artifact `<step-number>-<slug>.md` is a **projection**; its working lives in the sibling folder
of the same stem, one **worklog per method**: `<step-folder>/<tool>.md`, where `<tool>` is the id in
the section's `<!-- tool: <tool> -->` marker. **The worklog is the source of truth; the artifact
section is its projection** — every projected section has a worklog (check P), and the method's
change-log history lives there, not in the artifact. How a section resolves to exactly one worklog —
the id-thread, synthesis sections, a marker naming several tools —
[`reference/worklog-resolution.md`](reference/worklog-resolution.md). Raw external inputs are never
worked in a worklog directly: they live in `sources/` and are dispatched in by `source-intake`
(see *Raw data & access*). A worklog is **private to its method** — read only by that method, its
projection, provenance audit, and a card that **declares** it (`worklog:<step>/<method>` in `reads`);
**undeclared cross-step exchange runs through the registers and the signed artifact sections**,
never by reading another step's worklog (OPERATING-LOOP move 2; linter check T).

## Section confirmation

An artifact section is a **thesis** — the linter holds its *structure*, a **human** holds its
*meaning* by signing it:

```markdown
## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
<!-- confirmed: 2026-08-13 -->
```

- **`confirmed: YYYY-MM-DD`** (optional ` by:<who>`) — approval of *this* version. Absence = pending.
  Re-projection from a changed worklog **drops** the marker.
- **`contested: YYYY-MM-DD`** — a human reviewed and pushed back (distinct from pending: someone
  looked). Confirmed or contested, never both (check R); the reason goes in the change log.
- **`rests-on: <step>#<section-id>, …`** — a **schema** marker (lives in the step template): the
  upstream sections a conclusion depends on. Confirmed-on-unconfirmed-foundation warns (check S).
- **`open`** — an agent→human inbox (`to-clarify`, `open-questions`, `blockers`): resolved by
  *removing* items, never confirmed (check R), left out of the "N of M confirmed" count. **Every
  item names which kind it is** — *the human chooses* (it waits for a person) · *nobody knows yet*
  (it waits for work someone must go and do) · *a later step owns it* (naming the step). The kinds
  are not decoration: an inbox where the second kind is filed as the first reads as decided when
  it is merely unasked, and the reader most likely to act on it is the one the label is for. Where
  the inbox is a **table with an owner column** (`#blockers`), that column *is* the kind — it already
  names who must act, and a second label beside it would be the same fact spelled twice.

The procedure — walking the human through each thesis, never self-issued — is the
[`theses`](../tool-skills/operations/theses/SKILL.md) operations skill (OPERATING-LOOP move 5).

## Gradation vs confirmation — two orthogonal axes

**Confirmation** answers *has a human signed this?* — the binary marker above. **Gradation** answers
*how good is it?* — ordinal scales carried inside the row (enums in
[`REGISTERS.md`](REGISTERS.md)). The axes are independent: a reader renders **two chips**, never
folding one into the other.

## Instance config (`config.yaml`)

`config.yaml` is the **human's decisions** about the instance; cycle position lives in `state.yaml`
(OPERATING-LOOP). Keys are canon, spelled exactly one way (check H); the pinned schema is
[`reference/config-schema.md`](reference/config-schema.md) — read it when writing or validating a
`config.yaml`.

## Cards

Everything an agent acts on is a **card** — a step README, a library method, an operations or outputs
skill, a product's own exchange skill. **One entity, one frontmatter schema, five `kind`s**; the
header *is* the pass plan (`prerequisites` · `reads` · `writes` · `surfaces`), declaring types and
slots while the pass resolves the instances from the data. Ranks and routing are the
[goal map](goal-map.md)'s; the schema is [`reference/card-schema.md`](reference/card-schema.md), read
when writing or validating a card.

**Two homes, and the author decides which** (check Z): a card shipped with the framework lives in
`tool-skills/`, a card written for one product in that instance's `skills/`, where a framework update
never touches it. Objective, like the delivery channel in `sources/` — never a judgement about content.

## One mechanism, one way

Product decisions fork; **framework mechanics must not**. For anything the framework itself does
there is exactly **one canonical way** — no dual formats, no migration thresholds, no documented
alternatives. If two ways exist, pick one and eliminate the other in the same change.

## Where a new rule goes — contract · method · check

Only a **contract two independent readers must agree on** earns a place in this file — a check or a
skill is cheaper and is tried first. Classify before adding:
[`extending/rules.md`](../extending/rules.md).

## Forks & options

**Triage first.** Escalate a decision to the human only if it is (a) consequential AND (b) not
closable from evidence — everything reversible and cheap the agent decides itself, marks **⚙️**, and
logs; it does not ask. A surviving fork is presented as **2–4 concrete options with trade-offs**, the
recommended one marked **⚙️** — never a single option with the alternatives hidden.
Technical/implementation gaps are noted as forks in the artifact, not asked. An open fork is an
unresolved risk: close it, or escalate it with an owner.

## Talking to the human

In chat, never send a bare register ID, section anchor, or link — decode it in the same sentence
("`H-009` — the bet that tech leads stay for the frontier stream"). IDs stay bare only inside
artifacts, where the register is one click away.

## Raw data & access

**A source is what comes from outside**; no skill produces one from inside — agent reasoning is a
worklog, a file for outside use is an export file (`export-files/`, the mirror of `sources/`). What
fits none of the entities is recut along these seams — a new entity or hybrid home is never minted.
`sources/` holds **only what came from outside**, in three subfolders indexed by `sources/INDEX.md`:
**`originals/`** · **`snapshots/`** · **`access/`** — the last holding a source's **passport**,
written **only as the human's recorded answers**; an agent never invents one, and a passport of bare
`— to clarify —` is the defect (check T). A source is **dispatched into worklogs, never linked from
an artifact**; captured values go to the registers as dated rows. Who writes into which subfolder,
and an instance exchange card's rules — [`reference/boundary-layout.md`](reference/boundary-layout.md).
Hard rules (also in [`AGENTS.md`](../AGENTS.md)): **raw captures are never committed**, deleted once
their values land; where `origin` may be public, raw data and its analysis code live **outside** the
repo; **secrets** are never written anywhere — only *where* they live and how to rotate. The routing
procedure — [`source-intake`](../tool-skills/operations/source-intake/SKILL.md).

## Which conventions apply where

A file's `node_type` selects which conventions apply; the authoritative matrix is
[`reference/node-type-matrix.md`](reference/node-type-matrix.md) — consult it when in doubt.
Omitting a convention the matrix marks n/a is **correct**, not a lapse. A convention not in the
matrix (e.g. *Talking to the human*) is behavioral and applies always.

## Change logs

Every **instance artifact** ends with a change log — the `artifact`, `worklog`, `register`, `source`,
`sources-index`, and `handoff` rows in the matrix above — newest first, carrying the *motivation*.
The **worklog** is on that list and not by exception: a section is a projection and carries no history
of its own, so the method's history lives in the worklog (matrix, `worklog` row):

```markdown
## Change log

### 2026-07-16 — <one-line summary>
- **From → To:** <what the state was> → <what it is now>
- **Why:** <reasoning>
- **Trigger:** <what prompted it>
```

A **register** entry names the ids it moved (`H-004`, `M-activation`) inside its From → To — that
one habit is what lets the console assemble a single item's trail. Framework files carry **no**
inline change log; their history is the root [`CHANGELOG.md`](../CHANGELOG.md), keyed to git tags.
