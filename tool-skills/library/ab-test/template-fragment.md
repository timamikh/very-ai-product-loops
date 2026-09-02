<!--
  template-fragment: ab-test → fills {#hypotheses-to-test} (experiment case)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

## Hypotheses to test {#hypotheses-to-test}

<!-- card -->
**Test read:** <one sentence — the `H-…` under experiment, the OEC bar it must clear, and the n / run
length that can reach it> _(the same slot `hypothesis-test-design` declares — one face per section)_.

| `H-…` | Metric node (`M-…`) | Success | Failure | Sample / duration | Decision rule | Confidence |
|-------|---------------------|---------|---------|-------------------|---------------|------------|
| H-… — <what has to be true> | M-… (the OEC) | ≥ … | < … | n = … / arm · … weeks | ≥ success → `validated`; < failure → `refuted`; between → `inconclusive`; any guardrail breach → `refuted` | [assumption] |

### Experiment — <name>

- **Hypothesis:** `H-…` — <what has to be true> · **reads against:** `M-…`
- **OEC (primary metric):** `M-…` — <the one metric the decision hangs on>
- **Randomization unit / arms:** <user | account | session> · control vs <variant(s)> · split <e.g. 50/50>

**Guardrail metrics — must not drop**
| Guardrail (`M-…`) | Red line | Confidence |
|-------------------|----------|------------|
| e.g. p95 latency | < … ms | [assumption] |

**Sizing**
| Baseline | MDE (min effect worth detecting) | Power / α | Required n / arm | Run length |
|----------|----------------------------------|-----------|------------------|------------|
| … | … | 80% / 0.05 | … | … |

- **Stopping rule (pre-registered):** <fixed horizon at n=… | valid sequential test> — no peek-and-stop.
- **Decision rule:** OEC ≥ <success bar> → `validated` · < <failure bar> → `refuted` · between → `inconclusive` (→ <next>). Any guardrail breach → `refuted`.
- **Pitfall checks:** SRM ☐ · novelty/primacy ☐ · cross-arm spillover ☐ · segment interactions ☐

**Seeded / updated registers:** `H-…` → `testing` then `validated`/`refuted` · measured effect → `metrics.csv` (dated row).
