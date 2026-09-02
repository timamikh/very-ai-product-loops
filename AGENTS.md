---
node_type: agent-rules
title: Agent rules — very-ai-product-loops
status: draft
version: 0.10.0
updated: 2026-09-02
---

# Agent rules — very-ai-product-loops

**The door, not a second copy of the rules.** The reading order, and the non-negotiables as
*pointers* — each rule is written in full in exactly one place, named below. `AGENTS.md` is the
cross-vendor convention; the root `CLAUDE.md` points here. Any agent that reads and writes markdown
can run this — [`install/README.md`](install/README.md) → *Running on an agent other than Claude Code*.

**Read BEFORE any work, in this order (normative, not optional):**

1. `process/OVERVIEW.md` — the concept: planes, three homes, the loop model
2. `process/OPERATING-LOOP.md` — the procedure: the seven-move skeleton, delegation
3. `process/goal-map.md` — the router: which trigger becomes which card
4. `process/CONVENTIONS.md` — the notation: tags, IDs, links, markers, change logs
5. The instance: its `HANDOFF.md` (if present) → `sources/INDEX.md` → only the artifacts the task needs

**Read at the named moment, not every pass:** `process/REGISTERS.md` at loop moves 2 and 5;
`process/reference/` — schemas, matrices, skeletons, the glossary — where a core file points at it.

**Never trust auto-load.** Begun via a skill, from another session, or on a tool that loads nothing,
this file was not read for you — read the order above yourself. `start-work` (or `product-setup` for
first run) walks it; without slash-skills, read `.claude/skills/start-work/SKILL.md` as a plain file.

## Non-negotiables — the name, and where the rule lives

- **N1 · The agent prepares, the human decides.** Never invent; a gap is `— to clarify —`.
  → OPERATING-LOOP (the golden rule; forks at move 3) · CONVENTIONS → *Sources*.
- **N2 · Registers are the home of values.** A metric reading lands in `metrics.csv` at capture
  time; a gathering errand is still a pass. → OPERATING-LOOP move 5 · REGISTERS → *Metric register*.
- **N3 · A handoff restores state — not rules, not truth.** → OPERATING-LOOP → *Session handoff*.
- **N4 · Read the card before acting.** Its header is the pass plan. → OPERATING-LOOP moves 1 and 3 ·
  CONVENTIONS → *Cards*.
- **N5 · One mechanism, one way.** → CONVENTIONS → *One mechanism, one way*.
- **N6 · The write rule is a split.** The orchestrator writes the shared canon; a `draft` subagent
  writes only the worklog its brief names; the rest return text. → OPERATING-LOOP → *Delegation*.
- **N7 · Confidence tags; no tag = `assumption`.** → CONVENTIONS → *Confidence tags*.
- **N8 · No secrets or PII; raw captures are never committed.** The linter's secret scan holds it.
  → CONVENTIONS → *Raw data & access* · `process/reference/boundary-layout.md`.
- **N9 · In chat, no bare IDs, anchors or links** — decode each in the same sentence ("`H-009` — the
  bet that tech leads stay"); IDs stay bare only inside artifacts. (This line is the rule's home.)
- **N10 · Changing the framework itself** follows [`EXTENDING.md`](EXTENDING.md) — never an ad-hoc
  edit of the core.
