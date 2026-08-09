---
node_type: agent-rules
title: Agent rules — very-ai-product-loops
status: draft
version: 0.5.1
updated: 2026-08-08
---

# Agent rules — very-ai-product-loops

**This file is the one home of the rules, for any agent.** `AGENTS.md` is the cross-vendor convention
(Codex, Cursor and others auto-load it); the root `CLAUDE.md` is a one-line pointer here, not a second
copy. Whatever reads a folder and writes markdown can run this framework — see
[`install/README.md`](install/README.md) → *Running on an agent other than Claude Code*.

Read BEFORE any work, in this order (normative, not optional):

1. `process/OVERVIEW.md` — the model + the philosophy the agent lives by (§1)
2. `process/OPERATING-LOOP.md` — how one pass of a step runs
3. `process/CONVENTIONS.md` — notation: confidence tags, IDs, forks, change logs
4. `process/REGISTERS.md` — register schemas
5. The instance: its `HANDOFF.md` → `sources/INDEX.md` → only the artifacts the task needs

**Never trust auto-load.** When work begins via a skill, from another session, or on a tool that loads
nothing, this file was not read for you — read the order above yourself. The `start-work` skill (or
`product-setup` for first run) walks it; on a tool without slash-skills, read
`.claude/skills/start-work/SKILL.md` as a plain file and follow it.

Non-negotiables (details live in the files above; on conflict, those files win):

- **The agent prepares, the human decides.** Never invent; missing data = `— to clarify —`.
- **Registers are the home of values.** Metric readings land in `registers/metrics.csv` as dated
  rows at capture time; a `sources/` snapshot is evidence, not the home. A data-gathering errand
  is still a loop pass: it ends with register updates and a change-log entry.
- **A handoff restores state — not rules, not truth.** Verify its claims against the registers
  and artifacts; run its environment checks before relying on them.
- **Read the tool before filling.** Open `tool-skills/library/<tool>/SKILL.md` before writing its
  section. Missing prerequisites → ask or help obtain; never proceed on a guess. (Pluggable skills
  live under `tool-skills/`: `library/` methods · `operations/` runtime skills · `adapters/` output —
  pick by task phase; see [`tool-skills/README.md`](tool-skills/README.md).)
- **One mechanism, one way.** Never introduce a second format/path for something the framework
  already does one way.
- **Confidence tags on every claim**; agent proposals marked ⚙️. Never blanket-source your own
  derived conclusions.
- **No secrets or PII** in artifacts, handoffs, or chat. Raw captures are **never committed** and
  are deleted once their values land in the registers.
- **In chat with the human: no bare IDs or links** — decode what each one means in the same
  sentence.
- **Changing the framework itself** (a new skill, a status, the work directions, a step) follows
  [`EXTENDING.md`](EXTENDING.md) — never an ad-hoc edit of the core.
