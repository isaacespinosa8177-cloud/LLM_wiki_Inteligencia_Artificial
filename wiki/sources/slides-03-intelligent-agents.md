---
title: "Slides 03 — Intelligent Agents"
type: source
tags: [slides, agents, environments]
sources: [slides-03-intelligent-agents]
updated: 2026-10-01
---
# Slides 03 — Intelligent Agents (Agentes inteligentes)

> **Summary (EN):** Lecture on the agent abstraction. An agent perceives through sensors and acts through actuators; its behavior is an agent function (percept history → action) implemented by an agent program. It covers the vacuum world, rationality and performance measures, PEAS, the six dimensions of task environments, the four agent architectures (simple reflex, model-based reflex, goal-based, utility-based) and atomic / factored / structured state representations.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/slides/03_Intelligent Agents.pptx](../../raw/slides/03_Intelligent%20Agents.pptx) |
| Tipo | Diapositivas de clase, 18 slides |
| Unidad | 1 — Fundamentos |
| Libro de apoyo | AIMA 4e cap. 2 ([book-russell-norvig-aima](book-russell-norvig-aima.md)) |

## Resumen por secciones

- **Slide 2 — ¿Qué es un agente?** Ejemplos: humano (ojos/oídos → cerebro → manos/boca), robot (cámaras → procesador → motores), agente de software (teclado/archivos → programa → pantalla/red).
- **Slide 3 — Agent function vs. agent program.** La *función* es la especificación abstracta (historia de percepciones → acción; en teoría una tabla). El *programa* es la implementación concreta que la aproxima de forma compacta. "All AI design is the search for good programs that approximate the ideal function."
- **Slide 4 — Vacuum World.** 2 cuartos (A, B), sucios o limpios; sensores: posición + estado; actuadores: izquierda, derecha, aspirar. La tabla de historias crece exponencialmente → intratable.
- **Slide 5 — Racionalidad.** Un agente racional elige la acción que maximiza el valor *esperado* de la medida de desempeño, dada su historia de percepciones y su conocimiento. Debe explorar y aprender. La medida la define el **diseñador**: "you get what you ask for".
- **Slide 6 — PEAS.** Performance, Environment, Actuators, Sensors.
- **Slides 8–12 — Propiedades del entorno.** Totalmente vs. parcialmente observable; determinista vs. no determinista (estocástico); episódico vs. secuencial; estático vs. dinámico (semidinámico: ajedrez con reloj); discreto vs. continuo; un agente vs. multiagente (competitivo o cooperativo).
- **Slides 14–17 — Tipos de agentes.** Reflejo simple (reglas condición–acción, sin memoria); reflejo basado en modelo (estado interno con modelo del mundo y modelo de transición); basado en objetivos (planificación y búsqueda); basado en utilidad (maximiza utilidad esperada; maneja objetivos en conflicto e incertidumbre).
- **Slide 18 — Representación de estados.** Atómica, factorizada, estructurada; más expresividad = más razonamiento pero más costo computacional.

## Ideas clave

1. Distinguir **función** (qué hacer) de **programa** (cómo calcularlo eficientemente).
2. Racionalidad ≠ omnisciencia: maximiza el desempeño *esperado* con la información disponible.
3. El tipo de entorno determina qué arquitectura de agente hace falta.

## Conceptos que alimenta

- [Intelligent Agents](../concepts/intelligent-agents.md)
- [Task Environments](../concepts/task-environments.md)
- [Agent Types](../concepts/agent-types.md)
- [State Representation](../concepts/state-representation.md)

## Notas y discrepancias

- Slide 2 tiene, además del título "What Is an Agent?", tres viñetas sobre lógica proposicional ("A proposition is a statement that can be true or false…") que no corresponden al tema; parece texto sobrante de otra presentación.
- Slides 7 y 13 son solo imágenes (probablemente la tabla PEAS del taxi y el diagrama agente–entorno).
