---
title: Greedy Best-First Search
type: concept
tags: [search, informed-search]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Greedy Best-First Search (Búsqueda voraz primero el mejor)

> **Summary (EN):** Greedy best-first search always expands the node that looks closest to the goal according to h(n), using a priority queue ordered by h. It makes the locally best choice without considering the cost already paid, so it is fast when the heuristic is good but not optimal, and complete only with repeated-state control in finite spaces. It can be trapped by a misleading heuristic.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Best-first search | Búsqueda primero el mejor | Familia: expandir el nodo con mejor valor de una función de evaluación f. |
| Greedy | Voraz | Aquí f(n) = h(n): solo mira lo que falta. |
| Priority queue | Cola de prioridad | Frontera ordenada por h(n). |

## Explicación

- **Función de evaluación:** f(n) = h(n).
- **Propiedades:** completo solo con control de estados repetidos (y espacio finito); **no óptimo**; puede quedar atrapado en caminos subóptimos si la heurística engaña. Peor caso tiempo y espacio O(b^m) (complemento AIMA); con buena heurística, mucho menos.

**Ejemplo Rumania (AIMA 3.5.1, complemento).** Desde Arad, greedy con h\_SLD va Arad → Sibiu (253) → Fagaras (176) → Bucarest: costo 140 + 99 + 211 = **450**, mientras el óptimo es **418** por Rimnicu Vilcea y Pitesti. Greedy llega rápido, pero no al mejor.

```
function GREEDY-BEST-FIRST(problem, h):
    frontier ← priority queue ordered by h, containing initial state
    explored ← ∅
    while frontier not empty:
        node ← pop lowest h
        if goal(node): return path(node)
        explored.add(node)
        for child in expand(node):
            if child not in explored and not in frontier:
                frontier.push(child, h(child))
    return failure
```

**En la tarea** ([Deber 1](../assignments/deber-1-search-problems.md)): `best_fs(start, goal, heuristic)` resolvió el 8-puzzle en 6 movimientos generando 15 estados (Manhattan) vs. 135 de BFS. El 80-puzzle (`resolver_80_tile`) usa la misma idea con Manhattan.

## Errores comunes y tips de examen

- Greedy usa **solo h**; A\* usa **g + h**. Esta diferencia es la que da optimalidad a A\*.
- Que greedy encontrara el óptimo en el 8-puzzle de la tarea fue suerte del caso, no una garantía.

## Relacionado

- [A* Search](a-star-search.md)
- [Heuristics](heuristics.md)
- [Uninformed Search](uninformed-search.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 12–13.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5.1.
