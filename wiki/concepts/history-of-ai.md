---
title: History of AI
type: concept
tags: [foundations, history, timeline]
sources: [slides-01-introduction-to-ai, slides-04-optimization, slides-xx-logic-programming-prolog, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system]
updated: 2026-10-07
---
# History of AI (Historia de la IA — línea de tiempo)

> **Summary (EN):** One timeline with every date mentioned in the course sources, from mythical robots to today's LLM agents. Use it to answer "who proposed X and when?" questions and to see how each algorithm fits in history.

> **En palabras simples (ES):** Esta página es una línea de tiempo: quién inventó cada idea y en qué año. Para el examen, lo más preguntado es: prueba de Turing (Alan Turing, 1950), Dartmouth, donde nace el nombre "IA" (1956), perceptrón (Rosenblatt, 1958), Prolog (Colmerauer y Roussel, 1972), algoritmos genéticos (Holland, 1975), PSO (Kennedy y Eberhart, 1995) y colonia de hormigas (Dorigo y colegas, 1996).

## Las 8 fechas que más se preguntan

| Año | Quién | Qué |
|---|---|---|
| 1950 | Alan Turing | Prueba de Turing |
| 1956 | McCarthy, Minsky, Rochester, Shannon | Taller de Dartmouth: nace el nombre "IA" |
| 1958 | Frank Rosenblatt | Perceptrón (primera neurona artificial que aprende) |
| 1972 | Colmerauer y Roussel (Marsella), con la teoría de Kowalski | Prolog |
| 1975 | John Holland | Algoritmos genéticos |
| 1995 | Kennedy y Eberhart | PSO (enjambre de partículas) |
| 1996 | Dorigo, Maniezzo y Colorni | Ant System (colonia de hormigas) |
| 2007 | Karaboga | Colonia artificial de abejas (ABC) |

## Línea de tiempo completa

| Año | Hito | Por qué importa (en simple) | Fuente |
|---|---|---|---|
| ~800 a.C.? | **Talos** en la *Ilíada*: un gigante de bronce que se movía solo y protegía Creta | La idea de máquinas que actúan solas es muy antigua | slides-01 s19 |
| ~200 a.C. | **Mecanismo de Anticitera** | La "computadora" más antigua que se conoce: unos engranajes que predecían eclipses | slides-01 s17–18 |
| 1768–1774 | Autómatas de **Jaquet-Droz** (un músico, un dibujante y un escritor mecánicos) | Máquinas que seguían un "programa" mecánico | slides-01 s3 |
| 1770 | **Turco Mecánico** (von Kempelen) | IA falsa: escondía a una persona que jugaba ajedrez | slides-01 s3 |
| 1936–38 | **Z1** de Konrad Zuse | Calculadora programable que usaba números binarios | slides-01 s4 |
| 1945 | **ENIAC** | Primera computadora electrónica de uso general | slides-01 s4 |
| 1950 | **Prueba de Turing** | Forma práctica de decidir si una máquina es inteligente | slides-01 s5 |
| 1956 | **Taller de Dartmouth** | Nace la IA como campo y su nombre | slides-01 s7 |
| 1957 | **FORTRAN** (IBM) | Lenguaje para hacer cálculos numéricos | slides-01 s6 |
| 1958 | **LISP** (McCarthy) | Lenguaje de la IA simbólica: trabaja con listas y recursión | slides-01 s6 |
| 1958 | **Perceptrón** (Rosenblatt) | Primera neurona artificial que aprende de ejemplos | slides-01 s8 |
| 1960 | **Fogel**: programación evolutiva | Primera idea de "evolucionar" programas | slides-04 s2 |
| mediados 60s | **Holland** desarrolla el algoritmo genético | Soluciones que se cruzan y mutan como los genes | Holland 1992 |
| 1970 | **Rechenberg y Schwefel**: estrategias evolutivas | Evolución para ajustar números reales | slides-04 s2 |
| 1972 | **Prolog** (Colmerauer y Roussel, Marsella; teoría de Kowalski) | Programar escribiendo hechos y reglas lógicas | slides-XX s8 |
| 1975 | **Holland**, libro *Adaptation in Natural and Artificial Systems* | Publicación formal de los algoritmos genéticos | slides-04 s2 |
| 1975 | **Backpropagation** (fecha de la clase) | Permite entrenar redes de varias capas (y resolver XOR) | slides-01 s11 |
| 1979 | **Kowalski**: "Algoritmo = Lógica + Control" | Frase clave de la programación lógica | slides-XX s2 |
| 1986 | Aparece el término **deep learning** | — | slides-01 s13 |
| 1987 | **Pearl**: cálculo causal (fecha de la clase); nace SWI-Prolog | Modelos que dicen qué causa qué | slides-01 s15, slides-XX s9 |
| 1992 | Holland, artículo en *Scientific American* | Explica los algoritmos genéticos al público general | Holland 1992 |
| 1995 | **SVM** (Vapnik, AT&T Bell Labs) | Clasificador que deja el mayor espacio posible entre dos grupos | slides-01 s12 |
| 1995 | **PSO** (Kennedy y Eberhart) | Optimización imitando bandadas de pájaros | paper PSO |
| 1996 | **Ant System / ACO** (Dorigo, Maniezzo, Colorni) | Optimización de rutas imitando hormigas | paper AS |
| 2000s | **Deep learning** moderno (Bengio, Hinton, LeCun) | Redes con muchas capas que funcionan muy bien | slides-01 s13 |
| 2007 | **Artificial Bee Colony** (Karaboga) | Optimización imitando abejas | slides-04 s16 |
| 2020s | **IA generativa, LLMs, agentes** | Lo que existe hoy (como ChatGPT o Claude) | slides-01 s2 |

## Explicación

La historia de la IA tiene **dos grandes caminos** que el curso recorre:

1. **IA simbólica (con reglas):** las personas escriben el conocimiento a mano, como reglas y hechos. Ejemplos: LISP, Prolog, sistemas expertos y la búsqueda en mapas. Ver [Prolog](prolog.md) y [Problem Formulation](problem-formulation.md).
2. **IA que aprende de datos (subsimbólica o estadística):** la máquina **aprende** sola a partir de ejemplos. Ejemplos: perceptrón, backpropagation, SVM, deep learning. Ver [Neural Networks](neural-networks.md).

Además hay un **tercer camino inspirado en la naturaleza**: algoritmos que imitan la evolución (genéticos) y los grupos de animales (enjambres). Ver [Evolutionary Computation](evolutionary-computation.md) y [Swarm Intelligence](swarm-intelligence.md). La clase termina con los **modelos causales** como posible puente entre los dos primeros caminos ([Statistical vs. Causal Models](statistical-vs-causal-models.md)).

## Errores comunes y tips de examen

- **Prolog no es de Dennis Ritchie** (Ritchie creó el lenguaje C). Las slides tienen ese error; ver [errata](../study/errata.md).
- **Los algoritmos genéticos son de 1975** (Holland). 1992 es el año de un artículo de divulgación.
- Backpropagation suele atribuirse a Werbos (1974) y se hizo famoso con Rumelhart, Hinton y Williams (1986) — conocimiento general. Si en el examen preguntan la fecha de la clase, es 1975.

## Relacionado

- [What Is AI?](what-is-ai.md)
- [People](../people.md)
- [Overview](../overview.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), [Slides 04](../sources/slides-04-optimization.md), [Slides XX](../sources/slides-xx-logic-programming-prolog.md)
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md), [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md), [Dorigo et al. 1996](../sources/paper-dorigo-1996-ant-system.md)
