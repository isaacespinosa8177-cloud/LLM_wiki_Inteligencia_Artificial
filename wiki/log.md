# Log

Append-only record of wiki activity. Newest entries at the bottom.
Recent activity: `grep "^## \[" wiki/log.md | tail -5`

## [2026-10-01] setup | Wiki created from Karpathy's LLM Wiki pattern

- Downloaded the pattern (gist `karpathy/442a6bf555914893e9891c11519de94f`) to `docs/llm-wiki-pattern.md`.
- Decisions with Isaac: bilingual pages (English key terms, code and summaries; Spanish explanations); sources moved into `raw/` by type; standard markdown links (GitHub viewing, not Obsidian); first pass = slides + papers + code, books as chapter maps.
- Moved course files into `raw/{slides,papers,books,code/class,code/prolog_examples,assignments}`. Unzipped `01_Code (1).zip` into `raw/code/prolog_examples/` (dropped macOS metadata); removed `Espinosa_Isaac_lab01 (1).zip` (byte-identical to the `.pl`).
- Wrote schema `CLAUDE.md` (+ `AGENTS.md` pointer), `README.md`, `tools/extract_text.py`, `tools/lint_wiki.py`.

## [2026-10-01] ingest | Slides 01–04 and XX (5 lecture decks)

- Created sources: slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog.
- Created concepts: what-is-ai, history-of-ai, neural-networks, statistical-vs-causal-models, intelligent-agents, task-environments, agent-types, state-representation, problem-formulation, uninformed-search, heuristics, greedy-best-first-search, a-star-search, adversarial-search-minimax, alpha-beta-pruning, constraint-satisfaction-problems, n-queens, propositional-and-first-order-logic, horn-clauses-and-backward-chaining, unification, prolog, prolog-recursion-and-lists, optimization-basics, evolutionary-computation, genetic-algorithms, swarm-intelligence, particle-swarm-optimization, ant-colony-optimization, artificial-bee-colony.
- Flagged: Prolog attributed to Dennis Ritchie (slides 01 s9); GA dated 1992 (slides 04 s5). See study/errata.

## [2026-10-01] ingest | Papers: Kennedy & Eberhart 1995, Dorigo et al. 1996, Holland 1992

- Created sources: paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, paper-holland-1992-genetic-algorithms.
- Filled update equations missing from slides (images) in PSO, ACO pages; added schema theory to GA page.

## [2026-10-01] ingest | Code: class optimization scripts and Prolog examples

- Created sources: code-class-optimization, code-prolog-examples; concepts gradient-descent, simulated-annealing.
- Bugs recorded: gd_steroids surface (y+1 vs y+2); sa_functions cooling 0.8 too fast.

## [2026-10-01] ingest | Assignments (6) — code executed to record real results

- Created assignments: deber-1-search-problems, astar-vs-dijkstra, tic-tac-toe-4x4-minimax, prolog-lab-01-family, genetic-algorithm-task, pso-task.
- Ran: A\* (5 exp.) vs Dijkstra (9 exp.), cost 418; 8-puzzle BFS/DFS/greedy; farmer (7) and missionaries (11); Sudoku naive/MRV/FC on a sample board; GA (seed 0, optimum at epoch 20); PSO (seed 0, f = 10.0); Prolog lab in SWI-Prolog 9.0.4 (24/24 pass, 15 choicepoint warnings).
- Bugs recorded: tic-tac-toe win score ±1 < heuristic (2/54 positions miss an immediate win); lab spouse/2 asymmetry; DFS depth-limit + global visited.

## [2026-10-01] ingest | Books as chapter maps (not yet ingested in depth)

- Created sources: book-russell-norvig-aima, book-luger-ai, book-eiben-smith-evolutionary-computing, each mapping chapters to wiki pages.

## [2026-10-01] setup | Hub pages

- Created overview, glossary (≈75 terms), people, index; study pages search-algorithms-comparison, metaheuristics-comparison, exam-questions (34), errata.

## [2026-10-01] lint | First pass

- `python3 tools/lint_wiki.py`: 0 broken links, 0 orphans, all frontmatter present.
- Suggested next ingests: AIMA ch. 3–6 (deepen search pages), Eiben & Smith ch. 3–5 (selection methods), Karaboga 2007 ABC paper (not in raw/), the Deber 1 statement and Sudoku boards (missing from raw/).

## [2026-10-01] ingest | HW01 statement (Search Methods, Games and Heuristics)

