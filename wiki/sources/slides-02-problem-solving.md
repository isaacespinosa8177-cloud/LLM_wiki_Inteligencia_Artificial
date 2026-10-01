---
title: "Slides 02 — Problem Solving"
type: source
tags: [slides, search, games, csp]
sources: [slides-02-problem-solving]
updated: 2026-10-01
---
# Slides 02 — Problem Solving (Resolución de problemas)

> **Summary (EN):** Lecture on problem-solving agents and search. It defines problem formulation (initial state, actions, transition model, goal test, cost), the state space versus the search tree, and frontier/explored-set bookkeeping. It then covers uninformed search (BFS, DFS), informed search with heuristics (greedy best-first, A*), adversarial search (Minimax, Alpha–Beta pruning) and Constraint Satisfaction Problems.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/slides/02_Problem Solving.pptx](../../raw/slides/02_Problem%20Solving.pptx) |
| Tipo | Diapositivas de clase, 25 slides |
| Unidad | 2 — Búsqueda |
| Libro de apoyo | AIMA 4e caps. 3, 5 y 6 ([book-russell-norvig-aima](book-russell-norvig-aima.md)) |

## Resumen por secciones

- **Slide 2 — Problem-solving agents.** Agente basado en objetivos que *planifica* una secuencia de acciones: formula el problema → busca → ejecuta. Supone entorno observable, determinista, discreto y estático. La solución es siempre una **secuencia** de acciones.
- **Slide 3 — Formulación.** Initial State, Actions, Transition Model `Result(s, a) → s'`, Goal Test, Cost Function. Juntos definen el **espacio de estados**.
- **Slide 4 — State space.** Grafo: nodos = estados, aristas = acciones con costo. No se construye explícitamente (es enorme); se explora progresivamente.
- **Slide 5 — Estados repetidos.** Grafo de estados vs. árbol de búsqueda. Sin control de repetidos el algoritmo puede no terminar. Solución: **Frontier** (generados, no explorados) + **Explored set** (ya expandidos).
- **Slide 6 — Búsqueda no informada.** Solo conoce estado inicial, acciones y test de objetivo. Criterios: completitud, optimalidad, complejidad temporal y espacial.
- **Slide 7 — BFS.** Cola FIFO; completo; óptimo con costos uniformes; tiempo y espacio O(b^d).
- **Slide 9 — DFS.** Pila LIFO; completo solo con control de repetidos y espacio finito; no óptimo; tiempo O(b^m), espacio O(b·m).
- **Slide 11 — Búsqueda informada.** Heurística h(n) = costo estimado de n al objetivo; h(objetivo) = 0; h(n) ≥ 0.
- **Slide 12 — Best-First (greedy).** Cola de prioridad por h(n); voraz; completo solo con control de repetidos; no óptimo.
- **Slide 14 — A\*.** f(n) = g(n) + h(n); completo y óptimo si h es admisible/consistente; espacio O(b^d).
- **Slide 16 — Propiedades de heurísticas** (contenido en imagen).
- **Slide 17 — Búsqueda adversarial.** Dos jugadores MAX y MIN, suma cero, información perfecta, determinista.
- **Slide 18 — Minimax.** Valor minimax recursivo; tiempo O(b^m), espacio O(b·m).
- **Slide 20 — Alpha–Beta.** Mismo resultado que Minimax explorando menos; óptimo O(b^(m/2)); α = mejor valor para MAX (cota inferior), β = mejor para MIN (cota superior).
- **Slides 23–24 — CSP.** Estados con estructura: variables, dominios, restricciones. Asignación consistente y completa. Ejemplos: Sudoku, horario escolar. Propagación: Forward Checking, Arc Consistency, Minimum Remaining Values.
- Slides 8, 10, 13, 15, 19, 21, 22, 25 son solo figuras (ejemplos paso a paso).

## Ideas clave

1. Formular bien el problema (estados, acciones, costo) es la mitad de la solución.
2. Los algoritmos de búsqueda difieren **solo en el orden de expansión** de la frontera.
3. Una buena heurística admisible hace que A\* encuentre el óptimo expandiendo muchos menos nodos (ver [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md)).
4. En juegos, se busca una **estrategia**, no un camino; alpha-beta poda sin cambiar el resultado.

## Conceptos que alimenta

- [Problem Formulation](../concepts/problem-formulation.md)
- [Uninformed Search](../concepts/uninformed-search.md)
- [Heuristics](../concepts/heuristics.md)
- [Greedy Best-First Search](../concepts/greedy-best-first-search.md)
- [A* Search](../concepts/a-star-search.md)
- [Minimax](../concepts/adversarial-search-minimax.md)
- [Alpha–Beta Pruning](../concepts/alpha-beta-pruning.md)
- [Constraint Satisfaction Problems](../concepts/constraint-satisfaction-problems.md)

## Notas y discrepancias

- Slide 14 dice que A\* es "complete ... if h is admissible". La completitud además requiere factor de ramificación finito y costos de acción ≥ ε > 0 (AIMA 4e §3.5.2). Para **búsqueda en grafo** con conjunto de explorados, la optimalidad requiere **consistencia** (admisibilidad basta en búsqueda en árbol).
- Slide 7: BFS es óptimo solo si todos los costos son iguales; con costos distintos se usa Uniform-Cost Search / Dijkstra (no aparece en las slides pero sí en la tarea [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md)).
