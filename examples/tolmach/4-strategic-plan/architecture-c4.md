---
node_type: worklog
step: 4-strategic-plan
method: architecture-c4
produces: architecture-instrumentation
status: draft
updated: 2026-08-14
---

# Worklog — Architecture & instrumentation (Толмач, шаг 4)

Метод: `architecture-c4` (primary) + `product-surface` (contributing). Уточняет архитектуру и
инструментовку шага 3: **откуда метрик-дерево берёт данные** и **что драйвит инфра-стоимость**.

## Уточнение (от C4 Context шага 3)

Контекст не меняется (шаг 3): один блок Толмач, акторы A/B, внешние foundation-модели. Здесь
добавляем **связь поверхность → инструментовка → узел метрик** и **драйверы стоимости**.

| Поверхность/компонент | Instrumentation | Данные (→ узел) | Драйвер инфра-стоимости |
|---|---|---|---|
| Конвейер перевода (client-side телеметрия) | proxy (на прототипе) → instrumented (план) | задержка → `M-latency`; срыв → `M-breakdown` | **инференс foundation-моделей пер-минуту (ASR+MT+TTS+voice-clone)** — главный COGS |
| Онбординг двоих + сессия разговора | not-instrumented → instrumented (план) | активация → `M-activation`; разговоры/нед → `M-northstar` | product-analytics (малый) |
| Пост-сессионный опрос | not-instrumented | рейтинг голоса → `M-voice-rating` | — |
| Контур согласия на голос | not-instrumented | согласие → `M-consent-rate` | хранилище голосовых профилей (R-007) |
| Биллинг | not-instrumented | free→paid → `M-free-to-paid` | провайдер платежей (малый) |
| Повторные разговоры | not-instrumented | удержание → `M-w4-retention` | product-analytics |

## Главный вывод для экономики

⚙️ **Драйвер COGS — инференс foundation-моделей в реальном времени, тяжелее всего voice-clone TTS.**
Стоимость **линейна по минутам живого разговора** (внешние API, нет экономии масштаба на compute) →
это и потолок в финмодели, и вход в unit-economics. Развилка «свои vs внешние модели» (шаг 3, ⚙️
гибрид) прямо двигает `R-004` и эту COGS-линию. [assumption]

## Change log

### 2026-08-14 — created
- **From → To:** — → связь поверхность→инструментовка→узел метрик + драйверы стоимости; главный
  COGS = инференс real-time (voice-clone), линеен по минутам
- **Why:** заполнить `{#architecture-instrumentation}`; проследить источники данных метрик и драйверы COGS
- **Trigger:** шаг 4 (оркестратор)
