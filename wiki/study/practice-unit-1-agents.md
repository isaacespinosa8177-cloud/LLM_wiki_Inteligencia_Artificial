---
title: Practice problems — Unit 1 (Foundations and agents)
type: study
tags: [study, practice, agents, environments]
sources: [slides-01-introduction-to-ai, slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-07
---
# Practice problems — Unit 1: Foundations and agents (Problemas de práctica — Unidad 1)

> **Summary (EN):** Exam-style exercises on definitions of AI, rationality, PEAS, environment properties, agent architectures and state representations. Questions are in English (as in the exam); worked solutions are in Spanish with the final answer in English. Try each one on paper before opening the solution.

## Problem 1 — PEAS

Write the PEAS description for (a) an automated Sudoku-solving app, (b) a robot soccer player, (c) an online shopping assistant.

> *En español:* Escribe el PEAS (nota, entorno, actuadores, sensores) de (a) una app que resuelve Sudokus, (b) un robot que juega fútbol, (c) un asistente de compras en línea.

<details><summary>Solución</summary>

| | Performance | Environment | Actuators | Sensors |
|---|---|---|---|---|
| (a) Sudoku app | Tablero correcto, tiempo de resolución | Tablero 9×9 con pistas | Escribir dígitos en celdas, mostrar solución | Lectura del archivo / cámara del tablero |
| (b) Robot de fútbol | Goles a favor − goles en contra, ganar el partido | Cancha, pelota, compañeros, rivales, árbitro | Piernas/ruedas, pateador | Cámara, odómetro, sensores de contacto |
| (c) Asistente de compras | Precio, calidad, satisfacción del usuario, tiempo | Tiendas web, productos, vendedores, usuario | Mostrar productos, comprar, preguntar | Páginas web (HTML), entradas del usuario |

**EN:** "PEAS = Performance measure, Environment, Actuators, Sensors; it is the first step in designing an agent."
</details>

## Problem 2 — Classify the environments

For each task say whether it is fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous, single/multi-agent: (a) crossword puzzle, (b) poker, (c) 4×4 tic-tac-toe against a person, (d) image classification, (e) an autonomous delivery drone.

> *En español:* Para cada tarea, di si es total o parcialmente observable, determinista o estocástica, episódica o secuencial, estática o dinámica, discreta o continua, y de uno o varios agentes: (a) crucigrama, (b) póker, (c) gato 4×4 contra una persona, (d) clasificar imágenes, (e) un dron de reparto autónomo.

<details><summary>Solución</summary>

| Tarea | Obs. | Det. | Epis. | Est. | Disc. | Agentes |
|---|---|---|---|---|---|---|
| Crucigrama | Total | Determinista | Secuencial | Estático | Discreto | Uno |
| Póker | Parcial | Estocástico | Secuencial | Estático | Discreto | Multi |
| Tic-tac-toe 4×4 | Total | Determinista | Secuencial | Estático | Discreto | Multi (competitivo) |
| Clasificar imágenes | Total | Determinista | **Episódico** | Semi | Continuo | Uno |
| Dron de reparto | Parcial | Estocástico | Secuencial | Dinámico | Continuo | Multi |

Clave: la clasificación de imágenes es episódica porque cada imagen es independiente de la anterior. Ver [Task Environments](../concepts/task-environments.md).
</details>

## Problem 3 — Which agent type?

Classify: (a) a thermostat, (b) a robot vacuum that builds a map of the house, (c) a GPS app that computes a route to an address, (d) a self-driving taxi that trades off speed, comfort and safety, (e) a chess program that improves by playing itself.

> *En español:* ¿Qué tipo de agente es cada uno? (a) un termostato, (b) una aspiradora robot que hace un mapa de la casa, (c) una app de GPS que calcula la ruta a una dirección, (d) un taxi autónomo que equilibra rapidez, comodidad y seguridad, (e) un programa de ajedrez que mejora jugando contra sí mismo.

<details><summary>Solución</summary>

(a) **Reflejo simple**: regla "si temperatura < objetivo → encender". (b) **Basado en modelo**: mantiene un estado interno (el mapa). (c) **Basado en objetivos**: planifica una secuencia hacia la meta. (d) **Basado en utilidad**: compara resultados con objetivos en conflicto e incertidumbre. (e) **Agente que aprende** (cualquier arquitectura + elemento de aprendizaje, crítico y generador de problemas).
</details>

## Problem 4 — "You get what you ask for"

A cleaning robot is rewarded with +1 for every unit of dirt it vacuums. What could a rational agent do that the designer did not want? Propose a better performance measure.

> *En español:* Un robot de limpieza gana +1 por cada unidad de suciedad que aspira. ¿Qué podría hacer un agente racional que el diseñador no quería? Propón una mejor medida de desempeño (nota).

<details><summary>Solución</summary>

Podría **ensuciar para volver a aspirar** (tirar la basura al piso y recogerla otra vez) y así maximizar la medida. Mejor: +1 por cada cuadro **limpio** en cada paso de tiempo (premiar el estado del entorno que queremos, no el comportamiento que imaginamos), con penalización por energía o ruido.

**EN:** "Design performance measures according to what one actually wants in the environment, not how one thinks the agent should behave."
</details>

## Problem 5 — Is it rational?

In the two-square vacuum world, the reflex agent cleans if dirty and otherwise moves to the other square. (a) Is it rational if the measure gives +1 per clean square per time step? (b) And if each move also costs −1? (c) What kind of agent fixes (b)?

> *En español:* En el mundo de la aspiradora con dos cuadros, el agente reflejo aspira si hay suciedad y, si no, se mueve al otro cuadro. (a) ¿Es racional si la nota da +1 por cada cuadro limpio en cada paso de tiempo? (b) ¿Y si además cada movimiento resta 1? (c) ¿Qué tipo de agente arregla el caso (b)?

<details><summary>Solución</summary>

(a) **Sí** (AIMA §2.2.2): con geografía conocida y percepciones correctas, ningún agente lo hace mejor en valor esperado. (b) **No**: cuando todo está limpio sigue oscilando y pierde puntos. (c) Un agente **basado en modelo** que recuerda que ambos cuadros están limpios y hace *NoOp* (y revisa de vez en cuando si pueden volver a ensuciarse).
</details>

## Problem 6 — Rational vs. omniscient

Explain with an example why a rational agent is not necessarily successful.

> *En español:* Explica con un ejemplo por qué un agente racional no siempre tiene éxito.

<details><summary>Solución</summary>

La racionalidad maximiza el desempeño **esperado** con la información disponible; la perfección maximizaría el desempeño **real**, lo que requeriría conocer el futuro. Ejemplo de AIMA: cruzar la calle después de mirar es racional aunque luego caiga la puerta de un avión. En cambio, cruzar **sin mirar** no es racional: hay que recolectar información.
</details>

## Problem 7 — Representations

Is each state atomic, factored or structured? (a) "Sibiu" in the Romania route problem, (b) the 8-puzzle tuple (2,4,3,1,0,6,7,5,8), (c) a Sudoku as variables with domains, (d) `parent(hector, ana). parent(ana, sofia).`

> *En español:* ¿Cada estado es atómico, factorizado o estructurado? (a) "Sibiu" en el problema de rutas de Rumania, (b) la lista del 8-puzzle (2,4,3,1,0,6,7,5,8), (c) un Sudoku como variables con dominios, (d) `parent(hector, ana). parent(ana, sofia).`

<details><summary>Solución</summary>

(a) **Atómico** (caja negra). (b) **Factorizado** (vector de valores; permite heurísticas como Manhattan). (c) **Factorizado** (variables + valores: CSP). (d) **Estructurado** (objetos y relaciones: lógica de primer orden). Ver [State Representation](../concepts/state-representation.md).
</details>

## Problem 8 — History (short answers)

Who / when: (a) Turing Test, (b) Dartmouth workshop, (c) perceptron, (d) Prolog, (e) genetic algorithms, (f) PSO, (g) Ant System.

> *En español:* ¿Quién y cuándo? (a) prueba de Turing, (b) taller de Dartmouth, (c) perceptrón, (d) Prolog, (e) algoritmos genéticos, (f) PSO, (g) Ant System.

<details><summary>Solución</summary>

(a) Alan Turing, 1950. (b) McCarthy, Minsky, Rochester, Shannon, 1956. (c) Frank Rosenblatt, 1958. (d) Colmerauer y Roussel, Marsella 1972 (teoría de Kowalski) — **no** Dennis Ritchie. (e) John Holland, 1975. (f) Kennedy y Eberhart, 1995. (g) Dorigo, Maniezzo y Colorni, 1996. Ver [History of AI](../concepts/history-of-ai.md).
</details>

## Relacionado

- [Intelligent Agents](../concepts/intelligent-agents.md) · [Task Environments](../concepts/task-environments.md) · [Agent Types](../concepts/agent-types.md)
- [Exam questions](exam-questions.md) · [Study plan](study-plan.md)
