---
node_type: card
kind: operation
name: theses
prerequisites:
  - the step's sections are worked (projected from their worklogs), so there is a result to sign off
  - the human is present — a confirmation is theirs to give and is never delegated or self-issued
reads: [source:kb]
writes: [file:section confirmation markers]
surfaces: [sign-off]
opinionated: true
method_basis: "Human sign-off as the semantic gate: the agent presents the section's thesis in plain language, the human confirms THIS version, and the confirmation is stamped on the section and dropped when the section changes. Runs at scope step (one step) or instance (every step, plus cross-step rests-on provenance)"
status: draft
version: 0.3.0
updated: 2026-08-14
---
# Theses — walk the human through a step's results and record the sign-off

**What it is.** The pass at [operating-loop](../../../process/OPERATING-LOOP.md) **move 5** where the
human **confirms the step's results**. Each artifact section is a **thesis** — the step's conclusion in
the reader's language, projected from its worklog. This skill presents each written section's thesis in
chat, the human confirms it (or edits, or sends it back), and a confirmation marker
`<!-- confirmed: <date> -->` is stamped on the section. That marker is what the console reads to show a
section as *confirmed* rather than *to confirm*, and what a reader trusts as "a human signed off this
version" (CONVENTIONS → *Section confirmation*).

**Why it is an operations skill, not a library method.** It fills no section and belongs to no step —
it acts on the *state* of every section: whether a human has signed it. It is triggered by an event
(a step's sections just got worked; a section was re-projected and lost its marker) and it writes only
confirmation markers, never content.

**The one thing it exists to prevent.** A step that looks done because its structure is complete, that
no human actually read. The linter holds a section's *structure*; only a person holds its *meaning*.
Without a recorded sign-off, "the tables are full" silently passes for "the conclusion is right", and
the framework's golden rule — the agent prepares, the human decides — quietly lapses at the last step.

## Scope — one step, or the whole instance

The same pass runs at one of two scopes; the mechanics of a sign-off are identical, only the set of
sections walked differs.

- **`scope: step` (default).** Sign off the sections of the *current* step — the step-7 pass that
  closes a step. This is the common case and the one referenced by the operating loop.
- **`scope: instance`.** Walk **every** step's sections in one sitting — a standing review of what the
  whole instance has signed. It does everything the step pass does, and additionally reads the
  **rests-on provenance across steps**: a section confirmed while a section it rests on is **not** shows
  as *foundation unconfirmed* (CONVENTIONS → *Rests-on*). This pass is where that cross-step debt is
  cleared — re-confirm the foundation, or send the dependent thesis back. A per-step pass cannot see it,
  because the unsigned foundation lives in a different step.

## When to apply

1. **At move 5, after a step's sections are worked** (`scope: step`) — the agent has projected the
   sections from their worklogs; now the human signs off the results before the step is treated as closed.
2. **After a section is re-projected** (`scope: step`) — *Act* dropped its `confirmed` marker because the
   conclusion changed; the changed thesis is re-confirmed, never assumed still-good.
3. **After a *big* re-projection** (`scope: instance`) — *Act* re-worked many sections across steps and
   dropped their markers; a step-by-step pass would miss the cross-step staleness a foundation change
   spreads downward.
4. **Before a step change** (`scope: instance`) — moving to the next step should not build on unsigned
   ground; confirm the foundation the next step will rest on first.
5. **On request** (either scope) — the human asks to review and sign off what stands, for one step or
   the whole instance.

## Prerequisites

- **A worked section to sign.** An empty or gap section has no result to confirm — it is skipped, not
  stamped. Confirmation is about a conclusion, not a placeholder.
- **The human in the loop.** A confirmation is the human's decision. The agent **never** stamps a marker
  on its own reasoning unprompted, and a subagent never stamps one at all — the marker lives on the
  artifact, and the artifact is the orchestrator's to write, never a subagent's.

## How to do it

**1 · Read the confirmation state.** List the written sections and which already carry a
`<!-- confirmed: <date> -->` marker — for one step (`scope: step`) or across every step
(`scope: instance`). The pending ones (and any whose worklog changed since the marker) are the work of
this pass. In instance scope, also flag every section that is **confirmed but rests on an unconfirmed
foundation** (the console's *foundation unconfirmed*, linter check S) — those are the cross-step debt
this pass exists to clear.

**2 · Present each thesis, in plain language.** For each pending section, show its conclusion in chat —
the section already *is* the thesis, so lead with its headline claim, not the whole table. Reuse the
loop's **Show reasoning first**: the human reacts to the thesis as stated, decoding every id in the same
sentence (no bare `H-006` / `R-001`). Group them so the human signs a step in one sitting, but shows
**each** thesis — a single "confirm all" without seeing them is the anti-pattern below.

**3 · Take the human's verdict, per section.**

- **Confirm** → stamp `<!-- confirmed: <today> -->` right after the section's `<!-- tool: … -->` /
  `<!-- synthesis -->` marker. Add ` by:<who>` when the product records an operator identity — read it,
  never invent it; if none is recorded, ask once and reuse it, or omit it.
- **Edit** → the human changes the conclusion. That is an *Act* re-projection (fix the worklog, re-project
  the section); only then stamp the confirmation on the new version.
- **Send back** → the human reviewed it and wants it reworked. Stamp `<!-- contested: <today> -->` (in
  place of a confirmation) and record the reason in the change log. This is distinct from *pending*: it
  says a person looked and pushed back, not that nobody has read it yet. When *Act* re-projects the
  fixed section, it drops the `contested` marker just as it would a `confirmed` one, and the section
  comes back through this pass.

Never self-confirm, never confirm on silence — absence of a marker is the honest state. `confirmed` and
`contested` are mutually exclusive: a section carries at most one (the linter's check R holds it).

**4 · Record it.** A dated **change-log** entry in the artifact naming the sections confirmed and any
sent back (with the reason for the send-back), then **`python3 tools/lint.py <instance>` reports 0
errors** — check Q catches a malformed date (which would silently read as pending) and a schema that
shipped a marker at all; check R catches a section left both confirmed and contested.

Then tell the human what now stands confirmed and what is still pending, in the same plain language.

## Anti-patterns

- **The agent self-confirming.** Stamping a marker on its own reasoning without the human. The marker
  means *a human signed this*; an agent writing it is a forged signature.
- **Confirm-all-unseen.** One keystroke confirming a whole step without each thesis shown. The point is
  the reading, not the stamp.
- **The stale marker.** Editing a section's conclusion and leaving the old `confirmed` date — a sign-off
  outliving the thesis it approved. A changed section is re-confirmed or left pending.
- **Confirming a placeholder.** Stamping a section that is empty or all `— to clarify —`. There is no
  result to sign.
- **Confirmation in a second place.** Recording the sign-off anywhere but the section marker — a note in
  the worklog, a field in `state.yaml`. The date on the section is its one home; the console reads only
  that.
- **A step change on unsigned ground.** Advancing to the next step while a section it will rest on is
  still pending or contested. That is the *foundation unconfirmed* flag an `scope: instance` pass exists
  to catch — confirm the foundation, or move forward knowing the debt, but never by not looking.

## Output

- `<!-- confirmed: <date> -->` (optionally ` by:<who>`) markers on the sections the human signed, and
  `<!-- contested: <date> -->` on the ones sent back for rework — in the artifact.
- A dated change-log entry naming what was confirmed and what was sent back (with the reason).
- No new content and no register write — this pass records a decision, it does not make one.
