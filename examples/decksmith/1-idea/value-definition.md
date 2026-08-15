---
node_type: worklog
method: value-definition
produces: value-defensibility
step: 1-idea
status: draft
updated: 2026-08-14
---

# Worklog — Value & Definition (Decksmith)

> Source of truth for the `{#value-defensibility}` projection. Everything here is a **draft** (⚙️),
> tagged. The orchestrator mints any register id; this worklog only **describes** the beliefs in words.
> Lens declared: **7 Powers → base/derivative moats**, read through the **post-AI test** — a value that
> does not survive an LLM rebuild is a feature, not a moat. This is an opinionated lens, not the only one.

## Inputs I was given (not re-derived)

- **Concept** — native-editable **AND** designed AI decks; the shift is collapsing the
  "pretty-but-locked vs editable-but-ugly" trade-off. [sourced: founder brief]
- **Riskiest bet** — feasibility: can the engine *reliably* emit editable-and-designed files **at scale**.
  [sourced: founder brief]
- **Honest have/can-build inventory** (founder-sourced, tags kept):
  1. Prototype rendering pipeline that emits **native slide objects** (not images) + layout/spacing
     rules; **quality-at-scale unproven**. [assumption — founder]
  2. Access to a **small corpus** of well-designed decks to learn patterns from, **to be assembled**.
     [assumption — founder]
  3. Founder's **design taste / credibility** in the design community. [assumption — founder]
- **Pricing** — deferred to Step 3; not invented here. [sourced: founder brief]

## Prerequisite check

| Prerequisite | Status | Note |
|---|---|---|
| Concept | Have | given by brief [sourced: founder brief] |
| Segments | Have (loose) | founder's early bet = salespeople & marketers; full segmentation out of scope [sourced: founder brief] |
| What we have / can build | Have | the honest inventory above [assumption — founder] |
| Competitor context | Not required at Step 1 | a Step-3 prerequisite; deferred with derivatives |

All Step-1 prerequisites present. Nothing was guessed.

## Step 1 — Core value (post-AI)

The question the post-AI test forces: **what would a generic "make slides with an LLM" wrapper NOT
have?** A wrapper can already generate slide *content* with any model — that part is a commodity.

⚙️ **Core value:** the ability to turn LLM content into output that is **simultaneously native-editable
AND genuinely designed, reliably and at scale** — i.e. the *collapse of the trade-off itself*, delivered
by (a) a deterministic native-object rendering layer and (b) encoded design judgment (corpus + taste)
that makes output look designed rather than templated. [assumption]

Note: the *positioning* (collapse the trade-off) is the value **statement**; it is not itself a moat —
anyone can aim at it. What could be defensible is the **execution depth, data and trust** that make the
collapse hard to replicate. Those are tested as moats below. [assumption]

## Step 2 — Base moats, each against the post-AI rebuild test

Working notes per candidate (the table for the projection follows):

- **Native-object rendering pipeline** — classify as **hard (unique algorithm / IP-leaning)** *if* the
  reliable-at-scale emission proves genuinely tacit/hard; today it reads as product-complexity/expertise.
  Status **Building** (prototype exists, quality-at-scale unproven). Rebuild verdict: **Partly** — the
  *approach* is copyable with an LLM, but reliable native-editable-and-designed emission **at scale** is an
  engineering problem a prompt does not solve; the tacit execution depth is slow to build. Its defensibility
  is exactly the riskiest bet (feasibility), so confidence is low. [assumption]
- **Design corpus** — classify as **hard (unique data)** *if* it becomes proprietary and hard to assemble.
  Status **Building/Aspiration** (small, to be assembled). Rebuild verdict: **Partly** — generic design
  knowledge is broadly available and a *small* corpus is not yet a moat; only a corpus grown into something
  proprietary and hard to reproduce would survive a rebuild. [assumption]
- **Founder design taste / credibility** — classify as **soft (brand/trust + expertise)**. Status **Have**.
  Rebuild verdict: **Yes** — an LLM rebuild copies the software, not the founder's reputation or taste; this
  is the classic soft moat that survives a rebuild. Caveat: it is a *personal* asset — hard to institutionalize
  and scale — so it buys early distribution/trust more than long-run durability. [assumption]

