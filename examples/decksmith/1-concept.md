---
node_type: artifact
artifact: concept
step: 1
title: "Product Concept — Decksmith (fictional sample)"
status: draft
version: 0.1.1
updated: 2026-08-17
---

<!--
  Concept artifact. Each section is filled by its recommended library tool (steps/1-concept/README.md),
  projected from that method's worklog in 1-concept/. Section IDs and column keys are stable.
  Follow process/CONVENTIONS.md for confidence tags, sources, IDs, links, and the change log.
  ⚙️ marks agent-proposed defaults awaiting human approval.
-->

# Product Concept — Decksmith (fictional sample)

> Status: concept-viability · Owner: acting PO (agent) · Last review: 2026-08-16

## Idea {#idea}
<!-- tool: concept-formation -->

<!-- card -->
_Decksmith is an **AI deck generator** that produces **native, fully editable** `.pptx`/`.key` slides
that **also look designed** — for people who make client-facing decks._  [sourced: founder brief]

**The shift:** today every AI slide tool forces one of two bad trades — **pretty-but-locked** (images
or a rigid template you can't really edit) or **editable-but-ugly** (plain text in default PowerPoint
styling), so people regenerate by hand and the tool saves less time than promised; with Decksmith the
output is **editable AND designed at once** — real shapes, text and layouts you edit like your own
file, already designed and structured for the audience.  [assumption]

**Riskiest assumption:** the engine can *reliably* produce files that are **both** genuinely editable
**and** genuinely well-designed **at scale** — across arbitrary user content, not just demos.  [assumption] → `H-001`

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** leading on
demand rather than feasibility (rejected — the founder's own read, which I share, is that the concept
lives or dies on whether the engine holds quality at scale; demand is real but not the long pole).

## Job-to-be-Done {#jtbd}
<!-- tool: jtbd-concept -->
_The job the customer hires the product for, the four forces around switching, and the outcomes
they judge success by. Anchors `#segments` and `#problems`; the job feeds Step 2 `substitutes`._

<!-- card -->
**Job statement.** _When_ I need to produce a client-facing deck (pitch / proposal / QBR) that must
look credible to an external audience, usually on a deadline, _I want to_ turn my raw content into a
finished, on-brand, well-structured deck **without hand-fixing every slide**, _so that_ I come across
as professional and spend my time on the message, not the formatting.  [assumption]

| Force <!--c:force--> | Direction <!--c:dir--> | For this job <!--c:forjob--> | Confidence <!--c:conf--> |
|-------|-----------|--------------|------------|
| Push | away from status quo | AI tools return templated-looking / wrong-structure output → the maker regenerates or rebuilds by hand and the time saving evaporates [sourced: founder brief]; doing it manually is slow and a designer is costly / not on-demand [assumption] | mixed (see cell) |
| Pull | toward this product | a deck that is editable **and** designed — polished and correctly structured, yet a native file you still tweak like your own | [assumption] |
| Anxiety | resists switching | "will it really be editable, not locked/images?" · "will the design hold on **my** content, not just the demo?" · "will it match our brand?" · another tool to learn | [assumption] |
| Habit / inertia | resists leaving status quo | the maker already knows PowerPoint / Slides / Keynote, owns templates, and defaults to "I'll fix the AI draft myself" or "I'll do it manually" | [assumption] |

_Progress needs push + pull > anxiety + habit. Push and pull are both strong, but so are anxiety
(does the design hold on my content? is it truly editable?) and habit (I already own the tools) — so
the feasibility bet `H-001` doubles as the desirability lever: proving design holds at scale is what
most collapses the anxiety term._

**Desired outcomes (ODI).** Minimize time from raw content → client-ready deck · minimize the share
of slides needing manual restyle before sending · minimize rework to get the structure/story right ·
increase the likelihood the deck reads as credible and on-brand.  [assumption]

## Segments {#segments}
<!-- tool: segmentation -->
_Who it's for and how segments are cut._

**Cut basis:** by the **job + stakes/context of the deck** — who regularly makes *client-facing,
credibility-critical* decks (vs internal/throwaway ones). That is the only cut where the whole value
bundle (editable **and** designed **and** on-brand **and** well-structured) is demanded at once.
Rejected cuts (kept in the worklog): role/function, company size, design-ability, buying cadence —
each predicts *how you sell* or a single facet, not the core need.

| Priority <!--c:priority--> | Segment <!--c:segment--> | How it's cut <!--c:cut--> | Buyer / user <!--c:buyer--> | Why it matters <!--c:why--> | Where to reach them <!--c:reach--> | Confidence <!--c:conf--> |
|----------|---------|--------------|--------------|----------------|---------------------|------------|
| 1 (lead) ⚙️ | Sales & marketing professionals making client-facing decks (pitches, proposals, QBRs, campaign decks) | job = recurring high-stakes client-facing decks | same person, or buyer = sales-enablement/marketing-ops lead vs user = the IC | highest frequency × stakes; usually a company budget behind the buy | LinkedIn; sales/marketing communities (RevGenius, Pavilion, r/sales); PLG via "pitch deck template" SEO | [assumption] |
| 2 | Independent consultants / agencies / freelancers building decks for clients | job = client deliverable decks | buyer = user (self-funded) | sharpest design + editability need (client handoff); frequent but price-sensitive, lower volume | consultant/agency communities, Upwork/Contra | [assumption] |
| 3 | Startup founders raising / pitching | job = fundraising & pitch decks | buyer = user | extreme stakes but bursty/one-shot; skews to done-for-you | accelerators, VC networks, founder communities | [assumption] |

