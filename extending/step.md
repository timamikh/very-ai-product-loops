---
node_type: extending
title: Add, remove or reorder a step — the fixed core
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add, remove or reorder a step

*Read this before touching `steps/`. The dial table is in* [`../EXTENDING.md`](../EXTENDING.md).

**Start from the assumption that you don't need to.** The six steps are the fixed core: the thing that
makes two instances comparable and every tool able to read them. Nearly every "we need a different step"
turns out to be one of the dials below, and each of those costs nothing.

## Almost always, it is one of these

| What you actually want | The dial |
|---|---|
| this stage should focus elsewhere | [`status.md`](status.md) — the `per_step` goals and tools |
| content the artifacts don't hold | [`section.md`](section.md), then [`method.md`](method.md) — a method whose written section is homed in an *existing* step artifact |
| a way of working the library lacks | [`method.md`](method.md) |
| a different output | [`output.md`](output.md) |
| another execution stream | [`config.md`](config.md) — `directions` |
| our stage isn't concept-viability / PMF / growth | [`status.md`](status.md) — a new status |
| something between passes | [`operation.md`](operation.md) |

If it is genuinely none of those, then a step change is a **change to the framework core** — a fork or an
upstream contribution, **never** an instance-level edit. A product folder that carries a seventh step is
an instance no other tool can read.

## What it drags with it

Read all of it before deciding, because each item is work you will owe:

- **Every gate checklist item is keyed to `artifact#section`**, and gate ids are derived from anchors —
  so a renumbered artifact renames every gate id it holds and **orphans every tick**.
- **Cross-artifact links are real relative paths**, so a renamed or renumbered artifact breaks them.
- **The filename prefix is a sort order** (`1-…` … `6-…`), so inserting in the middle renumbers the
  neighbours — and renumbering is a rename, with the link consequences above.
- **Check B fails for every method whose section you removed** — a method's output must have a home in
  some step template.
- **Every status file must gain a `per_step` block** for a new step, or it silently has no goals there.
- **Every filled instance is off-form** until it is migrated — see
  [`../install/UPDATE.md`](../install/UPDATE.md) → *Migrating a filled instance*.
- **The overview, the README and the diagrams** all state the count of steps.

## Procedure, if you accept all that

1. **Write down which of the redirect rows above you rejected, and why.** If you cannot, stop — the
   answer is one of them.
2. **Change `steps/`** — the template, the README, the gate checklist, the register touchpoints.
3. **Update every status's `per_step`** so no step is silently goal-less.
4. **Re-home the affected methods** — every card whose section moved or vanished.
5. **Fix every cross-artifact link** the renumbering broke.
6. **Migrate the instances** you own, and say what other instances owe.
7. **Update the count** wherever the framework states it — overview, README, diagrams.
8. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).
9. **Keep it in a fork or a pull request** — not in a product folder.

## Checklist

- [ ] The rejected alternatives are written down, not felt.
- [ ] Every status has a `per_step` block for every step that now exists.
- [ ] No method is left with a homeless section (check B).
- [ ] Every cross-artifact link resolves.
- [ ] Gate ticks accounted for: what was orphaned, and what happened to it.
- [ ] The stated count of steps agrees everywhere the framework states it.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] The change lives in a fork or a pull request, and `CHANGELOG.md` says what it was for.
