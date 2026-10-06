---
title: Exam questions (self-test)
type: study
tags: [study, exam, self-test]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, paper-holland-1992-genetic-algorithms]
updated: 2026-10-01
---
# Exam questions — self-test (Preguntas de examen — autoevaluación)

> **Summary (EN):** Practice questions for every unit, written from the course sources. Try each one before opening the answer. Ask the LLM to add new questions here after each class or to quiz you on a unit.

## Unidad 1 — Fundamentos y agentes

<details><summary>1. ¿Qué es el Test de Turing y qué tipo de definición de inteligencia propone?</summary>

Un interrogador conversa por texto con un humano y una máquina sin verlos; si no identifica a la máquina, esta se considera inteligente. Es una definición **operacional** (por comportamiento). → [What Is AI?](../concepts/what-is-ai.md)
</details>

<details><summary>2. Diferencia entre función del agente y programa del agente.</summary>

La función es la especificación abstracta (historia de percepciones → acción, como una tabla). El programa es la implementación concreta que la aproxima eficientemente en una arquitectura física. → [Intelligent Agents](../concepts/intelligent-agents.md)
</details>

<details><summary>3. Define agente racional. ¿Es lo mismo que omnisciente?</summary>

Elige la acción que maximiza el valor **esperado** de la medida de desempeño, dada su historia de percepciones y su conocimiento. No es omnisciente: decide con la información disponible.
</details>

<details><summary>4. Escribe el PEAS de un robot aspiradora.</summary>

P: suciedad aspirada, tiempo, energía, no chocar. E: cuartos, suciedad, muebles. A: ruedas, aspiradora. S: sensor de suciedad, posición, bumpers.
</details>

<details><summary>5. Clasifica el ajedrez con reloj según las 6 propiedades del entorno.</summary>

Totalmente observable, determinista, secuencial, **semidinámico**, discreto, multiagente competitivo. → [Task Environments](../concepts/task-environments.md)
</details>

<details><summary>6. ¿Por qué un agente basado en objetivos no basta a veces? ¿Qué agrega uno basado en utilidad?</summary>

Las metas son binarias (sí/no) y no distinguen caminos mejores o peores. La utilidad asigna un número y permite manejar objetivos en conflicto (velocidad vs. seguridad) e incertidumbre. → [Agent Types](../concepts/agent-types.md)
</details>

## Unidad 2 — Búsqueda

<details><summary>7. ¿Cuáles son los 5 componentes de la formulación de un problema?</summary>

Estado inicial, acciones, modelo de transición Result(s, a), prueba de objetivo, función de costo. → [Problem Formulation](../concepts/problem-formulation.md)
</details>

<details><summary>8. ¿Por qué hace falta un conjunto de explorados?</summary>

Porque el árbol de búsqueda puede contener el mismo estado muchas veces (caminos distintos, ciclos); sin control el algoritmo puede no terminar aunque haya solución.
</details>

<details><summary>9. Complejidad de BFS y DFS en tiempo y espacio. ¿Cuál es el problema de BFS?</summary>

BFS: O(b^d) tiempo y espacio. DFS: O(b^m) tiempo, O(b·m) espacio. El problema de BFS es la **memoria**. → [Uninformed Search](../concepts/uninformed-search.md)
</details>

<details><summary>10. ¿Cuándo es BFS óptimo? ¿Qué usar si no lo es?</summary>

Cuando todos los costos de acción son iguales. Si no, Uniform-Cost Search / Dijkstra.
</details>

<details><summary>11. Define heurística admisible y consistente. ¿Cuál implica a cuál?</summary>

Admisible: h(n) ≤ costo real. Consistente: h(n) ≤ c(n,a,n') + h(n'). Consistente ⇒ admisible. → [Heuristics](../concepts/heuristics.md)
</details>

<details><summary>12. Traza A* de Arad a Bucarest. ¿Por qué no se detiene cuando genera Bucarest con f = 450?</summary>

