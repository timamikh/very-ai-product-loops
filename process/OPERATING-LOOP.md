---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass
status: draft
version: 0.13.0
updated: 2026-08-19
---

# Operating Loop

The **runtime** that ties the four planes together; everything else (steps, statuses, library,
registers, conventions) is data this loop consumes. Every unit of work is a **pass** of the skeleton
below. What varies between passes is the **card** — the goal's own instructions (a skill, a step
README); the skeleton is fixed. The [goal map](goal-map.md) turns a trigger into a card.

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

**1 · Name the goal.** Classify the trigger against the [goal map](goal-map.md) and say it aloud —
which pass, which card. The commonest trigger, *the current step's gate has open items*, takes its
focus from the gate checklist and the status's per-step goals; an **empty `per_step`** never blocks
(work by step defaults, and at move 5 propose filling it). Every other trigger names its card
directly. An event matching **two rows is two passes**. **Open the card before acting** (N4).

**2 · Gather the inputs — and size the pass.** Check the card's **prerequisites** against what
exists. Inputs resolve by **data, not guess**: the card names the *types* (`reads_registers`, source
slots); the *instances* come from the section's theme (open `H-` on its theme, live `R-`, the metric
nodes it touches — semantics in doubt → [`REGISTERS.md`](REGISTERS.md)) and from the target section's
**rests-on** plus the step README's input map. **A worklog is never an input** — cross-step exchange
runs only through the registers and the **signed artifact sections**; if what you need lives only in
another method's worklog, its projection has lagged, and re-projecting it is the debt. Announce the
list — the **read perimeter**. Volume is now visible: decide **here, aloud**, split across subagents
or run alone, and why (the split itself runs at move 4; the contract is *Delegation* below).

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
perimeter** (one message naming every file the pass will touch).

**5 · Record.** **Unconditionally:** a dated **change-log** entry (from → to · why · trigger) and
the **open items** surfaced. Then **for every surface the pass touched** (which ones is in the card):
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
- **`delegation: off`** (or a runtime that cannot spawn agents): the orchestrator runs every pass
  itself and writes the worklogs directly; the write rule is unchanged, and a tick needing a `verify`
  stays `open`, reason surfaced (move 5).

The procedure — decomposition, brief/return templates, the passport, anti-patterns — is the
[`orchestration`](../tool-skills/operations/orchestration/SKILL.md) skill.

## Cross-cutting extras

A **late hypothesis** (one surfacing after its step) is placed **via the register, never by forking
the process** — [`reference/late-hypothesis.md`](reference/late-hypothesis.md). The loop end-to-end
on one concrete pass — [`reference/worked-example.md`](reference/worked-example.md).
