---
node_type: worklog
tool: synthesis
step: 2
fills: [niche-risks, opportunity]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — synthesis (fills `#niche-risks` [light Five Forces] + `#opportunity`)

No method skill — the orchestrator's own reasoning over the other three worklogs. Shared worklog for both
`<!-- synthesis -->` sections (CONVENTIONS → Step folders & worklogs).

## Niche risks (light Five Forces) → born risk register `R-001…R-005`

| Force | Risk | L | I | → | Status (Step 2) |
|-------|------|---|---|---|-----------------|
| Rivalry | Gamma dominant + profitable ($100M ARR, 70M users) — head-on displacement hard | H | H | R-001 | accepted (don't fight head-on) |
| Substitution / entry | Incumbents (Copilot, Canva) bundle native-editable AI gen + own distribution → close the wedge | H | H | R-002 | open (top threat) |
| Substitution | Capable users self-build with general LLMs → caps WTP | M | M | R-003 | accepted (monitored) |
| Supplier power | Engine quality/COGS depend on third-party LLM providers | M | H | R-004 | open |
| Entry barrier | Low barrier for "AI slide wrappers" → many entrants; only a true native-fidelity engine is a barrier | M | M | R-005 | open |

Buyer power folds into R-002/R-003 (buyers already hold bundled + self-build options → price pressure).
Mitigation/owner/due are **added at Step 4** — `—` in the register until then (per REGISTERS schema).

## Opportunity — the "so what" (the point of the step)

- **White space:** the category leader is weak exactly where Decksmith is strong. Gamma's `.pptx` export
  **flattens 30–40% of slides into uneditable images**; the whole market is racing toward "editable +
  designed," but native-editable *export* is unsolved by the leader. That gap is the wedge. [sourced: market-research]
- **The threat is real and closing:** Copilot **owns PowerPoint** and Canva owns distribution; both are shipping
  agentic "edit my real file" modes in 2026. Decksmith has neither distribution nor the format ownership.
  Tome's 2025 exit shows a funded standalone-slides player can fail. [sourced: market-research]
- **Why now:** AI-deck demand is accelerating (CAGR ~23–26%, 2–4× the broad presentation market); enterprise
  adoption >60%; the "editable" bar is the *new* battleground but not yet won on native export. [sourced]
- **Conclusion (⚙️):** attack a **narrow, fast wedge** — native-fidelity *editable + designed* decks for the
  lead segment — defended by **execution speed on the fidelity engine, not the app**. Viable **only if**
  Decksmith moves faster than incumbents close the gap. This reframes the moat: taste/corpus (H-005) is
  necessary but not sufficient; the durable bet is *speed vs incumbents* → **H-009**.

## Seeds (hypotheses, my numbering)

- **H-009** (viability; tags: moat): a standalone native-fidelity engine can stay ahead of Copilot/Canva
  closing the wedge long enough to build a position. (Sharpens/depends on H-005.)
- H-007/H-008 already seeded in `market-sizing.md`.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → 5 niche risks (born `R-001…R-005`); opportunity = narrow fast native-fidelity wedge,
  threat = incumbent bundling; moat reframed to speed (H-009).
- **Why:** analysis without a "so what" is inert — state the wedge and its condition.
- **Trigger:** Step-2 analysis, rebuild.
