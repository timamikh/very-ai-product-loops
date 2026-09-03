---
node_type: conventions
title: Conventions — markers, IDs, links, change logs
status: draft
version: 0.34.0
updated: 2026-09-02
---

# Conventions

The shared notation every step template, library tool and instance file uses — each section a
**contract** two independent readers (an agent and a tool, or two agents) must agree on. Procedures
live in the operations skills, authoring detail in [`reference/`](reference/README.md) — every
pointer below names the moment to read it.

## Confidence tags

Every non-trivial claim ends with a tag; **no tag = `assumption`**:
`[assumption]` · `[sourced: <where>]` (e.g. `[sourced: metrics W24]`) ·
`[validated: <evidence>]` · `[refuted: <why>]` (kept, never deleted — see change log). The agent's
own derived conclusion is `[assumption]` — never blanket-sourced to the inputs it rests on.
Agent-proposed defaults awaiting human approval are prefixed **⚙️**.

## Sources

`[sourced: ...]` names the origin. Source slots a tool/step may draw from:
`kb` · `interview` · `research` · `metrics` · `git` — the machine home is `cards.SOURCE_SLOTS`,
a new slot is a framework change. A **dated human decision** is a legal `[sourced:]` origin but not
a slot — an ambient input every perimeter carries ([`reference/card-schema.md`](reference/card-schema.md)
→ *reads is a perimeter*). Missing data is written literally as `— to clarify —`, never guessed.

## Sections and their IDs

Every artifact section carries a stable, kebab-case ID so tools can fill it and links can target it:
`## Value & Defensibility {#value-defensibility}`. Rename the heading text freely; keep the ID.
A section is **worked** when its body carries at least one line beyond the step template's
placeholder shell (compared by normalized line); a bare anchor or an untouched skeleton is *present*,
not worked — the reading the linter (checks E3 · L2) and the console share.

## Column keys

A table column is addressed by a **stable key** in a hidden header comment (`| Layer <!--c:layer--> |`),
never by its header text — so it is found in any language. A table is **all-keyed or none** (check O);
a filled instance section carries its template's keys (check O2); **no consumer, no key**. Key form
and the three homes of a key — [`reference/column-keys.md`](reference/column-keys.md), read when
authoring a template or a register.

## The decision line

A section whose conclusion rests on **a choice** ends in one canonical line; its three fields carry
**field keys** so a tool reads them in any language:

```markdown
**Decided:** <!--d:date--> 2026-08-20 · **by:** <!--d:by--> ⚙️ acting PO · **alternatives considered:**
<!--d:alts--> leading on demand rather than feasibility (rejected — the concept lives or dies on the engine)
```

Label prose is free and translatable, the keys are not. `·` separates the fields, so no value
*before* the last may hold one; `d:alts` runs to the end of the block, and the line is its section's
last. **All three keys or none** (check O4); the alternatives field is never a bare *none* — it names
one weighed alternative and why it lost, or what makes the choice forced
([`../tool-skills/library/README.md`](../tool-skills/library/README.md) → *The rejected alternative*).
Unlike a column key, this line lives in the method's `template-fragment.md`, copied verbatim.

## Card line

A section may mark **one of its own blocks** as its headline — what a board card shows collapsed:
`<!-- card -->` **trailing a line** names the block that line sits in; **alone on a line**, the
paragraph below. Always a block, never a physical line. One mark per section;
no mark = title + status. **The slot is declared in the method's `template-fragment.md`**, and every
projection places the mark on that same element. What the console shows and why a section may stay
unmarked — [`projection`](../tool-skills/operations/projection/SKILL.md) step 3.

## Links & register item IDs

Register items have stable IDs — prefixes and files enumerated once in [`REGISTERS.md`](REGISTERS.md).
Numbered ids count **sequentially and are never reused**; digit width is free (`F-01` and `F-001`
are both valid). Reference one inline in brackets: "drives `M-activation`".

**Cross-artifact links are a relative file path + the target's stable `{#anchor}`** —
`2-analysis.md#opportunity` (from a subdirectory: `../2-analysis.md#opportunity`). **Never** a
wiki-style double-bracket link; point at the `{#anchor}`, never a heading's changeable text. A gate
checklist may use the shorthand `artifact#section` (e.g. `concept#idea`).

## Artifacts, step folders & worklogs

