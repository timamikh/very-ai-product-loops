---
node_type: worklog
tool: hypothesis-test-design
step: 5
title: "hypothesis test design — Period 1"
updated: 2026-08-16
version: 0.1.0
---

# hypothesis test design — the working (Period 1)

_Source of truth for `5-tactical-plan.md#hypotheses-to-test`. For each `H-…` tested this period: its
riskiest assumption, the bound `M-…` node, the **success/failure bars referenced from Step 4
(`hypothesis-thresholds`) — never re-decided here**, the **smallest sufficient test** (sample /
duration), and the **decision rule fixed before running**. Writes `status: testing` + the test design
back to the register._

## Which bets this period (and which wait, with the reason)

Tested: **H-001, H-011, H-010** — the three that gate Period 1 and are testable now (pre/at-prototype).
Waiting: **H-003** (switch → needs usage history; `M-w4-retention` unobservable pre-launch), **H-012**
(moat/timing → a trajectory bet, not a one-period read), **H-013** (staged bundle B-02 → deferred to a
later period on founder capacity, `prioritization` §2). Recorded so they aren't silently dropped.

## 1 · H-001 — engine does editable-AND-designed at scale

- **Riskiest assumption:** the corpus+generator produce *kept* (non-restyled) native decks across
  **arbitrary** content, not just demo-friendly briefs.
- **Metric node:** `M-design-acceptance` (% of native exports kept without a full restyle).
- **Bars (referenced, Step 4):** success **≥ 70%**, failure **< 40%**; 40–70% inconclusive.
- **Smallest sufficient test:** an internal **design-acceptance eval** on **≥50 briefs across ≥5
  verticals** (agency pitch · consulting QBR · sales · marketing rebrand · investor), judged on the
  instrumented proxy from `G-D2`. 50 is the smallest set that separates 70% from 40% with margin at
  this coarse read (not a powered A/B — a feasibility gate).
- **Decision rule:** ≥70% kept → `validated` (build on); <40% → `refuted` (corpus/generator rework
  before any launch); 40–70% → `inconclusive` → **iterate the corpus on the worst verticals, re-eval**.

## 2 · H-011 — founder-community reaches S1 at PLG-viable CAC

- **Riskiest assumption:** the founder's warm audience contains *reachable S1 buyers* (not just
  applause), recruitable at near-zero direct cost.
- **Metric node:** `M-cac` (proxy) — blended acquisition cost of a recruited design partner; secondary
  read `M-activated`.
- **Bars (referenced, Step 4):** success **≤ $150** (payback ≤ ~5 mo), failure **> $300**
  (payback > ~14 mo). Bars provisional — `— to clarify —` on directional CAC data.
- **Smallest sufficient test:** **one founder-led recruitment push** (~2 weeks) across the staged warm
  bundles (B-01, B-05). Count qualified design partners recruited and estimate blended CAC (founder
  time proxied at a nominal rate + any spend). Target ≥8 recruited (`G-G1`).
- **Decision rule:** ≥8 recruited at proxy-CAC ≤$150 → `validated` (founder channel is the engine); <3
  or proxy-CAC >$300 → `refuted` (`R-008` fires → validate a 2nd channel); in between →
  `inconclusive` → **run one more push before committing**.

## 3 · H-010 — S1 pays a premium

- **Riskiest assumption:** S1 attaches premium WTP to editable-AND-designed, not just enthusiasm for a
  free tool.
- **Metric node:** `M-paid-conv` (**proxy** — qualified price-talk acceptance; the instrumented
  trial→paid funnel doesn't exist pre-launch, flagged).
- **Bars (referenced, Step 4 for the instrumented node):** success ≥ 8% / failure < 3% trial→paid.
  **This period reads a coarser proxy** (price-talk acceptance among partners), *not* the instrumented
  rate — the proxy→instrumented gap is stated, and the Step-4 bar is **not** moved to fit the proxy.
- **Smallest sufficient test:** a **price-talk** with the ~8 recruited partners (rides on `G-G1`, near-
  zero marginal cost): present the premium price, record willingness (a `strong` signal = price talk /
  pre-pay intent).
- **Decision rule:** ≥5 of ~8 accept a premium price-talk (medium+) → `validated (proxy)` → design the
  instrumented trial→paid test next period; ≤1 of 8 → `refuted` (`R-011` fires); in between →
  `inconclusive` → **price-sensitivity follow-up**.

## Register

Writes to `registers/hypotheses.md`: `H-001`, `H-011`, `H-010` → `status: testing`; the `test` column
augmented with the Period-1 design (sample/duration + decision rule) alongside its Step-4 threshold.
No thresholds re-decided (all referenced from Step 4). `H-013` stays `open` (staged, not tested this
period).

## Change log

### 2026-08-16 — Period-1 tests designed
- **From → To:** — → smallest-sufficient test + pre-registered decision rule for `H-001` (50-brief
  eval), `H-011` (2-wk recruit push), `H-010` (partner price-talk proxy); Step-4 bars referenced not
  re-decided; `H-003`/`H-012`/`H-013` recorded as waiting with reasons
- **Why:** Step 5 attaches the smallest test that can reach each Step-4 bar this period; a pre-declared
  rule so the readout reads itself
- **Trigger:** Step 5 pass, section `#hypotheses-to-test`; status→testing on 3 bets in the register
