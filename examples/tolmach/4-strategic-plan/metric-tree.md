---
node_type: worklog
step: 4-strategic-plan
method: metric-tree
produces: metric-tree
status: draft
updated: 2026-08-14
---

# Worklog — Metric tree (Толмач, шаг 4)

Метод: `metric-tree` (North Star Framework). Определения узлов — в `registers/metric-tree.md`
(источник истины реестра); здесь — **рассуждение**: почему такой North Star, что отклонено, как
дерево остаётся лёгким на concept-viability. Значения — в `metrics.csv`.

## Выбор North Star (leading · value-repeating · strategy-encoding)

⚙️ **North Star = `M-northstar` «успешные живые разговоры на активную пару в неделю».**
- **Leading:** предшествует выручке/удержанию — растёт раньше монетизации.
- **Value-repeating:** повторяющийся живой разговор «его голосом» = ровно доставляемая ценность
  (не разовое событие).
- **Strategy-encoding:** кодирует ставку — не «переводы» (утилита субститута), а *живые разговоры
  пар* (арена + дифференциатор).

**Отклонённые кандидаты в North Star:**
- «Число переводов/минут перевода» — это метрика утилиты (субститута), не нашей ценности; растёт и у
  разового пользователя. Отклонено. [assumption]
- «MAU/DAU» — vanity, не кодирует ни арену, ни дифференциатор. Отклонено. [assumption]
- «Выручка» — лаговая, не leading; на concept-viability преждевременна. Отклонено. [assumption]

## Метрика, доказывающая концепт (главное на concept-viability)

⚙️ **`M-activation` (доля новых пар с ≥1 успешным живым разговором в W1)** — это и есть «одна
метрика, доказывающая, что концепт работает» (цель статуса). Если пары не доходят до *успешного*
живого разговора — концепт не desirable/feasible. [assumption]

## Кластер осуществимости (риск-№1 → `H-001`)

`M-latency` (задержка) · `M-voice-rating` (сохранённость голоса) · `M-breakdown` (срывы) — тройка,
что делает `H-001` **измеримой**. Единственное реальное показание — `M-latency` прототипа (1750 мс,
одна пара, НЕ реальная речь — `metrics.csv`), помечено `proxy`. Всё остальное not-instrumented до
прототипного теста (шаги 5–6). [sourced: founder brief] (задержка прототипа) + [assumption]

## Ветви и что отложено

- Активация → M-activation; качество/осуществимость → latency/voice/breakdown; удержание →
  M-w4-retention (когорт нет); монетизация → M-free-to-paid; usability/приватность → M-consent-rate.
- **Not-instrumented (→ шаги 5–6):** всё, кроме latency-proxy. Инструментовка — из `product-surface`
  (шаг 3). Держим дерево лёгким: 8 узлов, не строим полную декомпозицию до появления данных.

## Подразумеваемые связи (для global-hypotheses)

- `H-001` ↔ M-latency/M-voice-rating/M-breakdown; `H-003`/`H-017` ↔ M-voice-rating/M-activation;
  `H-004` ↔ M-breakdown; `H-018` ↔ M-free-to-paid; удержание ↔ M-w4-retention.

## Change log

### 2026-08-14 — created
- **From → To:** — → North Star (живые разговоры на пару/нед) + метрика-доказательство концепта
  (M-activation) + кластер осуществимости; 8 узлов, большинство not-instrumented
- **Why:** заполнить `{#metric-tree}`; дать лёгкое дерево concept-viability и привязку гипотез к узлам
- **Trigger:** шаг 4 (метрик-дерево — оркестратор)
