---
node_type: extending
title: Add a rule — classify it first: check · method · contract
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add a rule

*Read this when a failure has just tempted you to write a paragraph that would have prevented it. The
dial table is in* [`../EXTENDING.md`](../EXTENDING.md).

The framework accretes. Every real failure tempts a sentence, and sentences land in the files an agent
reads on **every** pass. So a proposed rule is first **classified**, and only one of the three classes is
allowed to grow the always-loaded canon.

## The three classes

| Class | Home | What it costs | Use it for |
|-------|------|---------------|------------|
| **Check** | [`../tools/lint.py`](../tools/lint.py) | **nothing at read time**; catches the case every run | anything a machine can verify: shapes, ids, enum membership, cross-file agreement |
| **Method** | a card under `tool-skills/` | read only when that card is used | procedure, technique, judgement — *how* to do the thing well |
| **Contract** | `process/` (the always-loaded canon) | paid on every pass, by every agent | only what two independent readers must agree on: field names, enum values, id shapes, file roles (`node_type`), path and link form |

**Try the classes in that order.** A check costs no context and does not depend on the agent remembering;
a sentence in the canon costs context forever and does. "The linter is the gate" is not just enforcement
— it is where a rule belongs when it *can* live there.

## Two consequences worth stating

- **A budget on the always-loaded set.** The per-pass canon (`AGENTS.md` + `process/OVERVIEW.md` +
  `OPERATING-LOOP.md` + `process/goal-map.md` + `CONVENTIONS.md`) is watched by **linter check W** — a
  guideline that warns, never a gate that fails; the number lives in one place —
  `BUDGET_GUIDELINE_WORDS` in [`../tools/lint.py`](../tools/lint.py) (4600 words at this writing). The method library is several times that size and costs nothing
  until used. An addition to `process/` names what it displaces, or why it is neither a check nor a
  method. A reference only one task needs goes to
  [`../process/reference/`](../process/reference/README.md), pointed at from a one-line stub in the core;
  `process/REGISTERS.md` follows the same pattern — read at its named moments, outside the per-pass set.
- **Subtraction is part of the job.** A rule stated in two of these files is two places to drift. When a
  change touches a duplicated rule, delete the copy in the same change and leave a pointer.

## A rule with no carrier is not a rule

The commonest failure of this dial is not misclassification — it is a rule written where the person who
must obey it never reads. A contract in `process/` that no template placeholder, no card and no check
ever mentions will be broken by an agent who never had a reason to open that file.

So for every rule you keep, name its **carrier**: the placeholder in a template, the line in a card's
`template-fragment.md`, the item on a fresh reader's checklist, or the check that fails. A rule whose
carrier you cannot name is either a check you have not written yet, or a sentence to delete.

## Procedure

1. **Write the failure**, not the rule — the concrete case, once, in one sentence.
2. **Try `check` first.** Can a machine see it in the files? Then write the check, and write the test that
   proves it: inject the defect it must catch and watch it fail, then restore.
3. **Try `method` next.** Is it *how* to do something well? Then it goes in the card that does that thing,
   and nowhere else.
4. **Only then `contract`.** If two readers must agree on it, put it in `process/` — and in the same
   change, name what it displaces.
5. **Name the carrier** for whichever class you chose.
6. **Delete the duplicate** if the rule already exists somewhere else, and leave a pointer.
7. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).

## Checklist

- [ ] The failure it prevents is written down as a concrete case.
- [ ] The classes were tried in order, and the reason a cheaper class was rejected is written down.
- [ ] A new check comes with the injection that proves it catches the defect.
- [ ] The rule has a named carrier — a placeholder, a card line, a checklist item, or a failing check.
- [ ] An addition to `process/` names what it displaces.
- [ ] No copy of the rule survives anywhere else; every former home has a pointer.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.
