<!--
  template-fragment: feature-grooming → one groom block per featured item, in the worklog
  6-sprint-plan/feature-grooming.md. The artifact carries only the readiness annotation on the
  feature's block in {#must} / {#backlog}. Follow process/CONVENTIONS.md.
-->

## Groom: F-<n> · <feature name>  ·  doc type: [BRD | tech spec | both]

**Scope, one-to-one** (each item ↔ one scope bullet of the feature — nothing added, nothing dropped):
1. …
2. …

**Product decisions** (closed by the product owner — a spec is not written while one is open):
- **<fork name>** — options weighed: A … / B … (recommended: A) → **decided: <option>**
  **Decided:** <!--d:date--> <YYYY-MM-DD> · **by:** <!--d:by--> <who — prefix ⚙️ while the agent's
  proposal is unconfirmed> · **alternatives considered:** <!--d:alts--> <what lost and why — or what
  makes the choice forced; a bare "none" is a defect>
- **<fork name>** — **deferred** by the owner → the feature is NOT spec-ready until closed or
  scoped out (say which and when).

**Inputs the developer can't produce** (each named + owned — an unowned input blocks readiness):
- **<artifact>** — what it is · owner: <who> · due: <when — "with the handoff" is the default>

**Technical forks** (left open on purpose — they travel into the spec for the tech lead):
- **<fork name>** — context: <what the feature left unset and what it affects> · options: A … / B …
  · selection criterion: … · recommended default: <A/B — why> · owner: tech lead.

**Readiness:** [spec-ready | blocked: <which product fork>] — scope 1:1 ☐ · product forks closed ☐ ·
technical forks recorded ☐ · inputs owned ☐ · doc type picked ☐
