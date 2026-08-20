---
node_type: extending
title: Add an operation — a card whose perimeter is a pass, not a section
status: draft
version: 0.1.0
updated: 2026-08-20
---

# Add an operation

*Read this when something must happen between passes — at a session boundary, on a schedule, when data
arrives — rather than inside one section of an artifact. The dial table is in*
[`../EXTENDING.md`](../EXTENDING.md); *the anatomy is in*
[`../tool-skills/operations/README.md`](../tool-skills/operations/README.md) → *Anatomy*.

An **operation** is about how the agent *runs the process*, never about what the product decides. Its
perimeter is a **pass**; it is tied to no step and often to no section.

## Is this the right dial

| What you actually want | The dial |
|---|---|
| a way of working whose result is content in a section | [`method.md`](method.md) |
| a repeatable pull or push across the instance boundary, on a cadence | [`../process/reference/boundary-layout.md`](../process/reference/boundary-layout.md) — an **exchange** card. The goal map already routes to it, and it carries `cadence` and `last_run` |
| a file that leaves the framework | [`output.md`](output.md) |
| a habit you want the agent to hold, with no state of its own | [`rules.md`](rules.md) — probably a check or a line in a card, not a new card |
| what a delegated subagent is allowed to do | [`../tool-skills/operations/orchestration/SKILL.md`](../tool-skills/operations/orchestration/SKILL.md) → *On the runtime* |

**The test, in one question:** name its **trigger** and its **goal** in one line each. An operation that
cannot state both is not an operation — it is a step inside some other pass, and it belongs in that
pass's card.

## What makes its wiring different

A method is bound to a step and reached through its section's marker. An operation is the opposite:

- it carries **`surfaces`** and **no `steps`** — the law of ranks
  ([`../process/goal-map.md`](../process/goal-map.md) → *The law of ranks*);
- its **door is the goal map** — an `operation` is reached *only* through a router row, never by an
  agent noticing it in a folder;
- it reads and writes the instance's **operational state** (`state.yaml`, `HANDOFF.md`, `sources/INDEX.md`,
  a register) rather than a step section;
- where it has normative behavior, **the rule stays in the core** and the card carries the form. The
  card points at `process/` for the rule, so there is one source of truth.

## Procedure

1. **Write the trigger and the goal**, one line each, before anything else. One trigger, one goal, one
   row — an event that matches two rows is two passes.
2. **Create the folder** — `tool-skills/operations/<name>/` for a framework operation,
   `product-loops/tool-skills/operations/<name>/` for a product's own (but read the open question below
   first).
3. **Write `SKILL.md`** — what · when · how · anti-patterns — plus the frontmatter wiring
   ([`../process/reference/card-schema.md`](../process/reference/card-schema.md)): `reads`, `writes`,
   `surfaces`, `prerequisites`, and **no** `steps`.
4. **Add `template-fragment.md` / `questions.yaml`** only if it needs them. Most operations need
   neither; `handoff` and `orchestration` do.
5. **Add the router row** — [`../process/goal-map.md`](../process/goal-map.md) → *Passes*: the trigger,
   the goal, the card, and the move-5 surfaces it must touch. Without this row the card is unreachable
   by canon.
6. **Add the index rows** — [`../tool-skills/operations/README.md`](../tool-skills/operations/README.md)
   → *Skills* (with the authority for its mechanism) and the at-a-glance row in
   [`../tool-skills/README.md`](../tool-skills/README.md).
7. **Run the linter to zero**, then bump the `version` of every framework file you touched and record
   the change in [`../CHANGELOG.md`](../CHANGELOG.md).

## Checklist

- [ ] Trigger and goal, one line each — and no other row in the goal map already carries that trigger.
- [ ] `surfaces` names what move 5 must touch, and nothing it merely might.
- [ ] No `steps` field, and no section it fills by itself — if it writes a section, it does so through
      `projection` like any other pass.
- [ ] Every normative sentence in the card is either the form of the pass, or a pointer to the rule in
      `process/`.
- [ ] `python3 tools/lint.py <instance>` — 0 errors, and the `instances checked:` line names your
      instance.
- [ ] Framework files version-bumped, `CHANGELOG.md` entry written.

## Open question — a product's own operation has no door

The law of ranks says an operation is reached **only** through the goal map. The goal map is a vendored
framework file, overwritten on the next update — so a product cannot add a row to it, and a product's
own operation under `product-loops/tool-skills/operations/<name>/` is, by canon, unreachable.

Two things already work and are not affected: an **exchange** card (a pull or a push) has a generic row
of its own, and a product's own **method** needs no row at all — it is reached through its section's
marker.

Anything else a product wants as an operation is today reached only by the human naming it. **This is a
known gap, not a procedure** — do not invent a second router to close it. If you hit it, that is the
evidence the gap needs; record it and raise it upstream.
