---
title: Agent Types
type: concept
tags: [agents, architectures]
sources: [slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-01
---
# Agent Types (Tipos de agentes)

> **Summary (EN):** Four agent architectures of increasing power: the simple reflex agent (condition–action rules on the current percept, no memory), the model-based reflex agent (keeps internal state using a world model and a transition model), the goal-based agent (plans and searches toward desired states) and the utility-based agent (maximizes expected utility, handling conflicting goals and uncertainty).

## Términos clave

| English | Español | Significado |
|---|---|---|
| Simple reflex agent | Agente reflejo simple | Reglas condición–acción sobre la percepción actual. |
| Condition–action rule | Regla condición–acción | "si *suciedad* entonces *aspirar*". |
| Model-based reflex agent | Agente reflejo basado en modelo | Mantiene un estado interno actualizado. |
| World model / Transition model | Modelo del mundo / de transición | Cómo evoluciona el mundo solo / cómo lo afectan mis acciones. |
| Goal-based agent | Agente basado en objetivos | Elige acciones que lo acercan a un estado meta (búsqueda, planificación). |
| Utility-based agent | Agente basado en utilidad | Elige la acción con máxima utilidad esperada. |

## Explicación

| Tipo | Usa | Ventaja | Limitación |
|---|---|---|---|
| **Reflejo simple** | Solo la percepción actual | Simple y eficiente | Falla si el entorno es parcialmente observable |
| **Reflejo basado en modelo** | Estado interno + modelos del mundo y de transición | Actúa coherentemente sin ver todo | Sigue sin "querer" nada explícito |
| **Basado en objetivos** | Estado + metas + búsqueda/planificación | Se adapta si cambia la meta | Las metas son binarias: no distingue caminos mejores o peores |
| **Basado en utilidad** | Función de utilidad + probabilidades | Maneja objetivos en conflicto (velocidad vs. seguridad) e incertidumbre | Hay que definir bien la utilidad |

- **Reflejo simple:** funciona solo cuando la percepción actual contiene toda la información relevante.
- **Basado en modelo:** en cada paso actualiza su estado interno y después aplica las reglas a ese estado.
- **Basado en objetivos:** necesita saber *a dónde quiere ir*; esto conecta directamente con la unidad de [búsqueda](problem-formulation.md): el *problem-solving agent* es un agente basado en objetivos.
- **Basado en utilidad:** distingue soluciones de distinta calidad. En [optimización](optimization-basics.md), la función objetivo/fitness hace el papel de utilidad.

(Complemento: AIMA añade los **agentes que aprenden**, con elemento de desempeño, crítico, elemento de aprendizaje y generador de problemas — AIMA 4e §2.4.6.)

## Errores comunes y tips de examen

- La diferencia clave objetivo vs. utilidad: el objetivo es **sí/no**, la utilidad es **un número** que permite comparar.
- Un agente reflejo **con memoria** ya es "basado en modelo".

## Relacionado

- [Intelligent Agents](intelligent-agents.md)
- [Task Environments](task-environments.md)
- [Problem Formulation](problem-formulation.md)
- [State Representation](state-representation.md)

## Fuentes

- [Slides 03](../sources/slides-03-intelligent-agents.md), slides 14–17.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §2.4.
