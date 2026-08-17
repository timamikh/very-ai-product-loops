---
node_type: worklog
tool: competitor-analysis
step: 2
title: "competitor-analysis — the working"
updated: 2026-08-16
version: 0.1.0
---

# competitor-analysis — the working

_Source of truth for `2-analysis.md#competitors` and `#competitor-strategy` (this method fills both;
first tool in each marker). Evidence from a `loops-research` brief (web, `as_of 2026-08-16`)._

## 1 · The player sweep (≥5 named, ≥1 not named first)

| # | Player | What it offers | Output editability (a=native pptx/key · b=web-editor-only, lossy export · c=locked/image) | Shares segment+job? |
|---|--------|----------------|-------------------------------------------------------------------------------------------|---------------------|
| 1 | **Gamma** | AI doc/deck generator, card-based web canvas | **b (borderline a, contested)** — claims editable pptx but card→slide is a lossy conversion (vendor help flags render fallbacks) | partly — designed look, but export fidelity is the gap |
| 2 | **Canva** | Broad design suite + AI deck generation | **b** — exports pptx but text partly rasterized, layouts shift | partly — huge marketing overlap, general tool |
| 3 | **Microsoft Copilot in PowerPoint** | Prompt-to-deck built into PowerPoint | **a** — native, editable in-app; generic design | partly — native but not design-tuned |
| 4 | **Beautiful.ai** | "Smart template" web deck builder + AI | **b (CONFLICT)** — vendor "fully editable" vs reviews "charts→images, ~60–70% text editable" | partly — client-facing design, value trapped in editor |
| 5 | **Plus AI** | AI generator running *inside* PPT/Google Slides | **a** — native by construction, but template-bound | **yes** — business/sales decks, native |
| 6 | **Presentations.ai** | "ChatGPT for presentations," own format | **b** — one-way pptx export, no round-trip | partly — business decks, not design-led |
| 7 | **Decktopus** | Quick pro decks (web), PPT/PDF/PNG export | **b** — export exists, native-shape editability unverified | partly — sales target, editability [assumption] |
| 8 | **MagicSlides** *(registry-sweep pick — 1M+ installs, Google Workspace Marketplace)* | Google Slides add-on: text/PDF/URL → slides | **a (Slides)** — editable inside Slides | no — speed/volume, not design quality |

Retreated (confirmed exits, not active rivals): **Tome** (killed Slides ~Apr 2025, pivoted to sales
AI), **Pitch** (Jan 2024 reset, repositioned to sales enablement) — see `competitor-dynamics.md`.

## 2 · Detailed table (share our segment AND our job) vs excluded

**Enter the detailed scans** (client-facing sales/marketing decks, finished-editable-designed job):
**Gamma, Canva, Microsoft Copilot, Beautiful.ai, Plus AI.**

**Excluded, with reason:**

| Excluded | Reason |
|----------|--------|
| MagicSlides / SlidesAI | positioned on speed/volume, not design quality — a different job (fast content→slides) |
| Presentations.ai | one-way export (no round-trip editable file); business but not design-led — indirect |
| Decktopus | sales target overlaps but output editability unverified — indirect, revisit if it proves native |

## 3 · What game each plays (revenue/profit/share/social capital — how) vs our moats

| Player | Game | How they play it | Their moats vs ours (`H-007`: corpus+taste) |
|--------|------|------------------|----------------------------------------------|
| **Gamma** | share / hypergrowth | freemium virality (70M users) → "replace PowerPoint"; a16z-backed | distribution + brand + usage data — strong; but sacrifices native export fidelity (their card model), the exact axis of our moat |
| **Canva** | share / ecosystem | bundle AI into a design empire; own distribution (265M MAU) | distribution + brand — dominant; general design tool, deck export lossy; not deck-native |
| **Microsoft Copilot** | bundling / lock-in | ride 20M+ M365 Copilot seats into every enterprise | distribution + enterprise lock-in — dominant; design is generic, no taste/corpus edge |
| **Beautiful.ai** | niche / profit | "smart templates," stable ~$13.5M rev | template IP + brand — modest; value trapped in its editor, lossy export |
| **Plus AI** | wedge | add-in *inside* PPT/Slides → native by construction | integration/distribution inside the incumbents; but template-bound, not design-led |

**Read:** the two dominant moats in the field are **distribution** (Gamma, Canva, Microsoft) and
**integration** (Plus AI). None competes on **native-and-designed quality** — which is where `H-007`
(corpus + taste) bets Decksmith's moat lives. That is also the risk: distribution can beat a quality
edge if the quality gap is small or slow to show.

## Seeded registers

- Competitive-threat risks → `synthesis.md` niche-risks (R-…): well-funded rivals accelerating,
  Microsoft bundling.
- Assumption about a rival: none minted as `H-` here beyond the white-space claim carried in synthesis.

## Change log

### 2026-08-16 — competitors & strategy worked and projected
- **From → To:** empty → 8-player sweep, 5-player detailed table with exclusions, game-per-player vs our moats
- **Why:** Step 2 Act pass; map who solves this pain to find the white space (concept-viability)
- **Trigger:** Step 2 pass, sections `#competitors` + `#competitor-strategy`; evidence from `loops-research`
