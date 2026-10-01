---
title: A* Search
type: concept
tags: [search, informed-search, a-star]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# A* Search (Búsqueda A*)

> **Summary (EN):** A* expands the node with the lowest f(n) = g(n) + h(n), where g is the actual cost so far and h the heuristic estimate to the goal; f estimates the total cost of the cheapest solution through n. With an admissible heuristic (tree search) or a consistent one (graph search), A* is complete and optimal. Its weakness is memory: it keeps every generated node, O(b^d). On the Romania map it finds the 418 km route Arad–Sibiu–Rimnicu Vilcea–Pitesti–Bucharest expanding 5 nodes, versus 9 for Dijkstra.

## Términos clave

| English | Español | Significado |
|---|---|---|
| g(n) | g(n) | Costo real acumulado desde el inicio hasta n. |
| h(n) | h(n) | Estimación heurística del menor costo de n a la meta. |
| f(n) = g(n) + h(n) | f(n) | Costo total estimado de la solución que pasa por n. |
| Admissible / Consistent | Admisible / Consistente | Ver [Heuristics](heuristics.md). |
| Optimally efficient | Óptimamente eficiente | Ningún algoritmo óptimo con la misma h expande menos nodos (complemento). |

## Explicación

**Intuición.** A\* no solo mira qué tan cerca *parece* estar la meta (h, como greedy), sino también cuánto ya costó llegar (g, como Dijkstra). Combina lo mejor de ambos.

**Propiedades (slides 02, s14):**
- **Completo:** si existe solución y h es admisible (y además *b* finito, costos ≥ ε > 0).
- **Óptimo:** si h es admisible (búsqueda en árbol) / consistente (búsqueda en grafo).
- **Espacio:** O(b^d) — guarda todos los nodos en memoria. Es su principal limitación.
- **Tiempo:** depende de la calidad de h.

```
function A-STAR(problem, h):
    g[start] ← 0;  f[start] ← h(start)
    frontier ← {start};  explored ← ∅;  parent[start] ← None
    while frontier not empty:
        n ← node in frontier with lowest f
        if goal(n): return reconstruct_path(parent, n)
        frontier.remove(n);  explored.add(n)
        for (m, cost) in neighbors(n):
            if m in explored: continue
            if g[n] + cost < g[m]:
                g[m] ← g[n] + cost
                f[m] ← g[m] + h(m)
                parent[m] ← n
                frontier.add(m)
    return failure
```

Así está implementado `a_estrella()` en la tarea [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md).

## Ejemplo — Arad → Bucarest (AIMA Fig. 3.18)

| Paso | Expande | f = g + h | Nuevos en la frontera (f) |
|---|---|---|---|
| 1 | Arad | 0 + 366 = 366 | Sibiu 393, Timisoara 447, Zerind 449 |
| 2 | Sibiu | 140 + 253 = 393 | Rimnicu V. 413, Fagaras 415, Oradea 671 (Arad ya explorado) |
| 3 | Rimnicu Vilcea | 220 + 193 = 413 | Pitesti 417, Craiova 526 |
| 4 | Fagaras | 239 + 176 = 415 | Bucharest 450 |
| 5 | Pitesti | 317 + 100 = 417 | **Bucharest mejora a 418** (Craiova sigue en 526) |
| 6 | Bucharest | 418 + 0 = 418 | ✅ meta |

Observa el paso 4–5: Bucarest entra con f = 450 vía Fagaras, pero A\* **no** se detiene al *generar* la meta; se detiene al *expandirla*. Antes expande Pitesti (417 < 450) y encuentra el camino de 418. Por eso es óptimo.

Resultado real de la tarea: A\* 5 nodos expandidos, Dijkstra 9, ambos con costo 418.

## Errores comunes y tips de examen

- **Probar la meta al expandir, no al generar** — si no, se pierde la optimalidad (el 450 vía Fagaras).
- Con h = 0, A\* = UCS/Dijkstra. Con f = h, es greedy.
- Si h sobreestima, A\* puede devolver una solución subóptima (pero a veces más rápido: *weighted A\**).
- Complejidad espacial exponencial → variantes como IDA\* o SMA\* (AIMA §3.5.5, complemento).

## Relacionado

- [Heuristics](heuristics.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Uninformed Search](uninformed-search.md) (UCS/Dijkstra)
- [A* vs Dijkstra assignment](../assignments/astar-vs-dijkstra.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 14–15.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5.2 y Fig. 3.18 (traza: complemento verificado ejecutando la tarea).
