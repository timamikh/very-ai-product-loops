---
node_type: card
kind: output
name: to-document
output_kind: rendered
prerequisites: []
reads: [section:*, register:hypotheses, register:risks, register:metric-tree]
writes: [file:export-files/*]
surfaces: [file:export-files/*]
opinionated: false
formats: [docx, markdown, html]
status: draft
version: 0.2.0
updated: 2026-07-21
---
# to-document

Compile **selected instance sections** into **one presentable document a stakeholder opens** — a
one-pager brief, a full strategy doc, a weekly test report, or a status update. Default output is a
**formatted `.docx`** (headings, spacing, a summary table, a provenance footer); markdown/HTML on
request. Assembles from source — so the document is regenerated, not hand-maintained alongside the
artifacts.

**What it is for.** A stakeholder rarely wants the raw repo; they want *a document* they can open,
read, and forward. `to-document` picks the right sections, orders them into a narrative, resolves
the links and IDs into plain language, and emits a **finished, formatted file** — not a markdown
dump the reader has to render themselves. The instance stays the single source of truth.

**Opinionated about being human-consumable, flexible about section selection.** It ships a clean,
readable document with real typography and a summary table by default; it does **not** impose a
company's house identity (cover page, brand color, letterhead) — that's a company specialization
layered on top. Base = a real, neutral document; company = the house template.

## What it consumes
- A **document profile** — which sections, in what order. Base profiles:
  - **one-pager** — `concept#idea` + `concept#problems` + `strategy#uvp-cpv` +
    `strategy#pricing` + top `hypotheses` + one headline metric. (For a `brief`, render the brief file `product-loops/briefs/<slug>.md`.)
  - **full-doc** — a whole step artifact (e.g. all of `3-strategy.md`) cleaned for reading.
  - **report** — the weekly/period test readout: bundles tested → signals → decision (mirrors the
    `to-deck` report mapping, as a document).
  - **status-update** — goals this period + metric movement + open risks + next step.
- The **audience & tone** (internal / external / exec) and the **doc language** (from the instance
  config — the instance may be non-English while the framework is English).

## How to render
1. **Resolve the profile.** Gather the named sections/registers by stable id. Missing section →
   show `— to clarify —` (never invent to fill a gap).
2. **Order into a narrative.** Problem → who → value → how we'll know → status, or the profile's
   order. A document reads top-to-bottom; don't just concatenate tables.
3. **Decode IDs & links for the reader.** In prose, never a bare `H-009`/`M-activation`/section link —
   write what it means, per CONVENTIONS "Talking to the human". IDs may stay in an appendix/summary
   table for traceability.
4. **Carry confidence honestly.** Keep `[assumption]`/`[validated]` where a claim's status matters;
   for an external doc, translate them to plain phrasing ("early signal", "confirmed") rather than
   dropping them.
5. **Respect secrets/PII.** Never render tokens, raw captures, or PII into the document. Reference
   where data lives, not the secret itself.
6. **Render a formatted document** — the deliverable, not a raw outline. Default **`.docx`**: a real,
   styled file with a title block, section headings, readable body type, at least one summary table,
   and a footer stamping *product · status · date rendered · source instance*. Requirements:
   - a clear type hierarchy (title / section heading / body) and consistent spacing;
   - tabular content rendered as an actual table (header row, light shading), not ASCII;
   - a **neutral, house-agnostic** style — real formatting, no brand assumptions;
   - markdown or HTML instead **only when asked** (e.g. for a PR or a wiki).
   Keep the section-selection + narrative ordering as the reasoning step, then render to the file.

## The renderer (shipped, generic)
Because a `.docx` needs a library, this adapter ships a **generic, instance-agnostic** renderer here:
[`render.py`](render.py) — `markdown content → styled, house-neutral .docx` (requires `python-docx`).
It holds **no product data** (so it travels with the framework and never pollutes the base): the
agent authors the content markdown per this card (title / sections / bullets / a table / footer),
then the renderer styles it. `python3 render.py CONTENT.md --out <deliverables>/<profile>.docx`.
(HTML/CSV/markdown adapters need no shipped code — the agent authors those directly.)

## Output shape
A single formatted file placed with the instance's other deliverables — e.g.
`deliverables/<profile>.docx`. It opens in Word/Pages/Docs and is **regeneratable from source**.
The content model (before formatting) reads like:

```markdown
# <Product> — One-pager
_Status: pmf · rendered 2026-07-18 from instance @ <rev>_

**The problem.** <from concept#problems, plain language> [validated]
**Who it's for.** <lead segment from concept#segments>
**Our promise.** <strategy#uvp-cpv one-liner> — priced as <strategy#pricing headline>.
**How we'll know it's working.** <headline metric + target> · testing: <top hypothesis, decoded>.

_Summary table: key hypotheses / risks with status (for traceability)._
```

Like every adapter output, the document is a **view of the instance at a moment** — never hand-edited
as the source; change the artifact/register and re-render.

## Anti-patterns
- **Shipping a raw markdown dump** when a stakeholder asked for a document — render the formatted file.
- **Concatenating raw sections.** A document is a narrative, not a dump of tables.
- **Bare IDs in prose.** The reader shouldn't need the repo open to follow a sentence.
- **Editing the doc instead of the source.** Fix the artifact/register and re-render.
- **Leaking secrets/PII / raw captures** into a shareable file.
- **Overstating confidence.** Rendering an `[assumption]` as settled fact for a nicer read.
- **Brand assumptions in the base.** Cover pages, logos, letterhead belong in the company adapter.

## Company specialization
A company adapter wraps `to-document` with a house template — cover page, brand color, letterhead,
fixed section order — by overriding the base's neutral style. The section selection, ID-decoding, and
the fact that the output is a real formatted file stay here; only the *skin* lives in the company adapter.
