---
node_type: library-index
title: Library — product methods as skills
status: draft
version: 0.10.0
updated: 2026-08-20
---

# Library

The library is the framework's **method plane**: a catalog of product instruments, each
authored as a **skill**. A step's job is to say *which section must exist*; a tool's job is to
say *how to produce it*. Keeping methods here (not inside steps) is what makes the process
core neutral and the workflow adaptable — companies swap or extend tools without forking the
framework.

## When the agent reaches for a tool

- A **step** recommends tools for the sections of its artifact.
- A **status** re-prioritizes and highlights the tools relevant to the current product stage.
- A **hypothesis** that needs testing pulls a testing tool (e.g. `ab-test`; an interview is
  prepared by the `interview` **outputs** skill — its guide leaves the framework, the notes
  come back as a source).
- The **human** can call any tool directly, or override the recommendation.

All of this is soft: recommendations, not requirements.

## Anatomy of a tool

Each tool is a folder `tool-skills/library/<tool>/`:

```
tool-skills/library/<tool>/
  SKILL.md             # what it is · when to apply it · PREREQUISITES · how to do it · anti-patterns
  template-fragment.md # the DRAFT form of the section — the shape the method's worklog works in.
                       # It may be richer than the step template: the subagent drafts at full depth,
                       # the orchestrator projects only the theses into the step artifact (whose
                       # schema is steps/<n>/template.md). Never put <!--c:key--> keys here.
  questions.yaml       # the interview to gather inputs (also renders to a fillable file)
  references/          # deeper method notes, worked examples

tool-skills/library/references/   # shared by many methods — not a tool folder
  evidence-standards.md           # what a source may be used for, and what must be checked
```

**Prerequisites checklist (required).** Every `SKILL.md` lists the info / artifacts / access the
tool needs before it can run. In the [operating loop](../../process/OPERATING-LOOP.md) the agent
checks this list first; for anything missing it **asks the human to provide it, or offers to
help develop or obtain it** (draft the analysis, prepare an interview guide, write the access
request). A tool never runs on a guessed input.

`SKILL.md` frontmatter declares the tool's wiring so steps, statuses, and future aggregators
can find and compose it:

```yaml
---
node_type: card
kind: method                           # one of five card kinds — process/reference/card-schema.md
name: <tool>
steps: [3]                             # exactly ONE step (linter check U) — a method that would span
                                       # steps is recut: a different operation per step is a second
                                       # skill with its own name; the same operation revisited at
                                       # another step is a per-step variant (`jtbd-concept`, `cjm-strategy`)
prerequisites: [<info/artifact/access it needs>]  # checked first; asked for or helped-with if missing
reads: [register:metrics, register:hypotheses, source:interview, source:research, source:kb]
                                       # the read perimeter of move 2, as atoms. The prefix is
                                       # mandatory: `metrics` is both a register and a source slot.
                                       # `source:interview` = returned interview notes (they arrive
                                       # via sources/); `source:research` = a scoped desk-research pass
                                       # the method runs itself (`loops-research` briefs, discipline
                                       # per references/evidence-standards.md)
writes: [worklog, section:<section-id>, register:hypotheses]
                                       # the write perimeter of move 4: its worklog, the artifact
                                       # section it fills, the registers it updates
# a method carries NO `surfaces` — it is reached from inside a pass, never routed to (law of ranks)
# --- the quality declaration (all four required; the linter checks them) ---
evidence_standard: external-sources    # what class of evidence carries this method's claims
volume_rule: "10–15 situational segments → 20–30 bundles"   # generate-before-you-cut, or n/a
selection_rule: "5 criteria × 1/3/5 → top 3–5"              # how candidates are cut, or n/a
rejects_shown: required                # must the output show what was cut and why · required | n/a
---
```

## The quality declaration

A method that does not say what would make its output *wrong* produces plausible output forever. Four
frontmatter keys make each method state it, and the linter checks that all four are present and legal
(a check costs nothing at read time; a paragraph of good intentions in the canon costs every pass).

**`evidence_standard`** — the class of evidence that carries the method's load-bearing claims.
Exactly one value; a secondary class is discussed in the body, never compounded into the key.

