---
node_type: worklog
tool: risk-mitigation
step: 4
title: "risk mitigation — the working"
updated: 2026-08-16
version: 0.1.0
---

# risk mitigation — the working

_Source of truth for `4-strategic-plan.md#risk-mitigation`. Takes the **carried** `R-…` set (surfaced
+ triaged upstream by `pre-mortem` Step 3 / `niche-risks` Step 2) and makes each **managed**:
mitigation (an action, not a hope) · owner (one person) · observable **trigger** (the signal to act
now) · **due** (the review date, a different thing from the trigger) · lifecycle status. Upserted into
the **same** `registers/risks.md` rows — never a step-local copy. Scores are NOT re-derived here._

## Managed set (12 carried risks, incl. `R-012` newly seeded by `capabilities-systems`)

| `R-…` | L×I | Mitigation (action) | Owner ⚙️ | Trigger (observable) | Due (review) | Status |
|-------|-----|---------------------|----------|----------------------|--------------|--------|
| R-001 | H×H | Ship the editable+designed wedge in the narrow S1 niche where incumbents are conflicted; don't fight broad | founder | an incumbent announces real native-export parity | quarterly | mitigating |
| R-002 | H×H | Position on **taste**, not price, vs the Copilot bundle; target S1 the bundle won't satisfy | acting PO | Copilot ships on-brand designed decks | quarterly | mitigating |
| R-003 | H×H | Convert the wedge to data + lock-in moat on the `H-012` trajectory; instrument early | founder | a clone reaches design-acceptance parity | quarterly | mitigating |
| R-004 | M×M | Provider-abstraction layer + multi-provider fallback; monitor COGS per export | eng | provider price/rate/access change >20% | on provider change | mitigating |
| R-005 | M×H | Paid fences + tight trial from day one; measure `M-paid-conv`; never free-first-unlimited | acting PO | `M-paid-conv` below the `H-010` band | monthly (post-launch) | mitigating |
| R-006 | L×M | Export-fidelity test suite across PPT/Keynote versions; watch format/API changes | eng | a format/API change breaks native export | on Office/macOS release | open |
| R-007 | H×H | Race the data-loop + brand-kit lock-in before the export gap closes; close `R-012` first | founder | Gamma/Canva ship native `.pptx` parity | quarterly | mitigating |
| R-008 | M×H | Validate a 2nd inner-ring channel (content/SEO, paid) early; don't over-rely on the founder audience | acting PO | community new-payers plateau / `M-cac` > ~$300 | monthly | mitigating |
| R-009 | M×H | Corpus breadth + per-vertical style tests; a design-acceptance gate before scaling | founder / design | `M-design-acceptance` below floor across verticals | design gate + monthly | mitigating |
| R-010 | M×M | Codify taste into labelled rubrics (reduce founder-in-loop); document the system; train a 2nd curator | founder | founder review queue > threshold (bottleneck) | +6 mo | mitigating |
| R-011 | M×H | WTP survey + price test in the pilot before scaling; hold the premium, measure `M-arppu`/`M-paid-conv` | acting PO | `M-paid-conv` below the `H-010` failure bar | pilot readout | mitigating |
| R-012 | M×H | Build the design-acceptance proxy + edit-behaviour capture in the first release; prioritise North-Star instrumentation | eng | North Star still proxy-only at launch + 1 mo | launch gate | mitigating |

- "Monitor closely" is nowhere a mitigation — each row names an action, an owner, and a signal.
- **Trigger ≠ Due:** the trigger fires on a signal (act now); the due date is when someone reviews
  even if it never fires. Both columns filled.
- Scores (`L×I`) travel from the `pre-mortem`/`niche-risks` triage — **not re-scored here**.

## Change log

### 2026-08-16 — carried risks made managed
- **From → To:** 12 carried `R-…` (mitigation/owner/trigger empty) → each upserted with an action,
  owner, observable trigger, review date, lifecycle status (11 `mitigating`, 1 `open`); the same
  register rows, not a copy
- **Why:** Step 4 makes every carried risk actionable before the plan is signed
- **Trigger:** Step 4 pass, section `#risk-mitigation`; upserted into `registers/risks.md`
