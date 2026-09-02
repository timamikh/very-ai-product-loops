---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass
status: draft
version: 0.17.0
updated: 2026-09-02
---

# Operating Loop

The **runtime** that ties the four planes together; everything else is data this loop consumes.
Every unit of work is a **pass** of the skeleton below. What varies between passes is the **card**,
whose frontmatter is that pass's plan ([`reference/card-schema.md`](reference/card-schema.md)); the
skeleton is fixed. The [goal map](goal-map.md) turns a trigger and a goal into a card.

> The golden rule holds throughout: **the agent prepares, the human decides** — the loop never
> silently invents; it drafts (⚙️), asks, or marks `— to clarify —`.

## The skeleton — seven moves, every pass

**0 · Orient.** Read the **active status** from `config.yaml` (the human's decisions, rarely
changing) and the **position** from `state.yaml` (agent-written every pass, the single home of
position, never rules or truth — [`reference/state-schema.md`](reference/state-schema.md)). Missing
`state.yaml` → reconstruct from the artifacts and confirm. **At session start only**, also read `HANDOFF.md` and the recorded
**debts** — open items, unanswered questions, overdue cadences. **No scanning beyond this:** a
trigger is an event now, or a debt recorded when it was found.

**1 · Name the goal.** Find the [goal map](goal-map.md) row for this **trigger and goal**, say both
aloud, and **open the card before acting** (N4) — its frontmatter *is* this pass's plan. The commonest
trigger, *the current step's gate has open items*, has a section for its goal and resolves to a step
card plus that section's method (goal map → *The commonest row*); its focus comes from the gate
checklist and the status's per-step goals, and an **empty `per_step`** never blocks (work by step
defaults, and at move 5 propose filling it).

**One section per pass.** A section pass closes **one named section** through its method, then
proposes the next and lets the human steer — never a bulk fill of the artifact, which bypasses the
method, the prerequisites and the human's decisions at once. The one widening: a method whose single
worklog fills several sections projects them together, because they are one working. Passes that are
not section passes (`step-close`, `source-intake`, an output) take their unit from their own card.

**2 · Gather the inputs — and size the pass.** Check the card's **`prerequisites`** against what
exists, then take the read perimeter from its **`reads`**. Inputs
resolve by **data, not guess** — the card names the *types*, the *instances* come from the section's
theme (open `H-` on its theme, live `R-`, the metric nodes it touches — semantics in doubt →
[`REGISTERS.md`](REGISTERS.md)). The perimeter is a **union**, never one card's list alone: add the
target section's **rests-on** and the step README's input map. **A worklog is an input only when
the card declares it** (`worklog:<step>/<method>` in `reads`; tags carry verbatim) — an *undeclared*
need for another method's worklog means its projection has lagged, and re-projecting it is the debt.
And for a method the perimeter is **closed** — a missing input is a declared gap, never a substitute
from reach ([`reference/card-schema.md`](reference/card-schema.md) → *reads is a perimeter*).
Announce the list. Volume is now visible: decide **here, aloud**, split across
subagents or run alone, and why (the split runs at move 4; the contract is *Delegation* below).

**3 · Close the gaps — with the human.** A missing prerequisite → **ask** or offer to help obtain
it; never proceed on a guess. **Triage** decisions: the reversible and cheap the agent decides itself,
marks ⚙️ and logs; a decision that is consequential *and* not closable from evidence is a **fork** →
written questions, **2–4 concrete options with trade-offs**, a ⚙️ default, and **wait** — never one
option with the alternatives hidden. Technical gaps are not asked — they are forks noted in the
artifact. An open fork is an unresolved risk: close it, or escalate it with an owner.

**4 · Act.** Do the working in the pass's **worklog** (`<step-folder>/<tool>.md`) — the **source of
truth**; the **artifact section is its projection**, holding nothing the worklog does not, every
claim tagged, proposals ⚙️. These moves are cards of their own, never run bare:
**projection** ([`projection`](../tool-skills/operations/projection/SKILL.md) — the only way a
section is ever written), **delegation** (a split from move 2: one **brief** per part, **every return
scored against its passport before use** — [`orchestration`](../tool-skills/operations/orchestration/SKILL.md)),
external search (`gather`/`research`). Two obligations **before anything lands on disk**: **show
reasoning first** (a section resting mainly on the agent's reasoning or a spoken answer is
previewed in chat, in full), and **declare the write perimeter** — the card's **`writes`** resolved
to paths, one message naming every file touched.

