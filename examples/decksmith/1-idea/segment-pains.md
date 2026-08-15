---
node_type: worklog
method: segment-pains
step: 1-idea
produces: problems
segment: "Lead — salespeople & marketers making client-facing decks"
status: draft
updated: 2026-08-14
---

# Worklog — Segment Pains (lead segment)

Draft by `loops-draft`. Everything proposed here is ⚙️ awaiting orchestrator/human review.
Fills `{#problems}` for the lead segment only. No register ids minted here — implied desirability
beliefs are described in words for the orchestrator to mint.

## Job (given — not re-derived)

> _When_ I must produce a client-facing deck for a specific audience on a deadline, _I want to_ get a
> deck that already **looks designed** **and** carries the **right structure/story** for that audience —
> and that I can still **edit natively** — _so that_ I present credibly and win the meeting without
> rebuilding it by hand.
> `[sourced: founder brief for the two halves; deadline framing assumption]`

Two load-bearing halves: **look designed** and **right story**. Pains below are obstacles to *this*
job, not generic deck complaints.

## Evidence standing (read this before trusting the scores)

- **Segments** prerequisite: given (lead = salespeople & marketers). ✔
- **Evidence source** prerequisite: **thin.** The only input is the founder brief — a single
  observer's account, effectively an interview of one (the founder), not primary segment research and
  not product metrics. Per the method (step 4), a stated complaint with no behaviour behind it is
  `[assumption]`. The founder does report **past behaviour** ("regenerate AI output by hand"), which
  raises P1 above pure opinion — but it is the founder's *observation of others*, one source, unquantified.
- **Consequence for the table:** a pain's **existence** can be tagged `[sourced: founder brief]` where
  the founder named it, but every **Severity / Frequency score is my ⚙️ ordinal estimate `[assumption]`**
  — none is measured. The whole table should be read as desirability hypotheses to test, not findings.

## Candidate pains (≥5 per volume rule) — scored severity × frequency

Founder named three (P1–P3, kept with their tags). I add three justified from the job (P4–P6,
`[assumption]`) to clear the ≥5 floor and give the ranking something to do.

### P1 — AI output "looks templated" → forced hand-redesign
- **The pain:** generated decks read as generic/templated, so the user re-does the visual design by
  hand; the promised time saving evaporates. `[sourced: founder brief]`
- **Score:** Severity **H** ⚙️ (defeats the core "looks designed" half of the job) × Frequency **H** ⚙️
  (founder: happens "often"). `[assumption on the H/M/L values]`
- **Class:** **differentiator** — this is the primary axis Decksmith means to compete on (look).
  `[sourced: founder brief boundary + task brief]`

### P2 — Wrong structure/story for the audience
- **The pain:** decks come back with structure/narrative that doesn't fit the specific audience, so the
  user re-frames the story. `[sourced: founder brief]`
- **Score:** Severity **H** ⚙️ (defeats the "right story" half; wrong story loses the meeting) ×
  Frequency **M** ⚙️ (founder frames it as "also" alongside look — real but named second).
  `[assumption on the H/M/L values]`
- **Class:** **differentiator** — the second competitive axis (structure/framing).
  `[sourced: founder brief + task brief]`

### P3 — Locked / image-only output can't be edited
- **The pain:** output that is a flat image or rigid template can't be edited natively — a non-starter
  for this crowd. `[sourced: founder brief]`
- **Score:** Severity **H** ⚙️ (a hard gate — "non-starter") × Frequency **H** ⚙️ (native editing is
  needed on essentially every client deck). `[assumption on the H/M/L values]`
- **Class:** **table-stakes** — founder-stated boundary; a required baseline baked into the concept, not
  the thing that wins. Note the "editable but ugly" incumbents already meet it. `[sourced: founder brief — this is the founder's call, not mine]`

### P4 — The promised time saving fails to materialize (deadline risk)  `[assumption]`
- **The pain:** because output needs manual rework (P1) and re-framing (P2), the AI tool saves less
  time than promised and the deadline gets tighter, not looser. `[assumption]` — grounded in the job's
  "on a deadline / without rebuilding by hand" and the founder's "saves less time than promised."
- **Score:** Severity **H** ⚙️ × Frequency **M** ⚙️ — but see overlap note. `[assumption]`
- **Class:** ⚙️ **table-stakes** (leaning) — "an AI tool should save time" is a baseline expectation
  every generator claims; failing it loses users but meeting it wins no one on its own. **Contested /
  overlap:** P4 is largely the *consequence* of P1+P2, not a separable pain — scoring it high risks
  double-counting, which is why Frequency is held to M for its independent portion. Flagged as a fork below.

### P5 — Credibility / meeting-outcome risk  `[assumption]`
- **The pain:** a templated or off-story deck makes the presenter look unprofessional and risks losing
  the meeting. `[assumption]` — grounded in the job's "present credibly and win the meeting."
- **Score:** Severity **H** ⚙️ (worst outcome — losing the deal) × Frequency **M** ⚙️ (high-stakes
  client meetings are frequent for this segment but not every deck). `[assumption]`
