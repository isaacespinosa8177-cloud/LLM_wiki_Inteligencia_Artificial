---
title: History of AI
type: concept
tags: [foundations, history, timeline]
sources: [slides-01-introduction-to-ai, slides-04-optimization, slides-xx-logic-programming-prolog, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system]
updated: 2026-10-01
---
# History of AI (Historia de la IA — línea de tiempo)

> **Summary (EN):** A single timeline that merges every date mentioned across the course sources, from mythical automata to LLM agents. Use it to place each algorithm in context and to answer "who proposed X and when?" exam questions.

## Línea de tiempo

| Año | Hito | Por qué importa | Fuente |
|---|---|---|---|
| ~800 a.C.? | **Talos** en la *Ilíada*: gigante autómata de bronce que protege Creta | El sueño de máquinas que actúan solas es antiguo | slides-01 s19 |
| ~200 a.C. | **Mecanismo de Anticitera** | Computadora analógica más antigua conocida; predecía eclipses | slides-01 s17–18 |
| 1768–1774 | Autómatas de **Jaquet-Droz** (músico, dibujante, escritor) | Máquinas programables mecánicas | slides-01 s3 |
| 1770 | **Turco Mecánico** (von Kempelen) | Falsa IA: escondía a un humano | slides-01 s3 |
| 1936–38 | **Z1** de Konrad Zuse | Calculadora binaria programable con punto flotante | slides-01 s4 |
| 1945 | **ENIAC** | Computadora electrónica de propósito general | slides-01 s4 |
| 1950 | **Test de Turing** | Definición operacional de inteligencia | slides-01 s5 |
| 1956 | **Taller de Dartmouth** | Nace la IA como campo | slides-01 s7 |
| 1957 | **FORTRAN** (IBM) | Lenguaje imperativo para cálculo numérico | slides-01 s6 |
| 1958 | **LISP** (McCarthy) | Lenguaje de la IA simbólica: listas, recursión, cálculo λ | slides-01 s6 |
| 1958 | **Perceptrón** (Rosenblatt) | Primer modelo neuronal que aprende | slides-01 s8 |
| 1960 | **Fogel**: programación evolutiva (máquinas de estados finitos) | Inicio de la computación evolutiva | slides-04 s2 |
| mediados 60s | **Holland** desarrolla el algoritmo genético | Cruce + mutación | Holland 1992 |
| 1970 | **Rechenberg y Schwefel**: estrategias evolutivas | Optimización de parámetros | slides-04 s2 |
| 1972 | **Prolog** (Colmerauer y Roussel, Marsella; teoría de Kowalski) | Programación lógica | slides-XX s8 |
| 1975 | **Holland**, *Adaptation in Natural and Artificial Systems* (GA) | Formalización de los GA | slides-04 s2 |
| 1975 | **Backpropagation** (fecha de la clase) | Entrenar redes multicapa; resuelve XOR | slides-01 s11 |
| 1979 | **Kowalski**: *Algorithm = Logic + Control* | Lema de la programación lógica | slides-XX s2 |
| 1986 | Se acuña el término **deep learning** | — | slides-01 s13 |
| 1987 | **Pearl**: cálculo causal (fecha de la clase); nace SWI-Prolog | Causalidad con DAGs | slides-01 s15, slides-XX s9 |
| 1992 | Holland, artículo de *Scientific American* | Divulgación de los GA | Holland 1992 |
| 1995 | **SVM** (Vapnik, AT&T Bell Labs) | Clasificador de margen máximo | slides-01 s12 |
| 1995 | **PSO** (Kennedy y Eberhart) | Inteligencia de enjambre continua | paper PSO |
| 1996 | **Ant System / ACO** (Dorigo, Maniezzo, Colorni) | Inteligencia de enjambre combinatoria | paper AS |
| 2000s | **Deep learning** moderno (Bengio, Hinton, LeCun) | Redes profundas | slides-01 s13 |
| 2007 | **Artificial Bee Colony** (Karaboga) | Enjambre de abejas | slides-04 s16 |
| 2020s | **IA generativa, LLMs, agentes** | Estado actual | slides-01 s2 |

## Explicación

La historia de la IA alterna dos grandes corrientes que el curso recorre:

1. **Simbólica / lógica** — LISP, Prolog, sistemas expertos, búsqueda en espacios de estados. El conocimiento se escribe explícitamente (ver [Prolog](prolog.md), [Problem Formulation](problem-formulation.md)).
2. **Subsimbólica / estadística** — perceptrón, backprop, SVM, deep learning; el conocimiento se **aprende** de datos (ver [Neural Networks](neural-networks.md)).

En paralelo crece una tercera línea **bioinspirada**: computación evolutiva y enjambres (ver [Evolutionary Computation](evolutionary-computation.md), [Swarm Intelligence](swarm-intelligence.md)). La clase cierra con los **modelos causales** como posible puente ([Statistical vs. Causal Models](statistical-vs-causal-models.md)).

## Errores comunes y tips de examen

- **Prolog no es de Dennis Ritchie** (eso es C). Ver [errata](../study/errata.md).
- **Los GA son de 1975** (Holland); 1992 es el artículo divulgativo.
- Backpropagation suele atribuirse a Werbos (1974) y se popularizó con Rumelhart, Hinton y Williams (1986) — conocimiento general; la clase usa 1975.

## Relacionado

- [What Is AI?](what-is-ai.md)
- [People](../people.md)
- [Overview](../overview.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), [Slides 04](../sources/slides-04-optimization.md), [Slides XX](../sources/slides-xx-logic-programming-prolog.md)
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md), [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md), [Dorigo et al. 1996](../sources/paper-dorigo-1996-ant-system.md)
