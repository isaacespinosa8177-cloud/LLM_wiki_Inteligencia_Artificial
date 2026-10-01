---
title: Problem Formulation and State Space
type: concept
tags: [search, problem-solving]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Problem Formulation and State Space (Formulación de problemas y espacio de estados)

> **Summary (EN):** A problem-solving agent is a goal-based agent that formulates a problem, searches for a sequence of actions that reaches the goal, and executes it. A problem is defined by an initial state, actions, a transition model Result(s, a), a goal test and an action-cost function; together they define the state space, a graph explored incrementally. Because the same state can be reached by several paths, search keeps a frontier and an explored set to avoid infinite loops.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Problem-solving agent | Agente de resolución de problemas | Agente basado en objetivos que planifica una secuencia de acciones. |
| Initial state | Estado inicial | Donde arranca el agente. |
| Actions | Acciones | Lo que se puede hacer en cada estado. |
| Transition model `Result(s, a)` | Modelo de transición | Estado resultante de aplicar `a` en `s`. |
| Goal test | Prueba de objetivo | ¿Es este estado una meta? |
| Path / action cost | Costo de camino / acción | Define la calidad de la solución. |
| State space | Espacio de estados | Todos los estados alcanzables; un grafo. |
| Search tree | Árbol de búsqueda | Registro del proceso de búsqueda; un estado puede repetirse. |
| Frontier | Frontera | Nodos generados pero aún no expandidos. |
| Explored set (closed list) | Conjunto de explorados | Estados ya expandidos; no se vuelven a generar. |
| Branching factor *b* | Factor de ramificación | Máximo número de sucesores de un nodo. |
| Depth *d* / max depth *m* | Profundidad de la solución / máxima | Para medir complejidad. |

## Explicación

**Ciclo del agente.** (1) ¿Cuál es exactamente el problema? → *formular*. (2) ¿Cuál es la mejor forma de resolverlo? → *buscar* una secuencia de acciones. (3) *Ejecutar* el plan. Supone un entorno **observable, determinista, discreto y estático** ([Task Environments](task-environments.md)). La solución es **una secuencia** de acciones, no una sola.

**Los cinco componentes** definen el espacio de estados:

```
Problem:
  initial_state                  e.g. "Arad"
  actions(s)                     e.g. {Go(Sibiu), Go(Timisoara), Go(Zerind)}
  result(s, a) -> s'             e.g. result(Arad, Go(Sibiu)) = Sibiu
  is_goal(s)                     e.g. s == "Bucharest"
  action_cost(s, a, s')          e.g. 140 km
```

**Espacio de estados = grafo.** Nodos = estados del mundo; aristas = acciones con costo. Casi nunca se construye completo (es enorme: el 8-puzzle tiene 9!/2 = 181 440 estados alcanzables; el 80-puzzle de la tarea, astronómicamente más). El agente lo explora **progresivamente**.

**Grafo vs. árbol.** El grafo de estados representa el *problema* (cada estado una vez). El árbol de búsqueda representa el *proceso*: el mismo estado aparece varias veces si se llega por caminos distintos, lo que puede causar ciclos infinitos. Solución: mantener

- **Frontier:** generados, no explorados.
- **Explored set:** ya expandidos; nunca se vuelven a generar.

Sin control de estados repetidos, el algoritmo puede no terminar **aunque exista solución**; con control, cada estado se explora a lo sumo una vez.

```
function GRAPH-SEARCH(problem):
    frontier ← {Node(problem.initial)}
    explored ← ∅
    loop:
        if frontier is empty: return failure
        node ← frontier.pop()              # the ORDER of pop defines the algorithm
        if problem.is_goal(node.state): return solution(node)
        explored.add(node.state)
        for each child in expand(problem, node):
            if child.state not in explored and not in frontier:
                frontier.add(child)
```

**Ejemplos del curso.** Mapa de Rumania (Arad → Bucarest), 8-puzzle, 80-puzzle, granjero–lobo–cabra–col, N-Reinas (ver [Deber 1](../assignments/deber-1-search-problems.md)).

## Errores comunes y tips de examen

- Los algoritmos de búsqueda difieren **solo en el orden** en que sacan nodos de la frontera (FIFO → BFS, LIFO → DFS, prioridad g → UCS, h → greedy, g+h → A\*).
- Estado ≠ nodo: un nodo del árbol guarda estado + padre + acción + costo g.
- Criterios para comparar: **completitud, optimalidad, tiempo, espacio** (ver [Uninformed Search](uninformed-search.md)).

## Relacionado

- [Uninformed Search](uninformed-search.md)
- [A* Search](a-star-search.md)
- [Agent Types](agent-types.md)
- [State Representation](state-representation.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 2–5.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.1–3.3 (pseudocódigo: complemento).
