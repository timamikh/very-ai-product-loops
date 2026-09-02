---
node_type: agent-rules
title: Agent rules — very-ai-product-loops
status: draft
version: 0.9.0
updated: 2026-08-19
---

# Agent rules — very-ai-product-loops

**This file is the one home of the rules, for any agent.** `AGENTS.md` is the cross-vendor
convention; the root `CLAUDE.md` is a one-line pointer here, not a second copy. Whatever reads a
folder and writes markdown can run this framework — see
[`install/README.md`](install/README.md) → *Running on an agent other than Claude Code*.

**Read BEFORE any work, in this order (normative, not optional):**

1. `process/OVERVIEW.md` — the philosophy (§1) and the model
2. `process/OPERATING-LOOP.md` — the seven-move skeleton every pass runs
3. `process/goal-map.md` — the router: which trigger becomes which card
4. `process/CONVENTIONS.md` — notation: tags, IDs, links, markers, change logs
5. The instance: its `HANDOFF.md` (if present — absence just means no handoff is pending) →
   `sources/INDEX.md` → only the artifacts the task needs

**Read at the named moment, not every pass:** `process/REGISTERS.md` — register schemas — when
pulling register rows as inputs (loop move 2) and before writing rows (move 5);
`process/reference/` — the config schema, column keys, the node_type matrix, the glossary, worked
examples — each pointed at from the core file that needs it.

**Never trust auto-load.** When work begins via a skill, from another session, or on a tool that
loads nothing, this file was not read for you — read the order above yourself. The `start-work`
skill (or `product-setup` for first run) walks it; without slash-skills, read
`.claude/skills/start-work/SKILL.md` as a plain file and follow it.

## Non-negotiables

Details live in the files above; on conflict, those files win. Each rule: what to do — and the one
reason it exists.

- **N1 · The agent prepares, the human decides.** Never invent; missing data = `— to clarify —` —
  a guess in an artifact is a decision the human never made.
- **N2 · Registers are the home of values.** Metric readings land in `registers/metrics.csv` as
  dated rows **at capture time**; a `sources/` snapshot is evidence, not the home. A data-gathering
  errand is still a loop pass — it ends with move 5.
- **N3 · A handoff restores state — not rules, not truth.** Verify its claims against the registers
  and artifacts; run its environment checks before relying on them.
- **N4 · Read the card before acting.** Every instruction you act on is a **card** and its header is
  the pass plan — open it first; missing prerequisites → ask or help obtain, never proceed on a
  guess. (Framework cards live under `tool-skills/`: `library/` methods · `operations/` runtime ·
  `outputs/` output; a product's own live in its `skills/`.)
- **N5 · One mechanism, one way.** Never introduce a second format or path for something the
  framework already does one way — every variation point is where two readers diverge.
- **N6 · The write rule is a split.** The **orchestrator** alone owns the artifact, the registers,
  `state.yaml`, ticks and change log — it projects worklogs, mints ids, ticks gates. Spawned with a
  brief? You are a **subagent**: a `draft` writes exactly one file (its method's worklog); the rest
  return text. Never close a fork, never tick a gate, never mint an id. Transitive down the tree.
  (OPERATING-LOOP → *Delegation*.)
- **N7 · Confidence tags**: every number or fact from outside names its source (`[sourced: …]`,
  `[validated: …]`, `[refuted: …]`); **no tag = `assumption`** — never blanket-source your own derived
  conclusions. Agent proposals ⚙️.
- **N8 · No secrets or PII** in artifacts, handoffs, or chat. Raw captures are **never committed**,
  deleted once their values land in the registers.
- **N9 · In chat: no bare IDs or links** — decode what each one means in the same sentence, so the
  human never opens the repo just to follow the conversation.
- **N10 · Changing the framework itself** (a skill, a status, a step, a direction) follows
  [`EXTENDING.md`](EXTENDING.md) — never an ad-hoc edit of the core.
