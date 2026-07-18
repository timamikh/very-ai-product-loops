---
name: to-deck
kind: adapter
mode: deck
consumes: [artifacts, registers]
reads_ids: ["<a step artifact + its sections>", hypotheses, metric-tree]
produces: A slide-deck outline (one idea per slide) from one artifact — as markdown slides, ready to style
formats: [markdown-slides]
opinionated: true
status: draft
version: 0.1.0
updated: 2026-07-18
---

# to-deck

Turn **one artifact** into a **presentation outline** — one idea per slide, each slide
self-contained — as markdown slides ready to be styled. A strategy-defense deck, an analysis
readout, a sprint-review, or a weekly test report.

**What it is for.** Presenting the work needs a *deck*, not the doc. `to-deck` maps an artifact's
structure to a slide sequence, distills each section to a single message + its support, and leaves
styling to the renderer (or a company adapter). Content from source; design on top.

**This adapter is opinionated about structure, not visuals.** It enforces deck *hygiene* (one
message per slide, self-contained slides, no bare jargon); it does **not** impose a house visual
style — that's a company specialization.

## What it consumes
- A **deck profile** — which artifact and the story arc. Base profiles:
  - **strategy-defense** — aspiration → where-to-play → how-to-win/moats → UVP → pricing →
    key bets (hypotheses) → risks → the ask. (from `strategy.md` + `strategic-plan.md`)
  - **analysis-readout** — market size → competitors & their game → substitutes → the opportunity.
  - **sprint-review** — goals → what shipped → metric movement → what we learned → next.
  - **test-report** — per bundle: hypothesis → launch → signal (on the scale) → decision. (mirrors
    the segment-CVP weekly report: gipoteza · zapusk · signal · kachestvo · vyvod · next step)
- The **audience** and the **doc language** (from the instance config).

## How to render
1. **Resolve the profile → a slide list.** One artifact section usually maps to 1–2 slides. Add a
   title slide (product · status · date) and a closing slide (the decision/ask).
2. **One message per slide.** Each slide gets a headline that *states the point* (not a topic label:
   "Retention flattens at 41% — value recurs", not "Retention"), plus 3–5 support points or one
   table/chart. If a slide needs two messages, split it.
3. **Make each slide self-contained.** A reader who lands on one slide out of context should still
   get it — spell out the subject, no "as shown before". (The plain-language / stand-alone test.)
4. **Decode IDs & drop jargon.** No bare `H-…`/`M-…` on a slide; write the meaning. Prefer plain
   words over insider terms; if a term is unavoidable, gloss it on the slide.
5. **Carry the evidence, honestly.** Put the signal/confidence on the slide (a number with its
   source beats an adjective). Mark early vs confirmed; don't present an assumption as proven.
6. **Emit markdown slides.** Slides separated by `---`; headline as `#`, support as bullets/table.
   Leave visual styling (fonts, colors, min text size, layout) to the renderer / company adapter.

## Output shape

```markdown
# <Product> — Strategy
Status: pmf · 2026-07-18

---

# We win by owning the frontier stream, not the cheapest tokens
- Where we play: teams already using LLMs via workarounds
- How we win: fastest access to new models + trust + lock-in
- Moat: distribution + community (servers are the infra's moat, not ours)

---

# The bet we're testing this quarter
- If we ship model-day-one access, tech leads stay (retention ↑)
- Signal to watch: 90-day retention of the frontier cohort ≥ 55%
- Early read: cohort curve flattening at 41% overall  [early]
```

## Anti-patterns
- **Topic-label headlines.** "Pricing" says nothing; "Three tiers fence SMB from enterprise" is the point.
- **Two messages on one slide.** Split it — the deck's whole value is one idea at a time.
- **Slides that need the previous slide.** Each must stand alone.
- **Bare IDs / insider jargon** on a slide the audience must read cold.
- **Design in the outline.** Don't hard-code fonts/colors here; that's the renderer's/company's job.
- **Dumping the doc onto slides.** A deck distills; if it reads like the document, it isn't a deck.

## Company specialization
A company adapter (e.g. a branded `strategy-defense` deck) wraps `to-deck` to apply the house visual
system — grid, type scale, minimum text size, color, calm/strict layout, forks-as-ballot, etc. The
slide *structure and messaging discipline* stay here; the *look* lives in the company adapter.
