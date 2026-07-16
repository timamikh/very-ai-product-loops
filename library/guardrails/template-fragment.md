<!--
  template-fragment: guardrails → fills {#guardrails}
  Follow process/CONVENTIONS.md.
-->

## Guardrails {#guardrails}

**Protected metrics (must not cross the threshold while hitting goals):**
| Guardrail metric (`M-…`) | Threshold (floor/ceiling) | Watched where / how often | Confidence |
|--------------------------|---------------------------|---------------------------|------------|
| e.g. `M-retention-d30` | floor 35% | analytics, weekly | [sourced: …] |

**Red lines (qualitative "never"):**
- …

**Breach = risk:** logged as `R-…`.
