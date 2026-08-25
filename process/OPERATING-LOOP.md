---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass
status: draft
version: 0.16.0
updated: 2026-08-25
---

# Operating Loop

The **runtime** that ties the four planes together; everything else (steps, statuses, library,
registers, conventions) is data this loop consumes. Every unit of work is a **pass** of the skeleton
below. What varies between passes is the **card** — one entity in five kinds, whose frontmatter is
that pass's plan ([`reference/card-schema.md`](reference/card-schema.md)); the skeleton is fixed. The
[goal map](goal-map.md) turns a trigger and a goal into a card.

> The golden rule holds throughout: **the agent prepares, the human decides** — the loop never
> silently invents; it drafts (⚙️), asks, or marks `— to clarify —`.

## The skeleton — seven moves, every pass

**0 · Orient.** Read the **active status** from `config.yaml` (the human's decisions, rarely
changing) and the **position** from `state.yaml` (`current_step`, `last_pass`, gate ticks — agent-
written every pass, the single home of position, never rules or truth). Missing `state.yaml` →
reconstruct from the artifacts and confirm. A gate item's id is its **`artifact#section`** target
(an explicit `tick-id` where it spans sections); ticks are `done` · `open` · `n/a` · `deferred`.
**At session start only**, also read `HANDOFF.md` and the recorded **debts** — open items, unanswered
questions, overdue cadences. **No scanning beyond this:** a trigger is an event now, or a debt
recorded when it was found.

**1 · Name the goal.** Find the [goal map](goal-map.md) row for this **trigger and goal**, say both
aloud, and **open the card before acting** (N4) — its frontmatter *is* this pass's plan. The commonest
trigger, *the current step's gate has open items*, has a section for its goal and resolves to a step
card plus that section's method (goal map → *The commonest row*); its focus comes from the gate
checklist and the status's per-step goals, and an **empty `per_step`** never blocks (work by step
defaults, and at move 5 propose filling it). An event matching **two rows is two passes**.

**2 · Gather the inputs — and size the pass.** Check the card's **`prerequisites`** against what
exists, then take the read perimeter from its **`reads`**. Four laws hold over that list. Inputs
resolve by **data, not guess** — the card names the *types*, the *instances* come from the section's
theme (open `H-` on its theme, live `R-`, the metric nodes it touches — semantics in doubt →
[`REGISTERS.md`](REGISTERS.md)). The perimeter is a **union**, never one card's list alone: add the
target section's **rests-on** and the step README's input map. **A worklog is an input only when
the card declares it** (`worklog:<step>/<method>` in `reads`; tags carry verbatim, sign-off stays on
sections) — an *undeclared* need for another method's worklog means its projection has lagged, and
re-projecting it is the debt. And for a method the perimeter is **closed**: the primary working of
the worklog draws on this list and nothing else — an input the instance lacks is a declared gap
(`— to clarify —`), never a substitute pulled from reach; wider context enters only through the
orchestrator's two recorded doors ([`reference/card-schema.md`](reference/card-schema.md) →
*reads is a perimeter*). Announce the list. Volume is now visible: decide **here, aloud**, split across subagents or run
alone, and why (the split itself runs at move 4; the contract is *Delegation* below).

**3 · Close the gaps — with the human.** A missing prerequisite → **ask** or offer to help obtain
it; never proceed on a guess. An open **product decision** → written questions, 2–4 options each, a
⚙️ default, and **wait**. Technical gaps are not asked — they are forks in the artifact.

**4 · Act.** Do the working in the pass's **worklog** (`<step-folder>/<tool>.md`) — the **source of
truth**; the **artifact section is its projection**, holding nothing the worklog does not, every
claim tagged, proposals ⚙️. The moves available here are cards of their own, never run bare:
**projection** ([`projection`](../tool-skills/operations/projection/SKILL.md) — the only way a
section is ever written), **delegation** (a split from move 2: one **brief** per part, **every return
scored against its passport before use** — [`orchestration`](../tool-skills/operations/orchestration/SKILL.md)),
external search (`gather`/`research`). Two obligations **before anything lands on disk**: **show
reasoning first** (a section resting mainly on the agent's own reasoning or a spoken answer is
previewed in chat, in full — a section restating a source is not), and **declare the write
perimeter** — the card's **`writes`** resolved to actual paths, one message naming every file the
pass will touch.

