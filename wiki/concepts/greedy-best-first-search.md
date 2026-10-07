---
title: Greedy Best-First Search
type: concept
tags: [search, informed-search]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# Greedy Best-First Search (Búsqueda voraz primero el mejor)

> **Summary (EN):** Greedy best-first search always expands the node that looks closest to the goal, the one with the smallest heuristic h(n), using a priority queue ordered by h. It ignores the cost already paid, so it is often fast with a good heuristic but it is not optimal, and it is complete only in finite spaces when it avoids repeated states. A misleading heuristic can lead it astray.

> **En palabras simples (ES):** Greedy (voraz) va siempre hacia el lugar que **parece** más cerca de la meta, como caminar hacia una torre que ves a lo lejos sin mirar si el camino da vueltas. Ignora cuánto ya caminaste. Es rápido, pero puede no dar el camino más corto. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Best-first search | Búsqueda "primero el mejor" | Familia de algoritmos que siempre revisan el nodo con el mejor número f. |
| Greedy | Voraz / codicioso | Toma lo que parece mejor **ahora**, sin pensar en el costo total. |
| h(n) | Heurística | Mi estimación de cuánto falta desde n hasta la meta. |
| f(n) = h(n) | Función de evaluación | El número con el que greedy ordena la frontera: solo la estimación. |
| Priority queue | Cola de prioridad | Lista donde siempre sale el de menor h. |

## Explicación

### La idea

Greedy siempre revisa el nodo que **parece más cerca de la meta** según h(n). Usa f(n) = h(n): **solo mira lo que falta**, nunca lo que ya costó llegar. Es como un turista que siempre camina hacia la torre que ve en el horizonte, aunque la calle lo obligue a dar una vuelta enorme.

### Propiedades

- **¿Completo?** Si recuerda los estados visitados (graph search), sí en espacios finitos; en espacios infinitos, no.
- **¿Óptimo?** **No.** Puede elegir un camino que parecía bueno pero salió caro.
- **Tiempo y memoria:** en el peor caso revisa todo el grafo, O(|V|) (AIMA §3.5.1). Con una buena heurística puede bajar mucho, hasta O(b·m).

### Ejemplo: Rumania (AIMA §3.5.1, Fig. 3.17)

Desde Arad, con h = distancia en línea recta a Bucarest:

1. Vecinos de Arad: Sibiu (h = 253), Timisoara (329), Zerind (374) → va a **Sibiu**, que parece más cerca.
2. Vecinos de Sibiu: Fagaras (176), Rimnicu Vilcea (193), … → va a **Fagaras**.
3. Vecino de Fagaras: Bucarest (0) → **llega**.

Costo: 140 + 99 + 211 = **450 km**. Pero el mejor camino cuesta **418 km** (por Rimnicu Vilcea y Pitesti). Greedy no revisó ningún nodo de más (fue directo), pero su camino es 32 km más largo que el óptimo. Como dice el libro: "Greediness can lead to worse results than being careful."

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

### Relación con otros algoritmos

- Greedy es el extremo "W = ∞" de weighted A\*: solo cuenta h (ver [A\*](a-star-search.md)).
- *Speedy search* es greedy usando como h el número estimado de pasos que faltan (ignora los costos).

**En la tarea** ([Deber 1](../assignments/deber-1-search-problems.md)): `best_fs(start, goal, heuristic)` resolvió el 8-puzzle en 6 movimientos generando solo 15 estados con Manhattan, frente a 135 de BFS. El 80-puzzle (`resolver_80_tile`) usa la misma idea.

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

- Greedy usa **solo h**; A\* usa **g + h**. Esa diferencia es la que hace que A\* sea óptimo y greedy no.
- Que greedy encontrara el óptimo en el 8-puzzle de la tarea fue suerte de ese caso, no una garantía.

## Relacionado

- [A* Search](a-star-search.md)
- [Heuristics](heuristics.md)
- [Uninformed Search](uninformed-search.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 12–13.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5.1 (ingestado).
