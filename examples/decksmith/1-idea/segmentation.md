---
node_type: worklog
method: segmentation
produces: segments
step: 1-idea
status: draft
updated: 2026-08-14
---

# Worklog — Segmentation (Decksmith, Step 1)

> Source of truth for the `{#segments}` section. Projection shape:
> `tool-skills/library/segmentation/template-fragment.md`.
> All method proposals are ⚙️ and awaiting the human's decision. Inputs from the founder brief
> keep their `[sourced: founder brief]` tag; my own reasoning is `[assumption]`.

## Prerequisites check (before running)

- **Concept** — present: native-editable **AND** designed AI decks (real `.pptx`/`.key` shapes
  that also look designed). `[sourced: founder brief]` — prerequisite met.
- **Audience knowledge or analytics** — thin. We have the founder's field observations (sales &
  marketing regenerate AI output by hand; decks come back with the wrong structure) and one stated
  bet, but **no interviews and no usage data**. `[sourced: founder brief]`. Per the method, at this
  concept-viability stage this is expected to be thin, so every cut below stays `[assumption]`
  unless it is the founder's own stated bet. Prerequisite met at the "expected-thin" bar; see
  *Could not do* for what evidence would upgrade the tags.

**Evidence basis of this segmentation (stated plainly, per method step 5):** this rests on
**desk reasoning over one founder brief** — not customer conversations, not usage data. It fails the
way desk research fails: the cut can look clean and still not match how buyers actually group. Treat
the whole table as an audience *hypothesis*.

## Step 1 — Candidate cuts on ≥3 different bases, and what was rejected

The founder's framing is needs/job-based: *people who make client-facing decks often and are judged
on how those decks look*, cut by **use-context × stakes/frequency**. I list candidate bases before
choosing, so the choice is a choice and not the org's default cut.

| # | Basis | Verdict | Reasoning |
|---|-------|---------|-----------|
| 1 | **Use-context × stakes × frequency** (what the deck is *for*, who judges it, how high the stakes, how often) | **CHOSEN** | Predicts different needs directly: high-frequency + high-stakes + externally-judged deck-makers need speed **and** design **and** editability **and** the right structure at once — exactly the both-pains the concept attacks. `[assumption]` |
| 2 | Company size / firmographics (SMB vs enterprise) | Rejected | The firmographic reflex — the cut the market is already structured around. An SMB seller and an enterprise seller face the *same* deck job; size does not predict a different deck need. `[assumption]` |
| 3 | Job title alone (demographic role) | Rejected | Title without context does not predict need: a "marketer" writing an internal report and a marketer building an external pitch have different needs. The context, not the title, carries the signal — folded into cut #1. `[assumption]` |
| 4 | Willingness-to-pay / buyer-vs-user | Rejected **as the primary cut, kept as a secondary lens** | Monetization and WTP are deliberately deferred to Strategy `[sourced: founder brief]`, so we cannot evidence a WTP cut now. But "a company budget sits behind the purchase" is a real signal for the lead, so I carry buyer-vs-user as a secondary annotation, not the spine. `[sourced: founder brief]` / `[assumption]` |
| 5 | Buying trigger (new pitch, fundraise, campaign launch, QBR) | Rejected as spine, **folded in** | A useful sub-dimension but it largely tracks use-context; it sharpens tiers rather than forming a separate spine. `[assumption]` |
| 6 | Behaviour (deck-making frequency + already hand-regenerating AI output) | **Folded into the chosen cut** | This is the *frequency* axis of cut #1 and the strongest observed pain signal `[sourced: founder brief]` — kept inside the spine, not as a rival cut. |

**Chosen cut basis (for the section header):** we segment by **use-context crossed with
stakes × frequency** — what the deck is for, who judges it, how high the stakes are, and how often
the person makes one. This predicts different needs because the concept's value (editable **and**
designed **and** right-structured, fast) compounds exactly where stakes and frequency are both high
and the audience is external. `[assumption]`, with the lead placement `[sourced: founder brief]`.

## Step 2–3 — Named segments, why each matters, and where to reach them

### Priority 1 (lead) — Salespeople & marketers making client-facing decks
- **How it's cut:** use-context = external client/prospect-facing decks (pitches, proposals, sales
  collateral, campaign one-pagers); **high frequency × high stakes**; usually a **company budget**
  behind the purchase. `[sourced: founder brief]`
- **Why it matters:** highest frequency × stakes of any candidate, they already hand-regenerate AI
  output because it "looks templated," and a budget exists to pay — the founder's stated lead.
  `[sourced: founder brief]`. Best fit with the moat: they feel **both** halves of the pain
  (templated look **and** wrong structure). `[assumption]`
- **Where to reach them:** ⚙️ *genuinely open — see fork F1.* Candidate channels: sales/marketing
  communities (RevOps, sales-enablement Slack/Discord), LinkedIn, sales-enablement tool ecosystems
  (integration/partner surfaces), marketing/growth newsletters, sales conferences. `[assumption]`
- **Confidence:** segment existence + lead rationale `[sourced: founder brief]`; specific channels
  `[assumption]` ⚙️.

### Priority 2 — Founders / startup teams making fundraising & pitch decks
- **How it's cut:** use-context = investor/partner-facing pitch & fundraise decks; **very high
  stakes** (money on the line) but **episodic frequency** (fundraise cycles, not weekly). `[assumption]`
- **Why it matters:** feels both pains acutely — a bad-looking or badly-structured pitch deck has an
  outsized cost — and is unusually *reachable* as a group (accelerators, startup communities). Lower
  than lead only because frequency is episodic, so retention/repeat-use is thinner. `[assumption]`
- **Where to reach them:** accelerators/incubators (YC, Techstars), angel/VC networks, startup
  communities (IndieHackers, startup X/Twitter, founder Slacks). `[assumption]`
