---
node_type: worklog
step: 5-tactical-plan
method: metric-tree
produces: goal-targets
status: draft
updated: 2026-08-14
---

# Worklog — Goal targets (Толмач, шаг 5)

Метод: `metric-tree` (привязка целей). go-to-market → узел `M-…`; technical & back-office → DoD.
Узлы определены на шаге 4 (`registers/metric-tree.md`). Baseline на concept-viability пустой
(данных нет), кроме `M-latency` (прототип).

| Цель | Направление | Target: `M-…` или DoD | Baseline → target |
|---|---|---|---|
| Прототип мерит осуществимость на реальной речи | development | DoD: инструментованный прототип снимает `M-latency`/`M-voice-rating`/`M-breakdown` на ≥8–10 реальных пар | — → DoD |
| Пары доходят до успешного живого разговора | go-to-market | `M-activation` | — → ⚙️≥40% W1 |
| Голос воспринимается как «его/её», а не робот | go-to-market | `M-voice-rating` | — → ⚙️≥4.0/5 |
| Задержка приемлема на реальной речи | go-to-market | `M-latency` | 1750мс (прототип, 1 пара) → ⚙️≤800–1000мс на реальной речи |
| Контур согласия готов | back-office | DoD: явное согласие на голос, без сырого аудио, отзыв | — → DoD |

⚙️ Все таргеты — гипотезы порогов (см. `#global-hypotheses` шага 4), утверждает человек. [assumption]

## Change log
### 2026-08-14 — created
- **From → To:** — → цели привязаны: dev/back-office → DoD, go-to-market → узлы M-activation/voice/latency
- **Why:** заполнить `{#goal-targets}`
- **Trigger:** шаг 5 (оркестратор)
