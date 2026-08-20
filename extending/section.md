---
node_type: extending
title: Change a section or its columns — the shape of the record
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Change a section or its columns

*Read this when an artifact must hold a field it does not hold, when a table needs reshaping, or when a
column must become machine-readable. The dial table is in* [`../EXTENDING.md`](../EXTENDING.md); *the
key rules are in* [`../process/reference/column-keys.md`](../process/reference/column-keys.md).

A step artifact's shape is a **contract**, and its one home is the step template
`steps/<n>/template.md`: the clean copy an instance fills and the console that renders it are the *same
form*, read from there. So changing a section means changing that schema — everything else follows it,
and nothing is a second edit.

## Is this the right dial

| What you actually want | The dial |
|---|---|
| a field, a column, a new section in a step artifact | **this file** |
| a different way of *filling* an existing section | [`method.md`](method.md) — the shape stays, the method changes |
| a different stage to ask for something else | [`status.md`](status.md) — goals, not shape |
| the register schemas | not a dial. The three schemas are the contract every tool reads ([`../process/REGISTERS.md`](../process/REGISTERS.md)). What an instance may use instead: `tags` for a cross-cutting theme, `note` for a qualifier an enum cell cannot hold. A **fourth** register is [`register.md`](register.md) |
| a whole step | [`step.md`](step.md) |

## A section is three marks

- **`## Title {#anchor}`** — the stable handle. The prose language is free, the anchor is not.
- **`<!-- tool: X -->`** — the method that fills it. The same `X` names the skill folder
  `tool-skills/library/X/` and the worklog `<step-folder>/X.md`: **one id threads method, worklog and
  section.**
- **`<!--c:key-->` on each column a consumer reads** — a column is addressed by its key, never by header
  prose. A column nothing reads by key carries none ("no consumer, no key"). A table is
  **all-keyed or none**.

## Procedure

1. **Decide what reads the new field.** If nothing does, it takes no key — and if nothing reads the
   section either, ask once more whether it belongs in a worklog instead.
2. **Edit the step template** `steps/<n>/template.md` — the section, its marker, its columns and their
   keys. Keep existing anchors and keys stable: renaming one is a different act, with the consequences
   below.
3. **Declare a closed vocabulary** where the method genuinely fixes one — `<!-- enum:c:key: a | b | c -->`
   right under the table. Check O3 then holds every instance cell to those tokens. A free-text column
   takes none.
4. **Give the section a method** — its `<!-- tool: X -->` must name a card that exists and declares this
   step ([`method.md`](method.md)).
5. **Update the step README** — the artifact skeleton, the gate checklist, the register touchpoints, if
   the change touches them.
6. **Re-project the instances that already carry the section** — content moves into the new form, nothing
   is invented, anything with no home becomes `— to clarify —`, and the section keeps a dated change-log
   entry. If the conclusion did not change, the confirmation marker stands; if it did, the marker drops.
   For a shape change arriving with a framework update, see
   [`../install/UPDATE.md`](../install/UPDATE.md) → *Migrating a filled instance*.
7. **Run the linter to zero**, bump the template `version`, record it in
   [`../CHANGELOG.md`](../CHANGELOG.md).

## What the change drags with it

- **The gate item is derived, not maintained.** Every `{#anchor}` becomes `artifact#section` in
  `state.yaml` on its own (`tools/loops/framework.py`), so a renamed anchor renames its gate id and
  **orphans its ticks**. Keep anchors stable.
- **The linter holds the shape:** check **O** (keys well-formed on the template — all-keyed-or-none,
  unique; a key in a *method* template is an error), check **O2** (a filled instance section carries its
  template's keys), check **O3** (cells obey a declared vocabulary), check **P** (the `<!-- tool: X -->`
  has its worklog).
- **The console follows the keys by itself.** It reads every section by anchor + key, so a new or
  reshaped section renders generically with **no console edit** and no per-section widget to author. If
  you think you need to touch the console, read [`interface.md`](interface.md) before you do.
- **Cross-section references go by words, not row codes.** A code like `P1` that lives only in a worklog
  does not survive into another section's prose — a reader who was not in the room cannot resolve it.

## The one bypass the machine cannot see

**Change the shape = change the keys, then run the linter.** Editing the template's prose while leaving
the keys as they were is the one path the console cannot notice: it will keep reading the old columns and
render something that looks right. Checks O and O2 are what catch it, and they only catch it if you ran
them.

## Checklist

- [ ] Something actually reads every key you added.
- [ ] Every anchor that existed before still exists, spelled the same.
- [ ] No key landed in a method's `template-fragment.md`.
- [ ] The section names a method that exists and declares this step.
- [ ] Any declared vocabulary is closed, non-empty, and matches a key the table carries.
- [ ] Instances re-projected: content moved, nothing invented, gaps read `— to clarify —`.
- [ ] Confirmation markers dropped exactly where a conclusion changed, and kept where it did not.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Template `version` bumped, `CHANGELOG.md` entry written.
