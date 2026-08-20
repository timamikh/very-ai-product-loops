---
node_type: extending
title: Add or change a status — the product's stage plane
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add or change a status

*Read this when the shipped stages do not describe where the product actually is, or when a stage should
ask for something different. The dial table is in* [`../EXTENDING.md`](../EXTENDING.md); *the anatomy of
a status file is in* [`../statuses/README.md`](../statuses/README.md) → *Anatomy of a status*.

A **status** is the framework's adaptation dial: it parameterizes all six steps without touching the
process core. For each step it sets the **goals** that keep the agent focused, the **tools** to lean on,
and once, a **gate emphasis**.

## Is this the right dial

| What you actually want | The dial |
|---|---|
| this stage should focus elsewhere | **this file** — the `per_step.goals` |
| the same section worked by a different method at a different stage | **this file** — the `per_step.tools` |
| our stages are not concept-viability / PMF / growth | **this file** — add or rename them |
| a way of working nothing in the library does | [`method.md`](method.md) first; a status can only recommend a method that exists |
| content the artifacts do not hold | [`section.md`](section.md) — goals cannot create a home |
| another execution stream | [`config.md`](config.md) — directions, not stages |
| a different set of steps | [`step.md`](step.md) — and read the redirect table there first |

## Procedure

1. **Name the stage from how the product is actually run**, not from a maturity vocabulary you like.
   The question a status answers is *what are we optimizing for right now, and what evidence do we
   trust* — a stage that cannot answer both is a label.
2. **Create `statuses/<order>-<name>.md`** — numbered by maturity, so the folder reads youngest → most
   mature top to bottom. The number matches the `order` field.
3. **Fill `gate_emphasis`** — what the step checklists should weigh most at this stage.
4. **Fill `per_step` for every step**, `"1"` … `"6"`: its `goals` (flat, or split by direction where the
   step is direction-organized) and its `tools`. **A step you leave out silently has no goals there** —
   that is the one failure of this dial, and nothing warns you.
5. **Keep the goals concrete.** They exist to hold the agent's focus, not to restate theory. "Prove the
   value repeats and you can charge for it" is a goal; "achieve product-market fit" is a slogan.
6. **Slot it into the maturity order** — the filename number *and* the `order` field. Inserting in the
   middle renumbers the neighbours, and a renumber is a rename.
7. **Add the row** to [`../statuses/README.md`](../statuses/README.md) → *Default statuses* and to the
   *Choosing a status* table, which is what product setup shows the human.
8. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).

Nothing else needs editing: the process core reads whatever status is active and applies its per-step
parameters. No step file changes.

## The two rules a `tools:` list obeys (check V)

- **Library methods only.** *How* the data is gathered — interviews, a metrics pull, desk research — is
  named in the step's goals prose, never in this list.
- **Every listed method has a home in that step's template** — a `<!-- tool: … -->` marker. A
  recommendation with no section to land in forces the agent to invent one, so the linter refuses it.

A contributing method with no section of its own (`pricing-strategic-plan`) is named **second** in its
receiving section's marker and is listed by no status.

## Switching the active status

Changing stages is a different act from adding one. The active status is set at the instance level
(`config.yaml`, referenced from the strategy artifact), and switching it is a normal instance change: a
dated change-log entry with the **why**, not just the new name. Nothing in the artifacts is rewritten by
the switch — the next passes simply work under different goals.

## Checklist

- [ ] The stage answers both halves: what it optimizes for, and what evidence it trusts.
- [ ] Every one of the six steps has a `per_step` block — none silently empty.
- [ ] Goals are concrete enough that an agent could tell whether a pass served them.
- [ ] Every method in every `tools:` list exists and has a marker in that step's template.
- [ ] No gathering technique smuggled into a `tools:` list.
- [ ] Filename number and `order` agree, neighbours renumbered if you inserted in the middle.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.
