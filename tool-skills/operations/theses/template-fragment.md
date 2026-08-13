<!--
  template-fragment: theses → writes ONLY a confirmation marker onto an existing artifact section.
  It adds no content and no new section. Follow process/CONVENTIONS.md → Section confirmation.
  The marker records that a HUMAN signed off THIS version; an agent never writes it unprompted.
-->

# The confirmation marker (on an existing artifact section)

A confirmed section carries the marker right after its method marker — nothing else changes:

```markdown
## Market sizing {#market-sizing}
<!-- tool: market-sizing -->
<!-- confirmed: 2026-08-13 -->

<the section's projected content, unchanged>
```

- **Pending** is the absence of the marker — never a `confirmed: pending` value, never a second field.
- **A synthesis section** carries it after its `<!-- synthesis -->` marker, same as a tooled one.
- **On re-projection** (the conclusion changed), *Act* removes the marker; this skill re-adds it only
  after the human signs the new version.

## The change-log entry it writes

In the artifact's own change log — naming what was signed and what went back, never inventing a result:

```markdown
### 2026-08-13 — Step 2 results confirmed
- **From → To:** 8 sections pending → market-sizing, competitors, competitor-strategy/pricing/dynamics,
  substitutes, niche-risks, opportunity confirmed by the human; hypotheses + to-clarify left pending
  (open items, not results).
- **Why:** human sign-off of the step's theses — the semantic half of the two-layer check.
- **Trigger:** operating-loop step 7 (theses).
```

**Then:** run `python3 tools/lint.py <instance>` to 0 errors — check Q holds every marker to a real date.