<!-- card -->
**Lead segment:** ⚙️ **S1 — sales & marketing client-facing deck makers.** The only segment whose
need *recurs* often enough to fit a self-serve product rather than a one-off service; matches the
founder's bet (frequency × stakes × company budget). Ranking rests on need-difference + reachability;
moat-fit is revisited once `#value-defensibility` is set (see `#to-clarify`).

**Seeded hypotheses:** `H-006` — S1 is a reachable, recurring, company-budgeted beachhead → register.

## Problems {#problems}
<!-- tool: segment-pains -->
_Lead segment (S1: sales & marketing client-facing deck makers). Job: turn raw content into a
finished, on-brand, well-structured, client-ready deck without hand-fixing every slide. Rows in rank
order; the top 3 carry into the solution. Full 7-pain scoring in the worklog._

| Problem <!--c:problem--> | Severity <!--c:severity--> | Frequency <!--c:frequency--> | Cost of inaction <!--c:inaction--> | Class <!--c:class--> | Confidence <!--c:conf--> |
|---------|----------|-----------|------------------|-------|------------|
| AI output "looks templated" → restyled by hand, so the promised time-saving evaporates | H | H | already paying / improvising | differentiator | [sourced: founder brief] |
| Deck comes back with the wrong structure/story for the audience → narrative rewritten | H | M–H | already improvising | differentiator | [sourced: founder brief] |
| Locked / image output can't be edited → last-minute edits & reuse impossible (disqualifying) | H | H | already improvising | table-stakes | [sourced: founder brief] |
| Output isn't on-brand (fonts, colours, logo, layout) → manual re-branding every time | M–H | H | recurring irritation | differentiator | [assumption] |
| Deadline pressure → slow tools / manual rebuild risk missing the deadline | M | H | recurring irritation | table-stakes | [assumption] |
| Visual inconsistency across a deck (spacing, alignment, rhythm) → looks amateur | M | M | recurring irritation | differentiator | [assumption] |
| Getting existing content into slides is tedious reformatting | M | M | recurring irritation | table-stakes | [assumption] |

<!-- card -->
**Lead pain:** the "templated look" restyle tax (top differentiator). The editability gate is
table-stakes but *disqualifying* — the wedge against "pretty-but-locked" incumbents.
**Seeded hypotheses:** `H-003` (restyle tax), `H-004` (wrong-story pain), `H-005` (editability gate) → register.

## Solution {#solution}
<!-- tool: concept-expansion -->
_How the product solves each ranked problem. No orphan features (rejects in the worklog)._

| Problem <!--c:problem--> | How the product solves it <!--c:solution--> | Confidence <!--c:conf--> |
|---------|---------------------------|------------|
| "Templated look" restyle tax | Engine emits **native slide objects styled by design rules learned from a curated corpus** (grids, spacing, type hierarchy, colour) at generation — so the first output already reads as designed | [assumption] → `H-001` |
| Wrong structure/story | A **narrative-structuring pass** maps raw content to an audience-appropriate deck arc before styling — structure chosen for the audience, not bullet-dumped | [assumption] → `H-002` |
| Editability gate | **Native `.pptx`/`.key` emission** — real shapes, text and layout objects that round-trip as fully editable, never flattened images or a locked template | [assumption] → `H-001` |
| Not on-brand (tier-2) | **Brand-kit ingestion** (fonts, colours, logo, layouts) into the design engine; concept-level commitment, post-MVP in delivery | [assumption] |

<!-- card -->
**Feasibility bets:** `H-001` (native-editable **and** designed at scale) · `H-002` (audience-fit
narrative structure) → hypothesis register.
**Rejected as orphans** (no ranked pain): real-time collaboration, non-slide formats, chat-assistant
surface, deck analytics — all out of scope or a different job (see worklog).

**Decided:** 2026-08-16 · **by:** ⚙️ acting PO (agent) · **alternatives considered:** treating
narrative structure as part of H-001 (rejected — a deck can look good and still tell the wrong story,
so the build bet is split into H-001 visual/editable and H-002 narrative).

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition-concept -->
_Base moats only; derivatives deferred to Step 3. Lens: post-AI rebuild test (opinionated method)._

<!-- card -->
**Core value (post-AI):** not the generator (a commodity) but the ability to reliably hit
*editable-and-designed* quality on arbitrary content — which rests on **curated design taste encoded
as data + rules** and the **credibility to be trusted on design**. Software is copyable; taste,
labelled corpus, and reputation are slower.  [assumption]

**Base moats**

