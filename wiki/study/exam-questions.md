---
title: Exam questions (self-test)
type: study
tags: [study, exam, self-test]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, paper-holland-1992-genetic-algorithms]
updated: 2026-10-07
---
# Exam questions — self-test (Preguntas de examen — autoevaluación)

> **Summary (EN):** Practice questions for every unit, written from the course sources. Try each one before opening the answer. Ask the LLM to add new questions here after each class or to quiz you on a unit. Each answer has an explanation in Spanish and a model answer in English, ready to write in the exam.

> **En palabras simples (ES):** Lee la pregunta, intenta responderla tú (mejor en inglés, como en el examen) y luego abre la respuesta. Primero viene la explicación en español para entender, y al final una **respuesta modelo en inglés** para copiar el estilo.

## Unidad 1 — Fundamentos y agentes

<details><summary>1. ¿Qué es el Test de Turing y qué tipo de definición de inteligencia propone?</summary>

*Q (EN): What is the Turing Test, and what kind of definition of intelligence does it give?*

Un interrogador conversa por texto con un humano y una máquina sin verlos; si no identifica a la máquina, esta se considera inteligente. Es una definición **operacional** (por comportamiento). → [What Is AI?](../concepts/what-is-ai.md)

**Answer in English:** "In the Turing Test, a human judge chats by text with a person and a machine without seeing them. If the judge cannot tell which one is the machine, the machine is considered intelligent. It is an operational definition: it judges behavior, not what happens inside the machine."
</details>

<details><summary>2. Diferencia entre función del agente y programa del agente.</summary>

*Q (EN): What is the difference between the agent function and the agent program?*

La función es la especificación abstracta (historia de percepciones → acción, como una tabla). El programa es la implementación concreta que la aproxima eficientemente en una arquitectura física. → [Intelligent Agents](../concepts/intelligent-agents.md)

**Answer in English:** "The agent function is the abstract mapping from every possible percept history to an action, like a huge table. The agent program is the concrete code that runs on the agent and implements that mapping in a compact way."
</details>

<details><summary>3. Define agente racional. ¿Es lo mismo que omnisciente?</summary>

*Q (EN): Define a rational agent. Is it the same as omniscient?*

Elige la acción que maximiza el valor **esperado** de la medida de desempeño, dada su historia de percepciones y su conocimiento. No es omnisciente: decide con la información disponible.

**Answer in English:** "A rational agent chooses the action that maximizes the expected value of its performance measure, given its percept history and built-in knowledge. It is not omniscient: it decides with the information it has, so it can still have bad luck."
</details>

<details><summary>4. Escribe el PEAS de un robot aspiradora.</summary>

*Q (EN): Write the PEAS description of a robot vacuum cleaner.*

P: piso limpio (no "suciedad aspirada", ver *you get what you ask for*), tiempo, energía, no chocar. E: cuartos, suciedad, muebles. A: ruedas, aspiradora. S: sensor de suciedad, posición, bumpers.

**Answer in English:** "Performance: clean floor, time and energy used, no collisions. Environment: rooms, dirt, furniture. Actuators: wheels, vacuum. Sensors: dirt sensor, position sensor, bump sensors."
</details>

<details><summary>5. Clasifica el ajedrez con reloj según las 6 propiedades del entorno.</summary>

*Q (EN): Classify chess with a clock using the environment properties.*

Totalmente observable, determinista, secuencial, **semidinámico**, discreto, multiagente competitivo. → [Task Environments](../concepts/task-environments.md)

**Answer in English:** "Chess with a clock is fully observable, deterministic, sequential, semidynamic (the board does not change while you think, but the clock does), discrete and multi-agent competitive."
</details>

<details><summary>6. ¿Por qué un agente basado en objetivos no basta a veces? ¿Qué agrega uno basado en utilidad?</summary>

*Q (EN): Why is a goal-based agent sometimes not enough? What does a utility-based agent add?*

Las metas son binarias (sí/no) y no distinguen caminos mejores o peores. La utilidad asigna un número y permite manejar objetivos en conflicto (velocidad vs. seguridad) e incertidumbre. → [Agent Types](../concepts/agent-types.md)

**Answer in English:** "A goal is only reached or not reached, so it cannot tell a good path from a better one. A utility-based agent gives each outcome a number, so it can compare options, trade off conflicting goals such as speed and safety, and handle uncertainty."
</details>

## Unidad 2 — Búsqueda

<details><summary>7. ¿Cuáles son los 5 componentes de la formulación de un problema?</summary>

