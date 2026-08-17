---
node_type: worklog
tool: product-surface
step: 3
title: "product surface & instrumentation — the working"
updated: 2026-08-16
version: 0.1.0
---

# product surface & instrumentation — the working

_Source of truth for `3-strategy.md#product-surface`. The bridge from strategy to measurability: a
channel with no instrumentation can't be judged; a metric with no collection point can't exist.
Sketched here; refined at Step 4 (`instrumentation-plan`, with `#architecture`) into the
instrumentation map._

## 1 · Every surface the user touches

| Surface | Type | Purpose | Instrumentation (what we measure + how) | Gap? | Conf |
|---------|------|---------|-----------------------------------------|------|------|
| Landing + comparison pages | landing | acquisition | visits, source, signup CVR (analytics) | — | [assumption] |
| Self-serve signup / onboarding | in-product | activation | signup → first-deck time, onboarding drop-off (analytics/funnel) | — | [assumption] |
| Generation UI (brief → deck) | in-product | core value | generations, time-to-first-deck, regenerations (product events) | — | [assumption] |
| **Native export action** (`.pptx`/`.key`) | in-product | the promise | export rate, format, export→open success | **— to clarify —** (did the file open cleanly in the client's PowerPoint? hard to instrument outside our app) | [assumption] |
| **Edit-behaviour capture** | in-product | moat + `H-001` proof | which generated slides are kept vs restyled (in-app edit events) | **— to clarify —** (edits made *after* native export leave our surface) | [assumption] |
| Brand-kit manager | in-product | retention / lock-in | brand kits created, reuse rate (product events) | — | [assumption] |
| Admin / billing panel | admin | ops + revenue | seats, plan, MRR, churn (billing + analytics) | — | [assumption] |
| Activation / lifecycle emails | mailing | activation/retention | opens, clicks, return-to-paid-action (email + analytics) | — | [assumption] |
| "Made with Decksmith" share | in-product | assisted referral (gated) | shares, referred signups (analytics) | — | [assumption] |
| Docs / help | content | support/activation | article views, deflection (analytics) | — | [assumption] |

## 2 · Behavior-study tools

Product analytics (funnels), session capture on onboarding + export, in-app + email surveys (WTP,
CVP validation), the activation funnel signup → first-deck → export → **edit-in-native** → paid.

## 3 · The two load-bearing gaps (→ Step 4 / registers)

- **Export-open fidelity** and **post-export edit behaviour** both leave our surface once the file is
  native (which is the whole point of the product). Measuring "did it open clean / stay edited" needs
  a proxy (in-app pre-export lint; an opt-in "opened successfully?" ping; agency panel interviews).
  Flagged `— to clarify —`; feeds Step-4 `instrumentation-plan`. Note this is the instrumentation cost
  of the differentiation — an irony worth stating.

## 4 · Infra implications (→ Step 4 cost lines)

Analytics stack, email/lifecycle provider, session-capture tool, LLM inference (COGS — the big one),
file-rendering/export service. Carried to Step-4 `financial-model` / `unit-economics`.

## Change log

### 2026-08-16 — product surface worked and projected
- **From → To:** — → surface×instrumentation table (10 surfaces), behaviour-study tools, the two
  export/edit measurement gaps (`— to clarify —`), infra implications for Step-4 costs
- **Why:** Step 3 Act pass on `product-surface`; makes the strategy measurable
- **Trigger:** Step 3 operating-loop pass, section `#product-surface`
