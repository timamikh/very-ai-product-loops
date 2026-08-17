---
node_type: worklog
tool: guardrails
step: 5
title: "guardrails — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# guardrails — the working (Period 1)

_Source of truth for `5-tactical-plan.md#guardrails`. What must **not** drop while chasing the Period-1
goals. Method: check **all seven break-categories** against the goals (write down the cleared ones
too), pick guardrail `M-…` with a floor/ceiling, state qualitative red lines, assign monitoring, and
log each breach as a risk-not-to-realize (`R-…`)._

## 1 · Seven break-categories × the Period-1 goals (every one checked, cleared ones recorded)

| Category | Checked against the goals | Guardrail? |
|----------|---------------------------|------------|
| **Quality** | G-D1/G-G1 could chase export *volume* by shipping decks the maker restyles — killing the whole "designed" wedge | **YES → `M-design-acceptance` floor** |
| **CAC / unit economics** | the backlogged paid probe (C7) or an over-eager recruit push could buy the G-G1 signal with spend that breaks payback | **YES → `M-cac` ceiling** |
| **Brand / trust** | recruiting fast could tempt dark-pattern fences or off-brand/scraped corpus content | **red line** (no metric — logged, itself a Step 5–6 task) |
| **Retention** | can't be eroded because it can't yet be *observed* — `M-w4-retention` not-instrumented, pre-launch | considered, **not guardrailed** — no data (a later task) |
| **Churn** | same — no paying accounts, no churn to protect this period | considered, **not guardrailed** — no data |
| **Support load** | an 8-partner cohort generates negligible, hand-served support | considered, **not guardrailed** — below the threshold of concern this period |
| **Unit economics (margin)** | covered by the CAC ceiling + `M-contribution` — but contribution needs payers (none yet) | folded into CAC; `M-contribution` guardrail **deferred** to first-revenue period |

## 2 · Guardrail metrics (node + floor/ceiling)

| Guardrail (`M-…`) | Must stay | Red line (breach) | Monitored |
|-------------------|-----------|-------------------|-----------|
| `M-design-acceptance` | **≥ 60%** during the build (rising toward the 70% `H-001` bar) | < 40% on any vertical → **stop scaling the eval**, fix the corpus | per eval batch (weekly), founder/design |
| `M-cac` (proxy) | **≤ $150** blended on the founder channel | > $300 (the paid-blend line) → **halt the paid probe**, stay founder-only | per recruit push, acting PO |

The `M-design-acceptance` floor (60%) sits **below** its horizon target (70%) on purpose: the period is
a *build toward* the bar, so the guardrail catches a collapse, not an incomplete ramp.

## 3 · Red lines (qualitative "never do", no metric behind them — stated so they can't be argued later)

1. **Never ship locked / image-only export.** Editability is the table-stakes gate (`H-005`);
   violating it to hit an export number destroys the wedge itself.
2. **No dark-pattern fences / no charge without explicit consent.** The `R-005` monetisation
   discipline is conversion *mechanics* (fences + trial), never tricks — a distinction easy to blur
   under recruitment pressure.
3. **Corpus content must be licensed or original.** No scraped copyrighted client decks in the taste
   corpus — a legal *and* trust line. **This surfaced a genuinely uncovered risk → mints `R-013`.**

## 4 · Risks-not-to-realize (breaching a guardrail is a risk)

- `M-design-acceptance` floor breach → **`R-009`** (taste doesn't travel). Not re-minted.
- `M-cac` ceiling breach → **`R-008`** (channel doesn't scale) / **`R-011`** (WTP). Not re-minted.
- Red line 2 breach → **`R-005`** (monetisation trap). Not re-minted.
- Red line 3 (corpus IP/licensing) → **new `R-013`** (legal/IP: corpus licensing) — no existing risk
  covers copyright exposure of the design corpus. Minted to `registers/risks.md`.

## Change log

### 2026-08-16 — Period-1 guardrails set; `R-013` minted
- **From → To:** — → 7 break-categories checked against the 5 goals (3 cleared with reasons: retention/
  churn/support — no data or below concern); 2 guardrail metrics with floors/ceilings
  (`M-design-acceptance` ≥60%, `M-cac` ≤$150); 3 red lines; breaches logged as risks-not-to-realize
  (`R-009`/`R-008`/`R-011`/`R-005` reused, **`R-013` minted** for corpus IP/licensing)
- **Why:** a goal without guardrails wins the number and loses the product; the corpus-IP red line had
  no risk behind it, so it became one
- **Trigger:** Step 5 pass, section `#guardrails`; `R-013` seeded to `registers/risks.md`
