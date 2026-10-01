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

1. **Flashcards (15 min):** repaso en Anki ([cómo importar el mazo](flashcards.md)) — primero las tarjetas vencidas.
2. **Explicar en voz alta (10 min):** elige 2 algoritmos y escribe su pseudocódigo intuitivo **en inglés** de memoria; compáralo con la [hoja de pseudocódigo intuitivo](intuitive-pseudocode.md).
3. **Errata (5 min):** releer [Errata](errata.md) — son las "trampas" más probables.
4. **Quiz (5–10 min, opcional):** una ronda de 10 preguntas en el [IA Exam Drill](interactive-tools.md) de la unidad del día; al final de la semana, modo *Only my mistakes*.

## Plan por día

| Día | Tema principal | Leer | Practicar | ✔ |
|---|---|---|---|---|
| **Jue 1 oct** | Orientación | [Overview](../overview.md), [Errata](errata.md) | Hacer [Exam questions](exam-questions.md) de la unidad 1 sin mirar respuestas para diagnosticar | ☐ |
| **Vie 2 oct** | Unidad 1 + inicio Unidad 2 | [Intelligent Agents](../concepts/intelligent-agents.md), [Task Environments](../concepts/task-environments.md), [Agent Types](../concepts/agent-types.md), [Problem Formulation](../concepts/problem-formulation.md), [Uninformed Search](../concepts/uninformed-search.md) | [Práctica U1](practice-unit-1-agents.md) completa; problemas 1–3 de [U2](practice-unit-2-search.md) | ☐ |
| **Sáb 3 oct** | Unidad 2: informada, juegos, CSP | [Heuristics](../concepts/heuristics.md), [A*](../concepts/a-star-search.md), [Minimax](../concepts/adversarial-search-minimax.md), [Alpha–Beta](../concepts/alpha-beta-pruning.md), [CSP](../concepts/constraint-satisfaction-problems.md) | Problemas 4–10 de [Práctica U2](practice-unit-2-search.md); trazar A\* Arad→Bucarest de memoria y comprobarlo paso a paso en el [Algorithm Lab](interactive-tools.md) (pestañas *Search* y *Games*) | ☐ |
| **Dom 4 oct** | Unidad 3: lógica y Prolog | [Logic](../concepts/propositional-and-first-order-logic.md), [Horn](../concepts/horn-clauses-and-backward-chaining.md), [Unification](../concepts/unification.md), [Prolog](../concepts/prolog.md), [Recursion & Lists](../concepts/prolog-recursion-and-lists.md) | [Práctica U3](practice-unit-3-logic.md) completa; probar las reglas en SWISH | ☐ |
| **Lun 5 oct** | Unidad 4: optimización | [Optimization Basics](../concepts/optimization-basics.md), [GD](../concepts/gradient-descent.md), [SA](../concepts/simulated-annealing.md), [GA](../concepts/genetic-algorithms.md), [PSO](../concepts/particle-swarm-optimization.md), [ACO](../concepts/ant-colony-optimization.md), [ABC](../concepts/artificial-bee-colony.md) | [Práctica U4](practice-unit-4-optimization.md) completa (GD, SA, GA, PSO, ACO a mano); jugar con w, c₁, c₂ de PSO y α de SA en el [Algorithm Lab](interactive-tools.md) | ☐ |
| **Mar 6 oct** | Repaso mixto | [Search comparison](search-algorithms-comparison.md), [Metaheuristics comparison](metaheuristics-comparison.md) | Todas las [Exam questions](exam-questions.md) y el quiz completo (*All*) del [Exam Drill](interactive-tools.md); rehacer las que fallaste | ☐ |
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
- Herramientas: [flashcards](flashcards.md) · [quiz y visualizadores](interactive-tools.md) · [pseudocódigo intuitivo](intuitive-pseudocode.md) · problemas de práctica ([U1](practice-unit-1-agents.md), [U2](practice-unit-2-search.md), [U3](practice-unit-3-logic.md), [U4](practice-unit-4-optimization.md)).