*Q (EN): What are the five components of a search problem?*

Estado inicial, acciones, modelo de transición Result(s, a), prueba de objetivo, función de costo. → [Problem Formulation](../concepts/problem-formulation.md)

**Answer in English:** "Initial state, actions, transition model Result(s, a), goal test, and action cost function."
</details>

<details><summary>8. ¿Por qué hace falta un conjunto de explorados?</summary>

*Q (EN): Why do we need an explored (reached) set?*

Porque el árbol de búsqueda puede contener el mismo estado muchas veces (caminos distintos, ciclos); sin control el algoritmo puede no terminar aunque haya solución.

**Answer in English:** "Because the same state can be reached by different paths or by cycles, so it can appear many times in the search tree. Without remembering visited states, the algorithm can loop forever even when a solution exists."
</details>

<details><summary>9. Complejidad de BFS y DFS en tiempo y espacio. ¿Cuál es el problema de BFS?</summary>

*Q (EN): Give the time and space complexity of BFS and DFS. What is the main problem of BFS?*

BFS: O(b^d) tiempo y espacio. DFS: O(b^m) tiempo, O(b·m) espacio. El problema de BFS es la **memoria**. → [Uninformed Search](../concepts/uninformed-search.md)

**Answer in English:** "BFS takes O(b^d) time and O(b^d) memory. DFS takes O(b^m) time but only O(b·m) memory. The main problem of BFS is memory, because it keeps a whole level of the tree."
</details>

<details><summary>10. ¿Cuándo es BFS óptimo? ¿Qué usar si no lo es?</summary>

*Q (EN): When is BFS optimal? What should you use when it is not?*

Cuando todos los costos de acción son iguales. Si no, Uniform-Cost Search / Dijkstra.

**Answer in English:** "BFS is optimal when all actions cost the same, because it finds the path with the fewest steps. When costs differ, use uniform-cost search (Dijkstra), which always expands the cheapest path first."
</details>

<details><summary>11. Define heurística admisible y consistente. ¿Cuál implica a cuál?</summary>

*Q (EN): Define admissible and consistent heuristics. Which one implies the other?*

Admisible: h(n) ≤ costo real. Consistente: h(n) ≤ c(n,a,n') + h(n'). Consistente ⇒ admisible. → [Heuristics](../concepts/heuristics.md)

**Answer in English:** "A heuristic is admissible if it never overestimates the real cost to the goal: h(n) ≤ h*(n). It is consistent if h(n) ≤ c(n, a, n') + h(n') for every step. Consistency implies admissibility, but not the other way around."
</details>

<details><summary>12. Traza A* de Arad a Bucarest. ¿Por qué no se detiene cuando genera Bucarest con f = 450?</summary>

*Q (EN): Trace A* from Arad to Bucharest. Why does it not stop when it generates Bucharest with f = 450?*

Arad 366 → Sibiu 393 → Rimnicu Vilcea 413 → Fagaras 415 (genera Bucharest 450) → Pitesti 417 (mejora Bucharest a 418) → Bucharest 418 ✓. Se detiene al **expandir** la meta, y Pitesti (417) tenía menor f que 450. → [A* Search](../concepts/a-star-search.md)

**Answer in English:** "A* expands Arad (366), Sibiu (393), Rimnicu Vilcea (413), Fagaras (415, which generates Bucharest with f = 450) and Pitesti (417, which improves Bucharest to 418), then expands Bucharest with 418. It does not stop at 450 because the goal test is done when a node is expanded, not when it is generated, and Pitesti had a lower f."
</details>

<details><summary>13. ¿Qué devuelve greedy best-first de Arad a Bucarest y por qué no es óptimo?</summary>

*Q (EN): What does greedy best-first return from Arad to Bucharest, and why is it not optimal?*

Arad → Sibiu → Fagaras → Bucharest, costo 450 (vs. 418). Solo mira h, ignora el costo acumulado g.

**Answer in English:** "Greedy returns Arad, Sibiu, Fagaras, Bucharest with cost 450, while the optimal cost is 418. It is not optimal because it only uses h and ignores the cost already paid, g."
</details>

<details><summary>14. Para el 8-puzzle, ¿Manhattan o misplaced tiles? Justifica.</summary>

*Q (EN): For the 8-puzzle, which is better: Manhattan distance or misplaced tiles? Why?*

Manhattan: ambas son admisibles, pero Manhattan domina (≥ en todo estado), así que expande menos nodos. En la tarea: 15 vs. 20 estados generados.

