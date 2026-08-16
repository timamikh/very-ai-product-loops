---
node_type: reference
title: Moat taxonomy — base vs derivative
status: draft
version: 0.2.0
updated: 2026-08-16
---

# Moat taxonomy — base vs derivative

Deeper notes behind `value-definition-concept` (Step 1, base moats) and
`value-definition-strategy` (Step 3, derivatives). The core idea: some moats are **primitives** you can
hold directly; others are **derivatives** that only exist once a primitive meets a customer or
scale. Confusing the two is the most common mistake — claiming a derivative (network effects,
lock-in) at concept stage, before there is anything to derive it from.

## Base (primitive) moats

| Moat | Layer | What makes it hold | Fails when |
|------|-------|--------------------|-----------|
| Unique data | hard | Others can't assemble the dataset | The data is public or easily re-collected |
| Unique algorithms / IP | hard | Genuinely differentiated + protected/tacit | The method is standard or easily reproduced (esp. by an LLM) |
| Exclusive access / integrations / rights | hard | Privileged distribution, data, or legal rights | The access is open to anyone |
| Audience / distribution | soft | Cheap reach to demand others lack | The channel is rented and can be cut off |
| Brand / trust | soft | Chosen because of who you are | Trust hasn't been earned yet |
| Expertise | soft | Slow-to-build depth | The domain is shallow or well-documented |
| Processes (speed & precision) | soft | Ship & iterate faster/more accurately | Everyone ships at the same speed |
| Product complexity / depth | soft | Hard-to-replicate surface area | The surface is thin |
| Real-world assets / IRL processes | soft | Physical assets or offline ops an IT-only rival can't cheaply copy (servers, facilities, licences) | The asset is rentable/commoditized, or the ops are digital-only |

## Derivative moats

| Derivative | Derives from | Precondition | Note |
|------------|--------------|--------------|------|
| Lock-in / switching costs | exclusive access/integration | an **existing customer** embedded in it | Strongest when tied to the customer's own data/workflow |
| Network effects | audience | enough users that value grows with each new one | Not every audience creates them |
| Economies of scale / cost advantage | audience / scale | volume | Turns a soft barrier into a cost moat |

## Why post-AI

Before cheap LLM-built software, the product itself could be a moat — building it was hard.
Now the build is commoditized, so defensibility shifts entirely to what LLMs can't cheaply
replicate: proprietary **data**, real-world **access**, earned **trust/brand**, owned
**distribution/audience**, and **execution** speed. When rating any moat, apply the test:
*would this survive a competitor rebuilding the app with an LLM tomorrow?* If not, it's a
feature to enjoy, not a moat to bet on.
