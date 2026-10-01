---
title: Intelligent Agents
type: concept
tags: [agents, rationality, peas]
sources: [slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-01
---
# Intelligent Agents (Agentes inteligentes)

> **Summary (EN):** An agent perceives its environment through sensors and acts on it through actuators. Its behavior is described by an agent function (percept history → action) and implemented by an agent program that approximates that function compactly. A rational agent chooses, at each moment, the action that maximizes the expected value of a performance measure given its percepts and built-in knowledge. Task environments are specified with PEAS.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Agent | Agente | Algo que percibe y actúa. |
| Sensor / Actuator | Sensor / Actuador | Mecanismos para percibir / actuar. |
| Percept / percept history | Percepción / historia de percepciones | Lo que el agente percibe en un instante / todo lo percibido hasta ahora. |
| Agent function | Función del agente | Especificación abstracta: historia → acción (una tabla, en teoría). |
| Agent program | Programa del agente | Implementación concreta que corre en una arquitectura física. |
| Rational agent | Agente racional | Maximiza el valor esperado de la medida de desempeño. |
| Performance measure | Medida de desempeño | Criterio externo, definido por el diseñador. |
| PEAS | PEAS | Performance, Environment, Actuators, Sensors. |

## Explicación

**Agente = percibir → decidir → actuar.** Un humano (ojos → cerebro → manos), un robot (cámaras → procesador → motores) o un programa (teclado/archivos → código → pantalla/red).

**Función vs. programa.** La *función del agente* dice qué hacer en **cada** situación posible: mapea la historia de percepciones a una acción. Podría escribirse como una tabla gigante, pero en el mundo de la aspiradora la tabla crece exponencialmente con el tiempo → intratable. El *programa del agente* es lo que realmente escribimos: aproxima esa función de forma compacta. "Todo el diseño de IA es la búsqueda de buenos programas que aproximen la función ideal."

**Vacuum World (mundo de la aspiradora).** Dos cuartos A y B, cada uno sucio o limpio. Sensores: posición y estado del cuarto. Actuadores: izquierda, derecha, aspirar. Programa reflejo típico:

```
function REFLEX-VACUUM-AGENT([location, status]) returns action
    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

**Racionalidad.** Un agente racional, en cada momento, elige la acción que maximiza el valor **esperado** de la medida de desempeño, dada su historia de percepciones y su conocimiento incorporado. También debe **explorar** (recolectar información útil) y **aprender** de sus percepciones.

**La medida de desempeño la define el diseñador** — "you get what you ask for". Si premiamos "cantidad de suciedad aspirada", un agente racional podría ensuciar para volver a aspirar. Una medida mal especificada o incompleta produce comportamiento no deseado.

**PEAS.** Para especificar un entorno de tarea: *Performance* (criterio de éxito), *Environment* (el mundo), *Actuators*, *Sensors*. Ejemplo clásico (AIMA): taxi automático — P: seguridad, rapidez, legalidad, comodidad; E: calles, tráfico, peatones; A: volante, acelerador, freno, bocina; S: cámaras, GPS, velocímetro, sonar.

## Errores comunes y tips de examen

- Racional ≠ omnisciente ≠ exitoso siempre: se evalúa con la información disponible y en **valor esperado**.
- La medida de desempeño es **externa**: la define el diseñador, no el agente.
- Saber distinguir *función* (matemática, abstracta) de *programa* (código, concreto).

## Relacionado

- [Task Environments](task-environments.md)
- [Agent Types](agent-types.md)
- [State Representation](state-representation.md)
- [Problem Formulation](problem-formulation.md) — el agente de resolución de problemas
- [What Is AI?](what-is-ai.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slides 2–6.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §2.1–2.2 (ejemplo del taxi y pseudocódigo: complemento).
