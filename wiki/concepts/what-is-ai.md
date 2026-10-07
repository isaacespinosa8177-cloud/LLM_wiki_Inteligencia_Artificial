---
title: What Is AI?
type: concept
tags: [foundations, definitions, turing-test]
sources: [slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-07
---
# What Is AI? (¿Qué es la Inteligencia Artificial?)

> **Summary (EN):** There is no single definition of intelligence; the course lists understanding, problem solving, knowledge, meaning and skill. AI tries to make machines show those abilities. The Turing Test (1950) defines intelligence by behavior: if a judge cannot tell the machine from a human in a text conversation, the machine counts as intelligent. The 1956 Dartmouth workshop named the field, and the textbook (AIMA) defines AI as building rational agents.

> **En palabras simples (ES):** No hay una sola definición de inteligencia; el curso menciona entender, resolver problemas, tener conocimiento, dar significado y tener habilidad. La IA intenta que las máquinas hagan eso. La **prueba de Turing** (1950) dice: si al conversar no distingues a la máquina de una persona, la máquina se comporta de forma inteligente. El libro de Russell y Norvig dice que la IA construye **agentes racionales**: programas que eligen la mejor acción según lo que saben.

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Intelligence | Inteligencia | Capacidad de entender, resolver problemas y usar lo que sabes y lo que has vivido. |
| Turing Test | Prueba de Turing | Un juez conversa por texto con una persona y una máquina; si no las distingue, la máquina "pasa". |
| Operational definition | Definición operacional | Definir algo por una prueba que se puede observar, no por lo que "es" por dentro. |
| Rational agent | Agente racional | Programa o robot que elige la acción con mejor resultado esperado según lo que sabe. |
| Dartmouth conjecture | Conjetura de Dartmouth | La idea de 1956 de que cualquier parte de la inteligencia se puede describir tan bien que una máquina la pueda imitar. |

## Explicación

### 1. ¿Qué es la inteligencia?

La clase (slides 01, slide 2) da varias definiciones. Inteligencia puede ser:

- la capacidad de **entender** o comprender;
- la capacidad de **resolver problemas**;
- el **conocimiento** y el acto de entender;
- el **significado** que le damos a una frase;
- la **habilidad** y la experiencia.

Ninguna basta sola. Por eso la IA prefirió definiciones **prácticas**, que se puedan comprobar con una prueba.

### 2. La prueba de Turing (1950)

Alan Turing cambió la pregunta "¿las máquinas pueden pensar?" (muy difícil de responder) por un juego que sí se puede hacer:

1. Un juez humano chatea por texto con dos participantes que no ve: una persona y una computadora.
2. El juez hace las preguntas que quiera.
3. Si el juez **no logra adivinar** cuál es la computadora, decimos que la máquina se comporta de forma inteligente.

Esto es una definición **operacional**: mide solo el **comportamiento** (lo que la máquina responde), no lo que pasa dentro de ella.

### 3. Dartmouth (1956): nace el nombre "IA"

McCarthy, Minsky, Rochester y Shannon organizaron un taller en Dartmouth donde nace el nombre *Artificial Intelligence*. Su propuesta decía que **cualquier parte de la inteligencia se puede describir con tanta precisión que una máquina pueda imitarla**. Los temas que propusieron (lenguaje, redes neuronales, abstracción, mejorarse a sí misma, azar y creatividad) siguen vigentes.

### 4. Cuatro formas de definir la IA (complemento: AIMA 4e §1.1)

El libro ordena las definiciones con dos preguntas: ¿queremos que la máquina **piense** o que **actúe**? ¿Que lo haga **como un humano** o **de la mejor forma posible (racionalmente)**?

| | Como humano | Racionalmente (de la mejor forma) |
|---|---|---|
| **Pensar** | Imitar cómo piensa la mente humana (modelado cognitivo) | Pensar con lógica correcta (leyes del pensamiento) |
| **Actuar** | Comportarse como humano (prueba de Turing) | **Hacer lo mejor posible: agente racional** ← enfoque del libro y del curso |

El curso usa el enfoque del **agente racional** (ver [Intelligent Agents](intelligent-agents.md)): no importa si la máquina piensa como nosotros, sino que **elija bien** qué hacer.

## Errores comunes y tips de examen

- La prueba de Turing **no** mide si la máquina "entiende"; solo mide si su comportamiento no se distingue del de una persona.
- "Racional" no significa "perfecto" ni "que lo sabe todo": significa elegir la **mejor acción esperada con la información que tiene**.
- El Turco Mecánico (1770) **no** era IA: era una caja con un jugador de ajedrez humano escondido. Es un buen ejemplo de por qué hacen falta pruebas que se puedan comprobar.

## Relacionado

- [History of AI](history-of-ai.md)
- [Intelligent Agents](intelligent-agents.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md)
- [People](../people.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 2, 5, 7.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §1.1 (complemento).
