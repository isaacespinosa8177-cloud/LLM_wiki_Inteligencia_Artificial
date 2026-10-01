# Index — Inteligencia Artificial Wiki

Catalog of every page. The LLM reads this first when answering a question and updates it on every ingest. Pages: 72 · Sources ingested: 11 of 14 in full + book chapters (AIMA 2–6, Eiben & Smith 3–5) · Last update: 2026-10-01.

## Start here

- [Overview](overview.md) — course map: how the four units connect.
- [Glossary](glossary.md) — English term → Spanish explanation, alphabetical.
- [People](people.md) — who proposed what, and when.
- [Log](log.md) — history of ingests, queries and lint passes.

## Sources

**Slides (lectures)**
- [Slides 01 — Introduction to AI](sources/slides-01-introduction-to-ai.md) — definitions, timeline from Talos to LLMs, statistical vs. causal models.
- [Slides 02 — Problem Solving](sources/slides-02-problem-solving.md) — formulation, BFS/DFS, greedy, A\*, minimax, alpha–beta, CSP.
- [Slides 03 — Intelligent Agents](sources/slides-03-intelligent-agents.md) — agent function, rationality, PEAS, environments, agent types.
- [Slides 04 — Optimization](sources/slides-04-optimization.md) — evolutionary computation, GA, PSO, ACO, ABC.
- [Slides XX — Logic Programming with Prolog](sources/slides-xx-logic-programming-prolog.md) — Horn clauses to SWI-Prolog, N-Queens, Lab 01.

**Papers**
- [Kennedy & Eberhart 1995 — PSO](sources/paper-kennedy-eberhart-1995-pso.md) — how a flocking simulation became an optimizer.
- [Dorigo, Maniezzo & Colorni 1996 — Ant System](sources/paper-dorigo-1996-ant-system.md) — pheromone-based TSP solver; α=1, β=5, ρ=0.5.
- [Holland 1992 — Genetic Algorithms](sources/paper-holland-1992-genetic-algorithms.md) — crossover, schemata, implicit parallelism.

**Books (chapter maps; AIMA 2–6 and Eiben & Smith 3–5 ingested)**
- [Russell & Norvig — AIMA 4e](sources/book-russell-norvig-aima.md) — main textbook; ch. 2–6 ingested.
- [Luger — AI 6e](sources/book-luger-ai.md) — secondary textbook; Prolog §14.
- [Eiben & Smith — Evolutionary Computing](sources/book-eiben-smith-evolutionary-computing.md) — EA textbook; ch. 3–5 ingested.

**Code**
- [Class optimization scripts](sources/code-class-optimization.md) — gradient descent and simulated annealing (with 2 bugs noted).
- [Prolog examples (01_Code)](sources/code-prolog-examples.md) — family, factorial, fibonacci, lists, BST, queens.

## Concepts

**Unit 1 — Foundations and agents**
- [What Is AI?](concepts/what-is-ai.md) — definitions of intelligence, Turing Test, Dartmouth, four approaches.
- [History of AI](concepts/history-of-ai.md) — merged timeline of every date in the course.
- [Neural Networks](concepts/neural-networks.md) — perceptron, backprop, SVM, deep learning.
- [Statistical vs. Causal Models](concepts/statistical-vs-causal-models.md) — formal vs. statistical models; Pearl's causal DAGs.
- [Intelligent Agents](concepts/intelligent-agents.md) — agent function vs. program, rationality, PEAS.
- [Task Environments](concepts/task-environments.md) — six environment dimensions, course problems classified.
- [Agent Types](concepts/agent-types.md) — reflex, model-based, goal-based, utility-based.
- [State Representation](concepts/state-representation.md) — atomic, factored, structured.

**Unit 2 — Search**
- [Problem Formulation](concepts/problem-formulation.md) — five components, state space, frontier and explored set.
- [Uninformed Search](concepts/uninformed-search.md) — BFS, DFS, depth-limited, IDS, UCS/Dijkstra.
- [Heuristics](concepts/heuristics.md) — admissible, consistent, Manhattan, misplaced tiles, h_SLD.
- [Greedy Best-First Search](concepts/greedy-best-first-search.md) — f = h; fast, not optimal.
- [A* Search](concepts/a-star-search.md) — f = g + h; full Romania trace.
- [Adversarial Search and Minimax](concepts/adversarial-search-minimax.md) — MAX/MIN, cutoff, evaluation functions.
- [Alpha–Beta Pruning](concepts/alpha-beta-pruning.md) — same answer, O(b^(m/2)).
- [Search in Complex Environments](concepts/search-in-complex-environments.md) — nondeterminism (AND–OR search), belief states, online search.
- [Monte Carlo Tree Search](concepts/monte-carlo-tree-search.md) — selection/expansion/simulation/back-propagation, UCB1; Go, AlphaGo, Chess vs. Go.
- [Stochastic and Partially Observable Games](concepts/stochastic-and-partially-observable-games.md) — expectiminimax, Kriegspiel, limits of game search.
- [Constraint Satisfaction Problems](concepts/constraint-satisfaction-problems.md) — backtracking, MRV, forward checking, arc consistency.
- [N-Queens](concepts/n-queens.md) — Prolog and Python versions; generate-and-test vs. test-as-you-go.

