---
node_type: worklog
tool: pre-mortem
step: 3
title: "pre-mortem — the working"
updated: 2026-08-16
version: 0.1.0
---

# pre-mortem — the working

_Source of truth for `3-strategy.md#product-risks`. Lens: Klein's pre-mortem ("it's 12 months on and
the strategy failed — why?") → ≥8 named failure modes → triage by likelihood × impact (H/M/L backed
5/3/1, ranked by product) → an explicit **carried · parked · dropped** disposition for every one. This
tool **surfaces and triages only** — mitigation/owner/trigger are Step-4 `risk-mitigation`, which
extends these same `R-…`. The carried set is handed to Step 4 **unmanaged, on purpose._

## 1 · Pre-mortem — ≥8 named failure modes (it's Aug 2027, Decksmith failed)

| # | Failure story | L | I | L×I | Existing? |
|---|---------------|---|---|:---:|-----------|
| f1 | **`H-001` didn't hold** — the engine couldn't do editable-AND-designed beyond demos; output was generic or broke on export. | H | H | 25 | core (H-001) |
| f2 | **An incumbent closed the export gap first** — Gamma/Canva shipped real native `.pptx` export before we built a durable moat; the wedge vanished. | H | H | 25 | partial (R-001/R-003) |
| f3 | **Microsoft bundled it away** — Copilot made "editable designed deck" free in M365; buyers wouldn't pay standalone. | H | H | 25 | R-002 |
| f4 | **Monetisation trap** — grew free users, couldn't convert, ran out of runway (the Tome/Pitch path). | M | H | 15 | R-005 |
| f5 | **Founder-community channel didn't scale** past the founder's own audience; CAC exploded on saturation. | M | H | 15 | new |
| f6 | **Taste didn't travel** — the curated corpus produced samey/off-brand decks across diverse content; the "designed" claim failed at scale. | M | H | 15 | new |
| f7 | **WTP overestimated** — S1 wouldn't pay the premium; forced discounting to bundle levels broke the model. | M | H | 15 | new |
| f8 | **Key-person dependency** — the strategy leaned on the founder's taste/credibility; the founder became the moat *and* the bottleneck (bus factor). | M | M | 9 | new |
| f9 | **Model-supplier shock** — an LLM price/rate/access change blew unit economics or capability. | M | M | 9 | R-004 |
| f10 | **Platform/format break** — a PowerPoint/Keynote format or API change broke native export. | L | M | 3 | R-006 |
| f11 | **Editable wasn't actually a hard gate** for enough of S1 — many accepted "good enough" locked decks, shrinking the beachhead. | M | H | 15 | tests H-005 |

11 named failure modes — clears the ≥8 floor, and reaches execution + key-person risk (f5/f6/f8), not
only external/market ones (the pre-mortem's characteristic blind spot).

## 2 · Triage & disposition (every surfaced risk accounted for)

| # | Disposition | Reason | → register |
|---|-------------|--------|------------|
| f1 | **fold** | already the core hypothesis `H-001` (feasibility); it is a *bet* we test, tracked there — not re-minted as an R-. Its *even-if-built* failure is f6. | H-001 |
| f2 | **carry (new)** | the specific *timing/moat-erosion* failure isn't captured by R-001/R-003 as stated; it is the risk twin of bet `H-012`. | **R-007** |
| f3 | fold | already `R-002` (bundling). Surfaced again — noted, not duplicated. | R-002 |
| f4 | fold | already `R-005` (monetisation trap). | R-005 |
| f5 | **carry (new)** | channel-scaling failure; twin of channel bet `H-011`. | **R-008** |
| f6 | **carry (new)** | distinct from H-001 (can we *build* it) — this is *even if built, users reject the taste*. | **R-009** |
| f7 | **carry (new)** | WTP/pricing failure; twin of pricing bet `H-010`. | **R-011** |
| f8 | **carry (new)** | key-person/execution risk the pre-mortem exists to surface. | **R-010** |
| f9 | fold | already `R-004` (model-supplier). | R-004 |
| f10 | fold | already `R-006` (platform/format). | R-006 |
| f11 | **park** | it is the inverse of `H-005` (editability gate), which we already test as a hypothesis; if `H-005` refutes, mint an R- then. No duplicate now. | (H-005) |

**Carried, ranked by L×I (top first):** `R-007` (H×H, 25) · `R-009` (M×H, 15) · `R-011` (M×H, 15) ·
`R-008` (M×H, 15) · `R-010` (M×M, 9). Folded onto existing entries: **`H-001`** (f1 — a hypothesis,
the core feasibility bet, not a risk), `R-002` (f3), `R-004` (f9), `R-005` (f4), `R-006` (f10) —
surfaced again, re-confirmed, not duplicated. NB: `R-001` (rivalry) was *not* a target of any surfaced
failure mode; the nearest existing risk to new `R-007` is `R-003`, and f2 is argued distinct from it
(see the disposition row). Parked: f11. Dropped: none.

## 3 · New risks written to the register (status: open, UNMANAGED — handed to Step 4)

- **R-007** — Incumbent closes the export gap before the wedge converts to a durable moat (timing/
  moat-erosion). *market.* H×H.
- **R-008** — Founder-community channel doesn't scale past the founder's audience → CAC explodes.
  *execution.* M×H.
- **R-009** — Taste doesn't travel: curated corpus feels samey/off-brand across diverse content; the
  "designed" claim fails at scale. *product.* M×H.
- **R-010** — Key-person dependency on the founder's taste/credibility (moat = bottleneck; bus
  factor). *execution.* M×M.
- **R-011** — WTP overestimated: S1 won't pay the premium; forced discounting breaks the model.
  *financial.* M×H.

No mitigation/owner/trigger assigned — that is Step-4 `risk-mitigation`. The carried set is handed
forward **unmanaged, on purpose.**

## Change log

### 2026-08-16 — pre-mortem worked and projected
- **From → To:** — → 11 failure modes, L×I triage with a disposition for each (5 carried new, 5
  folded to existing, 1 parked), 5 new risks `R-007`…`R-011` seeded open/unmanaged
- **Why:** Step 3 Act pass on `pre-mortem`; surfaces and triages the risks to the *chosen* strategy
- **Trigger:** Step 3 operating-loop pass, section `#product-risks`
