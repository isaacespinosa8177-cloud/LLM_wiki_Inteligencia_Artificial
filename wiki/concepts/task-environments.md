---
title: Task Environments
type: concept
tags: [agents, environments]
sources: [slides-03-intelligent-agents, slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# Task Environments (Propiedades del entorno)

> **Summary (EN):** Environments are classified with yes/no style questions: fully or partially observable, deterministic or stochastic, episodic or sequential, static or dynamic, discrete or continuous, single- or multi-agent, and known or unknown. The answers tell us which kind of agent and which algorithms fit; for example, classical search assumes an observable, deterministic, static, discrete and known world.

> **En palabras simples (ES):** Para describir el "mundo" donde trabaja un agente, haz siempre las mismas 7 preguntas en el mismo orden. Cada respuesta es un par de opciones (por ejemplo, "lo ve todo" o "ve solo una parte"). *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Pregunta que responde (en simple) |
|---|---|---|
| Fully / Partially observable | Totalmente / parcialmente observable | ¿El agente ve todo lo importante, o le falta información? |
| Deterministic / Stochastic | Determinista / estocástico | ¿Si hago lo mismo, pasa siempre lo mismo, o hay azar? |
| Episodic / Sequential | Episódico / secuencial | ¿Cada decisión es independiente, o lo que hago ahora afecta lo que viene? |
| Static / Dynamic / Semidynamic | Estático / dinámico / semidinámico | ¿El mundo cambia mientras el agente piensa? |
| Discrete / Continuous | Discreto / continuo | ¿Las opciones se pueden contar, o son cualquier número? |
| Single / Multi-agent | Un agente / multiagente | ¿Hay otros jugadores? ¿Compiten o cooperan? |
| Known / Unknown | Conocido / desconocido | ¿El agente sabe qué hace cada acción? |

## Explicación

Piensa en estas propiedades como **una ficha técnica del mundo** donde trabaja el agente. Cada una tiene un ejemplo fácil:

1. **¿Ve todo? (observable).** En el ajedrez ves todo el tablero → **totalmente observable**. En el póker no ves las cartas del rival → **parcialmente observable**. Si no ve todo, el agente necesita **memoria** para recordar lo que no ve (un [agente basado en modelo](agent-types.md)).
2. **¿Hay azar? (determinista o estocástico).** En un crucigrama, escribir una letra siempre hace lo mismo → **determinista**. Al tirar dados, la misma acción da resultados distintos → **estocástico**, y el agente tiene que manejar esa incertidumbre.
3. **¿Las decisiones se conectan? (episódico o secuencial).** Revisar piezas defectuosas en una fábrica: cada pieza es un caso aparte → **episódico**. En el ajedrez, cada jugada cambia las siguientes → **secuencial**.
4. **¿El mundo cambia mientras pienso? (estático o dinámico).** Crucigrama: nada cambia mientras piensas → **estático**. Manejar un auto: los otros autos se siguen moviendo → **dinámico**. Ajedrez con reloj: el tablero no cambia, pero el reloj corre → **semidinámico**.
5. **¿Se puede contar? (discreto o continuo).** Ajedrez: hay un número fijo de casillas y jugadas → **discreto**. La velocidad de un auto puede ser cualquier número (52.3 km/h…) → **continuo**. Optimizar f(x, y) con números reales también es continuo.
6. **¿Hay más jugadores? (uno o varios agentes).** Pueden **competir** (juegos → [Minimax](adversarial-search-minimax.md)) o **cooperar** (enjambres → [Swarm Intelligence](swarm-intelligence.md)).
7. **¿Conoce las reglas? (conocido o desconocido)** (AIMA §2.3.2). Esta no es una propiedad del mundo, sino de **lo que el agente sabe** de él. Ojo, no es lo mismo que "observable": el solitario es *conocido* (sabes las reglas) pero *parcialmente observable* (no ves las cartas tapadas). Un videojuego nuevo puede ser *totalmente observable* pero *desconocido* (no sabes qué hace cada botón).

**El caso más difícil** (AIMA): parcialmente observable, multiagente, estocástico, secuencial, dinámico, continuo y desconocido. Manejar un taxi es difícil en casi todo; lo único fácil es que las reglas son conocidas.

### Ejemplos de AIMA (Fig. 2.6)

| Entorno | Observable | Agentes | Determinista | Episódico | Estático | Discreto |
|---|---|---|---|---|---|---|
| Crucigrama | Total | Uno | Determinista | Secuencial | Estático | Discreto |
| Ajedrez con reloj | Total | Multi | Determinista | Secuencial | Semi | Discreto |
| Póker | Parcial | Multi | Estocástico | Secuencial | Estático | Discreto |
| Backgammon | Total | Multi | Estocástico | Secuencial | Estático | Discreto |
| Conducir un taxi | Parcial | Multi | Estocástico | Secuencial | Dinámico | Continuo |
| Diagnóstico médico | Parcial | Uno | Estocástico | Secuencial | Dinámico | Continuo |
| Análisis de imágenes | Total | Uno | Determinista | Episódico | Semi | Continuo |

### Clasificación de los problemas del curso

| Problema | Observable | Determinista | Episódico | Estático | Discreto | Agentes |
|---|---|---|---|---|---|---|
| 8-puzzle / Rumania | Total | Sí | Secuencial | Estático | Discreto | Uno |
| Tic-tac-toe 4×4 | Total | Sí | Secuencial | Estático | Discreto | Multi (compiten) |
| Ajedrez con reloj | Total | Sí | Secuencial | Semidinámico | Discreto | Multi (compiten) |
| Mundo de la aspiradora | Parcial (solo ve su cuarto) | Sí | Secuencial | Estático | Discreto | Uno |
| Minimizar f(x,y) con PSO | — (optimización) | El algoritmo usa azar | — | Estático | Continuo | Multi (cooperan) |
| Taxi autónomo | Parcial | No | Secuencial | Dinámico | Continuo | Multi |

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Para describir el "mundo" donde trabaja un agente, haz siempre las mismas 7 preguntas en el mismo orden. Cada respuesta es un par de opciones (por ejemplo, "lo ve todo" o "ve solo una parte").

**Antes de empezar: qué significa cada cosa**

| Palabra | Qué es (en simple) | English |
|---|---|---|
| Estado | cómo está el mundo en un momento (posiciones, valores, etc.) | state |
| Entorno de tarea | el "mundo" donde trabaja el agente y las reglas de ese mundo | task environment |
| Agente | quien percibe y actúa (ver la página Intelligent Agents) | agent |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Can the sensors see everything that matters? → fully / partially observable.
   - *ES:* ¿El agente ve todo lo importante? Ajedrez: sí (totalmente observable). Póker: no ve las cartas del rival (parcialmente observable).
2. Is the next state completely decided by the current state and the action? → deterministic / nondeterministic (stochastic).
   - *ES:* ¿Si hago lo mismo, pasa siempre lo mismo? Crucigrama: sí (determinista). Lanzar dados: no (estocástico).
3. Do my current decisions affect future ones? → episodic / sequential.
   - *ES:* ¿Cada decisión es independiente? Clasificar fotos: sí, cada foto es aparte (episódico). Ajedrez: no, cada jugada afecta las siguientes (secuencial).
4. Does the world change while the agent is thinking? → static / dynamic (semidynamic if only the score changes).
   - *ES:* ¿El mundo cambia mientras pienso? Crucigrama: no (estático). Manejar un taxi: sí (dinámico). Ajedrez con reloj: el tablero no cambia pero el tiempo sí (semidinámico).
5. Are states, time and actions countable (finite steps)? → discrete / continuous.
   - *ES:* ¿Las opciones se pueden contar? Ajedrez: sí (discreto). Velocidad de un auto: no, es cualquier número (continuo).
6. Are there other agents? Do they compete or cooperate? → single / multi-agent.
   - *ES:* ¿Hay otros jugadores? Crucigrama: uno solo. Ajedrez: dos que compiten (multiagente competitivo).
7. Does the agent know the rules (what each action does)? → known / unknown.
   - *ES:* ¿El agente conoce las reglas del juego? Si no, tiene que aprenderlas probando.

**Ejemplo con números:** póker → parcialmente observable, estocástico, secuencial, estático, discreto, multiagente. Clasificar imágenes → totalmente observable, determinista, **episódico**, semidinámico, continuo, un solo agente.

**Say it in the exam (EN):** "Environments are classified as fully or partially observable, deterministic or stochastic, episodic or sequential, static or dynamic, discrete or continuous, single- or multi-agent, and known or unknown. The hardest case is taxi driving: partially observable, stochastic, sequential, dynamic, continuous and multi-agent. Classical search assumes the easiest case: observable, deterministic, static, discrete and known."

**Dilo así (ES):** "Los entornos se clasifican en observable total o parcial, determinista o estocástico, episódico o secuencial, estático o dinámico, discreto o continuo, de uno o varios agentes, y conocido o desconocido. El caso más difícil es manejar un taxi. La búsqueda clásica supone el caso más fácil: observable, determinista, estático, discreto y conocido."

## Errores comunes y tips de examen

- El entorno "más difícil" es el mundo real (el taxi): parcialmente observable, estocástico, secuencial, dinámico, continuo y multiagente.
- La [búsqueda clásica](problem-formulation.md) supone lo contrario: observable, determinista, discreto y estático (slides 02, s2).
- Que un algoritmo use azar (GA, PSO) **no** hace que el entorno sea estocástico: la función que se optimiza puede ser totalmente determinista.

## Relacionado

- [Intelligent Agents](intelligent-agents.md)
- [Agent Types](agent-types.md)
- [Problem Formulation](problem-formulation.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slides 8–12.
- [Slides 02](../sources/slides-02-problem-solving.md), slide 2.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §2.3 (ingestado: conocido/desconocido, caso más difícil, Fig. 2.6).
