---
node_type: artifact
artifact: passport
product: Decksmith (fictional sample)
step: 1
status_stage: concept-viability
owner: sample
updated: 2026-07-20
version: 0.2.0
---

# Product Passport — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-07-20
> Fictional example — every value is illustrative. Most claims are `[assumption]` by design:
> at concept stage there is no product data, so the passport is mostly a set of bets to test.
> Registers: `registers/hypotheses.md` (seeded here) · risks/metrics born at Steps 2/4.

## Concept {#concept}
<!-- tool: concept-formation -->

Decksmith is an **AI presentation generator** that outputs **native, fully-editable** `.pptx`/`.key`
(real shapes, text, layouts — editable like your own) that also **look designed**, not templated.
[sourced: founder brief 2026-07-16]

**The shift:** today AI slide tools force a trade-off — *pretty but locked* (image/template exports
you can't edit) **or** *editable but ugly* (plain text in default styling); with Decksmith the deck
is editable **and** well-designed, so you don't regenerate it by hand. [assumption]

**Riskiest assumption:** the engine can *reliably* produce native files that are both genuinely
editable and genuinely well-designed, at scale. This is the core bet. [assumption] → `H-001`

## Segments {#segments}
<!-- tool: segmentation -->

**Cut basis:** by *job + frequency + stakes* — people who make client-facing decks often and are
judged on how those decks look. This predicts different needs far better than demographics. [assumption]

| Priority | Segment | How it's cut | Why it matters | Where to reach them | Confidence |
|----------|---------|--------------|----------------|---------------------|------------|
| **1 (lead)** | Salespeople & marketers | Make client/brand-facing decks constantly; judged on look + on-brand | Highest frequency × stakes; company usually holds the budget | ⚙️ sales/marketing communities (revenue-ops & sales-enablement Slacks, LinkedIn sales circles) | [assumption] |
| 2 | Startup founders | Pitch decks — high stakes, low frequency | Strong pain but occasional use | ⚙️ accelerators, founder communities (Indie Hackers–style) | [assumption] |
| 2 | Consultants | Client deliverables, frequent | Volume + willingness to pay | ⚙️ consulting networks, LinkedIn, boutique-firm channels | [assumption] |
| 2 | Designers | Want a fast first draft to refine | Adjacent buyer; may resist "AI design" | ⚙️ design communities (Dribbble/Behance, design Slacks) | [assumption] |

**Lead segment:** ⚙️ **Salespeople & marketers** — highest frequency × stakes, and a budget holder.
Everything downstream leads with this segment; lower tiers are kept, not dropped. [sourced: founder brief 2026-07-16]

**Seeded hypotheses:** `H-002` (this segment is reachable and feels P1 strongly enough to switch) → hypothesis register.

## Problems {#problems}
<!-- tool: segment-pains -->
_For the lead segment (salespeople & marketers). Job-to-be-done: produce a client-facing deck that
looks credible and tells the right story — fast, without redoing it by hand._

| Rank | Problem (pain in the job) | Severity | Frequency | Class | Confidence |
|------|---------------------------|----------|-----------|-------|------------|
| 1 | AI decks look templated/generic/ugly → I redo them by hand anyway | H | H | differentiator | [assumption] |
| 2 | Wrong structure & framing — the deck doesn't tell the story right for the audience | H | M–H | differentiator | [assumption] |
| — | Output is locked/images — can't edit in PowerPoint/Keynote | H | H | table-stakes | [assumption] |

> Editability is a **table-stakes** baseline (it's in the concept); *look* (P1) and
> *structure/framing* (P2) are the differentiating pains Decksmith competes on.

**Seeded hypotheses:** `H-002` (P1 matters enough to switch) · `H-003` (P2 is a top pain, not just styling) → hypothesis register.

## Solution {#solution}
<!-- tool: concept-formation -->

| Problem | How Decksmith solves it | Confidence |
|---------|-------------------------|------------|
| P1 — looks templated/ugly | Design-quality generation: native slides that read as *designed*, not templated | [assumption] |
| P2 — wrong structure | Structures and sequences the *narrative* for the audience, not just styles slides | [assumption] |
| Baseline — locked/images | Emits native, editable `.pptx`/`.key` (real objects, not images) | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition -->
_Lens: 7 Powers → base/derivative moats, post-AI (software isn't the moat, position is). Swappable._

**Core value (post-AI):** what a generic "make slides with AI" wrapper would *not* have — a
rendering/design engine that keeps files editable *and* beautiful, plus the design taste to back it.
[assumption]

**Base moats**

| Moat | Layer | Have / Building / Aspiration | Survives an LLM rebuild? | Confidence |
|------|-------|------------------------------|--------------------------|------------|
| Unique algorithms / IP — the "editable + beautiful" engine | hard | Aspiration | Yes — sustained quality is hard to replicate | [assumption] → `H-004` |
| Unique data — corpus of high-quality designed decks the engine learns from | hard | Aspiration | Yes — feeds and compounds the engine | [assumption] |
| Brand / design expertise — recognized design taste | soft | Aspiration | Partly | [assumption] |

_Derivative moats (lock-in, network effects, scale economics) are **omitted at concept-viability** —
they need a customer or scale to derive from. Revisit at Strategy (Step 3): potential lock-in via
native-format/workspace integration once customers exist._

**Defensibility summary:** ⚙️ lead moat = the engine (unique IP), fed by a design corpus (unique
data), fronted by design brand; durability = **M–H if engine quality proves out**; why it holds =
the app is cloneable, the sustained *editable-and-beautiful* quality is not. [assumption]

**Seeded hypotheses:** `H-004` (the quality gap is defensible) → hypothesis register.

## Seeded hypotheses {#hypotheses}
_Everything above starts as an assumption. These are carried into `registers/hypotheses.md`._

| ID | Hypothesis | Type | From section | Confidence |
|----|------------|------|--------------|------------|
| H-001 | The engine can reliably produce native files that are both editable and well-designed at scale | feasibility | concept | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel P1 strongly enough to switch | desirability | segments/problems | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling | desirability | problems | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible (hard to replicate) | viability/moat | value | [assumption] |

## To clarify {#to-clarify}

- **Which specific community** to reach the lead segment through (channels above are ⚙️ proposals) — needed to design a demand test.
- **What counts as a passing "some demand" signal** for `concept-viability` (the bar to clear).
- **First format focus** — `.pptx`, `.key`, or both at once (scope decision affecting feasibility).
- **Monetization / willingness to pay** — deferred to Strategy (Step 3); noted here so it isn't lost.

## Change log

### 2026-07-20 — rebuilt from scratch through the Step-1 tools (example run)
- **From → To:** v0.1.0 passport → v0.2.0, regenerated method-by-method (`concept-formation` →
  `segmentation` → `segment-pains` → `value-definition`) and wired to the new instance registers.
  Aligned to current tool template-fragments: added the `Class` column (differentiator/table-stakes)
  to `#problems`, filled `Where to reach them` with ⚙️ channel proposals in `#segments` (was
  `— to clarify —`), and **omitted** the derivative-moats table at `concept-viability` (kept a
  one-line deferral to Step 3) per the `value-definition` status-suppression rule.
- **Why:** full-pipeline example run — Step 1 rebuilt from scratch to test the tools and seed the
  registers/sources scaffolding the rest of the run builds on.
- **Trigger:** example run, 2026-07-20.

### 2026-07-16 — created
- **From → To:** — → initial concept passport (fictional sample)
- **Why:** golden-path walkthrough of Step 1 at status `concept-viability`
- **Trigger:** framework dry-run