**5 · Record.** **Unconditionally:** a dated **change-log** entry (from → to · why · trigger) and
the **open items** surfaced. Then **every surface in the card's `surfaces`**:
**tick** the satisfied gate items in `state.yaml` and set `current_step`/`last_pass` — a tick on a
section resting mainly on the agent's own reasoning waits for a `verify` subagent that did not write
it (the human may waive; a runtime without agents leaves it `open`, reason surfaced); **seed/update
the registers** with stable ids (read [`REGISTERS.md`](REGISTERS.md) first); **propose sign-off** via
[`theses`](../tool-skills/operations/theses/SKILL.md) (`scope: step`; a big re-projection → `instance`).
A gathering-only errand is still a pass — "I only collected data" does not skip this move.

**6 · Bubble.** Next item or step. If the pass **invalidated** a higher or lower artifact (a refuted
hypothesis, a changed segment), raise it per the step's cadence & invalidation rules.

What each plane contributes is in [`OVERVIEW.md`](OVERVIEW.md) §2: the **step** gives goals · gate ·
skeleton · default tool · touchpoints · input map · cadence; the **status** refines focus and tool
emphasis; the **library** gives prerequisites · method · template-fragment · questions; the
**registers** give the live rows; **conventions** give the notation.

## Session handoff

Position persists in `state.yaml`; for what it does not hold (environment/access checks, open forks),
run the [`handoff`](../tool-skills/operations/handoff/SKILL.md) skill **before** the boundary. A
handoff **restores state, not rules** — its reading order sends the next agent through `process/`
first; and a gathering errand is still a pass, ending at move 5.

## Delegation (orchestrator ↔ subagents) — the contract

The agent holding the human's session is the **orchestrator**; every agent it spawns is a
**subagent**. Delegation moves the *gathering* out of a context that must stay clear enough to think —
it costs more tokens, never fewer.

- **The write rule (N6).** A `draft` subagent writes **exactly one file — its method's worklog**;
  `gather`/`research`/`verify` write **nothing** and return text. The artifact, the registers (and id
  minting), the projection, `state.yaml`, the gate ticks and the change log are the orchestrator's
  alone. Transitive down the tree.
- **Never delegated:** a **fork with the human** · register id allocation, register writes, gate
  ticks · the **move 1–3 reasoning chain** (cut into pieces it loses the coherence it exists for).
- **Closed task kinds:** `gather` · `research` · `draft` · `verify`; anything else stays with the
  orchestrator.
- **The return gate is hard.** Every return is scored against its **passport** before use; a failing
  one goes back **once** with named defects, then stop — record `— to clarify —` and surface it.
- **A `draft` brief's inputs are the card's `reads`, resolved** — the closed perimeter, assembled
  mechanically, never the orchestrator's context dump. Sending a draft back, the orchestrator may
  **supplement** the perimeter with named inputs the quality of the result needs — the supplement is
  written into the worklog's `Supplements` field, so an audit can tell a sanctioned widening from
  a leak.
- **`delegation: off`** (or a runtime that cannot spawn agents): the orchestrator runs every pass
  itself and writes the worklogs directly; the write rule is unchanged, and a tick needing a `verify`
  stays `open`, reason surfaced (move 5).

The procedure — decomposition, brief/return templates, the passport, anti-patterns — is the
[`orchestration`](../tool-skills/operations/orchestration/SKILL.md) skill.

## Cross-cutting extras

A **late hypothesis** (one surfacing after its step) is placed **via the register, never by forking
the process** — [`reference/late-hypothesis.md`](reference/late-hypothesis.md). The loop end-to-end
on one concrete pass — [`reference/worked-example.md`](reference/worked-example.md).
