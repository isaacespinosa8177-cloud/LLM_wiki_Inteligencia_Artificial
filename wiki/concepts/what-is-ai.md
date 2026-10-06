---
title: What Is AI?
type: concept
tags: [foundations, definitions, turing-test]
sources: [slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-01
---
# What Is AI? (¿Qué es la Inteligencia Artificial?)

> **Summary (EN):** There is no single definition of intelligence; the course lists understanding, problem solving, knowledge, meaning and skill. AI is the attempt to make machines exhibit such abilities. The Turing Test (1950) offers an operational, behavior-based definition, and the 1956 Dartmouth proposal states the founding conjecture that every aspect of intelligence can be described precisely enough for a machine to simulate it. AIMA frames AI as building *rational agents*.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Intelligence | Inteligencia | Capacidad de entender, resolver problemas, usar conocimiento y experiencia. |
| Turing Test | Test de Turing | Prueba por comportamiento: ¿puede un interrogador distinguir a la máquina de un humano? |
| Operational definition | Definición operacional | Definir algo por una prueba observable, no por su esencia. |
| Rational agent | Agente racional | Agente que actúa para maximizar su desempeño esperado. |
| Dartmouth conjecture | Conjetura de Dartmouth | Todo rasgo de la inteligencia puede describirse con tanta precisión que una máquina pueda simularlo. |

## Explicación

**¿Qué es inteligencia?** La clase (slides 01, slide 2) propone varias acepciones: la capacidad de entender o comprender; de resolver problemas; el conocimiento y el acto de entender; el significado que se asigna a una proposición; y la habilidad y experiencia. Ninguna basta sola, por eso la IA ha buscado definiciones **prácticas**.

**El Test de Turing (1950).** Alan Turing propuso reemplazar la pregunta "¿pueden pensar las máquinas?" por un juego: un interrogador humano conversa por texto con un humano y una computadora sin verlos. Si no logra identificar a la computadora, se considera que la máquina es inteligente. Es una definición **operacional**: mide comportamiento, no procesos internos.

**Dartmouth (1956).** McCarthy, Minsky, Rochester y Shannon organizaron el taller donde nace el nombre "Artificial Intelligence". Su propuesta enumeraba temas que siguen vigentes: lenguaje, redes neuronales, abstracción, auto-mejora, aleatoriedad y creatividad.

**Cuatro enfoques (complemento: AIMA 4e §1.1).** Russell y Norvig clasifican las definiciones según dos ejes — *pensar* vs. *actuar*, y *como humano* vs. *racionalmente*:

| | Como humano | Racionalmente |
|---|---|---|
| **Pensar** | Modelado cognitivo | Leyes del pensamiento (lógica) |
| **Actuar** | Test de Turing | **Agente racional** ← enfoque del libro y del curso |

El curso adopta el enfoque del **agente racional** (ver [Intelligent Agents](intelligent-agents.md)).

## Errores comunes y tips de examen

- El Test de Turing no mide si la máquina "entiende", sino si su comportamiento es indistinguible del humano.
- No confundir "racional" con "omnisciente" o "perfecto": racional = mejor acción esperada con la información disponible.
- El Turco Mecánico (1770) **no** era IA: escondía a un jugador humano. Es un buen ejemplo histórico de por qué hacen falta pruebas operacionales.

## Relacionado

- [History of AI](history-of-ai.md)
- [Intelligent Agents](intelligent-agents.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md)
- [People](../people.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 2, 5, 7.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §1.1 (complemento).
