---
title: Search algorithms comparison
type: study
tags: [study, search, comparison, cheat-sheet]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Search algorithms comparison (Comparación de algoritmos de búsqueda)

> **Summary (EN):** One-page cheat sheet for Unit 2: what each search algorithm puts first in the frontier, whether it is complete and optimal, its time and space complexity, and when to use it — including adversarial search and CSP backtracking.

## Tabla maestra

| Algoritmo | Frontera / orden | Completo | Óptimo | Tiempo | Espacio | Úsalo cuando… |
|---|---|---|---|---|---|---|
| [BFS](../concepts/uninformed-search.md) | FIFO | Sí (b finito) | Sí si costos iguales | O(b^d) | O(b^d) | Costos iguales, solución poco profunda |
| [DFS](../concepts/uninformed-search.md) | LIFO | No (sí en finito con control) | No | O(b^m) | **O(b·m)** | Poca memoria, muchas soluciones |
| Depth-limited | LIFO hasta l | No si l < d | No | O(b^l) | O(b·l) | Se conoce una cota de profundidad |
| IDS | DFS con l = 0,1,2… | Sí | Sí si costos iguales | O(b^d) | O(b·d) | Como BFS pero sin memoria |
| [UCS / Dijkstra](../concepts/uninformed-search.md) | Prioridad g(n) | Sí (costos ≥ ε) | **Sí** | O(b^(1+⌊C*/ε⌋)) | igual | Costos distintos, sin heurística |
| [Greedy best-first](../concepts/greedy-best-first-search.md) | Prioridad h(n) | No (sí en finito con control) | No | O(b^m) peor caso | O(b^m) | Rapidez > calidad |
| [A\*](../concepts/a-star-search.md) | Prioridad g(n)+h(n) | Sí | **Sí** (h admisible / consistente) | depende de h | O(b^d) | Hay una buena heurística admisible |
| [Minimax](../concepts/adversarial-search-minimax.md) | DFS sobre el árbol de juego | Sí (árbol finito) | Sí vs. rival óptimo | O(b^m) | O(b·m) | Juegos de suma cero |
| [Alpha–beta](../concepts/alpha-beta-pruning.md) | DFS con poda | Sí | Igual que minimax | O(b^(m/2)) ideal | O(b·m) | Siempre que uses minimax |
| [CSP backtracking](../concepts/constraint-satisfaction-problems.md) | DFS por variable | Sí | — (satisfacción) | exponencial | lineal | Estados factorizados con restricciones |

b = factor de ramificación, d = profundidad de la solución más superficial, m = profundidad máxima, C\* = costo óptimo, ε = costo mínimo de acción.

## Datos reales de las tareas

| Problema | Algoritmo | Resultado | Nodos |
|---|---|---|---|
| Rumania Arad→Bucharest | Dijkstra | 418 | 9 expandidos |
| Rumania Arad→Bucharest | A\* (h\_SLD) | 418 | **5** expandidos |
| 8-puzzle | BFS | 6 mov. | 135 generados |
| 8-puzzle | DFS (l = 10) | 10 mov. | 484 generados |
| 8-puzzle | Greedy Manhattan | 6 mov. | **15** generados |
| Sudoku clásico | Backtracking ingenuo | ✓ | 4 208 asignaciones |
| Sudoku clásico | MRV / forward checking | ✓ | **51** asignaciones |

## Reglas mnemotécnicas

- **"El orden de la frontera define el algoritmo."** FIFO → BFS · LIFO → DFS · g → UCS · h → greedy · g+h → A\*.
- **A\* = UCS + greedy.** h = 0 → UCS; ignorar g → greedy.
- **Probar la meta al expandir** (UCS, A\*), no al generar.
- **Alpha–beta no cambia la respuesta**, solo el trabajo.

## Relacionado

- [Problem Formulation](../concepts/problem-formulation.md)
- [Heuristics](../concepts/heuristics.md)
- [Exam questions](exam-questions.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md); [AIMA 4e](../sources/book-russell-norvig-aima.md) Fig. 3.15 (tabla de búsqueda no informada, complemento).
- [Deber 1](../assignments/deber-1-search-problems.md), [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md).
