---
node_type: extending
title: Add a register — the four-sign test
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add a register

*Read this when something feels like it needs a register of its own. The dial table is in*
[`../EXTENDING.md`](../EXTENDING.md); *the three shipped schemas are in*
[`../process/REGISTERS.md`](../process/REGISTERS.md).

Three is not a magic number, but a fourth register is a change to the **load-bearing core** — it appears
in the overview, the README, the diagram and every tool. So a candidate is **tested**, not argued.

## The four signs — all four, not three

1. **A stable id other artifacts reference.** `H-001`, `R-001`, `M-activation` are cited from prose across
   steps.
2. **An enumerable lifecycle** — a `status` column. A register is a state machine, not a filing cabinet.
3. **A life outlasting the step that bore it** — born at one step, *refined by others* (the table in
   [`../process/REGISTERS.md`](../process/REGISTERS.md)).
4. **State that flows both ways** — a result below revises a decision above (a refuted hypothesis triggers
   an upward revisit).

**Fail one sign and the home is a step artifact section**, whose change log already carries the reasoning.

Worked examples: *competitors* are a snapshot re-run when the market moves — no lifecycle, few referrers →
a section. *Value-for-the-customer* is an attribute of a segment with no identity of its own → a section
keyed to the segment.

## Two guards on the test

- **A register of "workings" fails by construction.** Registers hold **state**; artifacts hold the
  **reasoning** that produced it. A register that stored analyses would be a second home for artifact
  content — see CONVENTIONS → *One mechanism, one way*.
- **No halves.** An id plus a status inside an artifact *is* a register, hidden where nobody looks. Either
  it earns a register, or it stays prose in a section.

## Open candidate (not adopted): segments

They pass all four signs — cited by pains, value proposition, pricing, channels and retention (a read *by
segment* is a method requirement), and by guardrails; and they have a real cycle (candidate → chosen →
deprioritized → dropped). They are deliberately left as a Step 2 section until one of two triggers: **a
second instance reporting the same friction**, or **a method that must reference a segment by id and
cannot**.

Naming the candidate is how it gets decided on evidence instead of being re-argued every time it itches.

## Procedure, if all four signs hold

1. **Write the four signs out against the candidate**, one line each, with the evidence for each.
2. **Add the schema** to [`../process/REGISTERS.md`](../process/REGISTERS.md) — the id shape, the columns,
   the enums, the step that bears it and the steps that refine it.
3. **Key every column a tool reads** — the id, the statement, every enum, every descriptor. There is **no
   header-name fallback** ([`../process/reference/column-keys.md`](../process/reference/column-keys.md)).
4. **Add the enum validation** to [`../tools/lint.py`](../tools/lint.py) — check D holds register enums
   single-valued.
5. **Name its touchpoints** in every step README that reads or writes it.
6. **Teach the read layer** — [`../tools/loops/`](../tools/loops/), which both the linter and the console
   read through ([`interface.md`](interface.md)).
7. **Update the count** wherever the framework states three: the overview, the README, the diagram.
8. **Run the linter to zero**, bump the versions, record it in [`../CHANGELOG.md`](../CHANGELOG.md).

## Checklist

- [ ] All four signs written out with evidence — not three and an argument.
- [ ] It holds **state**, and the reasoning that produced it stays in an artifact.
- [ ] No half-register left behind in a section (an id plus a status).
- [ ] Every column a tool reads carries its key.
- [ ] Its enums are validated by the linter.
- [ ] Every step README that touches it names it.
- [ ] The stated number of registers agrees everywhere the framework states it.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.
