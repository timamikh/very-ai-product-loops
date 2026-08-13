---
name: theses
kind: template
produces: section confirmation markers
reads_registers: []
writes_registers: []
inputs: [kb]
prerequisites:
  - the step's sections are worked (projected from their worklogs), so there is a result to sign off
  - the human is present — a confirmation is theirs to give and is never delegated or self-issued
used_by_steps: [any]
opinionated: true
method_basis: "Human sign-off as the semantic gate: the agent presents the section's thesis in plain language, the human confirms THIS version, and the confirmation is stamped on the section and dropped when the section changes"
status: draft
version: 0.1.0
updated: 2026-08-13
---

# Theses — walk the human through a step's results and record the sign-off

**What it is.** The pass at [operating-loop](../../../process/OPERATING-LOOP.md) **step 7** where the
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

## When to apply

1. **At step 7, after a step's sections are worked** — the agent has projected the sections from their
   worklogs; now the human signs off the results before the step is treated as closed.
2. **After a section is re-projected** — *Act* dropped its `confirmed` marker because the conclusion
   changed; the changed thesis is re-confirmed, never assumed still-good.
3. **On request** — the human asks to review and sign off what stands.

## Prerequisites

- **A worked section to sign.** An empty or gap section has no result to confirm — it is skipped, not
  stamped. Confirmation is about a conclusion, not a placeholder.
- **The human in the loop.** A confirmation is the human's decision. The agent **never** stamps a marker
  on its own reasoning unprompted, and a subagent never stamps one at all (only the orchestrator writes).

## How to do it

**1 · Read the step's confirmation state.** List the written sections and which already carry a
`<!-- confirmed: <date> -->` marker. The pending ones (and any whose worklog changed since the marker)
are the work of this pass.

**2 · Present each thesis, in plain language.** For each pending section, show its conclusion in chat —
the section already *is* the thesis, so lead with its headline claim, not the whole table. Reuse the
loop's **Show reasoning first**: the human reacts to the thesis as stated, decoding every id in the same
sentence (no bare `H-006` / `R-001`). Group them so the human signs a step in one sitting, but shows
**each** thesis — a single "confirm all" without seeing them is the anti-pattern below.

**3 · Take the human's verdict, per section.**

- **Confirm** → stamp `<!-- confirmed: <today> -->` right after the section's `<!-- tool: … -->` /
  `<!-- synthesis -->` marker.
- **Edit** → the human changes the conclusion. That is an *Act* re-projection (fix the worklog, re-project
  the section); only then stamp the confirmation on the new version.
- **Reject** → the section goes back to *Act*; it stays pending and the reason is recorded, not the marker.

Never self-confirm, never confirm on silence — absence of a marker is the honest state.

**4 · Record it.** A dated **change-log** entry in the artifact naming the sections confirmed (and any
sent back), then **`python3 tools/lint.py <instance>` reports 0 errors** — check Q catches a marker whose
date is malformed (which would silently read as pending) and a schema that shipped a marker at all.

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

## Output

- `<!-- confirmed: <date> -->` markers on the sections the human signed, in the artifact.
- A dated change-log entry naming what was confirmed and what was sent back.
- No new content and no register write — this pass records a decision, it does not make one.
