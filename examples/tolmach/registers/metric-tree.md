---
node_type: register
register: metric-tree
title: Метрик-дерево — Толмач
status: draft
updated: 2026-08-14
---

# Метрик-дерево — Толмач

Одна каноническая декомпозиция North Star. **Определения узлов — здесь; значения — в `metrics.csv`**
(append-only, дата на каждой строке). Рождается на шаге 4. Схема — `process/REGISTERS.md`.

Стадия concept-viability → дерево **лёгкое**: одна метрика, доказывающая концепт (активация), +
кластер осуществимости (риск-№1), остальное **not-instrumented** (продукта/пользователей нет).
Единственное реальное показание на сегодня — задержка прототипа (слабое, не на реальной речи).

| ID <!--c:id--> | Имя <!--c:name--> | Определение <!--c:definition--> | Ед. <!--c:unit--> | Kind <!--c:kind--> | Instrumentation <!--c:instrumentation--> | Parent | Target | Owner | Source | Note |
|----|------|------------|-----|------|-----------------|--------|--------|-------|--------|------|
| M-northstar | Живые разговоры на пару в неделю | Успешных живых разговоров (обе стороны, ≥N минут, без срыва) на активную пару в неделю | count | derived | not-instrumented | — | ⚙️ определить на прототипе | PO | product-analytics (планируется) | value-repeating; окно недели |
| M-activation | Активация пары W1 | Доля новых пар с ≥1 успешным живым разговором в первую неделю (W1) | % | measured | not-instrumented | M-northstar | ⚙️ ≥40% W1 | PO | product-analytics (планируется) | **метрика, доказывающая концепт**; «успешный» — порог to-clarify |
| M-latency | Задержка реплики (медиана) | Медианная end-to-end задержка реплики (конец фразы говорящего → озвучен перевод) | ms | measured | proxy | M-activation | ⚙️ ≤800–1000 мс на реальной речи | tech | client-side телеметрия / прототип | риск-№1 (`H-001`); прототип ≠ реальная речь |
| M-voice-rating | Рейтинг сохранённости голоса | Средний рейтинг «слышу его/её, а не робота» (пост-сессия, 1–5) | score | measured | not-instrumented | M-activation | ⚙️ ≥4.0/5 | PO | micro-survey (планируется) | дифференциатор M2 (`H-003`/`H-017`) |
| M-breakdown | Срывов на разговор | Число срывов диалога (переспрос/переключение на жесты) на один разговор | count | measured | not-instrumented | M-activation | ⚙️ ≤1 на разговор | tech | телеметрия/опрос (планируется) | непрерывность (`H-004`); определение «срыва» to-clarify |
| M-free-to-paid | Конверсия free→paid | Доля пар, перешедших из free в платный тир (за окно N) | % | measured | not-instrumented | — | ⚙️ ≥3–5% | PO | биллинг (планируется) | монетизация (`H-018`); бизнес-ветвь |
| M-w4-retention | Удержание пар W4 | Доля пар с повторными живыми разговорами на неделе 4 | % | measured | not-instrumented | M-northstar | ⚙️ определить (когорт нет) | PO | product-analytics (планируется) | когорт нет (concept-viability); вход в LTV |
| M-consent-rate | Доля согласий на голос | Доля пользователей, давших явное согласие на голосовой профиль | % | measured | not-instrumented | M-activation | ⚙️ ≥90% | PO | контур согласия (планируется) | usability/приватность (`R-007`/`R-009`) |

**Not instrumented (→ шаги 5–6):** все узлы, кроме `M-latency` (proxy на прототипе). Инструментовку
даёт `product-surface` (шаг 3): client-side телеметрия латентности/качества, product-analytics
воронки (activation/retention), micro-surveys (voice-rating), биллинг (free→paid), контур согласия
(consent). Числа/цели ⚙️ — утверждает человек; когорты удержания появятся только с пользователями.

## Change log

### 2026-08-14 — рождён на шаге 4 (M-northstar…M-consent-rate)
- **From → To:** — → 8 узлов; North Star = живые разговоры на пару в неделю; метрика, доказывающая
  концепт = `M-activation` (W1); кластер осуществимости = `M-latency`/`M-voice-rating`/`M-breakdown`
  (риск-№1). Значения см. `metrics.csv` — на сегодня одна строка (`M-latency`, прототип).
- **Why:** шаг 4 строит метрик-дерево; на concept-viability оно лёгкое — большинство узлов
  not-instrumented (продукта нет), инструментовка определена в `product-surface` шага 3.
- **Trigger:** шаг 4 прогона (метрик-дерево — оркестратор).
