---
node_type: tool-skills-index
title: Tool-skills — the pluggable skills the agent runs
status: draft
version: 0.3.0
updated: 2026-08-09
---

# Tool-skills

The framework splits into two halves:

- **The fixed core** — `process/` (rules), `steps/` (skeleton), `statuses/` (stage config),
  `registers/` (living state). This is the board and the rules of the game; it changes rarely.
- **The pluggable skills** — everything under `tool-skills/`. These are instruction skills the
  agent *picks up and runs*: markdown that says how to do a thing, no build step. Companies swap
  or extend them without forking the core.

`tool-skills/` holds three categories, distinguished by **when in the process they run**:

| Category | What it does | When it runs | Index |
|----------|--------------|--------------|-------|
| [`library/`](library/README.md) | product methods that fill an artifact **section** (segmentation, pricing, jtbd, …) | *during* a step pass — recommended by the step & status | [`library/README.md`](library/README.md) |
| [`operations/`](operations/README.md) | runtime skills about how the agent **works** (handoff, metrics capture, delegation to subagents; future: scheduling, automation) | at session/process boundaries — triggered by events, not by a step | [`operations/README.md`](operations/README.md) |
| [`adapters/`](adapters/README.md) | render the instance into a **deliverable** (table · document · deck) | *after* the content exists — on a delivery request | [`adapters/README.md`](adapters/README.md) |

## How the agent finds the right skill (discovery rule)

One rule covers all three: **pick the category by the phase of the task, then read that
category's index.**

- The task is *"produce / update a section of an artifact"* → **`library/`**. The active step
  README and status `per_step` already name the recommended tool; the library index is the full
  catalog and fallback.
- The task is *"render this into a deliverable"* (a deck, a one-pager, a table for a stakeholder)
  → **`adapters/`**. Match the deliverable to a mode in the adapters index (`to-deck` for a
  presentation, `to-document` for a doc, `to-table` for a register/backlog).
- The task is *"carry state across a restart / go get a number the register doesn't have / split this
  pass across several agents / record what the framework got wrong"* → **`operations/`**. See also
  the OPERATING-LOOP sections "Session handoff" (the authority for the handoff mechanism and for the
  rule that a data-gathering errand is a full pass of the loop) and "Delegation" (the authority for
  who may write, and for what is never delegated).

The human may always call any skill directly or override the recommendation — discovery is a
default, not a gate.

## Where a product's OWN skills live

The vendored framework is **read-only**: updating it means re-vendoring at a newer tag, which
overwrites `tool-skills/`. So a company's or a product's own methods do **not** go here. Their one
canonical home is inside the product's working area, mirroring this layout:

```
product-loops/tool-skills/library/<name>/      # a product's own method
product-loops/tool-skills/operations/<name>/   # a product's own runtime skill
```

Three rules, and no other variant:

- **Same anatomy.** A local skill is a normal skill — `SKILL.md` (with the same frontmatter wiring) +
  `template-fragment.md` + `questions.yaml`. The linter checks it exactly like a vendored one, so a
  local method cannot quietly produce a homeless section.
- **Local wins.** If a local skill and a vendored one share a name, the local one is the method the
  agent runs. That is how a company specializes a base method without forking the framework.
- **Survives updates.** Because it sits under `product-loops/`, re-vendoring the framework never touches it.

The **agent** writes it, asked for in words — describe the method, or point at an existing skill to adapt.
The procedure is in [`EXTENDING.md`](../EXTENDING.md); the local console
([`tools/ui/`](../tools/ui/README.md)) then displays it, and never creates one itself.

## Not to be confused with `.claude/skills/`

`.claude/skills/` holds **Claude Code-native skills** (e.g. `product-setup`), invoked by the
harness as slash-skills. `tool-skills/` holds **framework skills** — markdown methods the agent
*reads and applies* as part of the workflow. Different mechanism, different home.

`.claude/agents/` is the same distinction one step further: the `loops-*` subagent definitions there
are **runtime enforcement** of a rule that is written in markdown. The write rule is a split — a
`draft` subagent writes exactly one file (its method's worklog), and `gather`/`research`/`verify`
write nothing — so three of the four definitions ship with no write tools at all, and `loops-draft`
carries `Write` and only `Write`. The rule lives in
[`process/OPERATING-LOOP.md`](../process/OPERATING-LOOP.md) → *Delegation* and the procedure in
[`operations/orchestration/`](operations/orchestration/SKILL.md); the definitions are how one
particular runtime happens to enforce it, and the framework runs without them.
