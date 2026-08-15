---
node_type: artifact
artifact: passport
product: Decksmith (fictional sample)
step: 1
status_stage: concept-viability
owner: sample
updated: 2026-08-14
version: 0.4.0
---

# Product Passport — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-08-14
> Fictional example — every value is illustrative. Most claims are `[assumption]` by design: at concept
> stage there is no product data, so the passport is mostly a set of bets to test. **Projection** of the
> Step-1 worklogs in `1-idea/` (concept-formation · jtbd · segmentation · segment-pains ·
> value-definition) — the worklogs are the source of truth; this file holds nothing they do not.
> Registers: `registers/hypotheses.md` (seeded here) · risks/metrics born at Steps 2/4. ⚙️ marks an
> agent-proposed default awaiting the human.

## Concept {#concept}
<!-- tool: concept-formation -->

Decksmith is an **AI slide generator** that produces **native, fully-editable** `.pptx`/`.key` decks
(real shapes, text, layouts you edit like your own) that **already look designed**, not templated — for
the people who make client-facing decks. [sourced: founder brief 2026-07-16]

**The shift:** today every AI slide tool forces one of two bad options — *pretty but locked* (image /
rigid-template exports you can't really edit) **or** *editable but ugly* (plain text in default styling).
With Decksmith the either/or collapses: the output is editable **and** designed, so you *edit* the deck
instead of *rebuilding* it by hand. [sourced: founder brief for the trade-off; that Decksmith collapses it — assumption]

**Riskiest assumption:** the engine can *reliably* produce native files that are both genuinely editable
and genuinely well-designed, **at scale** — not one hand-tuned demo. This is the core bet. [assumption] → `H-001`

**Concept scope (⚙️ sequenced).** The core shift is *editable + designed* (the tightest feasibility bet);
audience-aware structure/story is carried as a stated solution move and a differentiating pain (P2), on
shakier capability ground, to expand once the core holds. Alternatives — *narrow* (drop story) / *full*
(bet the concept on story too) — are the human's to weigh; noted in `#to-clarify`. [assumption]

## Job-to-be-Done {#jtbd}
<!-- tool: jtbd (lens — anchors #segments and #problems; the job feeds Step 2 substitutes) -->

**Job statement.** _When_ I have to produce a client-facing deck for a specific audience on a deadline,
_I want to_ get a deck that already looks designed **and** carries the right structure/story for that
audience — and that I can still edit natively like my own file — _so that_ I present credibly and win the
meeting without spending hours rebuilding it by hand. [sourced: founder brief for the two halves; deadline framing assumption]

The job has **two load-bearing halves**: *look designed* and *right story*. Both are what the segment hires for.

| Force <!--c:force--> | Direction <!--c:dir--> | For this job <!--c:forjob--> | Confidence <!--c:conf--> |
|-------|-----------|--------------|------------|
| Push | away from status quo | AI output "looks templated" / comes back with the wrong structure → the user hand-rebuilds it, so the tool saves less time than promised | [sourced: founder brief] |
| Pull | toward Decksmith | one tool with no trade-off: native, fully-editable `.pptx`/`.key` that also looks designed — editable **and** designed, in the format they already present from | [sourced: founder brief] |
| Anxiety | resists switching | "will it *actually* be both editable and well-designed this time, and get the story right for *my* audience — or will I redo it by hand again?" (trust that quality holds at scale) | [assumption] |
| Habit / inertia | resists leaving status quo | an established, controllable workflow: build by hand in PowerPoint/Keynote/Canva, lean on company templates, or prompt a general LLM and format it themselves | [assumption] |

_Progress happens only when push + pull > anxiety + habit. The adoption-killer here is the **anxiety
"I'll still have to fix it"** — the segment already tries AI tools and gets burned, so conversion turns
on retiring that trust gap, which is exactly the feasibility bet `H-001`. jtbd **sharpens** `H-001`/`H-002`/`H-003`;
it seeds no new hypothesis._

**Desired outcomes (ODI).** Measurable directions the segment judges success by:
- Minimize time from AI draft → presentation-ready deck (the "saves less time than promised" complaint). [sourced: founder brief]
- Minimize slides that must be manually re-designed after generation. [assumption]
- Maximize fit of structure/story to the specific audience. [sourced: founder brief]
- Maximize the likelihood the deck reads as *designed*, not templated, to the client. [sourced: founder brief]
- Maximize native editability of the output (locked/image output is a non-starter). [sourced: founder brief]

## Segments {#segments}
<!-- tool: segmentation -->

**Cut basis:** by *use-context × stakes × frequency* — what the deck is for, who judges it, how high the
stakes, how often the person makes one. This predicts different needs far better than firmographics or
job-title alone (both rejected): the concept's value compounds exactly where stakes and frequency are
both high and the audience is external. [assumption]

| Priority <!--c:priority--> | Segment <!--c:segment--> | How it's cut <!--c:cut--> | Why it matters <!--c:why--> | Where to reach them <!--c:reach--> | Confidence <!--c:conf--> |
|----------|---------|--------------|----------------|---------------------|------------|
| **1 (lead)** | Salespeople & marketers making client-facing decks | External client/prospect decks; high frequency × high stakes; a company budget behind the purchase | Highest frequency × stakes of any candidate; feel **both** pains (templated look + wrong structure); budget exists to pay | ⚙️ sales/marketing communities (RevOps & sales-enablement Slack/Discord) + LinkedIn — reach-channel is genuinely open (see `#to-clarify`) | [sourced: founder brief for lead; channels assumption] |
| 2 | Founders / startup teams making fundraise & pitch decks | Investor-facing decks; very high stakes, episodic frequency | Acute both-pains and unusually reachable (accelerators); below lead only on frequency | ⚙️ accelerators, angel/VC networks, founder communities | [assumption] |
| 3 | Independent consultants & agencies | Client proposals/readouts; design-judged, moderate–high frequency | Real volume and reachable, but weaker moat fit — many can already design | ⚙️ consulting/agency networks, LinkedIn | [assumption] |
| 3 | Internal deck-makers (analysts / PMs / ops) | Internal board/exec/team decks; high frequency, lower external stakes | Large volume, but an internal audience lowers the design-stakes half of the value | ⚙️ PM/ops communities, enterprise motion | [assumption] |
| 3 | Freelance / in-house designers | Decks as a design deliverable; high design taste in-house | Lowest moat fit — design is their skill, not their gap | ⚙️ design communities (Dribbble, Behance) | [assumption] |

**Lead segment:** ⚙️ **Salespeople & marketers** — the only candidate combining high frequency, high
stakes, both-pains, a budget, and nameable channels; matches the founder's stated bet. Lower tiers are
kept, not dropped. [sourced: founder brief 2026-07-16]

**Seeded hypotheses:** `H-002` (this segment is reachable and feels P1 strongly enough to switch) → hypothesis register.

## Problems {#problems}
<!-- tool: segment-pains -->
_For the lead segment (salespeople & marketers). Job: see `#jtbd`. Pains are obstacles inside that job,
scored by severity × frequency; editability is a table-stakes baseline, look (P1) and structure (P2) are
the differentiators. Every H/M/L below is a ⚙️ ordinal `[assumption]` — one observer, no segment research.
Lower-confidence added pains (time-saving, credibility, brand consistency) are kept in the worklog, not carried here._

| Problem <!--c:problem--> | Severity <!--c:severity--> | Frequency <!--c:frequency--> | Class <!--c:class--> | Confidence <!--c:conf--> |
|---------|----------|-----------|-------|------------|
| P1 — AI decks look templated/generic → I redo them by hand anyway | H | H | differentiator | [sourced: founder brief] |
| P2 — Wrong structure/story — the deck doesn't fit the audience | H | M | differentiator | [sourced: founder brief] |
| P3 — Locked/image output — can't edit in PowerPoint/Keynote | H | H | table-stakes | [sourced: founder brief] |

> Editability (P3) is a **table-stakes** baseline (it's in the concept); *look* (P1) and *structure/framing*
> (P2) are the differentiating pains Decksmith competes on. Pitch leads on the differentiators, not the gate.

**Seeded hypotheses:** `H-002` (P1 matters enough to switch) · `H-003` (P2 is a top pain, not just styling) → hypothesis register.

## Customer Journey {#cjm}
<!-- tool: cjm (optional lens — the temporal view behind #problems; fill when a drop-off needs explaining) -->

_Optional lens — **omitted** at concept stage. The flat pain list above is sufficient; there is no
unexplained drop-off to map (no product in market yet). Revisit if a specific stage-level breakage needs
explaining. Gate: `n/a`._

## Solution {#solution}
<!-- tool: concept-formation -->

_How Decksmith solves each carried-forward problem. No orphan features. Solution stub — feature design is downstream._

| Problem <!--c:problem--> | How the product solves it <!--c:solution--> | Confidence <!--c:conf--> |
|---------|---------------------------|------------|
| P1 — looks templated | **Design layer** — layout/spacing/type rules learned from a curated corpus of well-designed decks → output reads as *designed*, not templated | [assumption] |
| P2 — wrong structure | **Audience-aware structure** — shapes the narrative/outline for the target audience, not a generic dump (⚙️ sequenced — the expansion bet, capability not yet in the inventory) | [assumption] |
| P3 — locked/images | **Native renderer** — emits real slide objects (shapes/text/layouts), not images → editable in the user's own tool | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition -->
_Lens: 7 Powers → base/derivative moats, post-AI (software isn't the moat, position is). A value that does
not survive an LLM rebuild is a feature, not a moat. Swappable lens._

**Core value (post-AI):** what a generic "make slides with an LLM" wrapper would *not* have — turning LLM
content into output that is **simultaneously native-editable AND genuinely designed, reliably at scale**
(the collapse of the trade-off itself), delivered by a deterministic native-object rendering layer plus
encoded design judgment (corpus + taste). The *positioning* is the value statement, not itself a moat.
[assumption]

**Base moats**

| Moat | Layer | Have / Building / Aspiration | Survives an LLM rebuild? | Confidence |
|------|-------|------------------------------|--------------------------|------------|
| Native-object rendering pipeline — reliable editable-and-designed emission at scale | hard (IP-leaning) ⚙️ | Building | Partly — the *approach* is copyable; reliable emission *at scale* is slow-to-build execution depth (= the feasibility bet) | [assumption] → `H-004` |
| Design corpus — well-designed decks the engine learns from | hard (unique data) | Building / Aspiration | Partly — a *small* corpus is not yet a moat; only a proprietary, hard-to-assemble one survives | [assumption] |
| Founder design taste / credibility in the design community | soft (brand / trust) | Have | Yes — a rebuild copies the software, not the reputation; buys early trust/distribution, not long-run durability | [assumption] |

**Killed as features, not moats** (kept so they aren't re-proposed): *"the AI generation itself"* — any
LLM does it, reproducible in a week · *editability alone* — table-stakes · *nice-looking output alone* —
copyable · *"collapsing the trade-off" as a positioning claim* — copyable aim; only the execution depth
behind it defends.

_Derivative moats (lock-in, network effects, scale economics) are **omitted at concept-viability** — they
need a customer or scale to derive from. Revisit at Strategy (Step 3): potential lock-in via native-format
/ brand-kit integration once customers exist._

**Defensibility summary:** ⚙️ near-term lead moat = **founder credibility** (soft, Have, survives rebuild);
intended durable moat = **rendering reliability at scale + a proprietary corpus** (hard, Building, unproven).
Durability today = **L** — no proven hard moat yet; the whole durable case rests on the riskiest bet
(feasibility), trending to **M** only if the engine's tacit quality and the corpus become hard to replicate.
[assumption]

**Seeded hypotheses:** `H-004` (the editable-and-designed quality is defensible) → hypothesis register.

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. These are carried into `registers/hypotheses.md` (born Step 1)._

| ID <!--c:id--> | Hypothesis <!--c:hypothesis--> | Type <!--c:type--> | From section <!--c:from--> | Confidence <!--c:conf--> |
|----|------------|------|--------------|------------|
| H-001 | The engine can reliably produce native files that are both editable and well-designed at scale | feasibility | concept | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel P1 strongly enough to switch | desirability | segments | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling | desirability | problems | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible (hard to replicate) | viability | value-defensibility | [assumption] |

## To clarify {#to-clarify}
<!-- open -->
_Open items surfaced by the agent for the human to resolve._

- **Concept scope** — ⚙️ sequenced (editable+designed core, audience-aware story as the next bet). Confirm, or choose narrow / full. Widens or tightens the riskiest-assumption surface.
- **Positioning frame** — the job has two halves (design-led vs story-led vs both-as-one). ⚙️ both-as-one as the frame, design-led as the first-demo wedge. A Step-3 call, surfaced now.
- **Lead reach-channel** — genuinely open: community+content, LinkedIn outbound, sales-enablement partnerships, or events. ⚙️ community+content and LinkedIn in parallel. Needed to design a demand test.
- **Demand signal for the lead segment** — no interviews/analytics yet; needed to move `H-002`/`H-003` off `[assumption]`. Source: discovery interviews + analytics search.
- **Feasibility evidence** — no prototype quality eval yet; needed for `H-001`. Source: a prototype slice + design eval.
- **Monetization / willingness to pay** — deferred to Strategy (Step 3) by the founder; noted here so it isn't lost. Do not invent a price.

## Change log

### 2026-08-14 — rebuilt from the founder brief
- **From → To:** prior passport → projected fresh from the Step-1 worklogs (`1-idea/`: concept-formation, jtbd, segmentation, segment-pains, value-definition), each drafted by a `loops-draft` subagent and checked against the acceptance passport.
- **Why:** rebuild `examples/decksmith` with the framework's own methods (subagent draft → orchestrator projection) as a live test of the data loop; capture the concept, job, segments, pains, solution and value/moat as the long-lived source of truth.
- **Trigger:** rebuild-from-brief walkthrough. Sources: `sources/founder-brief.md`.
