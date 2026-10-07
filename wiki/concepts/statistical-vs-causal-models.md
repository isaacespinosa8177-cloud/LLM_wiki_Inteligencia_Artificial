---
title: Statistical vs. Causal Models
type: concept
tags: [foundations, models, causality]
sources: [slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-07
---
# Statistical vs. Causal Models (Modelos estadísticos vs. causales)

> **Summary (EN):** A model is a mathematical description of how a system works. Models are built with formal methods (logic, lambda calculus, causal calculus) or statistical methods (regression, classification, Bayesian and Markov networks). Statistical models capture correlation (things that happen together); causal models, from Judea Pearl, capture cause and effect with arrows in a directed acyclic graph. The lecture presents causal models as a bridge between machine learning and AI.

> **En palabras simples (ES):** Un modelo es una descripción matemática de cómo funciona algo. Un modelo **estadístico** encuentra cosas que suelen ocurrir juntas (correlación): "cuando hay paraguas, llueve". Un modelo **causal** dice qué causa qué ("la lluvia causa los paraguas, no al revés") y lo dibuja como un grafo de flechas. Solo el causal responde "¿qué pasa si yo cambio algo?".

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Model | Modelo | Descripción matemática de cómo funciona algo; una explicación que se puede probar. |
| Formal methods | Métodos formales | Modelos hechos con lógica y reglas escritas. |
| Statistical methods | Métodos estadísticos | Modelos que se ajustan a datos (regresión, clasificación, redes bayesianas). |
| Correlation | Correlación | A y B cambian juntos; no dice cuál causa al otro. |
| Causation | Causalidad | A **produce** B. |
| DAG (Directed Acyclic Graph) | Grafo dirigido acíclico | Dibujo con flechas causa → efecto y **sin ciclos** (no puedes volver al punto de partida siguiendo las flechas). |

## Explicación

### ¿Qué es un modelo?

Un modelo es una forma de describir algo con matemáticas, basada en reglas que fijamos antes o en datos que observamos (slides 01, s10). Hay dos familias:

- **Formales (con reglas):** lógica de primer orden (la base de [Prolog](prolog.md)), cálculo lambda (la base de LISP), lógica temporal, sistemas de reescritura y cálculo causal.
- **Estadísticos (con datos):** regresión, clasificación, redes bayesianas y redes de Markov. Son la base del aprendizaje automático (ver [Neural Networks](neural-networks.md)).

### El problema de los modelos estadísticos

Un modelo estadístico aprende **qué cosas pasan juntas**. Puede predecir muy bien sin saber **por qué**.

Ejemplo: en verano se venden más helados y también hay más ahogados en piscinas. Un modelo estadístico ve que suben juntos, pero los helados no causan ahogos: los dos los causa el **calor**. Si prohíbes los helados (una "intervención"), los ahogos no bajan. Cuando cambias la situación, la correlación puede dejar de servir.

### Los modelos causales (Pearl, 1987 según la clase)

La idea es decidir si A es la **causa** y B el **efecto**, o al revés (pero no las dos cosas a la vez). Judea Pearl dibuja estas relaciones como un **grafo de flechas sin ciclos (DAG)**:

```text
Calor → Helados vendidos
Calor → Ahogos en piscinas
```

Con ese dibujo se puede preguntar "**¿qué pasa si hago A?**" (intervención) y "**¿qué habría pasado si…?**" (contrafactual). La clase lo presenta como la teoría que puede unir el aprendizaje automático con la IA.

## Errores comunes y tips de examen

- "Correlación no implica causalidad". Además, un DAG causal **no puede tener ciclos**: "A causa B y B causa A a la vez" no vale en este modelo.
- Las redes bayesianas también son DAG, pero sus flechas dicen "estas variables dependen entre sí" (probabilidad); en una red **causal** dicen "esto produce aquello" (complemento: AIMA 4e §13.5).

## Relacionado

- [Neural Networks](neural-networks.md)
- [Propositional and First-Order Logic](propositional-and-first-order-logic.md)
- [What Is AI?](what-is-ai.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 10, 14, 15.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §13.5 Causal Networks (pendiente de ingestar).
