---
name: projection
kind: template
produces: (none of its own — it writes existing artifact sections, each in its method's template-fragment shape)
reads_registers: []
writes_registers: []
inputs: [kb]
prerequisites:
  - the section's worklog exists and holds the working — a projection with no worklog behind it is the source of truth gone missing (linter check P)
  - the projecting agent is the orchestrator — a subagent never writes the artifact (OPERATING-LOOP → Delegation, the write rule)
used_by_steps: [any]
opinionated: true
method_basis: "Single-source publishing: the worklog is the source of truth, the artifact section is its projection — the conclusion re-shaped into the method's fixed fragment schema, every claim carrying its original tag, the section's own headline marked for display, and any human sign-off dropped because the thesis it signed no longer exists"
status: draft
version: 0.1.0
updated: 2026-08-18
---

# Projection — write an artifact section from its worklog

**What it is.** The writing move at [operating-loop](../../../process/OPERATING-LOOP.md) **step 6**
that turns a **worklog** (the method's working — inputs, reasoning, numbers, open items) into its
**artifact section** (the chistovik the human signs). The *invariants* are canon: the worklog is the
source of truth and the section is its projection (CONVENTIONS → *Step folders & worklogs*), the
projection is writing only the orchestrator owns (OPERATING-LOOP → *Delegation*). This file is the
*how* — the procedure an agent follows every time a section is written or re-written.

**Why it is an operations skill, not a library method.** Every library method ends in a projection,
and none of them owns it: the method's `SKILL.md` says how to do the working, its
`template-fragment.md` fixes the target shape, and the move between them — worklog in, section out —
is the same regardless of method. It is triggered by an event (a worklog just got worked; a worklog
changed under an existing section), not by a step.

**The one thing it exists to prevent.** A section that says something its worklog does not — a claim
with no working behind it, a tag upgraded in transit, a headline the console invented, a sign-off
outliving the thesis it approved. The projection is where all four slip in, because it is the one
move where text is re-written rather than carried.

## When to apply

1. **A worklog just got worked** (own pass, or an accepted `draft` return — see `orchestration`
   step 7 for what delegation adds) — project it into its section.
2. **A worklog changed under an existing section** — re-project; the section never lags its source
   of truth.
3. **The human edits a conclusion in chat** — fix the worklog first, then re-project. The artifact
   is never patched directly over a stale worklog.

## Prerequisites

- **The worklog, whole.** Projection reads the worklog, not the agent's memory of the pass — what
  was just reasoned in chat lands in the worklog first. A section resolved to no worklog is not
  projected; the gap is the finding (check P).
- **The target shape.** The method's `template-fragment.md` (for a `<!-- synthesis -->` section: the
  step template's own schema) — the section's headings, tables and column keys are the fragment's,
  not improvised.

## How to do it

**1 · Read the worklog against the section's schema.** What is the conclusion, and which parts of
the working support it? The section gets the conclusion **in the fragment's shape — never the
working**: derivations, discarded branches and raw pulls stay in the worklog, reachable by the
one-id thread (`<!-- tool: <tool> -->` names both).

**2 · Write the section — nothing the worklog does not hold.** Every claim crossing over keeps
**its own tag verbatim**: an `[assumption]` stays an assumption, a `[sourced: …]` names the same
source, the agent's own proposals stay ⚙️-prefixed. A gap is `— to clarify —`, never a plausible
fill; an open fork is written as options, never closed in transit. Keep the skeleton's `{#id}` and
`<!-- tool: -->` / `<!-- synthesis -->` markers exactly — the id is how every reader and tool finds
the section and its worklog.

**3 · Mark the section's headline.** Choose the one line a collapsed board card should show and mark
it `<!-- card -->` (syntax — CONVENTIONS → *Card line*: trailing a line points at that line; alone on
a line points at the paragraph below). Choosing the headline is projection judgement, same as
ordering the section — and it is a *choice among the section's own lines*, never a new line written
to be the headline. A section with no natural headline (a table of rows, a list of open items) stays
**unmarked**: title + status is its honest face, and the body is one expand away. One mark per
section.

**4 · Drop a sign-off the change invalidated.** A re-projection that changes the conclusion removes
the section's `<!-- confirmed: … -->` or `<!-- contested: … -->` marker — the human signed (or
contested) a thesis that no longer exists; the new version goes back through the
[`theses`](../theses/SKILL.md) pass. A re-projection that provably changes nothing semantic (a typo,
a link fix) keeps the marker — when in doubt, drop it: a stale signature is worse than a repeated
sign-off.

**5 · The two chat obligations, before anything lands on disk** (OPERATING-LOOP step 6): a section
resting mainly on the agent's own reasoning or the human's spoken answer is shown **in chat, in
full, first**; and the same message **declares the write perimeter** — the artifact, the worklog,
anything else this pass touches.

**6 · Close.** The change log records the projection per the loop's step 7 (from → to · why ·
trigger), and `python3 tools/lint.py <instance>` reports 0 errors — check P holds the
worklog-behind-every-section rule, checks Q/R the confirmation markers.

## Anti-patterns

- **Projecting from memory.** The section written from the chat scroll while the worklog says less
  (or nothing). The worklog is the source of truth; if the reasoning is not in it, it is not
  projectable — write the worklog first.
- **The working leaking through.** Intermediate tables, per-source notes, the three discarded
  scenarios — in the section. The section is the conclusion in shape; the working is one link away.
- **Tag drift in transit.** An `[assumption]` arriving as `[sourced: …]`, a ⚙️ silently dropped.
  Projection re-shapes text; it never upgrades confidence.
- **A headline written for the mark.** A new summary line composed so the card has something to
  show. The mark points at a line the section already needed; if no line qualifies, the honest face
  is title + status.
- **The surviving signature.** A conclusion changed and the old `confirmed:` date kept — a sign-off
  outliving its thesis. Same for `contested:`.
- **Patching the artifact directly.** The human asks for a change and the section is edited with the
  worklog left behind — the projection now says what its source does not. Fix the worklog, then
  re-project.

## Output

- The **artifact section(s)** written or re-written — each in its fragment's shape, tags carried
  verbatim, `{#id}` and tool markers intact, at most one `<!-- card -->` headline per section.
- **Dropped** `confirmed:` / `contested:` markers wherever the conclusion changed.
- No register writes and no `state.yaml` — those belong to the loop's step 7, after the projection
  stands.
