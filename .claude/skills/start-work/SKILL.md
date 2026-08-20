---
name: start-work
description: >
  Begin or resume product work on a very-ai-product-loops instance (not onboarding — use
  product-setup for first run). Self-bootstraps the rules (does NOT trust AGENTS.md auto-load, which
  doesn't fire when invoked as a skill or from another session), orients on the instance state, then
  runs the operating loop ONE pass at a time — one section produced through its method, never a bulk
  fill. Use at the start of any working session, on resume after a restart/compaction, or when
  picking up an instance someone else set up.
status: draft
version: 0.5.0
updated: 2026-08-20
---

# Start work (begin / resume a session)

The reliable entry point into the working loop. Onboarding (`product-setup`) sets a product up once;
**this skill runs every working session after that.** Its whole job is to make sure the rules are
loaded and the agent works the disciplined loop instead of bulk-filling.

> Golden rule holds: **the agent prepares, the human decides.** One section per pass, drafts are ⚙️,
> real product forks are 2–4 options + a recommendation and then you **wait**; gaps stay `— to clarify —`.

## Step 0 — bootstrap the rules (before anything)

**Do not trust auto-load.** When this skill is invoked (or the repo wasn't opened as a fresh
session, or on a tool that auto-loads nothing), the framework's root `AGENTS.md` was not read for you. So load the rules
yourself, in order, before touching any artifact: `AGENTS.md` (the non-negotiables and the reading
order) → `process/OVERVIEW.md` → `OPERATING-LOOP.md` → `goal-map.md` → `CONVENTIONS.md`
(`REGISTERS.md` is read at its named moments — loop moves 2 and 5). These are the authority for
everything below — this skill only walks you into them, it does not restate them.

**Check delegation availability, now.** The loop delegates gathering, drafting and verification to
subagents (`loops-gather` · `loops-research` · `loops-draft` · `loops-verify`). Confirm two things
before the first pass and tell the human if either fails:
1. the `loops-*` agent types are visible to this session — definitions vendored mid-session are
   picked up only on the **next** session start; if absent, ask the human to restart;
2. spawning agents is permitted — the host repo's root `AGENTS.md` carries the owner's standing
   approval (written at install); if this session is still restricted, say so: every pass then runs
   solo and gate ticks that need a `verify` stay `open`. Never work around it silently.

## Step 1 — Orient (read state, never guess)

Read the instance's current state (state, not rules — verify it against the registers/artifacts):

1. **The linter, first** — `python3 tools/lint.py <instance>`, and show the human the verdict line
   plus every error. This report is the debt a previous session may have left **silently** (a weaker
   agent, an interrupted pass, an update that changed a shape) — session start is the one moment a
   human is guaranteed to see it. Check the `instances checked:` line names the instance: after
   setup, a run that found nothing to check is a failure wearing a success message. **Fix nothing
   yet** — a finding becomes a trigger, worked as an ordinary pass, at the human's order.
   **`instances checked: none` and no instance folder exists → this is a first run, not a resume:
   stop here and run `product-setup` instead** — there is no state to orient on, and improvising a
   setup from this skill is exactly the bulk-fill it exists to prevent.
2. **`HANDOFF.md`** (if present) — where the last session left off. It restores *state, not rules or
   truth*; treat anything older than its last change-log entry as suspect, and run its
   "Environment & access" checks before relying on them.
3. **`config.yaml`** — `active_status`, `language`, `directions`, source slots.
4. **`sources/INDEX.md`** — the knowledge map; open only the sources a task needs, not the whole folder.
5. **Recorded debts** — open items in the artifacts, unanswered `questions.yaml`, and any **overdue
   exchange cadence**: compare each `<instance>/skills/*/SKILL.md` `cadence:` against its `last_run` in
   `state.yaml`. This session-start scan is the framework's only sweep — an overdue pull/push surfaces
   here as a trigger, never by the framework polling in the background.
6. Determine the **active status** and the **current step**. Both are read, not guessed; if unclear, ask.

Then read only what this task needs: the current step's `README.md` (its gate checklist + skeleton)
and the active status's `per_step[N]` (goals + tool emphasis). Do not pre-load the whole framework.

## Step 2 — Run ONE pass of the operating loop

`OPERATING-LOOP.md` is the authority — the seven-move skeleton is written **there**, not here. What
this skill holds you to is the shape of a pass:

1. **The router names the card.** Find the `goal-map.md` row for this **trigger and goal** and say
   both aloud; the common case is the current step's gate — its goal is one named section (the human
   may redirect). A trigger matching two rows is two passes.
2. **The card's header is the pass plan** — open the card **before acting** (N4): `prerequisites`
   are move 3's gaps, `reads` is move 2's read perimeter, `writes` is move 4's write perimeter,
   `surfaces` is what move 5 owes. For the commonest row the plan is a **pair** — the step card plus
   the section's method (from its `<!-- tool: -->` marker; the status `per_step` sets emphasis, the
   marker names the method) — and move 2's perimeter is their **union**. Filling from `template.md`
   without opening the method's card is the failure this skill exists to prevent.
3. **Run the seven moves as written** — gaps with the human (product forks as 2–4 options + a ⚙️
   recommendation, then **wait**), act within the declared perimeter, tag every claim, and end at
   move 5 unconditionally: change-log entry, open items, every surface the header names.

**Hard rule: one section per pass.** Propose the next section and let the human steer — do **not**
barrel through the artifact set in one go. A bulk fill bypasses the method, the prerequisites, and
the human's decisions all at once (see anti-patterns).

**Delegation is the loop's default posture, not an exception:** subagents gather, research, draft
and verify; **only you write** — they never edit a file, close a fork or tick a gate, and a return
that fails its passport is not integrated. The contract is canon (`process/OPERATING-LOOP.md` →
*Delegation*); the procedure is `tool-skills/operations/orchestration/`. The one case not to
delegate: the pass fits comfortably in one context — delegation costs more tokens, not fewer.

## Step 3 — At a session boundary

Before context compaction, a restart, an environment change, or end of session, run the **`handoff`**
operations skill (`tool-skills/operations/handoff/`) to write/update `HANDOFF.md` *before* the
boundary — so the next `start-work` can resume cleanly.

## Anti-patterns

- **Trusting auto-load.** Starting work without Step 0 because "AGENTS.md is in the repo" — it isn't
  in context unless it auto-loaded, which a skill invocation / cross-session start does not do.
- **Bulk-filling.** Producing several sections (or a whole "first cycle") in one pass. One section,
  one method, one pass — then propose the next.
- **Template without method.** Filling `template.md` sections without opening each one's `SKILL.md`.
- **Working from the handoff alone.** It restores state, not rules — Step 0 still runs first.
- **Letting a subagent write.** Even "just the register row". Two agents allocating `H-0xx` at once
  is a corrupted register, and the fix costs more than the delegation saved.
- **Asking technical gaps as forks.** Only product decisions become 2–4 options; implementation gaps
  are noted as forks in the artifact, not put to the human.
