---
title: Study plan — Test on Thursday, October 8, 2026
type: study
tags: [study, plan, exam]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# Study plan — Test on Thursday, October 8 (Plan de estudio)

> **Summary (EN):** A seven-day plan from Thursday Oct 1 to the test on Thursday Oct 8, 2026. It assumes the test covers all four units seen so far (foundations & agents, search & games & CSP, logic & Prolog, optimization). Each day has one main unit, a fixed daily routine (flashcards + explaining pseudocode aloud in English), and a checklist. Tell the LLM the official test scope when you know it and this plan will be adjusted.

## Rutina diaria (≈ 30 min, todos los días)

1. **Flashcards (15 min):** repaso en Anki — primero las tarjetas vencidas.
2. **Explicar en voz alta (10 min):** elige 2 algoritmos y escribe su pseudocódigo intuitivo **en inglés** de memoria; compáralo con la [hoja de pseudocódigo intuitivo](intuitive-pseudocode.md).
3. **Errata (5 min):** releer [Errata](errata.md) — son las "trampas" más probables.

## Plan por día

| Día | Tema principal | Leer | Practicar | ✔ |
|---|---|---|---|---|
| **Jue 1 oct** | Orientación | [Overview](../overview.md), [Errata](errata.md) | Hacer [Exam questions](exam-questions.md) de la unidad 1 sin mirar respuestas para diagnosticar | ☐ |
| **Vie 2 oct** | Unidad 1 + inicio Unidad 2 | [Intelligent Agents](../concepts/intelligent-agents.md), [Task Environments](../concepts/task-environments.md), [Agent Types](../concepts/agent-types.md), [Problem Formulation](../concepts/problem-formulation.md), [Uninformed Search](../concepts/uninformed-search.md) | PEAS de 3 agentes; clasificar 5 entornos; trazar BFS y DFS a mano | ☐ |
| **Sáb 3 oct** | Unidad 2: informada, juegos, CSP | [Heuristics](../concepts/heuristics.md), [A*](../concepts/a-star-search.md), [Minimax](../concepts/adversarial-search-minimax.md), [Alpha–Beta](../concepts/alpha-beta-pruning.md), [CSP](../concepts/constraint-satisfaction-problems.md) | Trazar A\* Arad→Bucarest de memoria; un árbol alpha-beta; forward checking en un Sudoku pequeño | ☐ |
| **Dom 4 oct** | Unidad 3: lógica y Prolog | [Logic](../concepts/propositional-and-first-order-logic.md), [Horn](../concepts/horn-clauses-and-backward-chaining.md), [Unification](../concepts/unification.md), [Prolog](../concepts/prolog.md), [Recursion & Lists](../concepts/prolog-recursion-and-lists.md) | Convertir a CNF; 6 unificaciones; árbol SLD de `ancestor`; escribir reglas en SWISH | ☐ |
| **Lun 5 oct** | Unidad 4: optimización | [Optimization Basics](../concepts/optimization-basics.md), [GD](../concepts/gradient-descent.md), [SA](../concepts/simulated-annealing.md), [GA](../concepts/genetic-algorithms.md), [PSO](../concepts/particle-swarm-optimization.md), [ACO](../concepts/ant-colony-optimization.md), [ABC](../concepts/artificial-bee-colony.md) | Un paso de GD, una actualización PSO y una probabilidad ACO a mano; cruce y mutación de bits | ☐ |
| **Mar 6 oct** | Repaso mixto | [Search comparison](search-algorithms-comparison.md), [Metaheuristics comparison](metaheuristics-comparison.md) | Todas las [Exam questions](exam-questions.md); rehacer las que fallaste | ☐ |
| **Mié 7 oct** | Simulacro | [History of AI](../concepts/history-of-ai.md) (fechas y autores), [People](../people.md) | Simulacro cronometrado (60–90 min) sin apuntes; corregir; repasar solo lo fallado. **Dormir bien.** | ☐ |
| **Jue 8 oct** | 🎯 Test | — | 20 min de flashcards en la mañana; nada nuevo | ☐ |

## Prioridades si falta tiempo

1. Propiedades de los algoritmos de búsqueda (completo / óptimo / complejidad) y A\*.
2. Minimax + alpha-beta (trazar a mano).
3. Ecuaciones de PSO y ACO; operadores de GA; aceptación de SA.
4. Unificación, cláusulas de Horn, `is` vs `=`, negación por fallo.
5. Fechas y autores ([History](../concepts/history-of-ai.md)) — y las erratas (Prolog ≠ Ritchie; GA = 1975).

## Notas

- Alcance del test supuesto: unidades 1–4. Si el profesor confirma otro alcance, pídele a la IA que ajuste este plan.
- Las herramientas de estudio (flashcards, quiz, visualizadores, pseudocódigo intuitivo, problemas de práctica) se enlazan aquí a medida que se crean.
