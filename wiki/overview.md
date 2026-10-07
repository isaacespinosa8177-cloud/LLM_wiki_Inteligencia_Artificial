---
title: Course overview
type: overview
tags: [overview, course-map]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog]
updated: 2026-10-07
---
# Course overview (Mapa del curso de Inteligencia Artificial)

> **Summary (EN):** The course is built around one idea — the rational agent — and four ways for an agent to decide what to do: search a state space for a plan (Unit 2), reason logically from a knowledge base (Unit 3), or optimize an objective with nature-inspired metaheuristics (Unit 4), after foundations and history (Unit 1). This page shows how the units connect and where to start reading.

> **En palabras simples (ES):** Todo el curso gira alrededor de una idea: un **agente** (un programa o robot) que tiene que decidir qué hacer. La Unidad 1 explica qué es un agente y en qué tipo de "mundo" trabaja. Las otras tres son **tres formas de decidir**: buscar un camino en un mapa de posibilidades (Unidad 2), razonar con reglas lógicas (Unidad 3) o ir mejorando una solución poco a poco, imitando a la naturaleza (Unidad 4).

## Mapa

```mermaid
flowchart TB
    U1["UNIT 1 · Foundations & Agents<br/>What is AI · History · Agents · Environments · Representations"]
    U2["UNIT 2 · Search & Games<br/>BFS · DFS · UCS · Greedy · A* · Minimax · Alpha-beta · MCTS · CSP"]
    U3["UNIT 3 · Logic & Prolog<br/>Propositional/FOL · Horn clauses · Unification · SLD · Prolog"]
    U4["UNIT 4 · Optimization<br/>Hill climbing · SA · GD · GA/EAs · PSO · ACO · ABC"]
    U1 -- "atomic states" --> U2
    U1 -- "structured states" --> U3
    U1 -- "factored / continuous states" --> U4
    U2 -- "DFS + backtracking = SLD resolution" --> U3
    U2 -- "N-Queens: CSP ↔ Prolog" --> U3
    U2 -- "heuristics ↔ fitness functions; local search" --> U4
```


## Unidades

| Unidad | Pregunta central | Páginas de entrada | Tareas |
|---|---|---|---|
| 1. Fundamentos y agentes | ¿Qué es la IA y cómo modelamos un agente? | [What Is AI?](concepts/what-is-ai.md), [Intelligent Agents](concepts/intelligent-agents.md) | — |
| 2. Búsqueda | ¿Cómo encuentra un agente una secuencia de acciones? | [Problem Formulation](concepts/problem-formulation.md), [A*](concepts/a-star-search.md) | [Deber 1](assignments/deber-1-search-problems.md), [A* vs Dijkstra](assignments/astar-vs-dijkstra.md), [Tic-tac-toe 4×4](assignments/tic-tac-toe-4x4-minimax.md) |
| 3. Lógica y Prolog | ¿Cómo razona un agente con conocimiento explícito? | [Logic](concepts/propositional-and-first-order-logic.md), [Prolog](concepts/prolog.md) | [Prolog Lab 01](assignments/prolog-lab-01-family.md) |
| 4. Optimización bioinspirada | ¿Cómo encontrar el mejor punto de un espacio enorme? | [Optimization Basics](concepts/optimization-basics.md), [Swarm Intelligence](concepts/swarm-intelligence.md) | [GA](assignments/genetic-algorithm-task.md), [PSO](assignments/pso-task.md) |

## Hilos que cruzan las unidades

Seis ideas que aparecen una y otra vez, y que sirven para conectar temas en el examen:

1. **Cómo guardas el estado decide qué algoritmo usar** ([State Representation](concepts/state-representation.md)). Si el estado es solo un nombre ("Sibiu") → búsqueda. Si es una lista de valores ((x, y), un Sudoku) → CSP y optimización. Si son objetos con relaciones ("Ana es hija de Héctor") → lógica.
2. **La búsqueda en profundidad (DFS) está en todas partes.** DFS normal, minimax, el backtracking de los CSP y la forma en que Prolog responde son, en el fondo, "seguir un camino hasta el fondo y retroceder si falla".
3. **Heurística ≈ función de aptitud.** Las dos son un número que orienta la búsqueda: h(n) guía a A\*; f(x) guía a GA y PSO; la cercanía η = 1/d guía a las hormigas.
4. **Explorar vs. explotar.** Probar cosas nuevas o mejorar lo que ya funciona: aparece desde greedy vs. A\* hasta la mutación (GA), la inercia (PSO) y la evaporación (ACO).
5. **"Algoritmo = Lógica + Control"** (Kowalski). La misma lógica de N-reinas con un orden distinto de pasos cambia el costo 77 veces.
6. **Tres caminos históricos:** IA con reglas (simbólica), IA que aprende de datos (estadística) e IA inspirada en la naturaleza ([History of AI](concepts/history-of-ai.md)).

## Estado de la wiki

- Ingestado: las 5 presentaciones, los 3 papers, el código de clase, los ejemplos de Prolog, las 6 tareas y el enunciado de HW01.
- Plan para el test del jueves 8 de octubre: [Study plan](study/study-plan.md).
- Libros: AIMA caps. 2–6 y Eiben & Smith caps. 3–5 ingestados (2026-10-01); resto de AIMA, Luger y Eiben con mapas de capítulos listos para ingestar por partes.
- Revisar antes del examen: [Errata](study/errata.md).
