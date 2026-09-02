---
node_type: artifact
artifact: concept
step: 1
title: "Fixture — concept"
status: draft
version: 0.1.0
updated: 2026-09-01
---

# Fixture — concept

## Idea {#idea}
<!-- tool: concept-formation -->
_What the product is and the shift it makes._

The fixture product is a tiny slide generator for linter tests, and it carries risk R-001 on purpose. <!-- card -->

**Decided:** <!--d:date--> 2026-09-01 · **by:** <!--d:by--> the fixture author · **alternatives considered:**
<!--d:alts--> a real instance (rejected — too slow to lint in CI)

## Job to be done {#jtbd}
<!-- tool: jtbd-concept -->
_The job the customer hires the product for._

When a check has no test, I want a fixture that fails in a known way, so that a regression is caught before a push. <!-- card -->

| Force | Direction | For this job | Confidence |
|-------|-----------|--------------|------------|
| Push | away from status quo | untested checks | [assumption] |

## Segments {#segments}
<!-- tool: segmentation -->
_Who it's for and how segments are cut._

Framework maintainers who edit the linter are the lead segment; they read this first. <!-- card -->

| Priority <!--c:priority--> | Segment <!--c:segment--> | How it's cut <!--c:cut--> | Buyer / user <!--c:buyer--> | Why it matters <!--c:why--> | Where to reach them <!--c:reach--> | Confidence <!--c:conf--> |
|----------|---------|--------------|--------------|----------------|---------------------|------------|
| 1 (lead) | maintainers | edits lint.py | same | they break checks | the repo | [assumption] |

## Problems {#problems}
<!-- tool: segment-pains -->
_Боли сегмента, ранжированные по тяжести и частоте._

| Problem <!--c:problem--> | Severity <!--c:severity--> | Frequency <!--c:frequency--> | Cost of inaction <!--c:inaction--> | Class <!--c:class--> | Confidence <!--c:conf--> |
|---------|----------|-----------|------------------|-------|------------|
| … | … | … | … | … | [assumption] |

## Customer journey {#cjm}
<!-- tool: cjm-concept, cjm-strategy -->
_Where the drop-off is._

## Solution {#solution}
<!-- tool: concept-expansion -->
_How the problems are addressed._

A fixture instance under tools/tests with one defect per check, exercised by a stdlib runner; it also cites feature F-001 that no register defines. <!-- card -->

## Value defensibility {#value-defensibility}
<!-- tool: value-definition-concept, value-definition-strategy -->
_Why this holds._

## To clarify {#to-clarify}
<!-- open -->
- — to clarify — the fixture's owner

## Hypotheses {#hypotheses}
_Seeded hypotheses live in the register._

## Журнал изменений

### 2026-09-01 — segments reopened for re-sign
- **From → To:** `#segments` signed → reopened, content changed; the tick set to `open` on purpose
- **Why:** the lead segment was renamed — the owner re-signs after a fresh verify
- **Trigger:** the test fixture needs a recorded reopen; also mentions H-999 and **Decided:** in history only
