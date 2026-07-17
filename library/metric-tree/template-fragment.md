---
node_type: template-fragment
tool: metric-tree
produces: strategic-plan#metric-tree
---

```markdown
## Дерево метрик {#metric-tree}
_Метод: North Star Framework. Узлы — в реестре метрик (`registers/metric-tree.md` — определения,
`metrics.csv` — значения)._

**North Star:** `M-…` — <формула> [статус решения: ⚙️ / утверждено <кем, когда>]
_Почему она: leading / value-repeating / strategy-encoding — одной строкой каждое._

| Драйвер | Узел | Инпуты (узлы) | Instrumentation |
|---------|------|---------------|-----------------|
| <acquisition/активация> | `M-…` | `M-…` | instrumented/proxy/not |
| <conversion> | … | … | … |
| <deepening — ось стратегии> | … | … | … |
| <retention> | … | … | … |

**Guardrails:** `M-…` — <что не должно просесть и почему>.

**Не инструментировано (→ Шаги 5–6):** список узлов + чем закрывать.
```
