---
node_type: worklog
tool: channels-expansion
step: 3
fills: [channels-expansion]
product: "Decksmith (fictional sample)"
updated: 2026-08-14
---

# Worklog — channels-expansion (fills `#channels-expansion`)

Bullseye. ≥8 candidates across ≥3 categories, scored **1/3/5** on reach · cost-to-test (inverted: cheap=high) ·
testability. Inner ring = 3 highest.

| # | Channel | Category | Reach | Cost | Test | Σ | Ring |
|---|---------|----------|-------|------|------|---|------|
| 1 | LinkedIn content / thought-leadership | content | 5 | 5 | 3 | 13 | **inner** |
| 2 | Sales/design communities (Slack/Discord/Reddit) | communities | 3 | 5 | 5 | 13 | **inner** |
| 3 | PLG virality ("made with Decksmith" on shared decks) | existing-base | 5 | 3 | 3 | 11 | **inner** |
| 4 | SEO/content ("editable AI pptx", "fix Gamma export") | content | 3 | 3 | 1 | 7 | middle |
| 5 | Paid social (LinkedIn/Meta) | paid | 3 | 1 | 5 | 9 | middle |
| 6 | Creator/influencer partnerships (design/sales) | partnerships | 3 | 3 | 3 | 9 | middle |
| 7 | Add-in / app marketplaces (PPT, Google Slides, Canva) | marketplaces | 3 | 1 | 1 | 5 | outer |
| 8 | Outbound to sales teams | outbound | 1 | 1 | 3 | 5 | outer |
| 9 | Webinars/events (sales/marketing) | events | 1 | 1 | 1 | 3 | outer |
| 10 | Reseller/agency partnerships | partnerships | 3 | 1 | 1 | 5 | outer |

Outer/middle kept with reason (they lost on cost or slow read), never deleted.

## Inner-ring tests (metric · cost · threshold set BEFORE running)

- **LinkedIn content:** metric = signups/1k impressions; cost ~2wk of posting; threshold ⚙️ ≥ 0.5% → keep.
- **Communities:** metric = qualified trial starts per community-week; cost ~low; threshold ⚙️ ≥ 10/wk.
- **PLG virality:** metric = k-factor (invited/active); cost = watermark build; threshold ⚙️ k ≥ 0.3.

## Expansion path (sequenced, with triggers)

1. Lead segment (sales/marketing) — now.
2. → Founders/consultants (Seg 2) once PLG k-factor > 0.3 and Pro retention holds.
3. → Teams/orgs (Seg 3, seat expansion) once the brand-kit "Team" tier shows repeat use.
4. → (later) API/embed or enterprise, per cascades C/D.

## Seeds

- Channel bet → `H-011` (viability: communities + PLG acquire the beachhead at viable CAC).
- Channel risk (PLG doesn't fire → CAC too high without distribution) → `R-006`.

## Change log

### 2026-08-14 — created (rebuild)
- **From → To:** — → 10 candidates scored into rings; inner = LinkedIn/communities/PLG with measurable tests;
  expansion path with triggers.
- **Why:** rank channels before spending; a channel with no metric isn't a test.
- **Trigger:** Step-3 strategy, rebuild.
