---
name: to-deck
kind: adapter
mode: deck
consumes: [artifacts, registers]
reads_ids: ["<one or more step artifacts + their sections>", hypotheses, metric-tree]
produces: A self-contained, presentable HTML slide deck rendered from the instance — one idea per slide, ready to open and present. Neutral, house-agnostic styling by default; a company adapter re-skins it.
formats: [html]
opinionated: true
status: draft
version: 0.2.0
updated: 2026-07-21
---

# to-deck

Turn the instance into a **presentable slide deck** — one idea per slide, each slide
self-contained — rendered as a **self-contained HTML file a human can open and present**. A
strategy-defense deck, an analysis readout, a sprint-review, a weekly test report, or a full
concept pitch.

**What it is for.** An adapter's whole job is the last hop: from what's structured for an *agent*
to read (artifacts, register IDs, typed links) into what's convenient for a *human* to consume.
For a deck that means an **actual, openable presentation — not a markdown outline**. `to-deck`
maps the instance's structure to a slide sequence, distills each section to one message + its
support, and renders a real deck. Content from source; a real (but neutral) design shipped by
default.

**Opinionated about structure AND about being human-consumable.** It enforces deck *hygiene* (one
message per slide, self-contained slides, no bare jargon) **and** emits a finished, presentable
HTML deck with readable typography, spacing, and navigation. It does **not** impose a *house*
visual identity (brand color, logo, type) — that's a company specialization layered on top.
Base = a real, neutral deck you can already present; company = the brand skin.

## What it consumes
- A **deck profile** — which artifact(s) and the story arc. Base profiles:
  - **strategy-defense** — aspiration → where-to-play → how-to-win/moats → UVP → pricing →
    key bets (hypotheses) → risks → the ask. (from `strategy.md` + `strategic-plan.md`)
  - **analysis-readout** — market size → competitors & their game → substitutes → the opportunity.
    (from `analysis.md`)
  - **sprint-review** — goals → what shipped → metric movement → what we learned → next.
    (from `sprint-plan.md` + `metrics.csv`)
  - **test-report** — per bundle: hypothesis → launch → signal (on the scale) → decision. (mirrors
    the segment-CVP weekly report: hypothesis · launch · signal · quality · conclusion · next step)
  - **concept-pitch** — the full story across the instance: the job/problem → market white space →
    what the product is → market & threat → beachhead / how-to-win → the metric that proves it →
    the bet & the test → status. (from `passport.md` + `analysis.md` + `strategy.md` +
    `strategic-plan.md` + `tactical-plan.md` + `sprint-plan.md`)
- The **audience** and the **doc language** (from the instance config).

## How to render
1. **Resolve the profile → a slide list.** One artifact section usually maps to 1–2 slides; a
   concept-pitch spans several artifacts. Add a title slide (product · status · date) and a closing
   slide (the decision/ask).
2. **One message per slide.** Each slide gets a headline that *states the point* (not a topic label:
   "Retention flattens at 41% — value recurs", not "Retention"), plus 3–5 support points or one
   table/chart. If a slide needs two messages, split it.
3. **Make each slide self-contained.** A reader who lands on one slide out of context should still
   get it — spell out the subject, no "as shown before". (The plain-language / stand-alone test.)
4. **Decode IDs & drop jargon.** Write the meaning; an ID (`H-…`/`M-…`) may appear only as a
   *secondary* label next to its plain-language meaning, never bare and never alone.
5. **Carry the evidence, honestly.** Put the signal/confidence on the slide (a number with its
   source beats an adjective). Mark early vs confirmed; don't present an assumption as proven.
6. **Render a self-contained HTML deck** — the deliverable, not an outline. One file, inline CSS/JS,
   **no external/CDN dependencies** (opens offline as a file, survives a strict CSP). It must have:
   - keyboard **and** click navigation, plus a slide counter / progress indicator;
   - a readable **minimum text size** and generous spacing; one clear type hierarchy;
   - a **neutral, house-agnostic** visual default — real design, not a wireframe, but no brand
     assumptions (a company adapter supplies the brand);
   - each slide fits its frame without the audience scrolling; wide content scrolls inside its own
     container, never the page;
   - `prefers-reduced-motion` respected.
   Keep the one-message-per-slide **outline as an internal step** (that's the messaging discipline),
   then render it to the deck — the outline is scaffolding, not the deliverable.

## Output shape
A single self-contained `.html` file placed with the instance's other deliverables — e.g.
`deliverables/<profile>-deck.html`. It opens in any browser and presents as-is, and is
**regeneratable from source**. Like every adapter output, the deck is a **view of the instance at a
moment** — never hand-edited as if it were the source; change the artifact/register and re-render.

## Anti-patterns
- **Shipping an outline as the deliverable.** A markdown slide list isn't a presentation — a human
  can't present from it. Render it to an openable, styled deck. (The original failure mode: stopping
  halfway, at the agent-readable form.)
- **Topic-label headlines.** "Pricing" says nothing; "Three tiers fence SMB from enterprise" is the point.
- **Two messages on one slide.** Split it — the deck's whole value is one idea at a time.
- **Slides that need the previous slide.** Each must stand alone.
- **Bare IDs / insider jargon** on a slide the audience must read cold.
- **Brand assumptions in the base.** Don't bake a company's colors/logo/type into the base render —
  ship a neutral default; the house skin is the company adapter's job.
- **Dumping the doc onto slides.** A deck distills; if it reads like the document, it isn't a deck.

## Company specialization
A company adapter (e.g. a branded `strategy-defense` or `concept-pitch` deck) wraps `to-deck` to
apply the house visual system — brand color, logo, type scale, minimum text size, grid, calm/strict
layout, forks-as-ballot, etc. — by **overriding the base's neutral design tokens**. The slide
*structure, the messaging discipline, and the fact that the output is a real openable deck* stay
here; only the *skin* lives in the company adapter.

## Change log

### 2026-07-21 — the deliverable is a real HTML deck, not a markdown outline
- **From → To:** `formats: [markdown-slides]` → `[html]`. The output is now a **self-contained,
  presentable HTML deck** (readable, navigable, neutral-but-real design), with the markdown outline
  demoted to an internal step. Reframed the base/company boundary from "structure vs. any visuals"
  to "a real neutral deck (base) vs. the brand skin (company)". Added the **concept-pitch** profile
  (spans the whole instance).
- **Why:** an adapter's purpose is to turn agent-readable structure into a **human-consumable**
  deliverable; a markdown deck isn't something a human presents, so the base stopped halfway and
  contradicted the adapters README ("a presentation a human actually shares").
- **Trigger:** decksmith live run — a real deck was needed at the Step-6 wrap and the adapter only
  emitted an outline.

### 2026-07-18 — created
- **From → To:** — → `to-deck` base adapter (profiles + slide-hygiene rules; emitted a markdown outline).
- **Trigger:** base-converters pass, 2026-07-18.