| Value | The claims rest on | Obligation it creates |
|-------|--------------------|------------------------|
| `external-sources` | sources outside the company — registries, filings, statistics, competitors, press | follow [`references/evidence-standards.md`](references/evidence-standards.md): judge each source per fact type, stay out of the forbidden zone, record `as_of`, run the headline check on any number that reaches a conclusion |
| `primary-research` | talking to or observing people directly — interviews, usability sessions, field observation | non-leading questions, past behaviour over stated intent, the sample and its bias named; a quote is evidence of one person, and *n* is stated |
| `internal-data` | the product's own instrumentation and registers — **including controlled experiments run on it** | the reading is reproducible — population, window, derivation written down per [`operations/metrics-capture/`](../operations/metrics-capture/SKILL.md); never a number without its denominator |
| `derived` | no new empirical claim — it composes, computes or ranks what other methods established | every input names the method or register it came from; the method's own reasoning is `[assumption]`, never blanket-sourced to its inputs |
| `decision` | a choice, a plan or a specification the humans own | the decision is dated and attributed and the alternatives are shown, in one canonical line at the end of the produced section, its three fields **keyed** so a tool reads them in any language — `**Decided:** <!--d:date--> <date> · **by:** <!--d:by--> <who> · **alternatives considered:** <!--d:alts--> <what lost, and why>` ([`process/CONVENTIONS.md`](../../process/CONVENTIONS.md) → *The decision line*), with ⚙️ while the agent's proposal is unconfirmed. **The alternatives field is not optional and a bare *none* is a defect** — see *The rejected alternative* below |

**The tie-break**, because most methods touch more than one class: declare the class of **the claims a
reader is most likely to take on trust**. A channel plan is a choice, but what a reader swallows
whole is "this channel reaches our segment" — so it is `external-sources`. A strategy cascade rests on
analysis, but what a reader takes is the choice itself — so it is `decision`. Ask what would embarrass
you if it turned out to be unfounded; that is the class.

**`volume_rule`** — how much is generated *before* anything is cut, or `n/a`. It exists because the
default failure of a generative method is not a bad candidate, it is **too few candidates**: four
polite options, all of them survivors, and no selection actually happened. A volume rule states the
number that makes the selection real. **The questionnaire carries the rule**: the question that
gathers the set states the floor (`min:` on the `list` question) and runs *before* any choice
question — an interview that opens with "pick one" has already broken its own method.

**`selection_rule`** — how the set is cut down: the criteria, the scale, and how many survive. `n/a`
where the method produces one thing rather than a set. A method with a `volume_rule` and no
`selection_rule` is generating candidates nobody chooses between.

**`rejects_shown`** — `required` when the output must carry what was cut *and why it was cut*, `n/a`
otherwise. Rejects are the cheapest artifact in the framework and the most re-derived: without them
the next pass re-proposes the same discarded option, and nobody can tell a filter that was applied
from one that was never reached. Any method with a `volume_rule` or a `selection_rule` shows its
rejects.

### The rejected alternative — the `Decided:` line

A `decision` method's canonical line has three fields, and the third is the only one an agent can
satisfy by writing nothing: a date is a date, an author is an author, and *alternatives considered:
none* is legal prose. It is also the commonest shape of a bad decision — the first idea, written down
and dated. So the field carries a rule of its own:

**Name at least one alternative that was actually weighed and why it lost — or name what makes the
choice forced.** A forced choice is honest and frequent: a constraint that leaves no second option, an
upstream decision already signed, a scope the step inherited rather than chose. What is not honest is
the empty field, because an alternative nobody looked for and a choice with none look identical there.

Where the alternative comes from when the pass produced none: the **refutation lens** of a `verify`
subagent ([`operations/orchestration/`](../operations/orchestration/SKILL.md) → *The two lenses of a
`verify`*) — a fresh reader argues the other side, and what survives the argument is what the line
records. One route to the obligation, not a second obligation: a pass that already weighed a real
alternative owes no subagent.

**What holds it.** The line's three fields carry keys — `<!--d:date-->` · `<!--d:by-->` ·
`<!--d:alts-->` — so **check O4** reads the alternatives field in any language and errors on an empty
or bare-*none* one ([`process/CONVENTIONS.md`](../../process/CONVENTIONS.md) → *The decision line*).
That is the machine half, and it can only judge whether something is written there. Whether what is
written is a real alternative is held by two readers: a `verify` return (the fresh reader's checklist
carries the field) and the human at sign-off, whom [`theses`](../operations/theses/SKILL.md) asks what
makes the chosen option better than the one it beat.

## How to add a tool

