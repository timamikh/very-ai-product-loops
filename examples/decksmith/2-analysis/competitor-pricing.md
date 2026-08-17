---
node_type: worklog
tool: competitor-pricing
step: 2
title: "competitor-pricing — the working"
updated: 2026-08-17
version: 0.1.1
---

# competitor-pricing — the working

_Source of truth for `2-analysis.md#competitor-pricing`. Feeds `market-sizing`'s price anchor,
Step-3 pricing, and the Step-4 financial model — not our price. Every price is a dated snapshot.
Evidence from a `loops-research` brief; all prices read `as_of 2026-08-16` from vendor pricing pages
(primary for their own published price)._

## Dated pricing — detailed-table players (+ nearby)

| Player | Plan / model | Price (read 2026-08-16) | Export notes | Conf |
|--------|--------------|-------------------------|--------------|------|
| **Gamma** | per-seat + AI credits | Free $0 · Plus **$8/mo** · Pro **$18/mo** · Ultra $100/mo | pptx export on paid; branding removed on paid | [sourced: gamma.app/pricing, med — read as snippet, page JS-blocks fetch] |
| **Beautiful.ai** | flat / per-seat | Pro **$12/mo** (annual) · Team **$40/user/mo** (annual) · single deck $45 one-off | editable pptx export | [sourced: beautiful.ai/pricing, high] |
| **Microsoft 365 Copilot** | per-seat add-on | enterprise "M365 Copilot" **$30/user/mo** (annual) · SMB "Copilot Business" (≤300 seats) **$21 list / $18 promo** (thru 2026-09-30) — each + qualifying M365 base | native pptx (runs in PowerPoint) | [sourced: microsoft.com pricing pages, high] |
| **Plus AI** | per-seat + credits | Basic **$10/mo** · Pro **$20/mo** · Team **$30/mo** · Max $200/mo (annual) | native Slides/PPT (add-in, no separate export) | [sourced: plusai.com/pricing, high] |
| **Presentations.ai** | flat + credits | Free $0 · Pro **$20/mo** · Gold $100/mo | pptx export paid, one-way | [sourced: presentations.ai/pricing, med] |
| **Pitch** | per-seat + credits | Free €0 · Plus **€10/mo** · Team €15/mo · Business €20/mo | pptx on paid | [sourced: pitch.com/pricing, high] |
| **Decktopus** | flat + credits | Pro **$9.99/mo** (annual) / $24.99 monthly | PPT/PDF/PNG | [sourced: decktopus.com/pricing, med] |
| **SlidesAI** | flat + credits | Free · Pro **$10/mo** · Premium $20.83/mo | add-in (native Slides/PPT) | [sourced: slidesai.io/pricing, med] |
| **Chronicle** | per-seat + tokens | Free · Pro $12/mo · Plus **$25/mo** (pptx here) · Max $45/mo | pptx only from Plus tier up | [sourced: chroniclehq.com/pricing, med] |

## Rejects — non-comparable (kept with reason)

| Player / tier | Reason not comparable |
|---------------|-----------------------|
| Enterprise tiers (Beautiful.ai, Pitch, Plus AI, Canva, Decktopus, Chronicle) | "contact sales" — no public number to anchor a comparison |
| **Canva Pro** | `— to clarify —` — canva.com JS-renders / 403s to fetch; Pro price not recoverable. Confirmed only Canva **Business = $20/user/mo** (help/newsroom snippet) |
| Google Gemini for Workspace | no standalone add-on price; bundled (Business Starter $8.40/user/mo reached; Standard/Plus `— to clarify —`) |

## Read for the anchor

The comparable prosumer/business AI-deck tier clusters at **~$8–20/mo/seat**; business/team tiers at
**~$20–40/mo/seat**; Microsoft's bundle at **$18–30/seat by tier** *on top of* an M365 licence users
already buy. **Blended market anchor ⚙️ ≈ $15/mo = $180/yr/seat** (used in `market-sizing.md`). The bundle
(Copilot) and freemium (Gamma, Pitch, Canva) tiers are the real WTP pressure — a paid standalone must
justify itself against "it's already in PowerPoint."

**No `[CONFLICT]` (>20%)** on any entered figure; a Gamma billing-cadence divergence ($8 annual vs
$10 monthly) is noted, not a conflict.

## Change log

### 2026-08-17 — human review pass: Copilot enterprise tier added
- **From → To:** the Copilot row quoted only the SMB price ($18 promo / $21 list) → both tiers named
  and priced: enterprise "Microsoft 365 Copilot" $30/user/mo (annual) and SMB "Copilot Business"
  $21 list / $18 promo (promo window thru 2026-09-30); the anchor read updated to "$18–30 by tier"
  (verified on microsoft.com pricing pages, read 2026-08-17: /microsoft-365/copilot/enterprise,
  /microsoft-365-copilot/pricing, /microsoft-365/business/compare-all-microsoft-365-business-products)
- **Why:** quoting the cheapest tier alone understated the bundle's price envelope — the enterprise
  tier is the one an S1 in-house buyer most likely sits behind; the blended anchor (~$15/mo ⚙️) holds
- **Trigger:** human review pass on the finished run (evidence lens); re-verified via a fresh
  research brief

### 2026-08-16 — competitor pricing worked and projected
- **From → To:** empty → dated pricing for 9 players + reject table; blended anchor ~$180/yr
- **Why:** Step 2 Act pass; give sizing a price anchor and Step 3 a positioning reference
- **Trigger:** Step 2 pass, section `#competitor-pricing`; evidence from `loops-research`