**Answer in English:** "Manhattan distance. Both are admissible, but Manhattan is always greater than or equal to misplaced tiles, so it dominates it and A* expands fewer nodes with it. In the assignment, greedy generated 15 states with Manhattan versus 20 with misplaced tiles."
</details>

<details><summary>15. ¿Qué es la poda alfa-beta y cuál es su complejidad ideal?</summary>

*Q (EN): What is alpha–beta pruning, and what is its best-case complexity?*

Elimina ramas que no pueden cambiar la decisión de minimax (α = mejor para MAX, β = mejor para MIN; podar si α ≥ β). Mismo resultado, O(b^(m/2)) con orden perfecto. → [Alpha–Beta](../concepts/alpha-beta-pruning.md)

**Answer in English:** "Alpha–beta pruning skips branches that cannot change the minimax decision. Alpha is the best value MAX can already guarantee and beta the best value MIN can already guarantee; when alpha ≥ beta the remaining children are pruned. It returns the same result as minimax, and with perfect move ordering it takes O(b^(m/2)), so it can search about twice as deep."
</details>

<details><summary>16. En tu tic-tac-toe 4×4, ¿por qué la IA a veces no gana teniendo la jugada ganadora?</summary>

*Q (EN): In the 4×4 tic-tac-toe assignment, why does the AI sometimes not take a winning move?*

Ganar vale +1 y la heurística puede valer más (p. ej. 2). Hay que dar a los estados terminales valores que dominen (±1000). → [Tarea](../assignments/tic-tac-toe-4x4-minimax.md)

**Answer in English:** "Because a win is worth only +1, while the heuristic value of a non-terminal position can be higher, so the AI prefers a 'promising' position to an actual win. Terminal values must dominate heuristic values, for example ±1000."
</details>

<details><summary>17. Componentes de un CSP y qué hacen MRV y forward checking.</summary>

*Q (EN): What are the components of a CSP, and what do MRV and forward checking do?*

Variables, dominios, restricciones. MRV elige la variable con menos valores legales; forward checking elimina valores incompatibles de los vecinos al asignar. → [CSP](../concepts/constraint-satisfaction-problems.md)

**Answer in English:** "A CSP has variables, domains and constraints. MRV chooses the variable with the fewest legal values left, so failures are found early. Forward checking removes inconsistent values from the neighbors' domains right after each assignment."
</details>

## Unidad 3 — Lógica y Prolog

<details><summary>18. ¿Qué es una cláusula de Horn? Da un ejemplo de regla, hecho y consulta.</summary>

*Q (EN): What is a Horn clause? Give an example of a rule, a fact and a query.*

A lo sumo un literal positivo. Regla `c :- a, b.` (¬a ∨ ¬b ∨ c), hecho `c.`, consulta `?- a, b.` (¬a ∨ ¬b). → [Horn Clauses](../concepts/horn-clauses-and-backward-chaining.md)

**Answer in English:** "A Horn clause has at most one positive literal. Rule: c :- a, b. (¬a ∨ ¬b ∨ c). Fact: c. Query: ?- a, b. (¬a ∨ ¬b)."
</details>

<details><summary>19. ¿Por qué Prolog no puede expresar P ∨ Q?</summary>

*Q (EN): Why can Prolog not express P ∨ Q?*

Tiene dos literales positivos: no es una cláusula de Horn. Es el precio de la inferencia eficiente.

**Answer in English:** "Because P ∨ Q has two positive literals, so it is not a Horn clause. That is the price Prolog pays for efficient inference."
</details>

<details><summary>20. Unifica f(a, Y) = f(X, b) y [H|T] = [1,2,3]. ¿Qué pasa con X = f(X)?</summary>

*Q (EN): Unify f(a, Y) = f(X, b) and [H|T] = [1,2,3]. What happens with X = f(X)?*

{X/a, Y/b}; {H/1, T/[2,3]}. X = f(X) crea un término cíclico porque Prolog no hace occurs check. → [Unification](../concepts/unification.md)

**Answer in English:** "f(a, Y) = f(X, b) gives {X/a, Y/b}. [H|T] = [1,2,3] gives {H/1, T/[2,3]}. X = f(X) creates a cyclic term, because Prolog does not do the occurs check by default."
</details>

<details><summary>21. ¿Qué diferencia hay entre X = 3 + 4 y X is 3 + 4?</summary>

*Q (EN): What is the difference between X = 3 + 4 and X is 3 + 4?*