1. Create `tool-skills/library/<tool>/` with the anatomy above.
2. Fill `SKILL.md` (what / when / how / anti-patterns) and its frontmatter wiring.
3. Add `template-fragment.md` and `questions.yaml`.
4. Register it in the index below.
5. Link it from the relevant step and status(es) as a *recommendation*.

Before it lands, four gates a donated method must clear (each learned from a real failure):

- **One step, one operation** (check U). If it spans steps, recut it along the step seam first.
- **A home for every recommendation** (check V). If a status will recommend it at step *n*, the
  step-*n* template must carry its `<!-- tool: … -->` marker — otherwise the agent has to invent
  a section.
- **Jurisdiction- and vendor-neutral.** A region-specific registry, data vendor or legal-id scheme
  (a national company register, a local analytics vendor) belongs in a company adapter or a local
  skill, never in the base method.
- **One owner per definition.** A scale, enum or gate the library already defines lives in exactly
  one skill — grep before adding; point at the owner instead of restating it (drifted duplicates
  are how two "identical" 1/3/5 scales end up with different criteria).

Keep tools **single-purpose** and **opinion-explicit**: if a method reflects a particular
school of thought (e.g. a post-AI view of defensibility), say so in `SKILL.md` — that is
exactly why it lives here and not in the neutral core, so another company can supply its own.

## Index

Status: `planned` = named, not yet authored · `draft` = authored, in review · `stable` = merged to main.

Every authored tool cites a **method basis** — a recognized, current methodology it applies —
so the library stays sharp without reinventing theory. Keep it to the method(s) that matter;
don't turn a tool into a literature review.