- **Class:** ⚙️ **differentiator** — credibility is what look+story buy. **Caveat:** this is really the
  *stake behind* P1/P2 (the job's "so that"), not a fully separable pain; risks the outcome-in-disguise
  anti-pattern. Kept in the table for completeness, flagged as a fork.

### P6 — Brand / visual consistency  `[assumption]`
- **The pain:** client-facing decks must match company (or client) brand; a generic AI look breaks brand
  consistency and needs manual correction. `[assumption]` — reasonable for sales/marketing client work;
  **not** named by the founder, so lowest confidence.
- **Score:** Severity **M** ⚙️ × Frequency **M** ⚙️. `[assumption]`
- **Class:** ⚙️ **table-stakes** — brand adherence is expected; it overlaps the "looks designed" axis but
  is a compliance baseline rather than a win.

## Ranking (order = rank; by Severity × Frequency, class is orthogonal)

Strict severity×frequency order puts the two H×H pains first, then the H×M cluster, then M×M. This
happens to surface the founder's three as the top 3 that carry forward — the two differentiators (look,
structure) plus the editability baseline — which matches the concept bet.

| Rank | Pain | Sev | Freq | Class | Confidence (existence) |
|------|------|-----|------|-------|------------------------|
| 1 | P1 — AI output "looks templated" → hand-redesign | H | H | differentiator | [sourced: founder brief] |
| 2 | P3 — Locked / image-only output can't be edited | H | H | table-stakes | [sourced: founder brief] |
| 3 | P2 — Wrong structure/story for the audience | H | M | differentiator | [sourced: founder brief] |
| 4 | P4 — Time saving fails to materialize (deadline risk) | H | M | table-stakes ⚙️ (contested) | [assumption] |
| 5 | P5 — Credibility / meeting-outcome risk | H | M | differentiator ⚙️ (outcome-adjacent) | [assumption] |
| 6 | P6 — Brand / visual consistency | M | M | table-stakes | [assumption] |

Notes on ties: ranks 3–5 are all H×M. Within the tie, P2 leads (founder-sourced + a load-bearing half of
the job); P4/P5 follow as `[assumption]` and each partly derivative of P1/P2. Every Sev/Freq value is a
⚙️ ordinal estimate `[assumption]` — see *Evidence standing*.

**Top 3 carried forward:** P1, P3, P2 — i.e. compete on look (P1) and structure/story (P2), with native
editability (P3) as the baked-in baseline gate. Consistent with the founder's boundary that editability
is table-stakes, not the differentiator.

## Desirability beliefs implied (described in words — orchestrator to mint the ids)

Each top pain is founder-observed but unproven by segment research, so each implies a **desirability**
hypothesis ("does this pain exist and matter enough?"):

1. **Behind P1 (look):** Salespeople & marketers experience AI decks as "templated" often enough and
   painfully enough that they routinely hand-redesign them — and output that genuinely *looks designed*
   would remove that rework. (desirability; strongest evidence — founder reports past behaviour, still
   single-source.)
2. **Behind P2 (structure/story):** For client-facing decks, wrong audience structure/story is a
   frequent, meeting-costing failure this segment can't cheaply fix themselves — so audience-right
   structure is a pain worth solving. (desirability.)
3. **Behind P3 (editability):** Non-editable/locked output is a hard non-starter for this segment;
   native editability is a required adoption baseline regardless of look. (desirability / table-stakes gate.)

The added `[assumption]` pains, if the orchestrator chooses to carry them, each also imply a desirability
belief: P4 — the segment's real complaint is net time-to-usable-deck, not raw generation; P5 — meeting
outcomes ride visibly on deck quality; P6 — brand consistency is a hard requirement for client work.
These are lower-confidence and I flag them as candidates, not recommendations to mint.

## Anti-patterns checked

- No feature-in-disguise (pains are obstacles in the job, not "they need our button"). P5/P6 flagged for
  the adjacent risks (outcome-in-disguise / compliance) and held below the founder pains.
- List is ranked and scored, not flat.
- The pitch leads on differentiators (P1/P2), not on the table-stakes gate (P3).
- No guessed number is presented as fact — all Sev/Freq are ⚙️ `[assumption]`.

## Open forks — for the human, NOT decided here

1. **Include the three added pains (P4/P5/P6) or fold them into P1/P2?**
   - (a) Keep all three ranked in the table (transparent, re-checkable next quarter — method's default).
   - (b) Keep only P6 (a genuinely distinct compliance pain); fold P4 (consequence) and P5 (outcome) into
     the P1/P2 narrative to avoid double-counting.
   - (c) Drop all three; carry only the founder's three.
   - ⚙️ **Recommendation:** (a) — the method says keep ranked pains, never delete; the overlap is noted so
     it won't inflate the CVP.
2. **Class of P4 (time saving): table-stakes vs differentiator?**
   - ⚙️ **Recommendation:** table-stakes — every AI generator promises time saving; Decksmith's *edge* is
     P1/P2, and net-time-saved is the by-product of solving them, not a separate axis to pitch.

## Could not do

- **No primary segment evidence.** The `evidence-source` prerequisite is met only by the founder brief
  (one observer). No interviews (count/who), no product metrics. So: pain *existence* for P1–P3 is
  `[sourced: founder brief]` but **every Severity/Frequency score is an `[assumption]`-grade ⚙️ estimate**,
  and the whole table should be treated as desirability hypotheses to test, not measured findings. To
  raise confidence, run `interview` / `analytics-search` on real salespeople & marketers.
- **No numeric evidence to cross-check.** Severity/Frequency are ordinal (H/M/L) judgments, not measured
  metrics — nothing here to reconcile across sources.
- Scope held to `#problems` for the lead segment only: no segmentation, no job re-derivation, no solution
  design, no moats.