`=` unifica: X = 3+4 (término). `is` evalúa: X = 7.

**Answer in English:** "= unifies terms without evaluating, so X becomes the term 3+4. is evaluates the arithmetic expression, so X becomes 7."
</details>

<details><summary>22. ¿Por qué `path(X,Z) :- path(X,Y), link(Y,Z).` como primera cláusula causa stack overflow?</summary>

*Q (EN): Why does path(X,Z) :- path(X,Y), link(Y,Z). as the first clause cause a stack overflow?*

SLD toma la meta más a la izquierda y las cláusulas en orden: path llama a path sin consumir nada → recursión infinita por la izquierda. Arreglo: caso base primero, recursión a la derecha, o `:- table path/2.` → [Prolog](../concepts/prolog.md)

**Answer in English:** "SLD resolution always takes the leftmost goal and tries clauses in order, so path calls path again without making progress: infinite left recursion. Fixes: put the base case first and recurse on the right, or use :- table path/2."
</details>

<details><summary>23. ¿Qué es la negación por fallo y cuándo coincide con la negación lógica?</summary>

*Q (EN): What is negation as failure, and when does it match logical negation?*

`\+ G` tiene éxito si G no se puede probar. Coincide bajo el supuesto de mundo cerrado. Solo usar con variables ligadas.

**Answer in English:** "\+ G succeeds when G cannot be proved. It matches logical negation only under the closed-world assumption, where everything true is in the program. It should only be used when the variables in G are already bound."
</details>

<details><summary>24. ¿Por qué isPerm([1,1,2],[1,2,2]) da true?</summary>

*Q (EN): Why does isPerm([1,1,2],[1,2,2]) return true?*

Porque comprueba inclusión mutua (igualdad de conjuntos), no que sean reordenamientos. Arreglo: `msort(X,S), msort(Y,S)`. → [Recursion and Lists](../concepts/prolog-recursion-and-lists.md)

**Answer in English:** "Because isPerm only checks that every element of each list appears in the other list, which is set equality, not permutation. A fix is to sort both lists with msort and compare them."
</details>

<details><summary>25. ¿Por qué fibo ingenuo es lento y cómo se arregla?</summary>

*Q (EN): Why is the naive Fibonacci slow, and how can it be fixed?*

Cada llamada genera dos y se repiten subproblemas → exponencial. Acumulador (lineal) o `:- table fibo/2.`

**Answer in English:** "Each call makes two recursive calls and the same subproblems are solved again and again, so the time is exponential. It can be fixed with an accumulator, which makes it linear, or with tabling (:- table fibo/2)."
</details>

## Unidad 4 — Optimización

<details><summary>26. ¿Qué es exploración vs. explotación? Da un mecanismo de cada uno en GA, PSO y ACO.</summary>

*Q (EN): What is exploration vs. exploitation? Give one mechanism of each in GA, PSO and ACO.*

Explorar = probar regiones nuevas; explotar = refinar las buenas. GA: mutación / selección. PSO: inercia / atracción a p_best, g_best. ACO: elección probabilística y evaporación / refuerzo de feromona. → [Optimization Basics](../concepts/optimization-basics.md)

**Answer in English:** "Exploration means searching new regions; exploitation means refining good regions already found. In GAs, mutation explores and selection exploits. In PSO, inertia explores and the attraction to p_best and g_best exploits. In ACO, probabilistic choices and evaporation explore, and pheromone reinforcement exploits."
</details>

<details><summary>27. Escribe la ecuación de velocidad de PSO (original y con inercia).</summary>

*Q (EN): Write the PSO velocity update (original and with inertia).*

Original: v ← v + 2·rand·(p_best − x) + 2·rand·(g_best − x). Con inercia: v ← w·v + c₁φ₁(p_best − x) + c₂φ₂(g_best − x). Luego x ← x + v. → [PSO](../concepts/particle-swarm-optimization.md)

**Answer in English:** "Original: v ← v + 2·rand·(p_best − x) + 2·rand·(g_best − x). With inertia: v ← w·v + c1·r1·(p_best − x) + c2·r2·(g_best − x). In both cases the particle then moves: x ← x + v."
</details>

<details><summary>28. ¿Qué pasa en PSO si se elimina el momentum (la velocidad anterior)?</summary>

*Q (EN): What happens in PSO if the momentum (previous velocity) is removed?*

Según Kennedy y Eberhart, se vuelve "bastante ineficaz" para encontrar óptimos globales: la inercia es la que produce el sobrepaso (exploración).

