---
title: State Representation
type: concept
tags: [agents, representation]
sources: [slides-03-intelligent-agents, slides-02-problem-solving, slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# State Representation (Representación de estados)

> **Summary (EN):** States can be atomic (an indivisible black box), factored (a vector of variables with values) or structured (objects and relations among them). More expressive representations allow more reasoning but cost more computation. The course uses all three: atomic states in classical search, factored states in CSPs and optimization, structured representations in first-order logic and Prolog.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Atomic | Atómica | El estado es una "caja negra" sin estructura interna. |
| Factored | Factorizada | El estado es un conjunto de variables/atributos con valores. |
| Structured | Estructurada | El estado describe objetos y relaciones entre ellos. |
| Expressiveness | Expresividad | Cuánto se puede decir con la representación. |

## Explicación

| Representación | Ejemplo en el curso | Algoritmos típicos |
|---|---|---|
| **Atómica** | "Arad", "Sibiu" en el mapa de Rumania | BFS, DFS, [A\*](a-star-search.md), Dijkstra |
| **Factorizada** | Tupla del 8-puzzle `(2,4,3,1,0,6,7,5,8)`; asignación de un [CSP](constraint-satisfaction-problems.md); cromosoma de 16 bits; vector (x, y) | CSP, [GA](genetic-algorithms.md), [PSO](particle-swarm-optimization.md), [heurísticas](heuristics.md) como Manhattan |
| **Estructurada** | `parent(hector, ana)`, `node(5, node(3,…), …)` en Prolog | [Lógica de primer orden](propositional-and-first-order-logic.md), [Prolog](prolog.md) |

**Por qué importa el nivel de representación.** Con una representación factorizada podemos mirar *dentro* del estado: por ejemplo, la heurística Manhattan mide cuánto se aleja cada ficha; con una representación atómica no podríamos. Con una estructurada podemos expresar reglas generales ("para todo X, Y…"). A cambio, el razonamiento es más costoso (FOL es indecidible).

**La representación hace la mitad del trabajo.** En N-Reinas, representar el tablero como una permutación de 1..N garantiza por construcción una reina por fila y por columna; solo quedan las diagonales por verificar (slides XX, s25).

## Errores comunes y tips de examen

- En búsqueda clásica los estados se tratan como atómicos **aunque** internamente sean tuplas: el algoritmo solo los compara y genera sucesores. En un CSP sí se explota su estructura.

## Relacionado

- [Agent Types](agent-types.md)
- [Problem Formulation](problem-formulation.md)
- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md)
- [N-Queens](n-queens.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slide 18.
- [Slides 02](../sources/slides-02-problem-solving.md), slide 23 ("In standard search, states are black boxes").
- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slide 25.