- **Confidence:** `[assumption]`.

### Priority 3 — Independent consultants & agencies
- **How it's cut:** use-context = client-facing decks (proposals, readouts, workshop decks);
  design-judged; moderate–high frequency. `[assumption]`
- **Why it matters:** real volume and clearly reachable, but **weaker moat fit** — many already have
  design capability, so the "look designed" half of the value is less decisive; their sharper need
  is speed + editability. Kept as a distinct tier, not dropped. `[assumption]`
- **Where to reach them:** consulting communities, agency networks, Upwork/Fiverr deck-work,
  LinkedIn. `[assumption]`
- **Confidence:** `[assumption]`.

### Priority 3 — Internal deck-makers (analysts / PMs / ops making board & exec updates)
- **How it's cut:** use-context = internal board/exec/team decks; **high frequency** but **lower
  external stakes** (internal audience); editability matters, polished design matters less. `[assumption]`
- **Why it matters:** large volume and reachable inside companies, but the "look designed" half of
  the moat is weaker for an internal audience, so it sits below the externally-judged tiers. `[assumption]`
- **Where to reach them:** PM/ops communities, corporate/internal-comms channels, enterprise sales
  motion. `[assumption]`
- **Confidence:** `[assumption]`.

### Priority 3 — Freelance / in-house designers making decks for others
- **How it's cut:** use-context = decks produced as a design deliverable; high design taste already
  in-house. `[assumption]`
- **Why it matters:** lowest moat fit of the set — they can design themselves, so "designed output"
  is not their gap; they may value native-editability/speed, or may even be adjacent to a competitor
  behaviour. Kept for completeness, lowest tier. `[assumption]`
- **Where to reach them:** design communities (Dribbble, Behance), design Slacks/Discords. `[assumption]`
- **Confidence:** `[assumption]`.

## Step 4 — Priority tiers and the ground that decided each placement

Grounds per method: **need-difference × reachability × fit with the moat** (moat = native-editable
AND designed, from the concept).

| Priority | Segment | Deciding ground |
|----------|---------|-----------------|
| 1 (lead) | Salespeople & marketers | **Fit-with-moat + frequency×stakes + budget** — feels both pains, pays, and recurs. Matches the founder's stated bet. `[sourced: founder brief]` |
| 2 | Founders / pitch-deck makers | **Need-difference + reachability** — acute both-pains and very reachable via accelerators; below lead only on **frequency** (episodic). `[assumption]` |
| 3 | Independent consultants & agencies | **Weaker moat fit** — many can already design; need is more speed/editability than "designed". `[assumption]` |
| 3 | Internal deck-makers | **Weaker moat fit** — internal audience lowers the design-stakes half of the value, despite high frequency. `[assumption]` |
| 3 | Freelance / in-house designers | **Lowest moat fit** — design is their skill, not their gap. `[assumption]` |

⚙️ **Recommended lead:** Salespeople & marketers — build for them first because they are the only
candidate that combines high frequency, high stakes, both-pains, a budget, and nameable channels.
This aligns with the founder's stated bet. **The final lead choice is the human's** (fork F2).

## Step 5 — Implied beliefs for the orchestrator to mint (I do NOT allocate ids)

Each segment carries a "segment X exists, is reachable at Y, and feels the pain enough to switch"
belief. Described in words for the orchestrator to mint as `H-…` in the hypothesis register:

1. **Lead:** *Salespeople & marketers who make client-facing decks often exist as a reachable
   segment (via sales/marketing communities, LinkedIn, sales-enablement ecosystems) and feel the
   both-pains — templated look + wrong structure — strongly enough to switch from their current
   tool.* Rests on `[sourced: founder brief]` for existence/lead rationale; reachability + switch
   intent are `[assumption]` (unevidenced).
2. **Founders:** *Founders making fundraise/pitch decks are reachable via accelerators & startup
   communities and feel design-stakes pain enough to adopt for an episodic, high-stakes job.* `[assumption]`
3. **Consultants & agencies:** *reachable via consulting/agency networks; their switch driver is
   speed + editability more than "designed".* `[assumption]`
4. **Internal deck-makers:** *reachable inside companies; switch driver is editability + speed, with
   design a weaker pull for an internal audience.* `[assumption]`
5. **Designers:** *reachable via design communities; weakest switch case since design is not their
   gap.* `[assumption]`

(The orchestrator decides which of these become register rows and mints the ids. Hypothesis 1 is the
load-bearing one for the lead.)

## Open forks — the human decides

- **F1 — Lead reach-channel (genuinely open).** Where to first reach salespeople & marketers:
  - **(a) Community + content** (RevOps/sales-enablement Slack/Discord, growth newsletters) — low
    cost, high trust, slow to scale.
  - **(b) LinkedIn outbound / social** — fast to start, targetable by role+context, noisy/low trust.
  - **(c) Sales-enablement tool ecosystem partnerships** (integration/partner surfaces) — high intent,
    warm context, but dependency on a partner and slow to land.
  - **(d) Conferences / events** — dense high-stakes buyers, expensive, episodic.
  - ⚙️ **Recommendation:** start with **(a) community + content** to learn the language and pains
    cheaply, and run **(b)** in parallel as a targeting test; treat (c) as a later scale lever.
    `[assumption]` — human decides.
- **F2 — Confirm the lead.** ⚙️ recommend **salespeople & marketers** (matches founder bet); the
  human confirms or overrides. Not closed here.

## Change log
- 2026-08-14 — first draft: chosen cut basis (use-context × stakes × frequency), 4 rejected bases,
  lead + 4 runner-up tiers, 5 implied beliefs described, forks F1/F2 opened.
