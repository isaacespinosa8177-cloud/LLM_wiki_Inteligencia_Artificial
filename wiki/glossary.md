---
title: Glossary
type: glossary
tags: [glossary, bilingual]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# Glossary (Glosario inglés → español)

> **Summary (EN):** Alphabetical English term list with the Spanish equivalent and a one-line Spanish explanation, linked to the page that covers each term. The LLM adds terms on every ingest.

| English | Español | Explicación breve | Página |
|---|---|---|---|
| A\* search | Búsqueda A\* | Expande el menor f = g + h; óptima con h admisible/consistente. | [A*](concepts/a-star-search.md) |
| Accumulator | Acumulador | Argumento que lleva el resultado parcial en una recursión. | [Recursion](concepts/prolog-recursion-and-lists.md) |
| Actuator | Actuador | Mecanismo con el que el agente actúa. | [Agents](concepts/intelligent-agents.md) |
| Admissible heuristic | Heurística admisible | Nunca sobreestima el costo real. | [Heuristics](concepts/heuristics.md) |
| Agent function / program | Función / programa del agente | Especificación abstracta / implementación concreta. | [Agents](concepts/intelligent-agents.md) |
| Alpha–beta pruning | Poda alfa–beta | Minimax sin explorar ramas irrelevantes. | [Alpha–Beta](concepts/alpha-beta-pruning.md) |
| Arc consistency | Consistencia de arcos | Todo valor de Xᵢ tiene un valor compatible en Xⱼ. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Backpropagation | Retropropagación | Calcula el gradiente de la pérdida respecto a cada peso. | [Neural Networks](concepts/neural-networks.md) |
| Backtracking | Retroceso | Deshacer la última elección y probar otra. | [CSP](concepts/constraint-satisfaction-problems.md), [Prolog](concepts/prolog.md) |
| Backward chaining | Encadenamiento hacia atrás | Razonar desde la consulta hacia los hechos. | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Branching factor | Factor de ramificación | Máximo número de sucesores de un nodo (b). | [Uninformed](concepts/uninformed-search.md) |
| Breadth-first search (BFS) | Búsqueda en anchura | Cola FIFO, nivel por nivel. | [Uninformed](concepts/uninformed-search.md) |
| Building block / schema | Bloque constructor / esquema | Patrón de bits como `1**0*`. | [GA](concepts/genetic-algorithms.md) |
| Causal model | Modelo causal | Relaciones causa→efecto en un DAG. | [Causal](concepts/statistical-vs-causal-models.md) |
| Choice point | Punto de elección | Lugar con alternativas pendientes en Prolog. | [Prolog](concepts/prolog.md) |
| Chromosome | Cromosoma | Solución codificada en un GA. | [GA](concepts/genetic-algorithms.md) |
| Clause / CNF | Cláusula / forma normal conjuntiva | Disyunción de literales / conjunción de cláusulas. | [Logic](concepts/propositional-and-first-order-logic.md) |
| Closed-world assumption | Supuesto de mundo cerrado | Lo no derivable es falso. | [Prolog](concepts/prolog.md) |
| Consistent heuristic | Heurística consistente | h(n) ≤ c(n,a,n') + h(n'). | [Heuristics](concepts/heuristics.md) |
| Constraint satisfaction problem | Problema de satisfacción de restricciones | Variables, dominios, restricciones. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Cooling schedule | Esquema de enfriamiento | Cómo baja la temperatura en SA. | [SA](concepts/simulated-annealing.md) |
| Crossover | Cruce | Intercambio de segmentos entre padres. | [GA](concepts/genetic-algorithms.md) |
| Cut (`!`) | Corte | Compromete las elecciones en Prolog. | [Prolog](concepts/prolog.md) |
| Definite clause | Cláusula definida | Exactamente un literal positivo (regla). | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Depth-first search (DFS) | Búsqueda en profundidad | Pila LIFO, rama por rama. | [Uninformed](concepts/uninformed-search.md) |
| Deterministic / stochastic | Determinista / estocástico | Resultado fijo / aleatorio de una acción. | [Environments](concepts/task-environments.md) |
| Elitism | Elitismo | Conservar los mejores sin cambios. | [GA](concepts/genetic-algorithms.md) |
| Episodic / sequential | Episódico / secuencial | Decisiones independientes / encadenadas. | [Environments](concepts/task-environments.md) |
| Evaluation function | Función de evaluación | Valor heurístico de un estado de juego no terminal. | [Minimax](concepts/adversarial-search-minimax.md) |
| Evaporation | Evaporación | Decaimiento de la feromona en ACO. | [ACO](concepts/ant-colony-optimization.md) |
| Exploration / exploitation | Exploración / explotación | Probar lo nuevo / refinar lo bueno. | [Optimization](concepts/optimization-basics.md) |
| Explored set | Conjunto de explorados | Estados ya expandidos. | [Problem Formulation](concepts/problem-formulation.md) |
| Fact | Hecho | Cláusula sin cuerpo. | [Prolog](concepts/prolog.md) |
| Fitness function | Función de aptitud | Calidad de una solución. | [Optimization](concepts/optimization-basics.md) |
| Forward checking | Comprobación hacia adelante | Podar dominios de vecinos al asignar. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Frontier | Frontera | Nodos generados aún no expandidos. | [Problem Formulation](concepts/problem-formulation.md) |
| Fully / partially observable | Total / parcialmente observable | ¿Se ve todo el estado? | [Environments](concepts/task-environments.md) |
| Global / local optimum | Óptimo global / local | Mejor de todo el espacio / de una vecindad. | [Optimization](concepts/optimization-basics.md) |
| Goal clause | Cláusula objetivo | Sin literal positivo (consulta). | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Gradient descent | Descenso de gradiente | w ← w − η∇f. | [GD](concepts/gradient-descent.md) |
| Greedy best-first search | Búsqueda voraz | Expande el menor h(n). | [Greedy](concepts/greedy-best-first-search.md) |
| Heuristic | Heurística | Estimación del costo a la meta. | [Heuristics](concepts/heuristics.md) |
| Horn clause | Cláusula de Horn | A lo sumo un literal positivo. | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Implicit parallelism | Paralelismo implícito | Una población muestrea muchos esquemas a la vez. | [GA](concepts/genetic-algorithms.md) |
| Inertia weight | Peso de inercia | w en PSO. | [PSO](concepts/particle-swarm-optimization.md) |
| Learning rate | Tasa de aprendizaje | η, tamaño del paso. | [GD](concepts/gradient-descent.md) |
| Minimax | Minimax | Valor de juego con MAX y MIN óptimos. | [Minimax](concepts/adversarial-search-minimax.md) |
| Minimum remaining values (MRV) | Mínimos valores restantes | Elegir la variable más restringida. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Mutation | Mutación | Cambio aleatorio de un gen. | [GA](concepts/genetic-algorithms.md) |
| Negation as failure | Negación por fallo | `\+ G`: éxito si G no se prueba. | [Prolog](concepts/prolog.md) |
| Occurs check | Prueba de ocurrencia | No ligar X a un término que contiene X. | [Unification](concepts/unification.md) |
| PEAS | PEAS | Performance, Environment, Actuators, Sensors. | [Agents](concepts/intelligent-agents.md) |
| Perceptron | Perceptrón | Neurona artificial con umbral. | [Neural Networks](concepts/neural-networks.md) |
| Performance measure | Medida de desempeño | Criterio externo de éxito. | [Agents](concepts/intelligent-agents.md) |
| Personal / global best | Mejor personal / global | p_best / g_best en PSO. | [PSO](concepts/particle-swarm-optimization.md) |
| Pheromone | Feromona | Memoria compartida de las hormigas. | [ACO](concepts/ant-colony-optimization.md) |
| Ply | Media jugada | Movimiento de un jugador. | [Minimax](concepts/adversarial-search-minimax.md) |
| Rational agent | Agente racional | Maximiza el desempeño esperado. | [Agents](concepts/intelligent-agents.md) |
| Relaxed problem | Problema relajado | Fuente de heurísticas admisibles. | [Heuristics](concepts/heuristics.md) |
| Resolution | Resolución | Regla de inferencia sobre cláusulas. | [Logic](concepts/propositional-and-first-order-logic.md) |
| Scout / employed / onlooker bee | Abeja exploradora / empleada / observadora | Roles en ABC. | [ABC](concepts/artificial-bee-colony.md) |
| Selection (roulette, tournament, truncation) | Selección (ruleta, torneo, truncamiento) | Elegir padres según aptitud. | [GA](concepts/genetic-algorithms.md) |
| SLD resolution | Resolución SLD | Estrategia de ejecución de Prolog. | [Prolog](concepts/prolog.md) |
| Stagnation | Estancamiento | Todas las hormigas hacen el mismo tour. | [ACO](concepts/ant-colony-optimization.md) |
| State space | Espacio de estados | Grafo de estados alcanzables. | [Problem Formulation](concepts/problem-formulation.md) |
| Static / dynamic / semidynamic | Estático / dinámico / semidinámico | ¿Cambia el entorno mientras se piensa? | [Environments](concepts/task-environments.md) |
| Stigmergy | Estigmergia | Comunicación indirecta vía el entorno. | [Swarm](concepts/swarm-intelligence.md) |
| Tabling | Tabulación | Memoización en Prolog (`:- table`). | [Prolog](concepts/prolog.md) |
| Tabu list | Lista tabú | Ciudades ya visitadas por una hormiga. | [ACO](concepts/ant-colony-optimization.md) |
| Temperature | Temperatura | Controla la aceptación de empeoramientos en SA. | [SA](concepts/simulated-annealing.md) |
| Transition model | Modelo de transición | Result(s, a) → s'. | [Problem Formulation](concepts/problem-formulation.md) |
| Turing Test | Test de Turing | Prueba operacional de inteligencia. | [What Is AI?](concepts/what-is-ai.md) |
| Unification | Unificación | Sustitución que iguala dos términos. | [Unification](concepts/unification.md) |
| Uniform-cost search | Búsqueda de costo uniforme | Expande el menor g(n) (Dijkstra). | [Uninformed](concepts/uninformed-search.md) |
| Utility | Utilidad | Medida numérica de preferencia. | [Agent Types](concepts/agent-types.md) |
| Visibility | Visibilidad | η = 1/d en ACO. | [ACO](concepts/ant-colony-optimization.md) |
