---
node_type: worklog
tool: value-definition-concept
step: 1
title: "value-definition-concept — the working"
updated: 2026-08-16
version: 0.1.0
---

# value-definition-concept — the working

_Source of truth for `1-concept.md#value-defensibility`; that section is the projection of this file._

## Inputs dispatched from sources {#intake}

_Routed here by `source-intake` from `../sources/`. Each row is a fact the method works from; the
analysis and conclusions are worked below and projected into the artifact section — never here._

| From source | What it gives this method | Value / claim | Captured | Confidence |
|-------------|---------------------------|---------------|----------|------------|
| `../sources/originals/founder-brief.md` | A candidate moat | The founder's own **design taste / credibility** in the design community. | 2026-07-16 | [assumption] |
| `../sources/originals/founder-brief.md` | A candidate accumulating asset | A corpus of well-designed decks the engine learns design patterns from (to be assembled) — could compound as a data/design advantage. | 2026-07-16 | [assumption] |
| `../sources/originals/founder-brief.md` | The value the moat must protect | A native, fully-editable-**and**-designed engine — the thing today's tools can't do (they force editable-XOR-designed). | 2026-07-16 | [sourced: founder brief] |

## The working

_Lens: 7 Powers → base moats, each put through the **post-AI rebuild test** (would it survive
someone rebuilding the app with an LLM tomorrow?). Derivatives deferred to Step 3. This is an
opinionated method — the post-AI view is stated, not presented as the only one._

### 1 · Core value (post-AI)

What a clone rebuilt with an LLM tomorrow would **not** have is **not the generator** — the generator
is a commodity. It is the ability to reliably hit *editable-and-designed* quality on arbitrary
content, which rests on **curated design taste encoded as data + rules**, plus the **credibility to
be trusted on design**. The software is copyable; the taste, the labelled corpus, and the reputation
are slower.

### 2 · Base moats, post-AI test

| Moat | Layer | Have / Building / Aspiration | Survives an LLM rebuild? | Confidence |
|------|-------|------------------------------|--------------------------|------------|
| **Curated design corpus + learned design patterns** (taste-labelled examples the engine learns layout/spacing/type from) | hard — unique data | Building (corpus "to be assembled") | **Partly** — a rival can assemble a corpus, but taste-curation + labelling is slow and compounding | [assumption] |
| **Founder design taste / credibility in the design community** | soft — brand/trust + expertise | Have (partial) | **Yes** — a clone gets the software, not the reputation or the taste that curates the corpus | [assumption] |
| **Design-quality-at-scale engineering** (the hard part of reliably native+designed on any content) | soft — processes + product depth | Building | **Partly** — an execution lead that erodes as others catch up | [assumption] |

### 3 · Candidates killed by the rebuild test (kept — the step's most valuable output)

| Candidate value | Why it fails the rebuild test |
|-----------------|-------------------------------|
| "Native `.pptx`/`.key` export" | reproducible with the same libraries + model in weeks — a feature, not a moat (it's table-stakes for the category we're defining) |
| "Great UX / clean product" | copyable; no barrier |
| "Uses a frontier LLM for generation" | the model is a commodity input available to everyone |
| "First to combine editable + designed" | first-mover is not a moat unless it compounds into data/brand/scale — which is what the three moats above are betting on |

### 4 · Lead moat & durability

**Lead moat ⚙️: the design corpus + founder taste/credibility** (unique data × brand/expertise) —
the *combination* is the least copyable, and the corpus compounds with use. **Durability: M** at
concept stage (nothing is validated; the corpus doesn't exist yet). **Why it could hold:** taste +
labelled data + reputation reinforce each other, and none is reproduced by cloning the app.

### 5 · Derivatives — derived at Step 3 (`value-definition-strategy` revisit)

_Added by the Step-3 revisit (same section, updated in place — one moat story). Now that a chosen
arena and a strategy exist, the derivatives deferred at concept stage can be named, each with its
**dependency** (a derivative with no dependency is an aspiration — tagged so)._

**Base moats re-tested in the chosen arena (S1, vs the known competitors):** the taste corpus +
founder credibility **still hold** the post-AI rebuild test. But the **design-quality-at-scale
engineering** re-reads more sharply as a **native-export *wedge*, not a durable moat** — it erodes as
OOXML/`.pptx` generation commoditises. Rated honestly as a timing advantage, not a possession.

**Derivatives now reachable (with dependencies):**

| Derivative moat | Type | Derives from | Dependency (named) | Confidence |
|-----------------|------|--------------|--------------------|------------|
| Edit-behaviour data loop | hard — unique data | usage + instrumentation | edit-capture ships **and** usage reaches scale | [assumption] |
| Brand-kit lock-in / switching cost | soft — switching cost | an embedded customer | brand-kit + deck-library storage ships **and** a customer embeds their brand system | [assumption] |

**Moat trajectory (order of construction):** enter on **taste corpus + founder distribution**
(exist now) → build the **edit-behaviour data loop** (needs scale) → build **brand-kit lock-in**
(needs product + customer embed). The export wedge buys the time to do this; it must be **converted
before it erodes** — carried as bet `H-012` / risk `R-007`.

### 6 · Seeded hypothesis (→ register)

- **H-007 (viability, tags: moat):** the design corpus + founder taste is a real moat — the
  editable-and-designed quality edge is hard to replicate cheaply, so an early lead compounds rather
  than being copied away.

## Change log

### 2026-08-19 — sources layout migrated
- **From → To:** `../sources/founder-brief.md` → `../sources/originals/founder-brief.md`
- **Why:** reorganized sources layout into originals/ · snapshots/ · access/ subfolders
- **Trigger:** framework 0.10 boundary layer

### 2026-08-16 — Step-3 strategy revisit (`value-definition-strategy`)
- **From → To:** §5 "derivatives — deferred" → derivatives **derived** (edit-behaviour data loop +
  brand-kit lock-in, each with a named dependency), base moats re-tested in the chosen arena
  (export-engineering re-read as an eroding *wedge*, not a moat), moat trajectory stated
- **Why:** the Step-3 revisit — a chosen arena and strategy make the derivatives nameable; feeds
  `#how-to-win` and `#bets` (`H-012`/`R-007` the timing bet). Same section, updated in place.
- **Trigger:** Step 3 operating-loop pass; `value-definition-strategy` as second tool on `#how-to-win`
  and `#bets`. Section `#value-defensibility` re-projected; it carried no `confirmed:` marker to drop
  (it was `[assumption]`).

### 2026-08-16 — value & defensibility worked and projected
- **From → To:** intake only → `#value-defensibility` worked (base moats, post-AI kills, lead moat, deferral) and projected
- **Why:** Step 1 Act pass on `value-definition-concept`; names the base moat bet and kills the feature-moats
- **Trigger:** Step 1 operating-loop pass, section `#value-defensibility`

### 2026-08-16 — created (intake)
- **From → To:** — → founder-brief facts dispatched into the intake block
- **Why:** seed the value-definition-concept worklog with its evidence before the Step 1 Act pass
- **Trigger:** `source-intake` at instance setup
