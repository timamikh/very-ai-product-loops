---
node_type: reference
title: A worked micro-example of one pass
status: draft
version: 0.1.0
updated: 2026-08-15
---

# A worked micro-example

*The operating loop shown end-to-end on one concrete pass. Pointed at from*
[`OPERATING-LOOP.md`](../OPERATING-LOOP.md); *the numbered loop it illustrates is there.*

Active status `2-pmf`, step `1-concept`, section `problems`:

1. Focus → "update `problems` for the lead segment" (a gate item).
2. Recommend → status `pmf` says pains come from *product metrics + a few interviews*
   (vs pure interviews at `concept-viability`); tool `segment-pains`.
3. Prerequisites → `segment-pains` needs: the segment list, access to usage metrics, ≥3
   recent user conversations. Sizing, aloud: "three small inputs, one section — running solo."
4. Gaps → metrics access is missing → agent offers to pull it via the metrics slot or asks
   for an export.
5. Clarify → "Which pain do we treat as primary for pricing — A or B? ⚙️ A." → waits.
6. Act → works the method in the worklog `1-concept/segment-pains.md` (severity × frequency, each
   `[sourced: metrics …]` / `[assumption]`) and projects the `problems` section from it; the ranking
   is the agent's own reasoning → shows the section in chat first, names the files this pass will
   touch (`1-concept/segment-pains.md`, `1-concept.md`, `registers/hypotheses.md`, `state.yaml`).
7. Update → writes the section, seeds `H-007` ("pain A blocks payment"), logs the change; the tick
   waits for a `verify` subagent's findings on the ranking, and the human signs off the `problems`
   thesis (`theses` skill) → `<!-- confirmed: … -->` on the section.
8. Loop → next section `solution`.
