---
node_type: template-fragment
tool: unit-economics
produces: strategic-plan#unit-economics
---

```markdown
## Юнит-экономика {#unit-economics}
_Метод: contribution margin, LLM-инференс — явная строка COGS. Две базы: operational / honest._

| Показатель | Operational | Honest (+износ/рыночный compute) | Допущения |
|-----------|-------------|----------------------------------|-----------|
| Выручка на платящего (blended, ₽/мес) | | | |
| COGS на платящего (₽/мес) | | | [assumption: правило аллокации] |
| Вклад (₽/мес · %) | | | |
| CAC (по каналам) | | | [sourced/⚙️] |
| Payback | | | |
| LTV | — сценарии по churn X/Y/Z% ⚙️ — | | до инструментовки честного churn |

**По тарифам:** <строка на тариф: цена · факт-ARPPU · вклад в обеих базах>
**Кто несёт free/грантовое потребление:** <явное решение>
**Сегменты-исключения:** <например, полигон-аккаунты — вклад в honest-базе>
```
