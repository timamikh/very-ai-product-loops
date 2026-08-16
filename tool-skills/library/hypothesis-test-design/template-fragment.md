<!--
  template-fragment: hypothesis-test-design → fills {#hypotheses-to-test}
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Hypotheses to test {#hypotheses-to-test}

**Test designs** — one row per `H-…` we test this period. Each is a pre-registered read:
metric node · success/failure threshold · sample or duration · decision rule fixed *before* running.

| Hypothesis (`H-…`) | Metric node (`M-…`) | Success threshold | Failure threshold | Sample / duration | Decision rule | Confidence |
|--------------------|---------------------|-------------------|-------------------|-------------------|---------------|------------|
| H-… — <what the bet claims> | M-… | ≥ … | < … | e.g. n = … / … weeks | ≥ success → `validated`; < failure → `refuted`; between → `inconclusive` → <next action> | [assumption] |

_The threshold and `M-…` link come from `hypothesis-thresholds` at Step 4 and are referenced, never
re-decided here; this section adds the smallest sufficient test that can reach that bar. A row with
no decision rule set in advance isn't a test._

**Seeded registers:** each `H-…` → hypothesis register (`status: testing`, `test` → this design).
Result later flips `confidence` to `[validated: …]` / `[refuted: …]`.
