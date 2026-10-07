---
title: Task Environments
type: concept
tags: [agents, environments]
sources: [slides-03-intelligent-agents, slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# Task Environments (Propiedades del entorno)

> **Summary (EN):** Environments are classified along six dimensions: fully vs. partially observable, deterministic vs. non-deterministic (stochastic), episodic vs. sequential, static vs. dynamic (semidynamic), discrete vs. continuous, and single- vs. multi-agent (competitive or cooperative). The classification determines which agent architecture and which algorithms are appropriate — e.g., classical search assumes observable, deterministic, discrete and static.

> **En palabras simples (ES):** Para describir el "mundo" donde trabaja un agente, haz siempre las mismas 7 preguntas en el mismo orden. Cada respuesta es un par de opciones (por ejemplo, "lo ve todo" o "ve solo una parte"). *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Pregunta que responde |
|---|---|---|
| Fully / Partially observable | Totalmente / parcialmente observable | ¿Los sensores ven todo lo relevante del estado? ¿Necesito memoria? |
| Deterministic / Non-deterministic (Stochastic) | Determinista / no determinista (estocástico) | ¿El siguiente estado queda totalmente determinado por estado + acción? |
| Episodic / Sequential | Episódico / secuencial | ¿Las decisiones actuales afectan las futuras? |
| Static / Dynamic / Semidynamic | Estático / dinámico / semidinámico | ¿El entorno cambia mientras el agente delibera? |
| Discrete / Continuous | Discreto / continuo | ¿Número finito de estados, percepciones y acciones? |
| Single / Multi-agent | Uno / varios agentes | ¿Hay otros agentes (competitivos o cooperativos)? |

## Explicación

- **Observable.** Si los sensores dan acceso al estado completo, el agente no necesita recordar. Si es parcialmente observable, necesita memoria y estimación de estado ([agente basado en modelo](agent-types.md)).
- **Determinista vs. no determinista.** Determinista: misma entrada → misma salida, sin aleatoriedad. Estocástico: la misma acción puede dar resultados distintos; hay que manejar incertidumbre.
- **Episódico vs. secuencial.** En uno episódico cada percepción-acción es independiente (clasificar piezas defectuosas). En uno secuencial, las decisiones de ahora cambian el futuro (ajedrez, conducir).
- **Estático vs. dinámico.** Si el mundo cambia mientras el agente piensa, debe actuar rápido. **Semidinámico:** el entorno no cambia pero el desempeño sí (ajedrez con reloj).
- **Discreto vs. continuo.** Número finito de estados/acciones bien definidos (ajedrez) vs. valores reales (conducir; optimizar f(x, y)).
- **Un agente vs. multiagente.** Con varios agentes pueden ser **competitivos** (juegos → [Minimax](adversarial-search-minimax.md)) o **cooperativos** (enjambres → [Swarm Intelligence](swarm-intelligence.md)).

- **Conocido vs. desconocido** (AIMA §2.3.2). No es una propiedad del entorno sino del **conocimiento del agente** sobre sus "leyes físicas": en uno conocido se saben los resultados (o probabilidades) de cada acción. Es distinto de observable: el solitario es *conocido* pero parcialmente observable; un videojuego nuevo puede ser totalmente observable pero *desconocido* (no sabes qué hace cada botón).

**El caso más difícil** (AIMA): parcialmente observable, multiagente, no determinista, secuencial, dinámico, continuo y desconocido. Conducir un taxi es difícil en todos los sentidos excepto que el entorno es mayormente conocido.

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
| Tic-tac-toe 4×4 | Total | Sí | Secuencial | Estático | Discreto | Multi (competitivo) |
| Ajedrez con reloj | Total | Sí | Secuencial | Semidinámico | Discreto | Multi (competitivo) |
| Mundo de la aspiradora | Parcial (solo ve su cuarto) | Sí | Secuencial | Estático | Discreto | Uno |
| Minimizar f(x,y) con PSO | — (optimización) | Algoritmo estocástico | — | Estático | Continuo | Multi (cooperativo) |
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

- El entorno "más difícil": parcialmente observable, estocástico, secuencial, dinámico, continuo y multiagente (el mundo real / el taxi).
- La [búsqueda clásica](problem-formulation.md) supone observable, determinista, discreto y estático (slides 02, s2).
- Un algoritmo estocástico (GA, PSO) **no** convierte al entorno en estocástico: la función objetivo puede ser determinista.

## Relacionado

- [Intelligent Agents](intelligent-agents.md)
- [Agent Types](agent-types.md)
- [Problem Formulation](problem-formulation.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slides 8–12.
- [Slides 02](../sources/slides-02-problem-solving.md), slide 2.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §2.3 (ingestado: conocido/desconocido, caso más difícil, Fig. 2.6).