Arad 366 → Sibiu 393 → Rimnicu Vilcea 413 → Fagaras 415 (genera Bucharest 450) → Pitesti 417 (mejora Bucharest a 418) → Bucharest 418 ✓. Se detiene al **expandir** la meta, y Pitesti (417) tenía menor f que 450. → [A* Search](../concepts/a-star-search.md)
</details>

<details><summary>13. ¿Qué devuelve greedy best-first de Arad a Bucarest y por qué no es óptimo?</summary>

Arad → Sibiu → Fagaras → Bucharest, costo 450 (vs. 418). Solo mira h, ignora el costo acumulado g.
</details>

<details><summary>14. Para el 8-puzzle, ¿Manhattan o misplaced tiles? Justifica.</summary>

Manhattan: ambas son admisibles, pero Manhattan domina (≥ en todo estado), así que expande menos nodos. En la tarea: 15 vs. 20 estados generados.
</details>

<details><summary>15. ¿Qué es la poda alfa-beta y cuál es su complejidad ideal?</summary>

Elimina ramas que no pueden cambiar la decisión de minimax (α = mejor para MAX, β = mejor para MIN; podar si α ≥ β). Mismo resultado, O(b^(m/2)) con orden perfecto. → [Alpha–Beta](../concepts/alpha-beta-pruning.md)
</details>

<details><summary>16. En tu tic-tac-toe 4×4, ¿por qué la IA a veces no gana teniendo la jugada ganadora?</summary>

Ganar vale +1 y la heurística puede valer más (p. ej. 2). Hay que dar a los estados terminales valores que dominen (±1000). → [Tarea](../assignments/tic-tac-toe-4x4-minimax.md)
</details>

<details><summary>17. Componentes de un CSP y qué hacen MRV y forward checking.</summary>

Variables, dominios, restricciones. MRV elige la variable con menos valores legales; forward checking elimina valores incompatibles de los vecinos al asignar. → [CSP](../concepts/constraint-satisfaction-problems.md)
</details>

## Unidad 3 — Lógica y Prolog

<details><summary>18. ¿Qué es una cláusula de Horn? Da un ejemplo de regla, hecho y consulta.</summary>

A lo sumo un literal positivo. Regla `c :- a, b.` (¬a ∨ ¬b ∨ c), hecho `c.`, consulta `?- a, b.` (¬a ∨ ¬b). → [Horn Clauses](../concepts/horn-clauses-and-backward-chaining.md)
</details>

<details><summary>19. ¿Por qué Prolog no puede expresar P ∨ Q?</summary>

Tiene dos literales positivos: no es una cláusula de Horn. Es el precio de la inferencia eficiente.
</details>

<details><summary>20. Unifica f(a, Y) = f(X, b) y [H|T] = [1,2,3]. ¿Qué pasa con X = f(X)?</summary>

{X/a, Y/b}; {H/1, T/[2,3]}. X = f(X) crea un término cíclico porque Prolog no hace occurs check. → [Unification](../concepts/unification.md)
</details>

<details><summary>21. ¿Qué diferencia hay entre X = 3 + 4 y X is 3 + 4?</summary>

`=` unifica: X = 3+4 (término). `is` evalúa: X = 7.
</details>

<details><summary>22. ¿Por qué `path(X,Z) :- path(X,Y), link(Y,Z).` como primera cláusula causa stack overflow?</summary>

SLD toma la meta más a la izquierda y las cláusulas en orden: path llama a path sin consumir nada → recursión infinita por la izquierda. Arreglo: caso base primero, recursión a la derecha, o `:- table path/2.` → [Prolog](../concepts/prolog.md)
</details>

<details><summary>23. ¿Qué es la negación por fallo y cuándo coincide con la negación lógica?</summary>

`\+ G` tiene éxito si G no se puede probar. Coincide bajo el supuesto de mundo cerrado. Solo usar con variables ligadas.
</details>

<details><summary>24. ¿Por qué isPerm([1,1,2],[1,2,2]) da true?</summary>