**Unit 3 — Logic and Prolog**
- [Propositional and First-Order Logic](concepts/propositional-and-first-order-logic.md) — syntax, CNF, decidability.
- [Horn Clauses and Backward Chaining](concepts/horn-clauses-and-backward-chaining.md) — rules, facts, goals; Criminal(West).
- [Unification](concepts/unification.md) — substitutions, occurs check.
- [Prolog](concepts/prolog.md) — syntax, SLD resolution, is/2, NAF, cut, debugging.
- [Recursion and Lists in Prolog](concepts/prolog-recursion-and-lists.md) — factorial, Fibonacci, lists, isPerm bug, BST.

**Unit 4 — Optimization**
- [Optimization Basics](concepts/optimization-basics.md) — local vs. global, exploration vs. exploitation, benchmark functions.
- [Local Search and Hill Climbing](concepts/local-search-hill-climbing.md) — hill climbing variants, random restarts, local beam search; 8-queens stats.
- [Gradient Descent](concepts/gradient-descent.md) — w ← w − η∇f; learning-rate behavior.
- [Simulated Annealing](concepts/simulated-annealing.md) — e^(−Δ/T), cooling schedules.
- [Evolutionary Computation](concepts/evolutionary-computation.md) — EP, ES, GA; the generic EA loop.
- [Genetic Algorithms](concepts/genetic-algorithms.md) — encoding, selection, crossover, mutation, schema theorem.
- [EA Representation and Variation](concepts/ea-representation-and-variation.md) — binary/integer/real/permutation operators: bit-flip, uniform, Gaussian, PMX, order crossover.
- [EA Selection and Population Management](concepts/ea-selection-and-population-management.md) — FPS, ranking, tournament, SUS, elitism, (μ+λ)/(μ,λ), takeover time, diversity.
- [Swarm Intelligence](concepts/swarm-intelligence.md) — Millonas' principles, stigmergy.
- [Particle Swarm Optimization](concepts/particle-swarm-optimization.md) — p_best, g_best, inertia.
- [Ant Colony Optimization](concepts/ant-colony-optimization.md) — τ^α η^β, evaporation, TSP.
- [Artificial Bee Colony](concepts/artificial-bee-colony.md) — employed, onlooker and scout bees.

## Assignments

- [Homework 01 — Search Methods, Games and Heuristics](assignments/deber-1-search-problems.md) — official statement, Chess vs. Go, 6 exercises; Sudoku on official boards (naive 335,637 vs. FC 309 assignments). ⚠️ AI agents forbidden.
- [A* vs. Dijkstra](assignments/astar-vs-dijkstra.md) — Romania map: 5 vs. 9 expansions, cost 418.
- [Tic-tac-toe 4×4 Minimax](assignments/tic-tac-toe-4x4-minimax.md) — depth-4 minimax; win-score bug and fix.
- [Prolog Lab 01 — Family](assignments/prolog-lab-01-family.md) — 24/24 tests pass; review and analysis answers.
- [Genetic algorithm task](assignments/genetic-algorithm-task.md) — 16-bit GA reaches (−2, 2) at epoch 20.
- [PSO task](assignments/pso-task.md) — vectorized PSO reaches (−2, 2), f = 10.

## Study

- [Intuitive pseudocode cheat sheet](study/intuitive-pseudocode.md) — every algorithm as plain-English steps + "say it in the exam" answer (generated).
- [Study plan — test Thu Oct 8](study/study-plan.md) — day-by-day plan with daily routine and priorities.
- [Search algorithms comparison](study/search-algorithms-comparison.md) — Unit 2 cheat sheet with real numbers.
- [Metaheuristics comparison](study/metaheuristics-comparison.md) — Unit 4 cheat sheet.
- Practice problems with worked solutions: [Unit 1 — Agents](study/practice-unit-1-agents.md) · [Unit 2 — Search, games, CSP](study/practice-unit-2-search.md) · [Unit 3 — Logic & Prolog](study/practice-unit-3-logic.md) · [Unit 4 — Optimization](study/practice-unit-4-optimization.md)
- [Interactive tools — Exam Drill & Algorithm Lab](study/interactive-tools.md) — browser quiz (61 MCQs, per-unit score, "only my mistakes") and step-through visualizers for search, alpha–beta and PSO/GA/SA/GD.
- [Quiz bank](study/quiz-bank.md) — the 61 multiple-choice questions behind the quiz and the `quiz` Anki cards (edit here, then rebuild).
- [Flashcards (Anki deck)](study/flashcards.md) — 239 auto-generated cards (glossary, exam questions, practice, pseudocode, quiz) tagged by unit; how to import.
- [Exam questions](study/exam-questions.md) — 34 self-test questions with hidden answers.
- [Errata](study/errata.md) — source contradictions and code bugs to remember.
