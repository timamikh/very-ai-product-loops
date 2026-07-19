---
name: to-document
kind: adapter
mode: document
consumes: [artifacts, registers]
reads_ids: ["<any step artifact + its sections>", hypotheses, risks, metric-tree]
produces: One compiled, human-readable document from selected instance sections (one-pager · full doc · report · status update)
formats: [markdown, html]
opinionated: false
status: draft
version: 0.1.0
updated: 2026-07-18
---

# to-document

Compile **selected instance sections** into **one readable document**: a one-pager brief, a full
strategy doc, a weekly test report, or a status update. Assembles from source — so the document is
regenerated, not hand-maintained alongside the artifacts.

**What it is for.** A stakeholder rarely wants the raw repo; they want *a document*. `to-document`
picks the right sections, orders them into a narrative, resolves the links and IDs into plain
language, and emits a clean file — while the instance stays the single source of truth.

## What it consumes
- A **document profile** — which sections, in what order. Base profiles:
  - **one-pager** — `passport#concept` + `strategy#uvp-cpv` + `strategy#pricing` +
    top `hypotheses` + one headline metric. (For a `brief`, use the `brief` tool's section.)
  - **full-doc** — a whole step artifact (e.g. all of `strategy.md`) cleaned for reading.
  - **report** — the weekly/period test readout: bundles tested → signals → decision (see the
    `to-deck` report mapping for the same content as slides).
  - **status-update** — goals this period + metric movement + open risks + next step.
- The **audience & tone** (internal / external / exec) and the **doc language** (from the instance
  config — the instance may be non-English while the framework is English).

## How to render
1. **Resolve the profile.** Gather the named sections/registers by stable id. Missing section →
   show `— to clarify —` (never invent to fill a gap).
2. **Order into a narrative.** Problem → who → value → how we'll know → status, or the profile's
   order. A document reads top-to-bottom; don't just concatenate tables.
3. **Decode IDs & links for the reader.** In prose, never a bare `H-009`/`M-activation`/`[[…]]` —
   write what it means ("the bet that tech leads stay for the frontier stream"), per CONVENTIONS
   "Talking to the human". IDs may stay in an appendix table for traceability.
4. **Carry confidence honestly.** Keep `[assumption]`/`[validated]` where a claim's status matters
   to the reader; for an external doc, translate them to plain phrasing ("early signal", "confirmed")
   rather than dropping them.
5. **Respect secrets/PII.** Never render tokens, raw captures, or PII into the document (CONVENTIONS
   "Raw data & access"). Reference where data lives, not the secret itself.
6. **Emit + stamp.** Markdown (default) or HTML. Add a header: product · status · date rendered ·
   the source instance revision, so the document says how current it is.

## Output shape

```markdown
# <Product> — One-pager
_Status: pmf · rendered 2026-07-18 from instance @ <rev>_

**The problem.** <from passport#problems, plain language> [validated]
**Who it's for.** <lead segment from passport#segments>
**Our promise.** <strategy#uvp-cpv one-liner> — priced as <strategy#pricing headline>.
**How we'll know it's working.** <headline metric + target> · testing: <top hypothesis, decoded>.

_Appendix: source IDs — segment S-1, H-012 (pricing bet), M-activation._
```

## Anti-patterns
- **Concatenating raw sections.** A document is a narrative, not a dump of tables.
- **Bare IDs in prose.** The reader shouldn't need the repo open to follow a sentence.
- **Editing the doc instead of the source.** Fix the artifact/register and re-render.
- **Leaking secrets/PII / raw captures** into a shareable file.
- **Overstating confidence.** Rendering an `[assumption]` as settled fact for a nicer read.

## Company specialization
A company adapter can wrap `to-document` with a house template, cover page, and section order (e.g.
an internal strategy memo format). The section selection and ID-decoding logic stays here.
