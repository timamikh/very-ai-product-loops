---
node_type: tool-skills-index
title: Tool-skills — the pluggable skills the agent runs
status: draft
version: 0.1.0
updated: 2026-07-19
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
| [`operations/`](operations/README.md) | runtime skills about how the agent **works** (handoff, and future: scheduling, automation) | at session/process boundaries — triggered by events, not by a step | [`operations/README.md`](operations/README.md) |
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
- The task is *"carry state across a restart / set up how the agent runs"* → **`operations/`**.
  See also the OPERATING-LOOP "Session handoff" section, which is the authority for the handoff
  mechanism.

The human may always call any skill directly or override the recommendation — discovery is a
default, not a gate.

## Not to be confused with `.claude/skills/`

`.claude/skills/` holds **Claude Code-native skills** (e.g. `product-setup`), invoked by the
harness as slash-skills. `tool-skills/` holds **framework skills** — markdown methods the agent
*reads and applies* as part of the workflow. Different mechanism, different home.
