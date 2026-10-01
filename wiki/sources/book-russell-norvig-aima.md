---
title: "Book — Russell & Norvig, Artificial Intelligence: A Modern Approach (4e, Global)"
type: source
tags: [book, reference, textbook]
sources: [book-russell-norvig-aima]
updated: 2026-10-01
---
# Book — Russell & Norvig, *Artificial Intelligence: A Modern Approach* (4th ed., Global Edition, 2021)

> **Summary (EN):** The main course textbook ("AIMA"). Several lecture slides reproduce its figures (Romania map, A* trace, Horn clauses AND–OR graph, Criminal(West) proof tree). Not yet ingested chapter by chapter; this page maps chapters to wiki topics so that any chapter can be ingested on request.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/books/Stuart J. Russell, Peter Norvig - …_compressed.pdf](../../raw/books/Stuart%20J.%20Russell%2C%20Peter%20Norvig%20-%20Artificial%20Intelligence_%20A%20Modern%20Approach%2C%20Global%20Edition-Pearson%20%282021%29_compressed.pdf) |
| Autores | Stuart J. Russell, Peter Norvig |
| Editorial | Pearson, 2021 (4.ª ed., Global Edition) |
| Extensión | 1167 páginas del PDF |
| Estado | 📘 Referencia — **pendiente de ingestar por capítulos** |

## Mapa de capítulos ↔ wiki

| Cap. | Título | Relevancia para el curso | Página(s) de la wiki |
|---|---|---|---|
| 1 | Introduction | Alta | [What Is AI?](../concepts/what-is-ai.md), [History of AI](../concepts/history-of-ai.md) |
| 2 | Intelligent Agents | Alta | [Intelligent Agents](../concepts/intelligent-agents.md), [Task Environments](../concepts/task-environments.md), [Agent Types](../concepts/agent-types.md) |
| 3 | Solving Problems by Searching | Alta | [Problem Formulation](../concepts/problem-formulation.md), [Uninformed Search](../concepts/uninformed-search.md), [A*](../concepts/a-star-search.md), [Heuristics](../concepts/heuristics.md) |
| 4 | Search in Complex Environments (local search, SA, GA, continuous) | Alta | [Optimization Basics](../concepts/optimization-basics.md), [Simulated Annealing](../concepts/simulated-annealing.md), [Gradient Descent](../concepts/gradient-descent.md), [Genetic Algorithms](../concepts/genetic-algorithms.md) |
| 5 | Constraint Satisfaction Problems | Alta | [CSP](../concepts/constraint-satisfaction-problems.md), [N-Queens](../concepts/n-queens.md) |
| 6 | Adversarial Search and Games | Alta | [Minimax](../concepts/adversarial-search-minimax.md), [Alpha–Beta](../concepts/alpha-beta-pruning.md) |
| 7 | Logical Agents (§7.5 Horn clauses, chaining) | Alta | [Logic](../concepts/propositional-and-first-order-logic.md), [Horn Clauses](../concepts/horn-clauses-and-backward-chaining.md) |
| 8 | First-Order Logic | Media | [Logic](../concepts/propositional-and-first-order-logic.md) |
| 9 | Inference in FOL (§9.2 unification, §9.4 backward chaining & logic programming) | Alta | [Unification](../concepts/unification.md), [Prolog](../concepts/prolog.md) |
| 10–11 | Knowledge Representation; Planning | Baja (por ahora) | — |
| 12–14 | Uncertainty, Bayesian networks (§13.5 causal networks), temporal models | Media | [Statistical vs. Causal Models](../concepts/statistical-vs-causal-models.md) |
| 15–18 | Decisions, MDPs, multiagent, probabilistic programming | Baja (por ahora) | — |
| 19–… | Learning from examples, neural networks / deep learning | Media | [Neural Networks](../concepts/neural-networks.md) |

Números de página del índice: cap. 1 p. 19, cap. 2 p. 54, cap. 3 p. 81, cap. 4 p. 128, cap. 5 p. 164, cap. 6 p. 192, cap. 7 p. 226, cap. 8 p. 269, cap. 9 p. 298 (numeración del libro, no del PDF).

## Notas

- Para ingestar un capítulo: `python3 tools/extract_text.py` (ya genera el texto completo en `.cache/text/books/`) y pedir "ingest AIMA chapter N".
