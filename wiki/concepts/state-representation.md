---
title: State Representation
type: concept
tags: [agents, representation]
sources: [slides-03-intelligent-agents, slides-02-problem-solving, slides-xx-logic-programming-prolog]
updated: 2026-10-07
---
# State Representation (Representación de estados)

> **Summary (EN):** A state is a snapshot of the problem. It can be stored as atomic (just a name with no parts), factored (a list of variables with values) or structured (objects and relations between them). Richer representations allow more reasoning but cost more to compute. The course uses all three: atomic in classical search, factored in CSPs and optimization, structured in logic and Prolog.

> **En palabras simples (ES):** Un "estado" es una foto de la situación del problema. Se puede guardar de tres formas. **Atómica:** solo un nombre, sin partes ("estoy en Sibiu"). **Factorizada:** una lista de valores (las 9 casillas del 8-puzzle, o (x, y)). **Estructurada:** objetos y relaciones entre ellos ("Héctor es padre de Ana"). Cuanto más detalle guardas, más puedes razonar, pero más cuesta calcular.

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| State | Estado | Una foto de la situación del problema en un momento. |
| Atomic | Atómica | El estado es solo un nombre, sin partes por dentro ("Sibiu"). |
| Factored | Factorizada | El estado es una lista de variables con valores ((x, y) = (1, 3)). |
| Structured | Estructurada | El estado describe objetos y cómo se relacionan ("Ana es hija de Héctor"). |
| Expressiveness | Expresividad | Cuántas cosas se pueden decir con esa forma de guardar el estado. |

## Explicación

Imagina que quieres describir **dónde estás** a alguien:

- **Atómica:** "Estoy en Sibiu". Es solo un nombre. No puedes preguntar nada sobre sus partes.
- **Factorizada:** "Estoy en latitud 45.8, longitud 24.1, con 30 litros de gasolina". Es una lista de valores; puedes comparar cada valor por separado.
- **Estructurada:** "Estoy en Sibiu, que está al norte de Rimnicu, y mi amigo está en Arad". Habla de objetos y sus relaciones.

| Representación | Ejemplo en el curso | Algoritmos típicos |
|---|---|---|
| **Atómica** | "Arad", "Sibiu" en el mapa de Rumania | BFS, DFS, [A\*](a-star-search.md), Dijkstra |
| **Factorizada** | El 8-puzzle como lista `(2,4,3,1,0,6,7,5,8)`; un [CSP](constraint-satisfaction-problems.md); un cromosoma de 16 bits; el punto (x, y) | CSP, [GA](genetic-algorithms.md), [PSO](particle-swarm-optimization.md), [heurísticas](heuristics.md) como Manhattan |
| **Estructurada** | `parent(hector, ana)`, un árbol `node(5, node(3,…), …)` en Prolog | [Lógica de primer orden](propositional-and-first-order-logic.md), [Prolog](prolog.md) |

**¿Por qué importa?**

- Con una representación **factorizada** puedes mirar *dentro* del estado. Por ejemplo, la heurística Manhattan del 8-puzzle mide cuánto se alejó **cada ficha**; con un estado atómico ("estado nº 4521") no podrías.
- Con una **estructurada** puedes escribir reglas generales: "para todo X, si X es padre de Y…".
- El precio: cuanto más rica la representación, más caro es razonar (la lógica de primer orden incluso puede no terminar: es indecidible).

**Una buena representación hace la mitad del trabajo.** En N-reinas, si guardas el tablero como una permutación de 1..N (un número de fila distinto para cada columna), ya garantizas una reina por fila y por columna; solo te queda revisar las diagonales (slides XX, s25).

## Errores comunes y tips de examen

- En la búsqueda clásica los estados se tratan como **atómicos aunque por dentro sean listas**: el algoritmo solo los compara y genera vecinos, no mira sus partes. En un CSP sí se aprovechan las partes.

## Relacionado

- [Agent Types](agent-types.md)
- [Problem Formulation](problem-formulation.md)
- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md)
- [N-Queens](n-queens.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slide 18.
- [Slides 02](../sources/slides-02-problem-solving.md), slide 23 ("In standard search, states are black boxes").
- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slide 25.
