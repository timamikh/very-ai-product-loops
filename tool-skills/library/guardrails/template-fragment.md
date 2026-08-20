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

**Considered, not guardrailed** — every break-category checked that did not become a guardrail. A
category nobody looked at and one that was looked at and cleared are indistinguishable afterwards.

| Category | What was checked | Why not a guardrail |
|----------|------------------|---------------------|
| retention · unit economics · CAC · quality · brand/trust · support load · churn | … | no metric node yet (→ instrumentation task) · no plausible mechanism this period · already covered by <other guardrail> |

**Decided:** <YYYY-MM-DD> · **by:** <who> · **alternatives considered:** <at least one alternative
actually weighed and why it lost — or what makes the choice forced; a bare "none" is a defect> ·
⚙️ if the agent proposed it and the human has not confirmed.
