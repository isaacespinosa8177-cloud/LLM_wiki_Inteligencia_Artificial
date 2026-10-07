---
title: Glossary
type: glossary
tags: [glossary, bilingual]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog]
updated: 2026-10-07
---
# Glossary (Glosario inglés → español)

> **Summary (EN):** Alphabetical list of course terms in English, with the Spanish term and a short plain-Spanish explanation, linked to the page that covers each one. The LLM adds terms on every ingest.

> **En palabras simples (ES):** Busca aquí cualquier palabra técnica en inglés. Cada una tiene su traducción, una explicación corta y sin jerga, y el enlace a la página donde se explica con calma.

| English | Español | Explicación breve (en simple) | Página |
|---|---|---|---|
| A\* search | Búsqueda A\* | Revisa siempre el lugar con menor "lo ya pagado + lo que creo que falta" (f = g + h). Da el camino más barato si h nunca exagera. | [A*](concepts/a-star-search.md) |
| Accumulator | Acumulador | Un argumento extra que va llevando el resultado parcial mientras la recursión avanza. | [Recursion](concepts/prolog-recursion-and-lists.md) |
| Actuator | Actuador | Con lo que el agente actúa: ruedas, brazos, pantalla. | [Agents](concepts/intelligent-agents.md) |
| Admissible heuristic | Heurística admisible | Una estimación que nunca dice que falta más de lo que de verdad falta. | [Heuristics](concepts/heuristics.md) |
| Agent function / program | Función / programa del agente | La regla ideal "qué hacer en cada caso" / el código real que la cumple. | [Agents](concepts/intelligent-agents.md) |
| Alpha–beta pruning | Poda alfa–beta | Minimax que deja de mirar las ramas que no pueden cambiar la decisión. | [Alpha–Beta](concepts/alpha-beta-pruning.md) |
| Arc consistency | Consistencia de arcos | Cada valor de una variable tiene al menos una "pareja" válida en la otra variable de la regla. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Backpropagation | Retropropagación | Calcula cuánta culpa tiene cada peso de una red en el error, yendo de la salida hacia atrás. | [Neural Networks](concepts/neural-networks.md) |
| Backtracking | Retroceso | Deshacer la última decisión y probar la siguiente opción. | [CSP](concepts/constraint-satisfaction-problems.md), [Prolog](concepts/prolog.md) |
| Backward chaining | Encadenamiento hacia atrás | Para probar algo, buscar una regla que lo concluya y probar sus condiciones, hasta llegar a hechos. | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Branching factor | Factor de ramificación | Cuántos hijos (vecinos) puede tener cada nodo como máximo (b). | [Uninformed](concepts/uninformed-search.md) |
| Breadth-first search (BFS) | Búsqueda en anchura | Revisa por niveles: primero todo lo que está a 1 paso, luego a 2… Usa una cola (fila). | [Uninformed](concepts/uninformed-search.md) |
| Building block / schema | Bloque constructor / esquema | Un patrón de bits con huecos, como `1**0*`: un "pedazo bueno" que se hereda en un GA. | [GA](concepts/genetic-algorithms.md) |
| Causal model | Modelo causal | Un modelo que dice qué causa qué, dibujado con flechas sin ciclos (DAG). | [Causal](concepts/statistical-vs-causal-models.md) |
| Choice point | Punto de elección | En Prolog, un lugar donde quedaron otras opciones por probar. | [Prolog](concepts/prolog.md) |
| Chromosome | Cromosoma | Una solución escrita en código (por ejemplo, una cadena de bits) dentro de un GA. | [GA](concepts/genetic-algorithms.md) |
| Clause / CNF | Cláusula / forma normal conjuntiva | Varias opciones unidas con "o" / varias cláusulas unidas con "y". | [Logic](concepts/propositional-and-first-order-logic.md) |
| Closed-world assumption | Supuesto de mundo cerrado | Lo que no se puede probar se considera falso. | [Prolog](concepts/prolog.md) |
| Consistent heuristic | Heurística consistente | Al dar un paso, la estimación no baja más de lo que costó ese paso: h(n) ≤ c(n,a,n') + h(n'). | [Heuristics](concepts/heuristics.md) |
| Constraint satisfaction problem | Problema de satisfacción de restricciones | Llenar variables con valores respetando reglas (colorear un mapa, Sudoku). | [CSP](concepts/constraint-satisfaction-problems.md) |
| Cooling schedule | Esquema de enfriamiento | Cómo va bajando la temperatura en el recocido simulado. | [SA](concepts/simulated-annealing.md) |
| Crossover | Cruce | Cortar a dos padres e intercambiar sus pedazos para formar hijos. | [GA](concepts/genetic-algorithms.md) |
| Cut (`!`) | Corte | En Prolog: "no vuelvas a probar otras opciones para lo que ya decidí aquí". | [Prolog](concepts/prolog.md) |
| Definite clause | Cláusula definida | Una regla "si… y… entonces…" (exactamente un literal sin negar). | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Depth-first search (DFS) | Búsqueda en profundidad | Sigue un camino hasta el fondo antes de probar otro. Usa una pila. | [Uninformed](concepts/uninformed-search.md) |
| Deterministic / stochastic | Determinista / estocástico | La misma acción siempre da lo mismo / puede dar resultados distintos (hay azar). | [Environments](concepts/task-environments.md) |
| Elitism | Elitismo | Pasar a los mejores, sin cambios, a la siguiente generación. | [GA](concepts/genetic-algorithms.md) |
| Episodic / sequential | Episódico / secuencial | Cada decisión es independiente / lo que haces ahora afecta lo que viene. | [Environments](concepts/task-environments.md) |
| Evaluation function | Función de evaluación | Una estimación de qué tan buena es una posición de juego que todavía no termina. | [Minimax](concepts/adversarial-search-minimax.md) |
| Evaporation | Evaporación | En ACO, la feromona de todos los caminos baja un poco en cada ciclo (para olvidar lo malo). | [ACO](concepts/ant-colony-optimization.md) |
| Exploration / exploitation | Exploración / explotación | Probar zonas nuevas / mejorar alrededor de lo bueno que ya tienes. | [Optimization](concepts/optimization-basics.md) |
| Explored set | Conjunto de explorados | Los lugares que ya revisaste, para no volver a ellos. | [Problem Formulation](concepts/problem-formulation.md) |
| Fact | Hecho | Algo que simplemente es verdad: `parent(hector, ana).` | [Prolog](concepts/prolog.md) |
| Fitness function | Función de aptitud | La "nota" de una solución: qué tan buena es. | [Optimization](concepts/optimization-basics.md) |
| Forward checking | Comprobación hacia adelante | Después de llenar una variable, tachar en sus vecinas los valores que ya no sirven. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Frontier | Frontera | La lista de lugares pendientes: descubiertos pero aún no revisados. | [Problem Formulation](concepts/problem-formulation.md) |
| Fully / partially observable | Total / parcialmente observable | El agente ve todo lo importante / le falta información. | [Environments](concepts/task-environments.md) |
| Global / local optimum | Óptimo global / local | La mejor solución de todas / la mejor solo de su zona (un valle pequeño). | [Optimization](concepts/optimization-basics.md) |
| Goal clause | Cláusula objetivo | Una pregunta (ningún literal sin negar): `?- a, b.` | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Gradient descent | Descenso de gradiente | Dar pasos pequeños cuesta abajo, en contra del gradiente: w ← w − η∇f. | [GD](concepts/gradient-descent.md) |
| Greedy best-first search | Búsqueda voraz | Ir siempre al lugar que parece más cerca de la meta (menor h), sin mirar lo ya pagado. | [Greedy](concepts/greedy-best-first-search.md) |
| Heuristic | Heurística | Una estimación de cuánto falta para llegar a la meta. | [Heuristics](concepts/heuristics.md) |
| Horn clause | Cláusula de Horn | Una regla simple, un hecho o una pregunta (como mucho un literal sin negar). | [Horn](concepts/horn-clauses-and-backward-chaining.md) |
| Implicit parallelism | Paralelismo implícito | Cada cadena de un GA "prueba" muchos patrones a la vez. | [GA](concepts/genetic-algorithms.md) |
| Inertia weight | Peso de inercia | En PSO, cuánto conserva cada partícula de su velocidad anterior (w). | [PSO](concepts/particle-swarm-optimization.md) |
| Learning rate | Tasa de aprendizaje | El tamaño de cada paso (η). | [GD](concepts/gradient-descent.md) |
| Minimax | Minimax | Valor de una jugada suponiendo que yo elijo lo mejor y el rival lo peor para mí. | [Minimax](concepts/adversarial-search-minimax.md) |
| Minimum remaining values (MRV) | Mínimos valores restantes | En un CSP, llenar primero la variable con menos opciones. | [CSP](concepts/constraint-satisfaction-problems.md) |
| Mutation | Mutación | Un cambio pequeño al azar en una solución (por ejemplo, cambiar un bit). | [GA](concepts/genetic-algorithms.md) |
| Negation as failure | Negación por fallo | En Prolog, `\+ G` es verdad si no se puede probar G. | [Prolog](concepts/prolog.md) |
| Occurs check | Prueba de ocurrencia | No darle a X un valor que contenga a X (como X = f(X)). | [Unification](concepts/unification.md) |
| PEAS | PEAS | Lista para describir una tarea: Performance (nota), Environment, Actuators, Sensors. | [Agents](concepts/intelligent-agents.md) |
| Perceptron | Perceptrón | Una neurona artificial: multiplica entradas por pesos, suma y responde 1 o 0. | [Neural Networks](concepts/neural-networks.md) |
| Performance measure | Medida de desempeño | La "nota" con la que el diseñador juzga al agente. | [Agents](concepts/intelligent-agents.md) |
| Personal / global best | Mejor personal / global | En PSO: el mejor lugar de cada partícula (p_best) / el mejor de todo el enjambre (g_best). | [PSO](concepts/particle-swarm-optimization.md) |
| Pheromone | Feromona | El rastro que dejan las hormigas; la "memoria" compartida del grupo en ACO. | [ACO](concepts/ant-colony-optimization.md) |
| Ply | Media jugada | Una jugada de un solo jugador. | [Minimax](concepts/adversarial-search-minimax.md) |
| Rational agent | Agente racional | El que elige la acción con mejor nota esperada según lo que sabe. | [Agents](concepts/intelligent-agents.md) |
| Relaxed problem | Problema relajado | El mismo problema con una regla menos; su solución exacta da una buena heurística. | [Heuristics](concepts/heuristics.md) |
| Resolution | Resolución | Una regla de razonamiento que trabaja con cláusulas (CNF) para demostrar cosas. | [Logic](concepts/propositional-and-first-order-logic.md) |
| Scout / employed / onlooker bee | Abeja exploradora / empleada / observadora | En ABC: busca fuentes nuevas al azar / mejora su fuente / elige fuentes buenas para mejorarlas. | [ABC](concepts/artificial-bee-colony.md) |
| Selection (roulette, tournament, truncation) | Selección (ruleta, torneo, truncamiento) | Formas de elegir a los padres: por sorteo según la nota / el mejor de k al azar / solo los mejores. | [GA](concepts/genetic-algorithms.md) |
| SLD resolution | Resolución SLD | Cómo responde Prolog: primera meta, primera regla que encaje, y retroceder si falla. | [Prolog](concepts/prolog.md) |
| Stagnation | Estancamiento | Todas las hormigas terminan haciendo el mismo recorrido. | [ACO](concepts/ant-colony-optimization.md) |
| State space | Espacio de estados | Todos los estados posibles y cómo se conectan (un mapa de puntos y flechas). | [Problem Formulation](concepts/problem-formulation.md) |
| Static / dynamic / semidynamic | Estático / dinámico / semidinámico | El mundo no cambia mientras piensas / sí cambia / no cambia pero el reloj corre. | [Environments](concepts/task-environments.md) |
| Stigmergy | Estigmergia | Comunicarse dejando señales en el entorno (como la feromona). | [Swarm](concepts/swarm-intelligence.md) |
| Tabling | Tabulación | En Prolog, guardar resultados ya calculados (`:- table`) para no repetirlos ni dar vueltas. | [Prolog](concepts/prolog.md) |
| Tabu list | Lista tabú | Las ciudades que una hormiga ya visitó y no puede repetir. | [ACO](concepts/ant-colony-optimization.md) |
| Temperature | Temperatura | En el recocido simulado, qué tan dispuesto está a aceptar empeorar. | [SA](concepts/simulated-annealing.md) |
| Transition model | Modelo de transición | A qué estado llego si hago una acción: Result(s, a) → s'. | [Problem Formulation](concepts/problem-formulation.md) |
| Turing Test | Prueba de Turing | Si un juez no distingue a la máquina de una persona al conversar, la máquina "pasa". | [What Is AI?](concepts/what-is-ai.md) |
| Unification | Unificación | Encontrar valores para las variables que hagan iguales dos expresiones. | [Unification](concepts/unification.md) |
| Uniform-cost search | Búsqueda de costo uniforme | Revisa siempre el camino más barato hasta ahora (menor g). Es Dijkstra. | [Uninformed](concepts/uninformed-search.md) |
| Utility | Utilidad | Un número que dice qué tan bueno es un resultado. | [Agent Types](concepts/agent-types.md) |
| Visibility | Visibilidad | En ACO, qué tan cerca está una ciudad: η = 1/distancia. | [ACO](concepts/ant-colony-optimization.md) |
