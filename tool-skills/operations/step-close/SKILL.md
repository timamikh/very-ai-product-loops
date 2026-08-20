---
node_type: card
kind: operation
name: step-close
prerequisites:
  - every section the step's gate names as its own is worked and projected — a reading of the whole taken over holes reports the holes, not the meaning
  - the reader is the orchestrator, with the step's sections, worklogs and registers in view at once — a subagent sees one section and cannot make this pass's finding by construction
reads: [section:*, worklog:*, register:*]
writes: [section:*, worklog:*, register:*]
surfaces: [ticks, change-log]
opinionated: true
method_basis: "The whole is a different reader: a step worked one section per pass is never read whole by anyone, so every conclusion that only the union shows — a link between two sections, a tension, a gap no single section could be missing — has no moment in which it can be found. This pass is that moment, and it lands what it finds through the ordinary channels"
status: draft
version: 0.1.1
updated: 2026-08-20
---
# Step close — read the step whole, land what only the whole shows

**What it is.** The pass that runs **once per step, after its sections are worked**: the step's
artifact, every worklog behind it, and the registers, read together in one sitting. Its output is not
a summary — it is the set of conclusions that **no section pass could have reached**, each landed
where it acts.

**Why the canon needs it.** One pass per *section* is the law, and it is the right law: a section is
the unit a human signs. But it means the sections are written in sequence, each before the later ones
exist — `#problems` is closed while the moat is still unwritten, so "which segment proves the moat"
is a question that *cannot be asked* on the pass that would care. Nobody is ever the reader of the
whole. That reader is this pass.

**Why it is an operations skill, not a library method.** It fills no section and belongs to no step's
content — it acts on the *relations between* sections, and it is triggered by an event (the step's own
sections are done). It is routed, not reached from a marker.

**The one thing it exists to prevent.** A step that is correct section by section and says nothing as
a whole: every table full, every tag honest, and not one line stating what the step *means* — no
tension named, no disqualifier drawn, no admission of what the step still has no evidence for. That
failure is invisible to the linter (structure is complete), invisible to `verify` (it reads one
section against its worklog), and invisible to `theses` (it walks what is written, not what is
missing).

**What it does not do.** It does not re-work a section's content — a wrong conclusion is an ordinary
`Act` re-projection on its own pass. It does not sign anything ([`theses`](../theses/SKILL.md) does,
after this pass). It has no new write permission of its own: what it finds reaches a section through
an ordinary re-projection, and the orchestrator's conclusions block that
[`projection`](../projection/SKILL.md) step 0 already sanctions is the channel into that section's
worklog. The only thing new here is the **perimeter**: the whole step, not one section.

## When to apply

1. **The step's own sections are all worked** — the common case, immediately before `theses`, and
   that is the *whole* trigger, the same one the router carries. The gate's derived items
   (`#to-clarify`, `#hypotheses`, an optional section) may already be ticked by the passes that fed
   them; a step whose sections were closed one at a time has still never been read whole, and a
   condition about the gate would make the common case unreachable exactly when the last section
   pass did its move 5 properly.
2. **A late section changed what an earlier one assumed** — a re-projection landed a conclusion the
   sections above it were written without.
3. **On request** — the human asks what the step means, not what it contains.

## Prerequisites

- **The sections, worked.** A gap section is a hole, and a reading of the whole taken over holes
  reports the holes. Close the sections first; that is the ordinary row of the router.
- **The worklogs, all of them.** Half of what this pass exists to find is already written down and
  stuck: a conclusion the section pass reached and did not project. Read the worklogs, not only the
  artifact.
- **The orchestrator, undelegated.** The whole-step read is the orchestrator's by the same rule that
  gives it the projection: a subagent sees the slice it was briefed on.

## How to do it

**1 · Read the step whole.** The artifact end to end as a reader meets it, then every worklog in the
step folder, then the registers the step wrote. In one sitting — the point is the simultaneity, and a
pass that reads them one at a time over a long session is doing the ordinary pass again.

**2 · Ask the four questions a section pass cannot ask.** Write the answers down before deciding
what to do with them; every line is **⚙️ or `[assumption]`** — this pass reasons, it does not source.

- **What does one section mean next to another?** A link, a tension, a disqualifier: a force in
  `#jtbd` that is the same bet as a risk in `#solution`; a moat that is sharpest for the segment
  ranked second.