| Moat | Layer | State | Survives LLM rebuild? | Confidence |
|------|-------|-------|----------------------|------------|
| Curated design corpus + learned patterns | hard — unique data | Building | Partly — corpus assembly + taste-labelling is slow, compounds | [assumption] |
| Founder design taste / credibility | soft — brand/trust + expertise | Have (partial) | Yes — a clone gets the software, not the reputation | [assumption] |
| Design-quality-at-scale engineering | soft — processes + depth | Building | Partly — execution lead that erodes | [assumption] |

**Lead moat:** ⚙️ the **design corpus + founder taste** (unique data × brand/expertise) — the
combination is least copyable and compounds with use. Durability M (nothing validated yet).
**Killed as features, not moats** (kept in worklog): native export, nice UX, "uses a frontier LLM",
first-mover — each reproducible by anyone with the same model.

**Derivative moats** (derived at the Step-3 `value-definition-strategy` revisit — same section,
updated in place): **edit-behaviour data loop** (dep: edit-capture ships + usage scale) and
**brand-kit lock-in / switching cost** (dep: brand-kit storage ships + a customer embeds their brand).
On re-test, the **native-export engineering re-reads as an eroding *wedge*, not a durable moat**.
**Trajectory:** enter on taste corpus + founder distribution (now) → build the data loop (needs scale)
→ build brand-kit lock-in (needs embed); convert the wedge before it erodes (`H-012`/`R-007`).

**Seeded hypotheses:** `H-007` — the corpus + taste is a real, compounding moat → register; the
derivatives + timing seed `H-012` at Step 3.

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. These are carried into the hypothesis register
(`registers/hypotheses.md`), where they are refined downward through the later steps._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-001 | Engine reliably produces slides both native-editable **and** well-designed at scale | feasibility | idea, solution | [assumption] |
| H-002 | Engine reliably produces audience-appropriate narrative structure, not just visual polish | feasibility | solution | [assumption] |
| H-003 | Deck makers hand-restyle "templated" AI output, so the time-saving doesn't materialise | desirability | problems | [assumption] |
| H-004 | The wrong-structure/story pain is significant and distinct from the visual pain | desirability | problems | [assumption] |
| H-005 | Editability is a hard gate — locked/image output disqualifies regardless of looks | desirability | jtbd, problems | [assumption] |
| H-006 | S1 (sales & marketing deck makers) is a reachable, recurring, budgeted beachhead | viability | segments | [assumption] |
| H-007 | The design corpus + founder taste is a real, compounding moat | viability | value-defensibility | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced by the agent for the human to resolve._

- **Moat-fit of the lead segment (⚙️ ranking).** S1 is ranked lead on frequency + reachability + a
  company budget, before the moat was stated. Now that the moat is the design corpus + taste, is S2
  (design-native consultants/agencies) the sharper early *proving ground* for design quality, even if
  S1 stays the scale bet? A choice for Step 3 (`where-to-play-how-to-win`), not resolved here.
- **No customer evidence yet.** Every desirability bet (H-003/H-004/H-005) rests on the founder's
  observation, not behavioural evidence from the segment. Discovery interviews are the first thing
  the tactical loop should buy.
- **"At scale" is undefined for H-001.** What content breadth and what quality bar count as "reliably
  designed"? Needs a concrete threshold — deferred to Step 4 (`hypothesis-thresholds`).
- **Technical fork (noted, not asked):** native emission via a `.pptx`/`.key` object model vs an
  intermediate open format then convert — an implementation choice for Step 3 architecture, not a
  product decision.

## Change log

### 2026-08-17 — card lines marked for the console board
- **From → To:** no section carried a `<!-- card -->` mark → 6 section(s) with a natural headline
  line now mark it; table-only sections stay unmarked (title and status only, the body one expand away)
- **Why:** the console no longer composes a card face of its own — a board card shows the author's
  marked line verbatim or nothing (CONVENTIONS → *Card line*)
- **Trigger:** console rework — a card is a collapsed section, not a third text

### 2026-08-16 — Step 1 concept worked and projected
- **From → To:** empty skeleton → all six method sections filled (`#idea`, `#jtbd`, `#segments`,
  `#problems`, `#solution`, `#value-defensibility`), `#hypotheses` seeded with H-001…H-007, and
  `#to-clarify` opened; each section projected from its worklog in `1-concept/`
- **Why:** the Step 1 operating-loop pass — concept as a positioning shift (editable-XOR-designed →
  editable-AND-designed), S1 as the beachhead, and feasibility (`H-001`) named as the riskiest bet
- **Trigger:** Step 1 pass; F2/F3/F4 corrections applied after a `loops-verify` review (tag split on
  the JTBD push force, H-002 source re-attributed, this change-log entry added)

### 2026-08-16 — created
- **From → To:** — → concept skeleton scaffolded (sections empty, founder brief dispatched to worklogs)
- **Why:** instance setup; the concept is filled section-by-section through its methods in the Step 1 pass
- **Trigger:** `product-setup` scaffolding of the Decksmith sample instance
