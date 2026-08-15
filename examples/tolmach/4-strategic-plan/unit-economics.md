---
node_type: worklog
step: 4-strategic-plan
method: unit-economics
produces: unit-economics
status: draft
updated: 2026-08-14
---

# Worklog — Unit economics (Толмач, шаг 4)

Метод: `unit-economics` (contribution margin; LLM-инференс как явная COGS-линия). Стадия
concept-viability → **плейсхолдеры**, WTP и COGS — явные гипотезы, не факты. Compute — **внешние
API** (архитектура ⚙️ гибрид, старт на внешних) → «честный/с амортизацией» базис **не применяется**
(он только для own-GPU); базисы схлопываются в один operational. [sourced: 3-strategy `#architecture`]

## Таблица (все числа ⚙️ плейсхолдеры, широкие погрешности)

| Метрика | Operational (⚙️) | Допущения |
|---|---|---|
| Revenue per payer ($/мес) | ~$10 | тир better midpoint; якорь WTP `H-015` (dating $16–28 / утилита $5) [assumption] |
| COGS per payer ($/мес) | ~$2–6 | **инференс real-time**, тяжелее всего voice-clone TTS; линейно по минутам live; ⚙️ активный платящий = ~X минут/мес (to-clarify) [assumption] |
| Contribution ($/мес · %) | ~$4–8 · ~40–70% | revenue − COGS; **чувствителен к COGS voice-clone** — при высокой цене инференса contribution уходит к нулю [assumption] |
| CAC (по каналу) | ~$15–40 | нишевые ручные каналы дешевле платного; данных нет → гипотеза [assumption] |
| Payback | ~3–8 мес | CAC / contribution [assumption] |
| LTV | ~$40–80 (сценарии churn 5/10/15%/мес ⚙️) | когорт нет → LTV = contribution / churn; **не** измеренная кривая (`#retention`) [assumption] |

## Ключевой вывод (риск экономики)

⚙️ **LTV/CAC ≈ 1.5–4× — на грани.** Определяющая неопределённость — **COGS инференса real-time
voice-clone**: если он ближе к верхней границе, contribution проваливается, и вся модель
нежизнеспособна при цене ~$10. Это порождает: (а) гипотезу `H-018`-квантификацию (contribution > 0
после COGS), (б) риск `R-012` (COGS voice-clone съедает contribution). → развилка «свои vs внешние
модели» и оптимизация инференса становятся экономическим приоритетом, не только техническим. [assumption]

## Подразумеваемые регистры (словами; id чеканит оркестратор)

- **Гипотеза (viability):** при выбранной цене contribution положителен ПОСЛЕ COGS real-time
  voice-clone (квантифицирует `H-018`). → global-hypotheses.
- **Риск (financial):** COGS перевода в реальном времени (voice-clone) съедает contribution ниже
  жизнеспособности. → risk register (`R-012`).

## Change log

### 2026-08-14 — created
- **From → To:** — → unit-economics плейсхолдеры; COGS = real-time инференс (voice-clone), внешние API
  → один базис; LTV/CAC на грани; COGS — определяющая неопределённость
- **Why:** заполнить `{#unit-economics}`; сделать LLM-инференс явной COGS-линией; вскрыть риск экономики
- **Trigger:** шаг 4 (оркестратор)