| Tool | Purpose | Method basis | Steps | Status |
|------|---------|--------------|-------|--------|
| `concept-formation` | Shape the concept from a raw idea | Dunford positioning ('the shift') | 1 | draft |
| `segmentation` | Define & cut segments | JTBD / needs-based, priority-tiered | 1 | draft |
| `segment-pains` | Surface problems in the job | JTBD + Value Proposition Canvas; severity × frequency; differentiator vs table-stakes | 1 | draft |
| `jtbd-concept` | Jobs-to-be-Done framing of the concept | JTBD — Christensen 'progress' + Ulwick ODI (job statement · forces · desired outcomes) | 1 | draft |
| `cjm-concept` | Customer journey map (concept lens) | Journey mapping — stages · touchpoints · emotion curve · pains → opportunities | 1 | draft |
| `concept-expansion` | Problem→solution mapping, no orphan features | Problem→solution articulation over ranked pains; orphan-feature reject table | 1 | draft |
| `value-definition-concept` | Base moats & defensibility | 7 Powers (Helmer) → base moats; post-AI LLM-rebuild test | 1 | draft |
| `market-sizing` | TAM / SAM / SOM | Bottom-up sizing (top-down cross-check) with named assumptions | 2 | draft |
| `competitor-analysis` | Competitors & the game each plays | 'What game are they playing' + moat comparison | 2 | draft |
| `competitor-pricing` | Dated competitor pricing scan | Per-player pricing with read-dates; comparability reject table | 2 | draft |
| `competitor-dynamics` | Competitor trend over time | Registry/filings trend read; per-fact-type sourcing with as_of | 2 | draft |
| `substitutes` | Non-obvious competition | JTBD competition incl. do-nothing / do-it-manually / self-build; Porter threat-of-substitutes | 2 | draft |
| `where-to-play-how-to-win` | Arena + winning logic | Playing to Win (Lafley/Martin) — winning-aspiration / where-to-play / how-to-win cascade | 3 | draft |
| `uvp-cpv` | Value proposition / CPV per situation | Dunford positioning + Value Proposition Canvas + customer-perceived value | 3 | draft |
| `pricing-strategy` | Pricing model & packaging | Value-based pricing — value metric, tiers/fences, WTP (van Westendorp), price vs the next-best alternative | 3 | draft |
| `channels-expansion` | Channels, GTM motion & expansion | Bullseye framework (*Traction*, Weinberg/Mares) + GTM-motion choice + expansion-path thinking | 3 | draft |
| `product-surface` | User-interaction surfaces + instrumentation sketch | Touchpoint mapping + instrumentation planning | 3 | draft |
| `architecture-c4` | System architecture (Context level) | C4 model — Context (Simon Brown) | 3 | draft |
| `bets` | Strategy bets seeded as hypotheses | JTBD forces (pull > anxiety + habit) + moat linkage; dedup against cascade H-seeds | 3 | draft |
| `value-definition-strategy` | Moat revisit: derivatives & trajectory | 7 Powers (Helmer) — derivative moats once customers/scale exist | 3 | draft |
| `cjm-strategy` | Journey revisit against the chosen strategy | Journey mapping — re-walk vs strategy/channels; feeds product-surface | 3 | draft |
| `pre-mortem` | Surface & triage strategy risks | Pre-mortem (Klein) + probability × impact triage (5/3/1); carried/parked/dropped disposition | 3 | draft |
| `instrumentation-plan` | Component → instrumentation → data → infra cost | Instrumentation planning over the C4 context (refines Step 3) | 4 | draft |
| `metric-tree` | North Star → drivers → inputs | North Star Framework (Amplitude); anti-lamppost: right metric over measurable metric | 4 | draft |
| `retention-analysis` | Cohort retention curve + engagement loop | Flattening cohort curve as PMF signal; retention by cohort/frequency; real churn input to LTV, not an assumed % | 4 | draft |
| `unit-economics` | CAC/LTV/payback/contribution | Contribution margin; LLM inference as explicit COGS; dual basis (operational/honest own-compute) | 4 | draft |
| `financial-model` | Projection off the metric tree | Driver-based modeling; churn as scenario axis; capacity caps as first-class constraint | 4 | draft |
| `strategic-targets` | Horizon commitments on key nodes | Values read off the projection (scenario named), 3–5 nodes, decision-attributed; the top of the target ladder | 4 | draft |
| `capabilities-systems` | Must-have capabilities + management systems | Playing to Win (Lafley/Martin) choices 4–5; have/partial/missing honesty, gaps seed execution `R-…` | 4 | draft |
| `risk-mitigation` | Carried risks → owned mitigations | Risk lifecycle: mitigation · owner · trigger · status; register upsert | 4 | draft |
| `hypothesis-thresholds` | Quantify strategy bets | Assumption mapping (Bland/Osterwalder) — success & failure thresholds on existing `M-…` nodes | 4 | draft |
| `pricing-strategic-plan` | Margin revisit of the pricing decision | Contribution/COGS re-read of Step-3 pricing (holds, or ⚙️ change proposal) | 4 | draft |
| `prioritization-tactical-plan` | Rank period goals against the gate | RICE / ICE as ranking aid, ranked by contribution to the period gate; capacity-bounded | 5 | draft |
| `goal-targets` | Period goals → metric nodes & DoD | Node selection off the metric tree; baseline from metrics.csv → reasoned target | 5 | draft |
| `guardrails` | What must not drop while hitting goals | Guardrail metrics + red lines (steering-committee reconciliation) | 5 | draft |
| `resource-check` | Assess available resources this period | Lightweight capacity survey | 5 | draft |
| `segment-cvp` | Compose a testable go-to-market entry bundle | Market-entry bundle (segment · situation · pain · CVP · offer · channel · signal) + 6-filter readiness gate + qualified-action signal scale | 5 | draft |
| `hypothesis-test-design` | Design a test for a hypothesis | Smallest viable test (metric · threshold · sample/duration · decision rule); thresholds referenced from Step 4 | 5 | draft |
| `ab-test` | Run a controlled experiment | Online controlled experiments (Kohavi/Tang/Xu) — OEC + guardrails, MDE-driven sizing, no-peek stopping rule | 5 | draft |
| `experiment-readout` | Read a finished test against its pre-registered rule | Pre-registered readout; signal/decision written back to the hypotheses register | 5 | draft |
| `prioritization-sprint-plan` | Rank must vs backlog, show excluded | RICE / ICE as ranking aid, ranked by contribution to the period gate; capacity-bounded must/backlog line | 6 | draft |
| `feature-spec` | Development item as a Feature | Description/Scope/Acceptance criteria/Business value/User value/User stories | 6 | draft |
| `activity-spec` | Go-to-market item as an Activity | Feature-altitude activity tied to a metric/hypothesis | 6 | draft |
| `task-spec` | Back-office item as a Task | Description · why-link · binary DoD · owner · estimate | 6 | draft |

> **Runtime skills live elsewhere.** `handoff` (session-to-session state transfer) was a library
> entry; it is a *runtime* capability, not a product method, and now lives in
> [`tool-skills/operations/`](../operations/README.md). The library holds product methods only.

The list is a starting set, not a closed spec — grow it as the community adds methods.
