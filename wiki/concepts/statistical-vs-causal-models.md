---
title: Statistical vs. Causal Models
type: concept
tags: [foundations, models, causality]
sources: [slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-01
---
# Statistical vs. Causal Models (Modelos estadísticos vs. causales)

> **Summary (EN):** A model is a mathematical description of a system or a hypothesis that explains a phenomenon. Models are built with formal methods (first-order calculus, lambda calculus, temporal logic, rewriting systems, causal calculus) or statistical methods (regression, classification, Bayesian and Markov networks). Statistical models capture correlation; causal models — Judea Pearl's causal calculus — encode cause→effect in a directed acyclic graph, which the lecture presents as a bridge between ML and AI.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Model | Modelo | Descripción matemática de un sistema; hipótesis explicativa. |
| Formal methods | Métodos formales | Modelos basados en lógica y cálculo simbólico. |
| Statistical methods | Métodos estadísticos | Modelos que se ajustan a datos (regresión, clasificación, redes bayesianas). |
| Correlation | Correlación | A y B varían juntos; no dice quién causa a quién. |
| Causation | Causalidad | A produce B. |
| DAG (Directed Acyclic Graph) | Grafo dirigido acíclico | Estructura donde flechas = relaciones causa → efecto. |

## Explicación

**¿Qué es un modelo?** (slides 01, s10) Algo que construimos, asumimos o creemos con base en reglas definidas *a priori* o en observaciones. Hay dos familias:

- **Formales:** cálculo de primer orden (base de [Prolog](prolog.md)), cálculo lambda (base de LISP), lógica temporal, sistemas de reescritura, cálculo causal.
- **Estadísticos:** regresión, clasificación, redes bayesianas, redes de Markov (base del aprendizaje automático, ver [Neural Networks](neural-networks.md)).

**Limitación de lo estadístico.** Un modelo estadístico aprende asociaciones: puede predecir muy bien sin saber *por qué*. Si cambia la situación (una intervención), la correlación puede dejar de valer.

**Modelos causales (Pearl, 1987 según la clase).** La idea es determinar si A es causa y B efecto, o al revés — pero no ambos a la vez. Pearl codifica estas relaciones en un **DAG**; esto permite razonar sobre intervenciones ("¿qué pasa si hago A?") y contrafactuales, y se presenta como la teoría que puede conectar el aprendizaje automático con la IA.

## Errores comunes y tips de examen

- "Correlación no implica causalidad" — y un DAG causal **no puede tener ciclos** (A causa B y B causa A a la vez no es válido en este modelo).
- Las redes bayesianas también son DAG, pero sus flechas expresan dependencia probabilística; en una red **causal** expresan mecanismo (complemento: AIMA 4e §13.5).

## Relacionado

- [Neural Networks](neural-networks.md)
- [Propositional and First-Order Logic](propositional-and-first-order-logic.md)
- [What Is AI?](what-is-ai.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 10, 14, 15.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §13.5 Causal Networks (pendiente de ingestar).
