---
title: Greedy Best-First Search
type: concept
tags: [search, informed-search]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# Greedy Best-First Search (Búsqueda voraz primero el mejor)

> **Summary (EN):** Greedy best-first search always expands the node that looks closest to the goal according to h(n), using a priority queue ordered by h. It makes the locally best choice without considering the cost already paid, so it is fast when the heuristic is good but not optimal, and complete only with repeated-state control in finite spaces. It can be trapped by a misleading heuristic.

> **En palabras simples (ES):** Greedy (voraz) va siempre hacia el lugar que **parece** más cerca de la meta, como caminar hacia una torre que ves a lo lejos sin mirar si el camino da vueltas. Ignora cuánto ya caminaste. Es rápido, pero puede no dar el camino más corto. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Best-first search | Búsqueda primero el mejor | Familia: expandir el nodo con mejor valor de una función de evaluación f. |
| Greedy | Voraz | Aquí f(n) = h(n): solo mira lo que falta. |
| Priority queue | Cola de prioridad | Frontera ordenada por h(n). |

## Explicación

- **Función de evaluación:** f(n) = h(n).
- **Propiedades:** la versión *graph search* es completa en espacios finitos, pero no en infinitos; **no óptimo**; puede quedar atrapado en caminos subóptimos si la heurística engaña. Peor caso tiempo y espacio O(|V|) (AIMA §3.5.1); con una buena heurística puede bajar a O(b·m).
- En Rumania con h\_SLD, greedy **no expande ningún nodo fuera del camino** que encuentra — pero ese camino es 32 millas más largo que el óptimo. "Greediness can lead to worse results than being careful."
- Es el extremo W = ∞ de weighted A\* (ver [A\*](a-star-search.md)). *Speedy search* es greedy usando como h el número estimado de acciones (ignora costos).

**Ejemplo Rumania (AIMA §3.5.1, Fig. 3.17).** Desde Arad, greedy con h\_SLD va Arad → Sibiu (253) → Fagaras (176) → Bucarest: costo 140 + 99 + 211 = **450**, mientras el óptimo es **418** por Rimnicu Vilcea y Pitesti. Greedy llega rápido, pero no al mejor.

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

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Greedy (voraz) va siempre hacia el lugar que **parece** más cerca de la meta, como caminar hacia una torre que ves a lo lejos sin mirar si el camino da vueltas. Ignora cuánto ya caminaste. Es rápido, pero puede no dar el camino más corto.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| h(n) | cuánto creo que falta desde n hasta la meta (p. ej. línea recta) | heuristic |
| f(n) = h(n) | el número con el que greedy ordena la frontera: solo la estimación | evaluation function |
| Frontera | lista de lugares pendientes por revisar | frontier |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Put the start in a priority queue ordered by h.
   - *ES:* Pon el inicio en una lista ordenada por la estimación h.
2. Take the node with the SMALLEST h (the one that looks closest to the goal).
   - *ES:* Saca el que parece estar más cerca de la meta.
3. If it is the goal → return the path.
   - *ES:* Si es la meta, termina.
4. Add its unexplored children with their h values, and go back to step 2.
   - *ES:* Agrega sus vecinos no revisados con su h y repite.

**Ejemplo con números:** de Arad a Bucarest. Vecinos de Arad: Sibiu h=253, Timisoara h=329, Zerind h=374 → va a **Sibiu** (menor h). Vecinos de Sibiu: Fagaras h=176, Rimnicu Vilcea h=193, … → va a **Fagaras**. Vecino de Fagaras: Bucarest h=0 → llega. Camino Arad–Sibiu–Fagaras–Bucarest = 140 + 99 + 211 = **450 km**. Pero existe uno de **418 km** por Rimnicu Vilcea y Pitesti: greedy no es óptimo.

**Say it in the exam (EN):** "Greedy best-first search expands the node with the lowest h(n), the one that looks closest to the goal, and ignores the cost already paid. It is often fast, but it is not optimal — on Romania it returns 450 km instead of 418 km — and it is complete only in finite spaces when it avoids repeated states."

**Dilo así (ES):** "Greedy expande el nodo con menor h(n), el que parece más cerca de la meta, e ignora lo que ya costó llegar. Suele ser rápido, pero no es óptimo (en Rumania da 450 km en vez de 418) y solo es completo en espacios finitos si evita repetir estados."

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
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5.1 (ingestado).