### Killed candidates (the step's most valuable output — kept so they are not re-proposed)

- **"The AI generation itself" / "we use an LLM to make slides."** KILLED. Fails the rebuild test outright:
  any LLM does it; a hundred wrappers already exist. Reproducible by anyone with the same model in a week.
  (Brief requires this be killed on the record.) [assumption]
- **"Editability" alone.** KILLED. Table-stakes in the target crowd, and any wrapper can emit editable
  (even if ugly) output. A necessary feature, not a moat. [sourced: founder brief — "editability is table-stakes"]
- **"Nice-looking output" / UX polish alone.** KILLED. A template library or prompt-tuning is copyable;
  the *look* by itself is a feature, not a position. [assumption]
- **"Collapsing the trade-off" as a positioning claim.** KILLED **as a moat** (kept as the value statement).
  The aim is copyable; only the execution depth / data / trust behind it can defend it. [assumption]

## Step 3 — Derivative moats

**Omitted at `concept-viability`** (status-driven suppression): there is no customer or scale yet to derive
from. **One deferral line for the projection:** *deferred to Step 3 — derivatives (lock-in, network effects,
economies of scale) need a customer/scale that do not exist at concept stage; revisit with competitor context.*

## Step 4 — Defensibility & confidence

⚙️ **Defensibility summary:**
- **Near-term lead moat = founder design taste/credibility** (soft, Have, survives rebuild) — the only moat
  Decksmith actually *has* today; it buys early trust/distribution, not long-run durability.
- **Intended durable moat = native-rendering reliability at scale + a proprietary design corpus** (hard,
  Building) — this is where the real defense must come from, and it is unproven.
- **Durability today = L.** No *proven* hard moat exists at concept stage. Honest finding: Decksmith's whole
  durable-defensibility case rests on execution that is **exactly the riskiest bet (feasibility)**. Durability
  trends to **M** only if the engine's tacit reliability and the corpus become genuinely hard to replicate.
- **Why it could hold:** a generic wrapper cannot cheaply produce native-editable **and** designed files at
  scale; if that gap is real and widens with a proprietary corpus, position (execution depth + data + trust),
  not the software, becomes the moat. [assumption]

## Step 5 — Moat beliefs to mint (described in words — orchestrator assigns ids)

The core moat intuition, framed as testable hypotheses. **None carry an id here.**

1. **(Primary — ties to the feasibility risk)** Reliable emission of native-editable **and** designed slide
   files **at scale** is hard enough to build that a generic LLM wrapper cannot cheaply replicate it — i.e.
   execution depth (pipeline reliability + proprietary corpus) is a durable moat, not just a feature. [assumption]
2. A proprietary design corpus, once assembled at sufficient scale, becomes **unique data** others can't
   cheaply assemble. [assumption]
3. Founder design-community **credibility** converts into cheaper early distribution/trust. [assumption]

The orchestrator should mint at least belief (1) as the moat hypothesis for `{#value-defensibility}`; (2)
and (3) are secondary and may be folded or deferred at its discretion.

## Projection map (what the fragment's slots draw from)

- **Core value bullet** ← Step 1.
- **Base-moat table** ← Step 2 three candidates (moat / layer / Have-Building-Aspiration / rebuild verdict / confidence).
- **Derivative table** ← omitted; one deferral line from Step 3.
- **Defensibility summary** ← Step 4.
- **Seeded hypotheses** ← Step 5 (ids to be minted).
- **Rejected-as-features table** ← Step 2 "Killed candidates".

## `— to clarify —`

- Is the rendering pipeline genuinely **hard (algorithm/IP)** or better classed **soft (product complexity /
  expertise)**? Turns on whether reliable-at-scale emission proves tacit — **unproven** (the feasibility bet).
  Drafted as hard-leaning with low confidence. — to clarify —
- Target corpus **scale/proprietary-ness** needed before it counts as unique data — not specified. — to clarify —

## Change log

- 2026-08-14 — draft created (value-definition applied to Decksmith concept). [assumption]
