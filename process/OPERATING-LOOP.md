---
node_type: operating-loop
title: Operating Loop — how the agent runs one pass of a step
status: draft
version: 0.4.0
updated: 2026-07-17
---

# Operating Loop

This is the **runtime** that ties the four planes together. Everything else (steps, statuses,
library, registers, conventions) is data this loop consumes. One pass produces or updates one
part of one step's artifact. The agent repeats the loop, item by item, step by step.

> The golden rule holds throughout: **the agent prepares, the human decides.** The loop never
> silently invents — it drafts (⚙️), asks, or marks `— to clarify —`.

## The loop, step by step

**0 · Orient.**
Determine the **active status** (instance config, e.g. `2-pmf`) and the **current step**
(where the product is in the loops, e.g. `3-strategy`). Both are read, not guessed; if unclear,
ask.

**1 · Focus.**
Read the step's **gate checklist** and the **goals the active status sets for this step**
(status › per_step › goals). Propose to the human which checklist item / artifact section to
create or update next. The human can redirect.

> **Empty `per_step` for this step?** (goals/tools still `— to define —`.) Do **not** block:
> work by the **step defaults**, and at *Update state* (step 7) the agent **must propose filling
> that status's `per_step`** from what this pass just learned — so statuses get completed as a
> by-product of the first run through each stage, never left as standing stubs.

**2 · Recommend tools.**
Offer the tools tied to that item, **filtered by step and status**:
- the **step** gives the default tool for the section (step › skeleton);
- the **status** refines it for the stage (status › per_step › tools) — e.g. at
  `concept-viability` step 1 pains come from *interviews + analytics search*, at `growth` from
  *internal product metrics*.
- **Rule:** prefer the status's per-step tools when present; otherwise the step default. The
  human may pick any tool.

**3 · Check the tool's prerequisites.**
Every tool declares a **prerequisites checklist** — the info / artifacts / access it needs.
The agent checks what is already available from the source slots (git · metrics · kb ·
prior artifacts) against that checklist.

**4 · Fill gaps.**
For each missing prerequisite, the agent either **asks the human to provide it**, or **offers
to help develop or obtain it** (draft the analysis, prepare an interview guide, write the
access request). It does not proceed on a guessed input.

**5 · Clarify (in writing).**
Once inputs are in, if any **product decisions** are still open, the agent asks concise written
questions — each with 2–4 options and a ⚙️ recommended default — and **waits**. Technical /
implementation gaps are not asked; they are noted as forks in the artifact.

**6 · Act.**
With no blank spots, the agent follows the tool's `SKILL.md` instructions and fills its
`template-fragment.md` into the artifact section — tagging every claim with a source and
confidence per `CONVENTIONS.md`, marking its own proposals ⚙️.

**7 · Update state.**
The agent then:
- ticks the step's **gate checklist** items now satisfied (and links them to the section they validate);
- **seeds / updates the registers** (hypotheses, risks, metric nodes) with stable IDs;
- adds a dated **change-log** entry (from → to · why · trigger);
- surfaces what remains open (`— to clarify —`).

**8 · Loop or bubble.**
Move to the next checklist item / section, or the next step. If this pass **invalidated** a
higher or lower artifact (e.g. a refuted hypothesis, a changed segment), raise that as a
trigger per the step's cadence & invalidation rules — the loops feed each other both ways.

## What each plane contributes to a pass

| Plane | What the loop reads from it |
|-------|----------------------------|
| **Step** | goals · gate checklist (tied to artifact sections) · artifact skeleton · default tool per section · register touchpoints · cadence/invalidation |
| **Status** | per-step goals (focus) · per-step tool emphasis (which method fits this stage) · gate emphasis |
| **Library tool** | prerequisites checklist · method (how) · template-fragment · questions |
| **Registers** | current hypotheses / risks / metric nodes to read and update |
| **Conventions** | confidence tags · sources · section IDs · links · change-log format |

## Session handoff (state transfer between sessions/agents)

The loop assumes one continuous context; reality restarts. Whenever a session boundary
approaches, run the **`handoff` tool** (`library/handoff/`) to write/update the instance's
`HANDOFF.md` — *before* the boundary, not after:

- **Environment change needs a restart** (MCP config, extensions, tokens) → write the handoff,
  tell the human what to do, restart, then verify the handoff's "Environment & access" checks.
- **End of session / task transfer / imminent context compaction** → same.

Two hard rules, learned from failures:
1. A handoff restores **state, not rules** — its reading order must send the next agent through
   `process/` first. An agent resuming from a handoff alone will violate the loop (typically
   step 7: registers not updated).
2. A source-gathering errand (pulling metrics, fetching docs) is still a **pass of this loop**:
   it ends with step 7 — register updates (dated metric readings → metric register), a change-log
   entry, and open items surfaced. "I only collected data" does not skip Update state.

## Handling a late, cross-cutting hypothesis

Sometimes a hypothesis surfaces *after* the step where it belongs — e.g. at Step 3 someone
realizes a new use-case that reframes the **concept** (Step 1). Do **not** fork the whole process
per hypothesis; the register is the single home. Escalate along a ladder, cheapest first:

| Level | Action | Use when |
|-------|--------|----------|
| **A · Register-first** | Log it in the hypothesis register with its type; tag it a **concept-variant** and an **invalidation trigger** on the step it touches; validate cheaply (a few interviews / a metric read) **before** editing the core artifact. | Default. It's a new segment / job / scenario — not a new product. |
| **B · Scoped spike** | Run the hypothesis as an **alternative lens through the affected steps only** (e.g. 1→3), in a separate `variants/<name>/` doc, then **compare to the main line** against a stated decision criterion and merge if it wins. Do **not** touch steps below the affected range. | Level-A signal is positive and the strategic implications need to be seen before committing. |
| **C · Full parallel run** | Treat it as a separate product/line and run all six steps. | Only when it is genuinely a different product, not a variant. |

Record the level chosen and the decision criterion in the change log. A spike (B) that loses is
kept, not deleted — it becomes a `[refuted: …]` note and a guard against re-litigating it.

## A worked micro-example

Active status `2-pmf`, step `1-idea`, section `problems`:
1. Focus → "update `problems` for the lead segment" (a gate item).
2. Recommend → status `pmf` says pains come from *product metrics + a few interviews*
   (vs pure interviews at `concept-viability`); tool `segment-pains`.
3. Prerequisites → `segment-pains` needs: the segment list, access to usage metrics, ≥3
   recent user conversations.
4. Gaps → metrics access is missing → agent offers to pull it via the metrics slot or asks
   for an export.
5. Clarify → "Which pain do we treat as primary for pricing — A or B? ⚙️ A." → waits.
6. Act → fills `problems` with severity × frequency, each `[sourced: metrics …]` / `[assumption]`.
7. Update → ticks the `problems` gate item, seeds `H-007` ("pain A blocks payment"), logs the change.
8. Loop → next section `solution`.
