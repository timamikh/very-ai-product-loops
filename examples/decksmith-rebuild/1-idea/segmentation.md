---
node_type: worklog
tool: segmentation
step: 1
fills: [segments]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — segmentation (fills `#segments`)

## Prerequisites

- Concept — from `concept-formation.md`. ✓
- Audience knowledge — thin (no product in market); founder observation of the sales/marketing crowd only.
  So cuts stay `[assumption]`. [sourced: founder brief]

## 1 · Candidate cuts (≥3 on different bases, rejects recorded)

| Basis | Cut | Verdict |
|-------|-----|---------|
| **Use-context × stakes/frequency** | client-facing decks (sales/marketing) · pitch/fundraise · internal/ops · education/personal | **chosen** — predicts different needs (design bar, editability, who pays) sharply |
| Role / demographics | "marketers", "consultants", "students" | rejected — same role makes very different decks; role doesn't predict the design/editability need |
| Company size (SMB/mid/ent) | by seat count | rejected — the org's default cut; doesn't predict the *pain*, and cross-cuts the real driver (stakes of the deck) |
| Buyer (individual vs company budget) | prosumer vs team | kept as a *secondary* lens inside the chosen cut (decides monetization, not the product) |

Rejected cuts kept per the method — the org-default cut (company size) is the one least likely to predict need.

## 2 · Segments on the chosen cut (1–3, lead first)

1. **Salespeople & marketers making client-facing decks** — recurring high-stakes decks (pitches, proposals,
   campaign readouts); design *and* editability both matter; usually a company budget behind the tool.
   [sourced: founder brief — the founder's lead bet]
2. **Founders / consultants making pitch & client decks** — very high stakes, lower frequency, individual
   buyer; strong design bar. [assumption]
3. **Internal / corporate deck-makers (PMs, analysts, ops)** — high frequency, lower design stakes, editability
   still required. [assumption]

## 3 · Reachability

- Seg 1 — LinkedIn, sales/marketing & RevOps communities, marketing-ops tool ecosystems. [assumption]
- Seg 2 — founder/accelerator networks, consulting communities, design-adjacent channels. [assumption]
- Seg 3 — inside companies (bottom-up/seat expansion), corporate templates. [assumption]

## 4 · Priority tiers (ground stated per placement)

- **Tier 1 = Seg 1.** Ground: *reachability + budget + frequency×stakes* — the founder's bet, and the segment
  where "looks templated → rebuild" bites most often with money behind the fix. ⚙️
- **Tier 2 = Seg 2.** Ground: *need-difference* — highest design stakes but lower frequency and individual
  wallet; distinct enough to keep, not to lead.
- **Tier 3 = Seg 3.** Ground: *need-difference* — editability matters but the design differentiator lands
  weakest; kept, deprioritized.

⚙️ Lead = Seg 1; the human decides. Everything downstream (problems, solution, value) leads with Seg 1;
lower tiers kept, never deleted.

## 5 · Evidence basis (stated plainly)

This segmentation rests on **founder desk observation only** — no customer conversations, no usage data. That
is the weakest of the three evidence kinds; a reader must not mistake it for validated. Each segment
`[assumption]`.

- "Seg 1 exists, is reachable, and feels the pains strongly enough to switch" → **H-002** (desirability).

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → three segments on a use-context×stakes cut; Seg 1 (sales/marketing) proposed as lead.
- **Why:** foundation for problems, value, channels.
- **Trigger:** rebuild-from-brief walkthrough.
