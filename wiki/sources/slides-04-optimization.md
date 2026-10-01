---
title: "Slides 04 — Optimization and Biology-Inspired Agents"
type: source
tags: [slides, optimization, evolutionary-computation, swarm-intelligence]
sources: [slides-04-optimization]
updated: 2026-10-01
---
# Slides 04 — Optimization and Biology-Inspired Agents (Optimización y agentes bioinspirados)

> **Summary (EN):** Lecture on optimization with nature-inspired algorithms. It introduces evolutionary computation (Fogel, Rechenberg & Schwefel, Holland), the idea of local vs. global optima, and then four algorithms: Genetic Algorithms (bit-string chromosomes, crossover, mutation), Particle Swarm Optimization (Kennedy & Eberhart 1995), Ant Colony Optimization (Dorigo 1996) and Artificial Bee Colony (Karaboga 2007), framed around the exploration–exploitation trade-off.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/slides/04_Optimization.pptx](../../raw/slides/04_Optimization.pptx) |
| Tipo | Diapositivas de clase, 19 slides |
| Unidad | 4 — Optimización |
| Lecturas asociadas | [Holland 1992](paper-holland-1992-genetic-algorithms.md), [Kennedy & Eberhart 1995](paper-kennedy-eberhart-1995-pso.md), [Dorigo et al. 1996](paper-dorigo-1996-ant-system.md), [Eiben & Smith](book-eiben-smith-evolutionary-computing.md) |
| Código asociado | [code-class-optimization](code-class-optimization.md), [GA](../assignments/genetic-algorithm-task.md), [PSO](../assignments/pso-task.md) |

## Resumen por secciones

- **Slide 2 — Computación evolutiva.** Nace para resolver optimización combinatoria con principios de la evolución. Lawrence J. Fogel (1960): evolución de máquinas de estados finitos. Rechenberg y Schwefel (1970): estrategias evolutivas para optimizar parámetros. John H. Holland (1975): algoritmos genéticos como modelo general de adaptación.
- **Slide 3 — Evolución como optimización.** Adaptación, herencia, selección natural. Optimizar = encontrar máximos/mínimos **globales** sin confundirlos con **locales**. Cada punto del espacio es un "individuo" con una aptitud (*fitness*).
- **Slide 5 — Algoritmos genéticos.** Variación, selección, herencia. Individuos = cadenas de bits; evaluación con función de aptitud; reproducción por cruce; mutación = invertir un bit con cierta probabilidad.
- **Slide 6 — Operadores.** Cromosoma = número decimal codificado en binario. Cruce de un punto (generalizable a dos puntos o k puntos). Mutación bit a bit con probabilidad dada.
- **Slides 8–10 — PSO.** Kennedy y Eberhart (1995); inspirado en bandadas de aves y cardúmenes. Cada partícula tiene posición x_t, velocidad v_t y mejor posición personal p_best; el enjambre guarda g_best. φ₁, φ₂ ~ U[0,1]. Slide 10: exploración vs. explotación (figura).
- **Slides 12–13 — ACO.** Marco Dorigo (1996); metaheurística para problemas combinatorios. Las hormigas dejan feromona al volver con comida; los caminos buenos se refuerzan y la **evaporación** debilita los malos.
- **Slides 16–18 — ABC.** Karaboga (2007); abejas empleadas, observadoras y exploradoras. Empleadas y observadoras explotan; exploradoras exploran. Parámetros: número de fuentes de comida (= abejas empleadas = observadoras), *limit*, número máximo de ciclos (MCN).
- Slides 4, 7, 11, 14, 15, 19: figuras (ecuaciones de actualización, ejemplos de cruce, diagramas).

## Ideas clave

1. Todas estas técnicas son **metaheurísticas poblacionales y estocásticas**: no garantizan el óptimo global pero lo encuentran a menudo en espacios difíciles.
2. El equilibrio **exploración vs. explotación** es el hilo conductor (mutación/cruce, p_best/g_best, evaporación, abejas exploradoras).

## Conceptos que alimenta

- [Optimization Basics](../concepts/optimization-basics.md)
- [Evolutionary Computation](../concepts/evolutionary-computation.md)
- [Genetic Algorithms](../concepts/genetic-algorithms.md)
- [Swarm Intelligence](../concepts/swarm-intelligence.md)
- [Particle Swarm Optimization](../concepts/particle-swarm-optimization.md)
- [Ant Colony Optimization](../concepts/ant-colony-optimization.md)
- [Artificial Bee Colony](../concepts/artificial-bee-colony.md)

## Notas y discrepancias

- Slide 5 encabeza "Genetic Algorithms — John Holland - 1992", pero slide 2 dice correctamente que Holland propuso los GA en **1975** (*Adaptation in Natural and Artificial Systems*). 1992 es el año del artículo divulgativo de Scientific American ([paper](paper-holland-1992-genetic-algorithms.md)) y de la 2.ª edición del libro.
- Las ecuaciones de actualización de PSO, ACO y ABC están como imágenes; en las páginas de conceptos se reconstruyen desde los papers originales.
- Gradient descent y simulated annealing no aparecen en estas slides, pero sí en el código de clase ([code-class-optimization](code-class-optimization.md)).
