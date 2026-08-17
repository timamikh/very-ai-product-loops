---
node_type: worklog
tool: substitutes
step: 2
title: "substitutes — the working"
updated: 2026-08-16
version: 0.1.0
---

# substitutes — the working

_Source of truth for `2-analysis.md#substitutes`. Framed by the job (`1-concept.md#jtbd`): "turn raw
content into a finished, on-brand, well-structured client-facing deck without hand-fixing." Three
baseline substitutes forced + ≥2 adjacent. Strong substitutes → risk register._

## The map

| Substitute | How it does the job today | Why the customer chooses it / when it wins | Switching friction to overcome | Conf |
|------------|---------------------------|--------------------------------------------|--------------------------------|------|
| **Do nothing** — live with the current deck / reuse an old one | copy last quarter's deck, swap a few numbers | wins when the deck is low-stakes or the deadline is brutal; zero cost, zero risk | must be faster than "just reuse the old one" | [assumption] |
| **Do it manually** — build in PowerPoint/Slides/Keynote by hand | the maker (or a teammate) formats every slide | wins when the maker trusts only their own hands, or the content is bespoke; **the dominant status quo** | habit + control: they already know the tool and own their templates (`jtbd` habit force) | [assumption] |
| **Build/host it themselves** — internal template system or a scripted pipeline (e.g. python-pptx) | an ops/enablement team maintains a locked corporate template; eng scripts bulk decks | wins for large orgs with brand governance and volume, or data-sensitive shops | not our fight early; the self-build threshold is *volume + a design team on staff* | [assumption] |
| **Hire a designer / agency** (adjacent) | outsource the deck to a human designer | wins for the highest-stakes one-shots (fundraise, keynote) where quality > speed and budget exists | cost + turnaround; we win on speed and price, lose on bespoke craft | [assumption] |
| **A general AI chat tool** (adjacent) — ChatGPT/Claude/Gemini → paste into slides | ask an LLM for an outline/content, format it yourself | wins for the content/outline half; free and already open | it does the *words*, not the *designed editable file* — leaves the restyle tax intact | [sourced: general availability, as_of 2026-08-16] |
| **The bundled incumbent** (adjacent) — Microsoft Copilot / Google Gemini in the suite | deck-gen already inside the tool they pay for | wins on "it's already here and native" for enterprise | our edge must be *visibly better design*, or the free-in-the-suite option wins (see risks) | [sourced: competitor-dynamics.md, as_of 2026-08-16] |

## Self-build threshold

"Just build it ourselves / use an internal template" beats buying when: the org has a **design team +
brand-governance mandate + deck volume** high enough to amortise a template system, or **data
sensitivity** forbids a third-party tool. Below that threshold (most of S1's individuals and SMBs),
buying wins — which is why the beachhead is individuals/teams, not enterprise brand-governance shops.

## Strong substitutes → risk register

- **"Do it manually" (the status quo)** is the substitute that wins most often — habit + control. It
  is the real competitor, not the other AI tools. → feeds `synthesis.md` (rivalry/habit) and the
  desirability bets `H-003`/`H-005`.
- **The bundled incumbent (Copilot/Gemini)** — a "free, already-here, native" substitute — is a
  genuine threat. → `R-002` (bundling) in the risk register.

## Change log

### 2026-08-16 — substitutes worked and projected
- **From → To:** empty → 3 baseline + 3 adjacent substitutes, self-build threshold, 2 strong → risk
- **Why:** Step 2 Act pass; find the non-obvious competition incl. do-nothing (concept-viability)
- **Trigger:** Step 2 pass, section `#substitutes`
