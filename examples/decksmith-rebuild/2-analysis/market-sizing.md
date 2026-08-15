---
node_type: worklog
tool: market-sizing
step: 2
fills: [market-sizing]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — market-sizing (fills `#market-sizing`)

Source: `../sources/market-research.md` (desk-research capture). Bottom-up SAM is the answer; top-down is a
cross-check only.

## 1 · SAM bottom-up (units × price) — the number that matters

Arena: **salespeople & marketers in NA+EU who build client-facing decks and would pay for a standalone
native-fidelity AI deck tool** (not just use bundled Copilot/Canva).

- Sales/marketing professionals in NA+EU who regularly build client-facing decks: **~15M**. [assumption]
- Share who would adopt a *standalone* AI deck tool AND pay (net of those satisfied by bundled
  Copilot/Canva or self-build): **~12%** → **~1.8M reachable payers**. [assumption — the load-bearing one]
- Price: **~$18/mo → ~$216/yr** (competitor band $13–25, `competitor-analysis.md`). [sourced: pricing scan 2026]
- **SAM ≈ 1.8M × $216 ≈ ~$390M/yr** (range **$300–500M** on the adoption-share assumption). [assumption]

## 2 · Top-down cross-check

- AI presentation *generation* segment 2025: **$1.94B / $2.8B / $3.1B — [CONFLICT]**, diverges 2–3× across
  reports; do not average. [sourced: multiple, conflicting] 2026 single-source high figure ~$4.7B [assumption].
- NA share ~38.5% (~$1.08B, 2025). [assumption — single-source]
- Derive same SAM top-down: NA+EU ≈ NA×~1.7 ≈ ~$1.8B of AI-gen spend; lead segment (sales/marketing client
  decks) ≈ ~20–25% of that ≈ **~$360–450M**. [assumption]
- **Bottom-up (~$390M) and top-down (~$360–450M) agree within ~20%** → no [CONFLICT] flag on SAM itself;
  confidence a notch higher than either method alone. (The AI-segment *TAM* stays conflicted; SAM does not.)

## 3 · TAM / SOM

- **TAM** (whole AI deck-generation market, global): **~$2–3B (2025), ~$4–5B (2026)**, CAGR ~23–26%. Wide
  error bars (the [CONFLICT] above). [sourced, range]
- **SOM** (obtainable, ~3-yr horizon): **~1–3% of SAM ≈ $4–12M ARR**. Rationale: crowded, incumbents bundling
  and owning distribution (`R-002`), standalone-slides is hard (Tome exited) → a narrow wedge, single-digit
  share is the honest ceiling early. [assumption]

## 4 · Seeds (my numbering continues from H-006)

- **H-007** (viability): SAM (~$390M) is large enough to build a business on.
- **H-008** (viability): the lead segment will pay a standalone ~$15–20/mo despite incumbents bundling — the
  load-bearing adoption-share + WTP assumption. (Pricing *decision* deferred to Step 3; this is its viability bet.)

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → SAM ~$390M bottom-up, cross-checked top-down (agree ~20%); TAM ~$2–3B (conflicted); SOM
  $4–12M. H-007/H-008 seeded.
- **Why:** size the bet honestly; the [CONFLICT] in published figures forces bottom-up.
- **Trigger:** Step-2 analysis, rebuild.
