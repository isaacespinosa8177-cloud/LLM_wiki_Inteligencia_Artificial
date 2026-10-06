---
title: Errata and source discrepancies
type: study
tags: [study, errata, lint]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog, code-class-optimization]
updated: 2026-10-01
---
# Errata and source discrepancies (Erratas y discrepancias entre fuentes)

> **Summary (EN):** Every place where a course source contradicts another source or established fact, or where class code has a bug. Check this page before an exam so you answer with the correct version, and ask the professor when in doubt. The LLM appends here on every ingest and lint pass.

## Contradicciones entre fuentes

| # | Dónde | Lo que dice | Lo correcto | Estado |
|---|---|---|---|---|
| 1 | [Slides 01](../sources/slides-01-introduction-to-ai.md), slide 9 | Prolog "created by Dennis Ritchie at Bell Labs… imperative, compiled language" | Prolog: Colmerauer y Roussel, Marsella, 1972, con teoría de Kowalski; **declarativo**. La descripción corresponde a **C**. Lo confirma [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slide 8. | Abierto — confirmar con el profesor |
| 2 | [Slides 04](../sources/slides-04-optimization.md), slide 5 | "Genetic Algorithms — John Holland - 1992" | Holland propuso los GA en **1975** (la propia slide 2 lo dice). 1992 = artículo de Scientific American / 2.ª ed. del libro. | Resuelto en la wiki |
| 3 | [Slides 04](../sources/slides-04-optimization.md), slide 12 | "Ant Colony Optimization — Dorigo 1996" | El paper de 1996 lo llama **Ant System**; "ACO" como metaheurística general es posterior (1999). Diferencia de nombre, no de fondo. | Nota |
| 4 | [Slides 02](../sources/slides-02-problem-solving.md), slide 14 | A\* "complete… if h is admissible"; óptimo "if h is admissible/consistent" | Completitud requiere además b finito y costos ≥ ε > 0. Optimalidad: admisible basta si el algoritmo **reabre** estados cuando encuentra un camino más barato (best-first de AIMA 4e); si **nunca reabre** estados expandidos (lista cerrada clásica, como en las tareas), hace falta **consistente**. | Nota (precisado con AIMA §3.5) |
| 5 | [Slides 03](../sources/slides-03-intelligent-agents.md), slide 2 | Bajo "What Is an Agent?" aparecen viñetas sobre proposiciones lógicas | Texto sobrante de otra presentación; ignorar. | Nota |
| 6 | [Slides 01](../sources/slides-01-introduction-to-ai.md), slide 11 | Backpropagation "1975" | Suele atribuirse a Werbos (1974) y popularizarse con Rumelhart, Hinton y Williams (1986). En examen, usar la fecha de clase si la piden. | Nota |
| 7 | [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) vs. [tarea PSO](../assignments/pso-task.md) | Paper: sin w, coeficientes 2 | La tarea usa la variante con inercia w (posterior). Ambas válidas; decir cuál se usa. | Nota |
| 8 | [AIMA 4e](../sources/book-russell-norvig-aima.md), notas del cap. 6 | AlphaGo venció a Lee Sedol "4–1 in 2015" | El match fue en **marzo de 2016** (conocimiento general). AIMA también imprime "9!/2 = 181,400" estados del 8-puzzle: son **181 440**. | Nota |
| 9 | [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md), Tabla 3.3 (p. 36) | Tras mutar, `11100` → x = 26, f = 676 y `10100` → x = 18, f = 324; media 588.5 | `11100`₂ = **28** (f = 784) y `10100`₂ = **20** (f = 400); media **634.5**. Probablemente las mutaciones pretendidas eran `11010` y `10010`. | Nota (verificado en el PDF) |

## Bugs en código de clase y tareas

| # | Archivo | Bug | Arreglo | Página |
|---|---|---|---|---|
| B1 | `gd_steroids.py` | La superficie animada usa (y+1)², la función optimizada (y+2)² | Usar `objective` para Z y para zs | [code-class-optimization](../sources/code-class-optimization.md) |
| B2 | `sa_functions.py` | Enfriamiento 0.8 con 100 000 iteraciones: T ≈ 0 tras ~100 iter.; división por cero tras ~3 400 | α ≈ 0.9999 o α = (T_f/T₀)^(1/iter) | [code-class-optimization](../sources/code-class-optimization.md) |
| B3 | `tic_tac_toe_4x4_isaac (2).py` | Victoria = ±1 < heurística → no toma victorias inmediatas (2/54 casos) | Victoria = ±1000 | [tarea](../assignments/tic-tac-toe-4x4-minimax.md) |
| B4 | `Espinosa_Isaac_lab01.pl` | `spouse/2` asimétrico → `father_in_law(marcelo, mauricio)` falla | `married/2` simétrico | [tarea](../assignments/prolog-lab-01-family.md) |
| B5 | `Espinosa_Isaac_lab01.pl` | 15 avisos "Test succeeded with choicepoint" | `!` al final o `[nondet]` | [tarea](../assignments/prolog-lab-01-family.md) |
| B6 | Deber 1, `dfs` | `visited` global + límite de profundidad puede perder soluciones dentro del límite | Guardar profundidad mínima o chequear solo el camino actual | [tarea](../assignments/deber-1-search-problems.md) |
| B7 | `isPerm.pl` (clase) | Igualdad de conjuntos, no permutación | `msort/2` | [Recursion and Lists](../concepts/prolog-recursion-and-lists.md) |

## Relacionado

- [Exam questions](exam-questions.md)
- [Overview](../overview.md)