**5 · Record.** **Unconditionally:** a dated **change-log** entry (from → to · why · trigger) and
the **open items** surfaced. Then **every surface in the card's `surfaces`**:
**tick** the satisfied gate items in `state.yaml` and set `current_step`/`last_pass` — **the tick is
conditional**: on a section resting mainly on the agent's own reasoning it waits for a `verify`
subagent that did not write it (the human may waive); **seed/update the registers** with stable ids ([`REGISTERS.md`](REGISTERS.md)) — a captured
metric value lands in `metrics.csv` as a dated row **at capture time**, a `sources/` snapshot is
evidence, not the home; **propose sign-off** via
[`theses`](../tool-skills/operations/theses/SKILL.md) (`scope: step`; a big re-projection → `instance`).
A written section left `open` is a **recorded reopen for re-sign**, else unfinished (G2).
A gathering-only errand is a pass too, and ends here.

**6 · Bubble.** Next item or step. If the pass **invalidated** another artifact (a refuted hypothesis, a
changed segment), raise it per the step's cadence and invalidation rules.

## Session handoff

Position persists in `state.yaml`; for what it does not hold (environment/access checks, open forks),
run the [`handoff`](../tool-skills/operations/handoff/SKILL.md) skill **before** the boundary. A
handoff **restores state — not rules, not truth**: its reading order sends the next agent through
`process/` first; its claims are verified against the registers and artifacts, and its environment
checks are run before anything relies on them.

## Delegation (orchestrator ↔ subagents) — the contract

The agent holding the human's session is the **orchestrator**; every agent it spawns is a
**subagent**. Delegation keeps the orchestrator's context clear enough to think — it costs more
tokens, never fewer.

- **The write rule (N6) — who writes what.** The **orchestrator** writes the artifact sections (the
  projection), the registers and their ids, `state.yaml` and the gate ticks, the sign-off markers,
  and the change-log entries of the artifact and the registers. A **`draft`** subagent writes
  **exactly one file: the worklog its brief names** — including that worklog's own change-log entry —
  and returns its path with a summary. **`gather` · `research` · `verify` write nothing** and return
  text. No subagent closes a fork, ticks a gate or mints an id. Transitive down the tree: what a
  subagent spawns is bound the same way. This paragraph is the rule's one home; the brief template
  §2 and the `.claude/agents/loops-*.md` definitions carry it to subagents.
- **Never delegated:** a **fork with the human** · the **move 1–3 reasoning chain** (cut into
  pieces it loses its coherence) · the whole-step read (`step-close`) and the projection.
- **Closed task kinds:** `gather` · `research` · `draft` · `verify`; anything else is the orchestrator's.
- **The return gate is hard.** Every return is scored against its **passport** before use; a failing
  one goes back **once** with named defects, then `— to clarify —` and surface it.
- **A `draft` brief's inputs are the card's `reads`, resolved** — the closed perimeter, never the
  orchestrator's context dump; a rework may **supplement** it with named inputs, recorded in the
  worklog's `Supplements` field ([`reference/card-schema.md`](reference/card-schema.md) → *reads is
  a perimeter*).
- **`delegation: off`** (or a runtime without typed subagents — anything but Claude Code): the
  orchestrator runs every brief itself, in the same session, and writes the worklogs directly; the
  write rule is unchanged, and a tick needing a `verify` stays `open`, reason surfaced (move 5).

The procedure — decomposition, brief/return templates, the passport — is the
[`orchestration`](../tool-skills/operations/orchestration/SKILL.md) skill.

## Cross-cutting extras

A **late hypothesis** is placed via the register, never by forking the process —
[`reference/late-hypothesis.md`](reference/late-hypothesis.md). One pass shown end-to-end —
[`reference/worked-example.md`](reference/worked-example.md).
