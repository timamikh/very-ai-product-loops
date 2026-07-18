<!--
  template-fragment: ab-test → fills {#hypotheses-to-test} (experiment case)
  Follow process/CONVENTIONS.md. ⚙️ = agent proposal awaiting approval.
-->

### Experiment — <name> {#hypotheses-to-test}

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