- Merged Isaac's upload from `main`; moved `001-HW01 (1) (1).pdf` to `raw/assignments/`.
- Found the AI policy: generative AI only in chat mode with transcript; **AI agents forbidden (grade 0)**. Asked Isaac: HW01 is already graded → reviews kept as study material.
- Rewrote assignments/deber-1-search-problems (official statement, coverage table, Sudoku on official boards: board 2 naive 335,637 / MRV 4,036 / FC 309 assignments; 1 solution each; 9^51 and 9^59 brute-force counts; Chess vs. Go concept summary).
- Added `⚠️ Política de IA` row to every assignment page; added the AI-policy rule to CLAUDE.md §5.

## [2026-10-01] setup | Study plan for the test on Thu Oct 8

- Created study/study-plan.md (7 days, daily routine, priorities). Isaac's preferences recorded: exams answered in English with Spanish explanations; wants intuitive pseudocode, Anki flashcards, interactive quiz, visualizers, diagrams, practice problems, search tool, Marp decks, textbook chapters (AIMA 2–6, Eiben & Smith 3–5).

## [2026-10-01] ingest | AIMA 4e chapters 2–6

- Updated: intelligent-agents (4 factors of rationality, omniscience, information gathering), task-environments (known/unknown, Fig. 2.6), agent-types (learning agents), problem-formulation (BEST-FIRST-SEARCH, node structure, redundant paths, graph vs. tree-like), uninformed-search (UCS example, IDS numbers, bidirectional, Fig. 3.15), heuristics (b*, Fig. 3.26, dominance, relaxed problems, pattern DBs, landmarks), a-star-search (optimality proof, contours, weighted A*, IDA*, RBFS, SMA*), greedy-best-first-search, simulated-annealing (AIMA version, sign convention), genetic-algorithms (EA design, 8-queens GA, schema), gradient-descent (continuous local search, Newton–Raphson), optimization-basics, constraint-satisfaction-problems (rewritten: AC-3, k-consistency, MRV/degree/LCV, FC vs. MAC, backjumping, min-conflicts, tree CSPs), adversarial-search-minimax (game definition, Fig. 6.2, H-MINIMAX, evaluation, quiescence, horizon effect), alpha-beta-pruning (Fig. 6.5, move ordering, transposition tables).
- Created: local-search-hill-climbing, search-in-complex-environments, monte-carlo-tree-search (UCB1 example verified), stochastic-and-partially-observable-games.
- Refined: admissible vs. consistent heuristics for A* optimality (errata #4, slides-02 note). Added errata #8 (AIMA AlphaGo date, 181,400 typo).

## [2026-10-01] ingest | Eiben & Smith chapters 3–5

- Created: ea-representation-and-variation (ch. 4), ea-selection-and-population-management (ch. 5 + §3.1–3.2).
- Updated: genetic-algorithms (x² cycle by hand, EA behaviour, No Free Lunch, 8-queens EA), evolutionary-computation (components, natural vs. artificial evolution).
- Found an error in Eiben & Smith Table 3.3 (mutants decoded wrongly) → errata #9, verified against the PDF page.

## [2026-10-01] update | Intuitive pseudocode, diagrams, practice problems

- Added a "Pseudocódigo intuitivo" section (ES idea + EN steps + EN exam answer) to 32 concept pages; `tools/build_study.py` generates study/intuitive-pseudocode.md. Convention added to CLAUDE.md §3.
- Added 17 Mermaid diagrams (agent loop and architectures, graph search, BFS/DFS order, Romania A*, minimax and alpha–beta trees, MCTS cycle, Australia constraint graph, Criminal(West) proof tree, SLD flow, SA/GA/PSO/ACO/EA loops, course map); all validated with mermaid-cli.
- Created practice problem pages for units 1–4 with worked solutions; every numeric answer verified with Python and every Prolog answer with SWI-Prolog.

## [2026-10-01] update | Interactive quiz and Algorithm Lab visualizers
- Created `study-tools/web/visualizer.html` (Algorithm Lab): BFS/DFS/UCS/greedy/A\* on the Romania map with frontier table; minimax and alpha–beta on AIMA Fig. 6.2 and practice problems 5–6; PSO, binary GA, SA and GD on the course function, Rastrigin and Ackley. Verified in headless Chromium: A\* and UCS give 418 km, greedy and BFS 450 km; A\* expands 5 nodes; pruned leaves match practice solutions.
- Published: quiz https://claude.ai/artifact/9hSKYonRePXtWC6XArdtQU · visualizer https://claude.ai/artifact/UGK26c8fFaBuEY4ADznnvC.
- Created [study/interactive-tools.md](study/interactive-tools.md); linked it and the (previously orphaned) [quiz bank](study/quiz-bank.md) from `index.md`.
- Updated `study/study-plan.md` (daily quiz round, Lab exercises on Sat/Mon/Tue), `study/flashcards.md` (`quiz` tag; 239 cards), `CLAUDE.md` §7 and `README.md`.