**Answer in English:** "According to Kennedy and Eberhart, PSO becomes quite ineffective at finding global optima, because the momentum makes particles overshoot, and that overshooting is how the swarm explores."
</details>

<details><summary>29. Escribe la probabilidad de transición de Ant System y la actualización de feromona.</summary>

*Q (EN): Write the Ant System transition probability and the pheromone update.*

p_ij = τ_ij^α η_ij^β / Σ τ_il^α η_il^β (l permitidas); τ_ij ← ρ τ_ij + Σ_k Q/L_k. → [ACO](../concepts/ant-colony-optimization.md)

**Answer in English:** "The probability of moving from city i to an allowed city j is τ_ij^α · η_ij^β divided by the sum of the same quantity over all allowed cities, with η_ij = 1/d_ij. After each cycle, τ_ij ← ρ·τ_ij + Σ_k Q/L_k, where each ant k adds Q/L_k to the edges of its tour."
</details>

<details><summary>30. En Ant System, ¿qué pasa con α = 0? ¿y con α muy alto?</summary>

*Q (EN): In Ant System, what happens with α = 0? And with a very high α?*

α = 0: greedy estocástico con múltiples inicios (no usa feromona). α alto: estancamiento — todas las hormigas siguen el mismo tour.

**Answer in English:** "With α = 0 the pheromone is ignored, so it becomes a stochastic greedy search with multiple starts and no cooperation. With a very high α the colony stagnates: all ants quickly follow the same, often poor, tour."
</details>

<details><summary>31. Explica el paralelismo implícito de Holland con el ejemplo 11011001.</summary>

*Q (EN): Explain Holland's implicit parallelism with the string 11011001.*

La cadena pertenece a muchas regiones/esquemas (11\*\*\*\*\*\*, 1\*\*\*\*\*\*\*, \*\*0\*\*00\*…); una población pequeña muestrea muchísimas regiones a la vez y las de mayor aptitud reciben más descendencia. → [GA](../concepts/genetic-algorithms.md)

**Answer in English:** "The string 11011001 belongs to many schemata at once, such as 11******, 1******* and **0**00*. So a small population samples a huge number of regions in parallel, and regions with above-average fitness receive more offspring."
</details>

<details><summary>32. ¿Por qué en simulated annealing se aceptan soluciones peores?</summary>

*Q (EN): Why does simulated annealing accept worse solutions?*

Para escapar de óptimos locales. Probabilidad e^(−Δ/T): alta al inicio (T alta), casi nula al final. → [SA](../concepts/simulated-annealing.md)

**Answer in English:** "To escape local optima. A worse move is accepted with probability e^(−Δ/T), which is high at the beginning, when the temperature is high, and almost zero at the end."
</details>

<details><summary>33. Roles de las abejas en ABC.</summary>

*Q (EN): What are the roles of the bees in ABC?*

Empleadas y observadoras explotan fuentes (las observadoras eligen según calidad); exploradoras abandonan fuentes agotadas (tras `limit` intentos) y exploran al azar. → [ABC](../concepts/artificial-bee-colony.md)

**Answer in English:** "Employed bees and onlooker bees exploit food sources; onlookers choose sources with probability proportional to their quality. Scout bees abandon sources that have not improved after 'limit' trials and search randomly for new ones, which provides exploration."
</details>

<details><summary>34. ¿Quién propuso qué y cuándo? Fogel, Rechenberg/Schwefel, Holland, Kennedy/Eberhart, Dorigo, Karaboga.</summary>

*Q (EN): Who proposed what, and when? Fogel, Rechenberg/Schwefel, Holland, Kennedy/Eberhart, Dorigo, Karaboga.*

Fogel 1960 (programación evolutiva) · Rechenberg & Schwefel 1970 (estrategias evolutivas) · Holland 1975 (GA) · Kennedy & Eberhart 1995 (PSO) · Dorigo 1996 (Ant System) · Karaboga 2007 (ABC). → [History of AI](../concepts/history-of-ai.md)

**Answer in English:** "Fogel proposed evolutionary programming in 1960; Rechenberg and Schwefel, evolution strategies in 1970; Holland, genetic algorithms in 1975; Kennedy and Eberhart, PSO in 1995; Dorigo, Ant System in 1996; and Karaboga, the Artificial Bee Colony in 2007."
</details>

## Relacionado

- [Search algorithms comparison](search-algorithms-comparison.md)
- [Metaheuristics comparison](metaheuristics-comparison.md)
- [Errata](errata.md)
