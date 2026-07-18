---
node_type: artifact
artifact: passport
product: Decksmith (fictional sample)
step: 1
status_stage: concept-viability
owner: sample
updated: 2026-07-16
version: 0.1.0
---

# Product Passport — Decksmith (fictional sample)

> Status: `concept-viability` · Owner: sample · Last review: 2026-07-16
> Fictional example — every value is illustrative. Most claims are `[assumption]` by design:
> at concept stage there is no product data, so the passport is mostly a set of bets to test.

## Concept {#concept}
<!-- tool: concept-formation -->

An AI presentation generator that outputs **native, fully-editable** `.pptx`/`.key` (real
shapes, text, layouts — editable like your own) that also **look designed**, not templated.
[sourced: PO decision 2026-07-16]

**The shift:** today's AI slide tools force a trade-off — *pretty but locked* (image/template
exports you can't edit) **or** *editable but ugly*. Decksmith removes the trade-off:
editable **and** well-designed. [assumption]

**Riskiest assumption:** the engine can *reliably* produce native files that are both genuinely
editable and genuinely well-designed, at scale. This is the core bet. [assumption] → `H-001`

## Segments {#segments}
<!-- tool: segmentation -->

**Cut basis:** by *job + frequency + stakes* — people who make client-facing decks often and
are judged on how they look. This predicts different needs better than demographics. [assumption]

| Priority | Segment | How it's cut | Why it matters | Where to reach them | Confidence |
|----------|---------|--------------|----------------|---------------------|------------|
| **1 (lead)** | Salespeople & marketers | Make client/brand-facing decks constantly; judged on look + on-brand | Highest frequency × stakes; company often pays | — to clarify — | [assumption] |
| 2 | Startup founders | Pitch decks, high stakes, low frequency | Strong pain but occasional use | — to clarify — | [assumption] |
| 2 | Consultants | Client deliverables, frequent | Volume + willingness to pay | — to clarify — | [assumption] |
| 2 | Designers | Want a fast first draft to refine | Adjacent buyer; may resist "AI design" | — to clarify — | [assumption] |

**Lead segment:** ⚙️ **Salespeople & marketers** — highest frequency × stakes, and a budget
holder. Everything downstream leads with this segment. [sourced: PO decision 2026-07-16]

## Problems {#problems}
<!-- tool: segment-pains -->
_For the lead segment (salespeople & marketers)._

| Rank | Problem | Severity | Frequency | Confidence |
|------|---------|----------|-----------|------------|
| 1 | AI decks look templated/generic/ugly → I redo them by hand anyway | H | H | [assumption] |
| 2 | Wrong structure & framing — the deck doesn't tell the story right | H | M–H | [assumption] |
| — (baseline) | Output is locked/images — can't edit in PowerPoint/Keynote | H | H | [assumption] |

> Note: editability is treated as a **baseline requirement** (it's in the concept), while
> *look* (P1) and *structure/framing* (P2) are the differentiating pains we lead on.

## Solution {#solution}
<!-- tool: concept-formation -->

| Problem | How Decksmith solves it | Confidence |
|---------|-------------------------|------------|
| P1 — looks ugly | Design-quality generation: native slides that read as designed, not templated | [assumption] |
| P2 — wrong structure | Structures and sequences the *narrative*, not just styles slides | [assumption] |
| Baseline — locked | Emits native, editable `.pptx`/`.key` (real objects, not images) | [assumption] |

## Value & Defensibility {#value-defensibility}
<!-- tool: value-definition -->

**Core value (post-AI):** a generic "make slides with AI" wrapper would *not* have — a
rendering/design engine that keeps files editable *and* beautiful, plus the design taste to
back it. [assumption]

| Priority | Moat | Layer | Have / Building / Aspiration | Survives an LLM rebuild? | Confidence |
|----------|------|-------|------------------------------|--------------------------|------------|
| A (lead) | Unique algorithms/IP — the "editable + beautiful" engine | hard | Aspiration | Yes — quality is hard to replicate | [assumption] → `H-004` |
| D | Brand / design expertise — recognized design taste | soft | Aspiration | Partly | [assumption] |
| B | Unique data — corpus of high-quality designed decks | hard | Aspiration | Yes — supports A | [assumption] |

**Derivative moats:** none claimed at concept stage (no customers/scale yet). Revisit at
Strategy — potential lock-in via native-format/workspace integration once customers exist.

**Defensibility summary:** ⚙️ lead moat = the engine (A), fed by a design corpus (B), fronted
by design brand (D). Durability = M–H *if* engine quality proves out. Why it holds = the app is
cloneable, the sustained editable-and-beautiful quality is not.

## Seeded hypotheses {#hypotheses}

| ID | Hypothesis | Type | From | Confidence |
|----|------------|------|------|------------|
| H-001 | The engine can reliably produce native files that are both editable and well-designed at scale | feasibility | concept | [assumption] |
| H-002 | Salespeople & marketers are a reachable segment who feel P1 strongly enough to switch | desirability | segments/problems | [assumption] |
| H-003 | "Wrong structure/framing" (P2) is a top pain worth solving, not just styling | desirability | problems | [assumption] |
| H-004 | The engine's editable-and-beautiful quality is defensible (hard to replicate) | viability/moat | value | [assumption] |

## To clarify {#to-clarify}

- Where to reach the lead segment (channel/community) — needed for a demand test.
- What counts as a passing "some demand" signal for `concept-viability`.
- First format focus — `.pptx`, `.key`, or both at once (scope).
- Monetization / willingness to pay — deferred to Strategy (Step 3), noted here so it isn't lost.

## Change log

### 2026-07-16 — created
- **From → To:** — → initial concept passport (fictional sample)
- **Why:** golden-path walkthrough of Step 1 at status `concept-viability`
- **Trigger:** framework dry-run
