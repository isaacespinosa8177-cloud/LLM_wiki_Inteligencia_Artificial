---
title: Uninformed Search
type: concept
tags: [search, uninformed-search, bfs, dfs, dijkstra]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Uninformed Search (Búsqueda no informada: BFS, DFS, UCS/Dijkstra)

> **Summary (EN):** Blind search knows only the initial state, the actions and the goal test; it explores systematically without preferring any path. Algorithms differ in the order they expand nodes and are judged by completeness, optimality, time and space. BFS (FIFO queue) is complete and optimal for uniform costs but uses O(b^d) memory; DFS (LIFO stack) needs only O(b·m) memory but is neither optimal nor, in general, complete. Uniform-cost search (Dijkstra) expands the lowest path cost g(n) first and is optimal for any non-negative costs.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Uninformed / blind search | Búsqueda no informada / ciega | Sin información extra sobre qué estados son prometedores. |
| Completeness | Completitud | ¿Encuentra solución si existe? |
| Optimality | Optimalidad | ¿Encuentra la de menor costo? |
| Time / space complexity | Complejidad temporal / espacial | ¿Cuánto tarda? ¿Cuánta memoria usa? |
| FIFO queue / LIFO stack | Cola FIFO / pila LIFO | Estructura de la frontera en BFS / DFS. |
| Uniform-cost search (UCS) | Búsqueda de costo uniforme | Expande el menor g(n); equivale a Dijkstra. |
| Depth-limited / Iterative deepening | Profundidad limitada / profundización iterativa | DFS con límite; IDS repite DFS con límite creciente. |

## Explicación

### BFS — Breadth-First Search (anchura)
Expande primero los nodos **menos profundos**, nivel por nivel. Frontera = **cola FIFO**.
- Completo: sí (si *b* es finito).
- Óptimo: encuentra el camino con **menos pasos**; óptimo en costo **solo si todos los costos son iguales**.
- Tiempo y espacio: **O(b^d)**. El problema es la memoria: la frontera crece exponencialmente.

### DFS — Depth-First Search (profundidad)
Expande primero el nodo **más profundo**, siguiendo una rama hasta el final. Frontera = **pila LIFO**.
- Completo: solo con control de repetidos **y** espacio finito.
- Óptimo: **no**.
- Tiempo **O(b^m)**, espacio **O(b·m)** — mucha menos memoria que BFS.
- Variante **depth-limited**: DFS con profundidad máxima *l* (la tarea usa `max_depth = 10`). **IDS** (complemento, AIMA §3.4.4): repetir con l = 0, 1, 2…; completo, óptimo con costos uniformes, tiempo O(b^d), espacio O(b·d).

### UCS / Dijkstra (complemento: AIMA §3.4.2)
Frontera = **cola de prioridad por g(n)** (costo acumulado). Óptimo con costos ≥ 0; completo si los costos son ≥ ε > 0. Es exactamente lo que implementa `dijkstra()` en la tarea [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md). Es A\* con h = 0.

### Comparación

| Criterio | BFS | DFS | Depth-limited | IDS | UCS (Dijkstra) |
|---|---|---|---|---|---|
| Frontera | FIFO | LIFO | LIFO | LIFO | Prioridad g(n) |
| Completo | Sí¹ | No² | No (si l < d) | Sí¹ | Sí³ |
| Óptimo | Sí⁴ | No | No | Sí⁴ | Sí |
| Tiempo | O(b^d) | O(b^m) | O(b^l) | O(b^d) | O(b^(1+⌊C*/ε⌋)) |
| Espacio | O(b^d) | O(b·m) | O(b·l) | O(b·d) | O(b^(1+⌊C*/ε⌋)) |

¹ si *b* es finito. ² completo en espacios finitos con control de repetidos. ³ si costos ≥ ε > 0. ⁴ si todos los costos son iguales.

## Ejemplo (8-puzzle de la tarea)

Inicio `(2,4,3,1,0,6,7,5,8)` → meta `(1,2,3,4,5,6,7,8,0)` (ver [Deber 1](../assignments/deber-1-search-problems.md)):

| Algoritmo | Movimientos | Estados generados |
|---|---|---|
| BFS | **6** (óptimo) | 135 |
| DFS (límite 10) | 10 (no óptimo) | 484 |
| Greedy best-first (Manhattan) | 6 | **15** |

BFS garantiza la solución más corta; DFS encontró una más larga; la búsqueda informada generó 9× menos estados.

## Errores comunes y tips de examen

- BFS es óptimo en **número de pasos**, no en costo con pesos distintos → para eso UCS/Dijkstra.
- d = profundidad de la solución más superficial; m = profundidad máxima del árbol (puede ser ∞).
- "DFS usa poca memoria" solo si se guarda el camino actual (O(b·m)); si se guarda un conjunto global de visitados, la memoria vuelve a crecer.

## Relacionado

- [Problem Formulation](problem-formulation.md)
- [Heuristics](heuristics.md)
- [A* Search](a-star-search.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 6–10.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.4 (UCS, IDS y tabla: complemento).
- Resultados reales: [Deber 1](../assignments/deber-1-search-problems.md).
