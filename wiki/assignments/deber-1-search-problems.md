---
title: "Deber 1 — Search problems (8-puzzle, 80-puzzle, N-Queens, river crossings, Sudoku)"
type: assignment
tags: [assignment, search, csp, python]
sources: [slides-02-problem-solving]
updated: 2026-10-01
---
# Deber 1 — Search problems (Problemas de búsqueda)

> **Summary (EN):** Isaac's first homework, exported from Google Colab as one Python file. It solves seven classic problems: the 8-puzzle with BFS, depth-limited DFS and greedy best-first (Manhattan, Euclidean, misplaced tiles); an 80-puzzle (9×9) with greedy best-first + Manhattan; N-Queens by backtracking; farmer–wolf–goat–cabbage and missionaries–cannibals with BFS; and Sudoku with naive backtracking, MRV and forward checking. All parts that could be run here produced correct solutions; the review below lists results and improvement points.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/assignments/isaac_espinosa_deber1_ia_final (1).py](../../raw/assignments/isaac_espinosa_deber1_ia_final%20%281%29.py) (1257 líneas) |
| Lenguaje | Python 3 (export de Colab; varias celdas concatenadas) |
| Unidad | 2 — Búsqueda; CSP |
| Enunciado | No está en `raw/` (se infiere del código). Si lo tienes, agrégalo a `raw/assignments/`. |

## Qué se implementó

| Parte | Problema | Algoritmos | Conceptos |
|---|---|---|---|
| 1 | 8-puzzle `(2,4,3,1,0,6,7,5,8)` → `(1,2,3,4,5,6,7,8,0)` | BFS, DFS (límite 10), best-first ×3 heurísticas | [Uninformed](../concepts/uninformed-search.md), [Greedy](../concepts/greedy-best-first-search.md), [Heuristics](../concepts/heuristics.md) |
| 2 | 80-puzzle 9×9 (fichas "1A".."9I", 9 cuadrantes en espiral) | Greedy best-first + Manhattan | [Greedy](../concepts/greedy-best-first-search.md) |
| 3 | N-Reinas (N por `input()`) | Backtracking por columnas | [N-Queens](../concepts/n-queens.md) |
| 4 | Granjero, lobo, cabra y col | BFS con función `safe` | [Problem Formulation](../concepts/problem-formulation.md) |
| 5 | Misioneros y caníbales | BFS | [Problem Formulation](../concepts/problem-formulation.md) |
| 6 | Sudoku desde `board1.txt` / `board2.txt` | Backtracking ingenuo, MRV, forward checking + conteo de soluciones | [CSP](../concepts/constraint-satisfaction-problems.md) |

## Resultados (ejecutado el 2026-10-01)

**8-puzzle**

| Algoritmo | Movimientos | Estados generados |
|---|---|---|
| BFS | 6 (óptimo) | 135 |
| DFS (max_depth = 10) | 10 | 484 |
| Best-first Manhattan | 6 | **15** |
| Best-first Euclidean | 6 | 20 |
| Best-first misplaced tiles | 6 | 20 |

**80-puzzle:** la instancia es resoluble (verificado por paridad de la permutación y distancia del hueco), pero no terminó en 90 s; el propio programa avisa "esto puede tardar mucho".

**Granjero:** 7 cruces — cabra →, vuelve solo, lobo →, cabra ←, col →, vuelve solo, cabra →. (Óptimo.)

**Misioneros y caníbales:** 11 cruces desde (3,3, bote izq.) hasta (0,0 | 3,3). (Óptimo.)

**Sudoku** (los tableros originales no están en el repo; se probó con el Sudoku clásico de Wikipedia `53..7....`):

| Método | Asignaciones | Backtracks | Tiempo |
|---|---|---|---|
| Ingenuo | 4 208 | 4 157 | 25 ms |
| MRV | 51 | 0 | 14 ms |
| Forward checking (+MRV) | 51 | 0 | **1 ms** |

Soluciones totales: 1 (Sudoku bien planteado).

## Revisión

**Fortalezas**
- Cubre muchos problemas y compara algoritmos con métricas (estados generados, backtracks, tiempo): exactamente el tipo de análisis que se pide en examen.
- Usa conjunto de visitados en todas las búsquedas (evita ciclos).
- El Sudoku muestra con datos el valor de MRV y forward checking.

**Puntos a mejorar**
1. **DFS con límite + `visited` global puede perder soluciones.** Un estado alcanzado primero por un camino profundo queda marcado y luego se bloquea un camino más corto que sí cabría en el límite. Solución: guardar en `visited` la profundidad mínima con la que se vio cada estado, o comprobar ciclos solo en el camino actual (como IDS).
2. **Best-first recorre toda la frontera en cada paso** (selección O(n)). Con `heapq` es O(log n); importa mucho en el 80-puzzle.
3. **80-puzzle:** greedy no es óptimo y guarda el camino completo en cada nodo (`camino_actual + [mov]`), que consume mucha memoria. Opciones: guardar padres en un diccionario, usar A\* ponderado (f = g + w·h) o IDA\*, y una heurística más fuerte (Manhattan + *linear conflict*).
4. **Funciones redefinidas** (`get_successors`, `bfs`, `main` aparecen varias veces) porque el archivo concatena celdas de Colab; funciona porque cada `main()` se llama justo después, pero conviene separar en módulos.
5. N-Reinas usa `input()`, lo que bloquea la ejecución no interactiva del archivo completo.

## Conceptos relacionados

- [Problem Formulation](../concepts/problem-formulation.md)
- [Uninformed Search](../concepts/uninformed-search.md)
- [Heuristics](../concepts/heuristics.md)
- [Greedy Best-First Search](../concepts/greedy-best-first-search.md)
- [Constraint Satisfaction Problems](../concepts/constraint-satisfaction-problems.md)
- [N-Queens](../concepts/n-queens.md)