Porque comprueba inclusión mutua (igualdad de conjuntos), no que sean reordenamientos. Arreglo: `msort(X,S), msort(Y,S)`. → [Recursion and Lists](../concepts/prolog-recursion-and-lists.md)
</details>

<details><summary>25. ¿Por qué fibo ingenuo es lento y cómo se arregla?</summary>

Cada llamada genera dos y se repiten subproblemas → exponencial. Acumulador (lineal) o `:- table fibo/2.`
</details>

## Unidad 4 — Optimización

<details><summary>26. ¿Qué es exploración vs. explotación? Da un mecanismo de cada uno en GA, PSO y ACO.</summary>

Explorar = probar regiones nuevas; explotar = refinar las buenas. GA: mutación / selección. PSO: inercia / atracción a p_best, g_best. ACO: elección probabilística y evaporación / refuerzo de feromona. → [Optimization Basics](../concepts/optimization-basics.md)
</details>

<details><summary>27. Escribe la ecuación de velocidad de PSO (original y con inercia).</summary>

Original: v ← v + 2·rand·(p_best − x) + 2·rand·(g_best − x). Con inercia: v ← w·v + c₁φ₁(p_best − x) + c₂φ₂(g_best − x). Luego x ← x + v. → [PSO](../concepts/particle-swarm-optimization.md)
</details>

<details><summary>28. ¿Qué pasa en PSO si se elimina el momentum (la velocidad anterior)?</summary>

Según Kennedy y Eberhart, se vuelve "bastante ineficaz" para encontrar óptimos globales: la inercia es la que produce el sobrepaso (exploración).
</details>

<details><summary>29. Escribe la probabilidad de transición de Ant System y la actualización de feromona.</summary>

p_ij = τ_ij^α η_ij^β / Σ τ_il^α η_il^β (l permitidas); τ_ij ← ρ τ_ij + Σ_k Q/L_k. → [ACO](../concepts/ant-colony-optimization.md)
</details>

<details><summary>30. En Ant System, ¿qué pasa con α = 0? ¿y con α muy alto?</summary>

α = 0: greedy estocástico con múltiples inicios (no usa feromona). α alto: estancamiento — todas las hormigas siguen el mismo tour.
</details>

<details><summary>31. Explica el paralelismo implícito de Holland con el ejemplo 11011001.</summary>

La cadena pertenece a muchas regiones/esquemas (11\*\*\*\*\*\*, 1\*\*\*\*\*\*\*, \*\*0\*\*00\*…); una población pequeña muestrea muchísimas regiones a la vez y las de mayor aptitud reciben más descendencia. → [GA](../concepts/genetic-algorithms.md)
</details>

<details><summary>32. ¿Por qué en simulated annealing se aceptan soluciones peores?</summary>

Para escapar de óptimos locales. Probabilidad e^(−Δ/T): alta al inicio (T alta), casi nula al final. → [SA](../concepts/simulated-annealing.md)
</details>

<details><summary>33. Roles de las abejas en ABC.</summary>

Empleadas y observadoras explotan fuentes (las observadoras eligen según calidad); exploradoras abandonan fuentes agotadas (tras `limit` intentos) y exploran al azar. → [ABC](../concepts/artificial-bee-colony.md)
</details>

<details><summary>34. ¿Quién propuso qué y cuándo? Fogel, Rechenberg/Schwefel, Holland, Kennedy/Eberhart, Dorigo, Karaboga.</summary>

Fogel 1960 (programación evolutiva) · Rechenberg & Schwefel 1970 (estrategias evolutivas) · Holland 1975 (GA) · Kennedy & Eberhart 1995 (PSO) · Dorigo 1996 (Ant System) · Karaboga 2007 (ABC). → [History of AI](../concepts/history-of-ai.md)
</details>

## Relacionado

- [Search algorithms comparison](search-algorithms-comparison.md)
- [Metaheuristics comparison](metaheuristics-comparison.md)
- [Errata](errata.md)