A step's artifact is **`<step-number>-<slug>.md`** (`2-analysis.md`; the prefix only sorts, links use
the real filename; registers and deliverables take no prefix). The artifact is a **projection**; its
working lives in the sibling folder of the same stem, one **worklog per method**: `<step-folder>/<tool>.md`, `<tool>` being the id in the section's
`<!-- tool: <tool> -->` marker. **The worklog is the source of truth; the section is its projection**
— every projected section has a worklog (check P), and the method's history lives there. A worklog
is **private to its method**: read by it, its projection, an audit, and a card that **declares** it
(`worklog:<step>/<method>` in `reads`); anything else crosses steps through the registers and the
signed sections (check T). Resolution — id-thread, synthesis, several tools on one marker, a revisit
in its own folder — [`reference/worklog-resolution.md`](reference/worklog-resolution.md); the
copyable shape — [`reference/worklog-skeleton.md`](reference/worklog-skeleton.md).

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
- **`contested: YYYY-MM-DD`** — a human reviewed and pushed back. Confirmed or contested, never both
  (check R); the reason goes in the change log.
- **`rests-on: <step>#<section-id>, …`** — a **schema** marker (lives in the step template): the
  upstream sections a conclusion depends on. Confirmed-on-unconfirmed-foundation warns (check S).
- **`open`** — an agent→human inbox (`to-clarify`, `open-questions`, `blockers`): resolved by
  *removing* items, never confirmed (check R), outside the "N of M confirmed" count. **Every item
  names its kind**: *the human chooses* · *nobody knows yet* · *a later step owns it* (naming the
  step); in a table with an owner column (`#blockers`), that column *is* the kind.

The procedure — walking the human through each thesis, never self-issued — is the
[`theses`](../tool-skills/operations/theses/SKILL.md) operations skill (OPERATING-LOOP move 5).

## Instance config and state

`config.yaml` is the **human's decisions** (keys spelled one way, check H —
[`reference/config-schema.md`](reference/config-schema.md)); `state.yaml` is the **agent-written
position** ([`reference/state-schema.md`](reference/state-schema.md)). Read the schema when writing
or validating the file.

## Cards

Everything an agent acts on is a **card** — a step README, a library method, an operations or outputs
skill, a product's own exchange skill. **One entity, one frontmatter schema, five `kind`s**; the
header *is* the pass plan (`prerequisites` · `reads` · `writes` · `surfaces`). The schema is
[`reference/card-schema.md`](reference/card-schema.md), read when writing or validating a card.
**Two homes** (check Z): a framework card lives in `tool-skills/`, a product's own in its instance's
`skills/`, where an update never touches it.

## One mechanism, one way

Product decisions fork; **framework mechanics must not**: for anything the framework itself does
there is exactly **one canonical way** — no dual formats, no documented alternatives; if two ways
exist, pick one and eliminate the other in the same change. Only a **contract two independent
readers must agree on** earns a place in this file — a check or a skill is cheaper and is tried
first: [`extending/rules.md`](../extending/rules.md).

## Raw data & access

**A source is what comes from outside**; no skill produces one from inside — agent reasoning is a
worklog, a file for outside use is an export file (`export-files/`, the mirror of `sources/`); what
fits no entity is recut along these seams, never given a new home. `sources/` holds **only**
`originals/` · `snapshots/` · `access/` + `INDEX.md` (check T); `access/` holds a source's
**passport**, written only as the human's recorded answers. A source is **dispatched into worklogs,
never linked from an artifact**; captured values become dated register rows. **N8: raw captures are
never committed** — deleted once landed; **secrets and PII are never written** — only *where* a
secret lives and how to rotate it (the linter's secret scan). Writer matrix, INDEX header, exchange
cards — [`reference/boundary-layout.md`](reference/boundary-layout.md); the routing procedure —
[`source-intake`](../tool-skills/operations/source-intake/SKILL.md).

## Which conventions apply where — and change logs

A file's `node_type` selects which conventions apply — the closed set of types and the matrix are
[`reference/node-type-matrix.md`](reference/node-type-matrix.md); omitting what the matrix marks n/a
is **correct**. Every **instance file** the matrix says so ends with a change log — newest first,
carrying the *motivation*; a section's history lives in its **worklog**:

```markdown
## Change log

### 2026-07-16 — <one-line summary>
- **From → To:** <what the state was> → <what it is now>
- **Why:** <reasoning>
- **Trigger:** <what prompted it>
```

A **register** entry names the ids it moved (`H-004`) inside its From → To — what lets the console
assemble one item's trail. Framework files carry **no** inline change log; their history is the
root [`CHANGELOG.md`](../CHANGELOG.md).
