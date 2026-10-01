---
title: Heuristics
type: concept
tags: [search, informed-search, heuristics]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Heuristics (Heurísticas)

> **Summary (EN):** A heuristic h(n) estimates the cost from node n to the goal (h(goal) = 0, h(n) ≥ 0). It encodes problem knowledge to guide search; it is an estimate, not a guarantee. A heuristic is admissible if it never overestimates the true cost and consistent if h(n) ≤ c(n, a, n') + h(n'). Classic examples from the course: straight-line distance (Romania), and Manhattan distance, Euclidean distance and misplaced tiles for sliding puzzles.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Heuristic function h(n) | Función heurística | Estimación del costo de n al objetivo. |
| Admissible | Admisible | Nunca sobreestima: h(n) ≤ h\*(n). |
| Consistent (monotone) | Consistente (monótona) | h(n) ≤ c(n,a,n') + h(n') (desigualdad triangular). |
| Dominance | Dominancia | h₂ domina a h₁ si h₂(n) ≥ h₁(n) para todo n (ambas admisibles). |
| Relaxed problem | Problema relajado | Versión con menos restricciones; su costo exacto es una heurística admisible. |
| Straight-line distance h_SLD | Distancia en línea recta | Heurística del mapa de Rumania. |

## Explicación

**Idea.** La búsqueda informada usa conocimiento adicional del problema, codificado en h(n). Una buena heurística **reduce drásticamente** los nodos explorados, pero no garantiza por sí sola el camino correcto: es una estimación.

Reglas básicas (slides 02, s11): h(n) = 0 si n es la meta; h(n) ≥ 0 siempre.

**Admisibilidad.** h nunca sobreestima el costo real restante. Es lo que garantiza que [A\*](a-star-search.md) (en árbol) devuelva el óptimo. Ejemplo: la distancia en línea recta a Bucarest nunca es mayor que la distancia por carretera.

**Consistencia.** Para todo n y sucesor n': h(n) ≤ c(n, a, n') + h(n'). Toda heurística consistente es admisible. Con consistencia, f = g + h nunca decrece a lo largo de un camino, y A\* con conjunto de explorados (búsqueda en grafo) es óptimo.

**Heurísticas para el 8-puzzle** (implementadas en [Deber 1](../assignments/deber-1-search-problems.md)):

| Heurística | Definición | ¿Admisible? |
|---|---|---|
| Misplaced tiles h₁ | Nº de fichas fuera de lugar (sin contar el hueco) | Sí: cada ficha mal ubicada necesita ≥ 1 movimiento |
| Manhattan h₂ | Σ \|fila − fila_meta\| + \|col − col_meta\| por ficha | Sí: cada movimiento mueve una ficha una casilla |
| Euclidean | Σ distancia euclidiana por ficha | Sí, pero más débil: Euclid ≤ Manhattan |

Manhattan **domina** a misplaced tiles y a la euclidiana → es la más informada de las tres. Resultado real: greedy best-first generó 15 estados con Manhattan y 20 con las otras dos.

**Cómo inventar heurísticas: problemas relajados** (complemento, AIMA §3.6). Si permitimos que una ficha se mueva a cualquier casilla adyacente aunque esté ocupada → Manhattan. Si permitimos teletransportarla → misplaced tiles. El costo óptimo de un problema relajado es admisible para el original.

**h\_SLD a Bucarest** (usada en la tarea A\* vs Dijkstra): Arad 366, Bucharest 0, Craiova 160, Fagaras 176, Oradea 380, Pitesti 100, Rimnicu Vilcea 193, Sibiu 253, Timisoara 329, Zerind 374.

## Errores comunes y tips de examen

- Admisible **no implica** consistente (al revés sí).
- h = 0 es admisible y consistente, pero no informa nada: A\* se convierte en UCS/Dijkstra.
- Entre dos heurísticas admisibles, usar la **mayor** (la que domina): expande menos nodos.
- Contar el hueco en *misplaced tiles* puede volverla no admisible.

## Relacionado

- [A* Search](a-star-search.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Uninformed Search](uninformed-search.md)
- [State Representation](state-representation.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 11, 14, 16 (s16 está en imagen).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5–3.6 (consistencia, dominancia, relajación: complemento).
- [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md), [Deber 1](../assignments/deber-1-search-problems.md).
