---
node_type: install
title: Update — move an installed framework to a newer version
status: draft
version: 0.3.1
updated: 2026-09-03
---

# Update

*Read this when a product repo already carries the framework and should move to a newer tag. The first
install is [`README.md`](README.md); adapting the framework rather than updating it is
[`../EXTENDING.md`](../EXTENDING.md).*

**An update is a re-vendor.** There is no patch mechanism and no migration script: the agent overwrites
the vendored tree at a newer tag and rewrites `FRAMEWORK-VERSION`. Everything the product owns lives
outside that tree and is not touched.

## What is overwritten, what survives

| Overwritten by the update | Survives untouched |
|---|---|
| the vendored set — the list under [`README.md` → *What lands in your repo*](README.md#what-lands-in-your-repo), `FRAMEWORK-VERSION` included | `product-loops/` — every artifact, register, worklog, source, `config.yaml`, `state.yaml`, `HANDOFF.md` |
| | `product-loops/tool-skills/` — the product's own methods and operations |
| | `product-loops/skills/` — the product's own exchange cards |
| | your repo's root `CLAUDE.md` pointer, if you added one |

**Anything you edited inside the vendored tree is lost.** That is not a warning about carelessness — it
is the design: the only way to keep a change is to put it where the update cannot reach, which is what
[`../EXTENDING.md`](../EXTENDING.md) routes every dial to.

## Procedure

1. **Read what changed** — diff the vendored tree between your pinned SHA and the new one
   (`git diff <old-sha> <new-sha> -- steps/ process/ tool-skills/ statuses/`); the CHANGELOG is a
   reading aid, the diff is the truth. Five things matter more than the rest, because only these can
   leave a filled instance off-form:
   **step templates** (a section, a column, a key), **register schemas**, **new or renamed checks**,
   **methods removed or recut**, and **a changed meaning of an existing column** — same name, new
   semantics (`metrics.csv` once carried the population inside `basis`; now `basis` is *how counted*
   and `population` *who*): append-only rows written under the old meaning stay, so the register's
   header notes the date the meaning changed and a reader compares across it with care.
2. **Re-vendor at the new tag** — overwrite the paths in the left column above, and touch nothing under
   `product-loops/`.
3. **Rewrite `FRAMEWORK-VERSION`** with the new tag **and** its commit SHA. The tag is the human-readable
   version, the SHA the immutable anchor.
4. **Restart the session once.** Agent definitions and skills vendored mid-session are picked up only at
   the next start.
5. **Run `python3 tools/lint.py <instance>`.** Expect reports that were silent before — a new check
   reading old content is the update working, not failing. A section left off-form by a moved template
   (checks O2/O3) reports as a **WARN** on a product instance: visible debt, worked as an ordinary pass,
   never a blocker. Check the `instances checked:` line names your instance.
6. **Work the report as ordinary passes**, not as a cleanup sweep:
   - a **shape** error → re-project the section into the new form
     ([`../extending/section.md`](../extending/section.md) → step 6);
   - a **homeless method** → the card it pointed at moved or was recut; re-home it
     ([`../extending/method.md`](../extending/method.md));
   - a **removed method** you relied on → the diff (and the CHANGELOG) name what replaced it; if nothing did, that is a
     local card ([`../extending/method.md`](../extending/method.md)), not a reason to stay behind.
7. **Re-check your local cards that shadow a vendored one.** A local card of the same name still wins —
   but it now shadows a *newer* card, which may fill a section whose shape changed under it. A shadow that
   was correct at the old tag is not automatically correct at the new one.
8. **Record what moved.** `FRAMEWORK-VERSION` is the record of the version you are on; anything the update
   changed *inside an artifact* takes a dated change-log entry in that artifact, with the why.

## Checklist

- [ ] The CHANGELOG was read for the five things that can leave an instance off-form.
- [ ] Nothing under `product-loops/` was touched by the re-vendor.
- [ ] `FRAMEWORK-VERSION` carries the new tag **and** SHA.
- [ ] The session was restarted once.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Every local card that shadows a vendored one was re-read against the new version.
- [ ] Every artifact the update changed carries a dated change-log entry with the why.
- [ ] No confirmation marker was left standing over a conclusion that changed.

## Adopt an existing instance

The case: a `product-loops/` instance was filled under an earlier framework version — by you, by
another team, or by a run whose vendored copy is gone — and must now live under the current one.
Adoption is an update whose starting point is the instance, not the framework:

1. **Pin the new version** — vendor the framework at the current tag and write `FRAMEWORK-VERSION`
   (tag **and** SHA). If the instance carries no record of the version it was built under, note that
   in its `HANDOFF.md`: the diff step below is then read from the instance's own change logs.
2. **Run `python3 tools/lint.py <instance>`** and keep the report — it is the adoption work list.
   Check the `instances checked:` line names the instance.
3. **Treat O2/O3 drift as debt, not as a blocker** — a section in an older template's form is a WARN
   on a product instance (ERROR only under `examples/`); the instance is usable while sections wait.
4. **Re-project each drifted section with its owning method** — the `<!-- tool: -->` marker names
   it; the section is rebuilt from its worklog into the new form
   ([`../extending/section.md`](../extending/section.md) → step 6), one section per pass, on the
   human's order. Missing worklogs (check P) are the first debt to work: a section with no working
   behind it is re-worked, not copied.
5. **Never hand-edit an artifact into shape.** A section patched straight into the new form says
   something its worklog does not; the sign-off it carried is dropped either way, and `theses`
   re-confirms the new version.

Registers follow the same path: a register missing a file or a key the current
[`REGISTERS.md`](../process/REGISTERS.md) enumerates is completed from the skeletons (headers copied,
never retyped); rows are never invented to fill a new column.

## Migrating a filled instance

The case: a new version changes the shape of a section — a column added, a key introduced, a table recut —
and the instance already filled that section. Re-vendoring the template is trivial; the filled artifact
stays in the old form, and the conformance check (O2) starts reporting it.

**There is no migration mechanism, on purpose** (decided 2026-08-20). Migration is ordinary work the
orchestrator does when the human asks for it in chat — no separate skill, no separate instruction. The
flow is:

1. the update lands, the linter reports which sections are off-form (that report *is* the work list);
2. the agent shows the list to the human;
3. the human says, in chat, what to migrate and when — now, later, or section by section;
4. each migration is a normal re-projection — content moves into the new form, nothing is invented,
   anything with no home reads `— to clarify —`, the section takes a dated change-log entry, and a
   confirmation marker stands only if the conclusion did not change
   ([`../extending/section.md`](../extending/section.md) → step 6).

An off-form section is a visible, linted debt — not a blocker. The update may land while sections wait.

**v0.12 (product axis) — what changed shape.** The feature register arrived
(`registers/features.md` `F-001…` + `registers/surfaces.md` `S-01…`, skeletons in
`process/reference/register-skeletons/`); Step-6 items lost their positional letters (`F-1`/`A-1`/
`T-1` → `1, 2, …` within the direction subsection) and gained three lines — `Feature:` (the
register row the item advances), `Expected impact:` (with a check-by), `Estimate:` (class S/M/L);
the Step-6 backlog gained a `feature` column; Step 5 gained `{#item-readouts}` (`impact-readout`
reads shipped items against their pre-registered expectations and flips `planned → live`). Typical
migration, per the flow above: copy the two skeletons into `registers/`, renumber the current
sprint's items (the linter's E2/E3 warnings and the O2 backlog-column report are the work list),
mint rows for items the human confirms, tick `item-feature` — and never back-fill an Expected
impact onto an already-shipped item (an item shipped without one gets exactly that said in its
readout row). `examples/decksmith` shows the migrated form; `examples/tolmach`'s change log shows
the minimal (register-skeleton + rename) variant with the rest deferred.

**v0.13 (the axis on every status + the priority cascade) — what changed shape.** The product axis
lost its status switch: `product-baseline` and `impact-readout` now run at `concept-viability` too —
each is gated by its own prerequisite (nothing live → baseline skips itself), and check E3 expects
the item pre-registration on every status. Surfaces gained their three birth doors in canon
(`product-surface` ledgers designed ones `planned` at Step 3; `product-baseline` inventories live
ones; a Step-6 `activity-spec` may mint a g2m surface). `features.md` gained an **optional**
`priority` column (`now · next · later` — Step 4 seeds the structural weight off the committed
targets, Step 5 finalizes by period fit, Step 6 reads it as a ranking input). Typical migration:
none required — a register without the column is legal until the first Step-4/5 pass writes it;
add `Priority <!--c:priority-->` when that pass runs (the linter validates values only when the
column exists).
