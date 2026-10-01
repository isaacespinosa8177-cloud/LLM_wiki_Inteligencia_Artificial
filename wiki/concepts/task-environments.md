---
title: Task Environments
type: concept
tags: [agents, environments]
sources: [slides-03-intelligent-agents, slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Task Environments (Propiedades del entorno)

> **Summary (EN):** Environments are classified along six dimensions: fully vs. partially observable, deterministic vs. non-deterministic (stochastic), episodic vs. sequential, static vs. dynamic (semidynamic), discrete vs. continuous, and single- vs. multi-agent (competitive or cooperative). The classification determines which agent architecture and which algorithms are appropriate — e.g., classical search assumes observable, deterministic, discrete and static.

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

### Clasificación de los problemas del curso

| Problema | Observable | Determinista | Episódico | Estático | Discreto | Agentes |
|---|---|---|---|---|---|---|
| 8-puzzle / Rumania | Total | Sí | Secuencial | Estático | Discreto | Uno |
| Tic-tac-toe 4×4 | Total | Sí | Secuencial | Estático | Discreto | Multi (competitivo) |
| Ajedrez con reloj | Total | Sí | Secuencial | Semidinámico | Discreto | Multi (competitivo) |
| Mundo de la aspiradora | Parcial (solo ve su cuarto) | Sí | Secuencial | Estático | Discreto | Uno |
| Minimizar f(x,y) con PSO | — (optimización) | Algoritmo estocástico | — | Estático | Continuo | Multi (cooperativo) |
| Taxi autónomo | Parcial | No | Secuencial | Dinámico | Continuo | Multi |

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
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §2.3.