- **Which conclusion never left its worklog?** A finding reached on its pass, addressed to a section
  that did not exist yet, and therefore stranded. It is now readable — land it or kill it, but do not
  leave it stranded a second time.
- **What is the whole missing?** The gap no single section could be missing, because no single
  section owns it: no evidence at all behind a whole class of claim, a threshold nobody defined, a
  decision every section quietly assumed. Most of what this question finds is an *open item*, not a
  fix.
- **Which section states no conclusion?** A section whose rows imply a judgement that no line makes
  (`projection` step 3). That line is missing from the section on its own merit.

**3 · Land each finding where it acts.**

- **It belongs to a section** → re-project that section: the conclusion goes into *its* worklog as
  the orchestrator's conclusions block (`projection` step 0), then the section is written from the
  worklog. Never patched straight into the artifact.
- **It belongs to the step** → an open item in `#to-clarify`, naming which of the two kinds it is:
  *the human must choose*, or *nobody knows and someone must go and find out*. A finding that is a
  bet rather than a question may instead take a **register the step's own card already writes** (a
  bet nobody tested is a hypothesis; a tension between two sections is often a risk) — this pass does
  not open a register plane the step never had: a step that seeds no risks does not start here.
- **It belongs to a later step** → an open item that says which step resolves it, so the next step's
  first pass inherits it instead of rediscovering it.
- **Nothing found** → a legal answer, and it is recorded in the change log as the answer. Skipping
  the question is not legal.

**4 · The step's face.** Every section either carries one marked `<!-- card -->` headline or a
recorded reason why it honestly has none (`projection` step 3). A board where most sections show
title-and-status is this pass's finding, not the board's problem.

**5 · Close.** The gate's derived items are ticked here if this pass is what closes them
(`#to-clarify` is complete, `#hypotheses` carries what the step seeded), a dated **change-log** entry
records what the whole showed — including *nothing new* if that is the answer — and
`python3 tools/lint.py <instance>` reports 0 errors. Then `theses`: the human signs a step that has
been read whole.

## Anti-patterns

- **Summary instead of synthesis.** The sections restated back in fewer words. A summary carries no
  information the artifact did not already have; if the pass produced no line that was not derivable
  from one section alone, it produced nothing.
- **Closing a fork to make the step look finished.** A tension resolved by asserting one side, so the
  gate reads clean. The honest output of a whole-step read is often **one more open item**, not fewer
  — a fork closed without evidence is worse than a fork left open, because it stops being asked.
- **Patching the artifact.** A conclusion written straight into a section because "the worklog is
  behind it anyway". The worklog first, then the projection — the rule does not soften because the
  writer is holding the whole step.
- **Laundering the reasoning.** A conclusion of this pass arriving in a section as `[sourced: …]` or
  bare. It is the agent's own reading and carries ⚙️ or `[assumption]`, wherever it lands.
- **Re-working content under cover of synthesis.** Rewriting a section's substance because the whole
  read suggests a better answer. That is an ordinary `Act` pass with its own trigger and its own
  `verify`; this pass names the finding and stops. Correcting a **provenance tag** is not that: a tag
  says where a claim came from, and where the claims came from is exactly what a whole-step read sees
  for the first time — a `[sourced: …]` naming no source that exists outside the instance, the same
  claim tagged two ways in two sections. The substance stays untouched, the tag is fixed, and the
  change log says which tag and why.
- **Delegating the whole-step read.** Briefing a subagent to "review the step". It returns a review of
  the text it was given; the pass exists for the reading only the context-holder can do.

## Output

- The **conclusions of the whole**, written down with ⚙️/`[assumption]` provenance, each either landed
  or explicitly killed — never left stranded in a worklog a second time.
- **Re-projected sections** where a conclusion belonged to one, through their worklogs.
- **Open items** in `#to-clarify`, each marked as *the human chooses* or *nobody knows yet* — and,
  where a finding is a bet or a threat rather than a question, an entry in a register **the step
  itself writes**: this pass reaches for the step card's own touchpoints and does not open a register
  plane the step never had (a step that seeds no risks does not start seeding them here). That is why
  `register:*` sits in `writes` and not in `surfaces`: a register entry is a destination this pass
  may use, never a surface it owes.
- **Card headlines** marked, or their absence justified.
- A dated **change-log** entry — including the honest *nothing the parts did not already say*.
