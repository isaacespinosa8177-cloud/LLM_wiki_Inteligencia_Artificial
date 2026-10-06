---
title: Quiz bank (multiple choice)
type: study
tags: [study, quiz, multiple-choice]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog, book-russell-norvig-aima, book-eiben-smith-evolutionary-computing, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, paper-holland-1992-genetic-algorithms]
updated: 2026-10-01
---
# Quiz bank (Banco de preguntas de opción múltiple)

> **Summary (EN):** Multiple-choice questions in English (exam language) with a one-line explanation each, grouped by unit. `tools/build_study.py` turns this page into the interactive quiz (`study-tools/web/quiz.html`) and Anki cards. To add a question, copy the format exactly: `### unitN | question`, then options with `- [ ]` / `- [x]` (exactly one correct), then a `>` explanation and an optional `see:` line with a wiki page.

## Unit 1 — Foundations and agents

### unit1 | What does the Turing Test try to provide?
- [ ] A proof that machines can think
- [x] An operational, behaviour-based definition of intelligence
- [ ] A benchmark for computer speed
- [ ] A test of whether a program is rational
> The interrogator only sees text answers; if they cannot tell the machine from the human, the machine counts as intelligent.
see: concepts/what-is-ai.md

### unit1 | What is the difference between the agent function and the agent program?
- [ ] They are synonyms
- [ ] The function runs on hardware; the program is a mathematical object
- [x] The function maps percept histories to actions abstractly; the program is the concrete implementation
- [ ] The program is a table; the function is learned
> AIMA: the agent function is the abstract specification; the agent program approximates it compactly on a real architecture.
see: concepts/intelligent-agents.md

### unit1 | A rational agent chooses the action that…
- [ ] always leads to the best actual outcome
- [x] maximizes the expected performance measure given its percepts and knowledge
- [ ] maximizes its own reward as defined by the agent itself
- [ ] imitates what a human would do
> Rationality is about expected value with the information available; it is not omniscience.
see: concepts/intelligent-agents.md

### unit1 | Who defines the performance measure?
- [x] The designer (or the user), outside the agent
- [ ] The agent, by learning it
- [ ] The environment
- [ ] The critic component
> "You get what you ask for": the measure is an external criterion set by the designer.
see: concepts/intelligent-agents.md

### unit1 | Chess played with a clock is…
- [ ] dynamic
- [ ] static
- [x] semidynamic
- [ ] stochastic
> The board does not change while you think, but your performance score (time) does.
see: concepts/task-environments.md

### unit1 | Which environment is episodic?
- [ ] Chess
- [ ] Taxi driving
- [x] Classifying defective parts on an assembly line, one image at a time
- [ ] Poker
> Each classification decision does not affect the next one.
see: concepts/task-environments.md

### unit1 | Which agent fails in a partially observable environment because it has no memory?
- [x] Simple reflex agent
- [ ] Model-based reflex agent
- [ ] Goal-based agent
- [ ] Utility-based agent
> It only uses the current percept; a model-based agent keeps an internal state.
see: concepts/agent-types.md

### unit1 | What does a utility-based agent add over a goal-based agent?
- [ ] Memory of the past
- [ ] The ability to plan
- [x] A numeric measure that ranks outcomes, handling trade-offs and uncertainty
- [ ] Sensors
> Goals are binary (achieved or not); utility distinguishes better from worse ways to reach them.
see: concepts/agent-types.md

### unit1 | In a learning agent, which component suggests exploratory actions?
- [ ] Critic
- [ ] Learning element
- [ ] Performance element
- [x] Problem generator
> The problem generator proposes new, informative experiences, even if they look suboptimal now.
see: concepts/agent-types.md

### unit1 | The 8-puzzle stored as a tuple (2,4,3,1,0,6,7,5,8) is a … representation.
- [ ] atomic
- [x] factored
- [ ] structured
- [ ] relational
> It is a vector of variable values, which lets heuristics like Manhattan distance look inside the state.
see: concepts/state-representation.md

### unit1 | Who created Prolog?
- [ ] Dennis Ritchie at Bell Labs
- [ ] John McCarthy at MIT
- [x] Alain Colmerauer and Philippe Roussel in Marseille, building on Kowalski's theory
- [ ] Alan Turing
> Slide 9 of the intro deck wrongly credits Ritchie (who created C). Prolog: Marseille, 1972.
see: study/errata.md

### unit1 | In which year was the Dartmouth workshop that named the field of AI?
- [ ] 1950
- [x] 1956
- [ ] 1958
- [ ] 1972
> McCarthy, Minsky, Rochester and Shannon organized it in 1956.
see: concepts/history-of-ai.md

### unit1 | Why can a single perceptron not learn XOR?
- [ ] It has too few weights
- [x] XOR is not linearly separable
- [ ] It has no bias term
- [ ] Backpropagation does not converge for XOR
> A perceptron draws one straight line; XOR needs a hidden layer.
see: concepts/neural-networks.md

## Unit 2 — Search, games and CSP

### unit2 | Which frontier gives breadth-first search?
- [ ] LIFO stack
- [x] FIFO queue
- [ ] Priority queue ordered by h
- [ ] Priority queue ordered by g + h
> BFS expands the shallowest node first: new nodes go to the back of a FIFO queue.
see: concepts/uninformed-search.md

### unit2 | What is the main practical problem of BFS?
- [ ] It is not complete
- [ ] It is not optimal with equal costs
- [x] It needs O(b^d) memory
- [ ] It loops forever on cycles
> At b = 10, d = 10 it needs about 10 terabytes; memory hurts more than time.
see: concepts/uninformed-search.md

### unit2 | Space complexity of depth-first (tree-like) search?
- [ ] O(b^d)
- [x] O(b·m)
- [ ] O(b^m)
- [ ] O(d)
> It only stores the current path and the siblings of its nodes.
see: concepts/uninformed-search.md

### unit2 | Why does uniform-cost search test for the goal when it EXPANDS a node, not when it generates it?
- [ ] It is faster
- [x] A cheaper path to the goal might still be found after the goal is first generated
- [ ] Because the frontier is a stack
- [ ] To save memory
> Sibiu→Bucharest: the goal appears with cost 310 via Fagaras, but the 278 path via Pitesti is found later.
see: concepts/uninformed-search.md

### unit2 | Iterative deepening with b = 10, d = 5 generates about how many more nodes than BFS?
- [x] About 11% more
- [ ] Twice as many
- [ ] Ten times as many
- [ ] The same number
> 123,450 vs. 111,110: most nodes are on the last level, which is generated only once.
see: concepts/uninformed-search.md

### unit2 | A heuristic is admissible if…
- [ ] h(n) ≤ c(n, a, n') + h(n') for every edge
- [x] it never overestimates the true cost to the goal
- [ ] it is always zero
- [ ] it is larger than every other heuristic
> Admissible = optimistic. The edge inequality is consistency, which implies admissibility.
see: concepts/heuristics.md

### unit2 | Greedy best-first search from Arad to Bucharest returns the path through…
- [ ] Rimnicu Vilcea and Pitesti, 418 km
- [x] Sibiu and Fagaras, 450 km
- [ ] Timisoara and Lugoj
- [ ] Zerind and Oradea
> It follows the smallest h at each step and ignores the cost already paid, so it misses the optimal 418 km route.
see: concepts/greedy-best-first-search.md

### unit2 | A* expands the node with the smallest…
- [ ] h(n)
- [ ] g(n)
- [x] g(n) + h(n)
- [ ] depth
> f(n) = g(n) + h(n) estimates the cost of the cheapest solution through n.
see: concepts/a-star-search.md

### unit2 | With h(n) = 0 for every node, A* behaves like…
- [ ] greedy best-first search
- [x] uniform-cost search (Dijkstra)
- [ ] depth-first search
- [ ] hill climbing
> f = g, so it expands by path cost only.
see: concepts/a-star-search.md

### unit2 | For the 8-puzzle, why prefer Manhattan distance over misplaced tiles?
- [ ] Manhattan is not admissible
- [x] Both are admissible and Manhattan dominates (is always ≥), so A* expands fewer nodes
- [ ] Misplaced tiles is not admissible
- [ ] Manhattan is cheaper to compute
> AIMA Fig. 3.26: at depth 20, A*(h1) generates 9,905 nodes, A*(h2) only 1,318.
see: concepts/heuristics.md

### unit2 | Minimax time and space complexity are…
- [ ] O(b^d) and O(b^d)
- [x] O(b^m) and O(b·m)
- [ ] O(b^(m/2)) and O(m)
- [ ] O(m) and O(b)
> It is a depth-first exploration of the whole game tree.
see: concepts/adversarial-search-minimax.md

### unit2 | With perfect move ordering, alpha–beta examines…
- [ ] O(b^m) nodes, like minimax
- [x] O(b^(m/2)) nodes
- [ ] O(b·m) nodes
- [ ] O(log b^m) nodes
> The effective branching factor becomes √b, so it can search about twice as deep.
see: concepts/alpha-beta-pruning.md

### unit2 | MAX's three MIN children have leaves [4, 8, 9], [3, 7, 1], [6, 2, 5]. How many leaves does alpha–beta prune?
- [ ] 0
- [ ] 2
- [x] 3
- [ ] 5
> After the first child α = 4: in the second child 3 < 4 prunes 7 and 1; in the third, 2 < 4 prunes 5.
see: study/practice-unit-2-search.md

### unit2 | Why does Go use Monte Carlo tree search instead of heuristic alpha–beta?
- [ ] Go has hidden information
- [ ] Go is stochastic
- [x] Its branching factor is huge (361 at the start) and good evaluation functions are hard to write
- [ ] Alpha–beta cannot handle two players
> MCTS evaluates positions by averaging playouts and needs only the rules.
see: concepts/monte-carlo-tree-search.md

### unit2 | In expectiminimax, a chance node returns…
- [ ] the maximum of its children
- [ ] the minimum of its children
- [x] the probability-weighted average of its children
- [ ] a random child's value
> Σ P(r)·value(r).
see: concepts/stochastic-and-partially-observable-games.md

### unit2 | The MRV heuristic chooses…
- [ ] the value that rules out the fewest options
- [x] the variable with the fewest legal values left
- [ ] the variable with the most constraints
- [ ] a random variable
> Minimum remaining values = fail-first. Value ordering is LCV; degree is the tie-breaker.
see: concepts/constraint-satisfaction-problems.md

### unit2 | Forward checking, after assigning X, …
- [ ] runs AC-3 on the whole CSP
- [x] removes from each unassigned neighbor of X the values inconsistent with X
- [ ] assigns all neighbors of X
- [ ] jumps back to the most recent conflicting variable
> It enforces arc consistency only for X and does not propagate further (MAC does).
see: concepts/constraint-satisfaction-problems.md

### unit2 | A tree-structured CSP with n variables and domain size d can be solved in…
- [ ] O(d^n)
- [ ] O(n!)
- [x] O(n·d²)
- [ ] O(n²·d)
> Directional arc consistency from the leaves, then assign from the root without backtracking.
see: concepts/constraint-satisfaction-problems.md

### unit2 | On the hard HW01 Sudoku, naive backtracking made 335,637 assignments. Forward checking + MRV made…
- [ ] 4,036
- [x] 309
- [ ] 51
- [ ] 335,000
> MRV alone made 4,036; adding forward checking detects empty domains before recursing.
see: assignments/deber-1-search-problems.md

## Unit 3 — Logic and Prolog

### unit3 | A Horn clause has…
- [ ] exactly one negative literal
- [x] at most one positive literal
- [ ] no positive literals
- [ ] exactly two literals
> Definite clause = exactly one positive (a rule); goal clause = none (a query).
see: concepts/horn-clauses-and-backward-chaining.md

### unit3 | Which clause is NOT a Horn clause?
- [ ] ¬A ∨ ¬B ∨ C
- [ ] C
- [ ] ¬A ∨ ¬B
- [x] A ∨ B
> Two positive literals; Prolog cannot say "one of these, I don't know which".
see: concepts/horn-clauses-and-backward-chaining.md

### unit3 | The CNF of (A ⇒ B) ⇒ C is…
- [ ] (¬A ∨ B) ∧ C
- [x] (A ∨ C) ∧ (¬B ∨ C)
- [ ] ¬A ∨ B ∨ C
- [ ] (A ∧ ¬B) ∧ C
> ¬(¬A ∨ B) ∨ C = (A ∧ ¬B) ∨ C, then distribute.
see: study/practice-unit-3-logic.md

### unit3 | First-order logic is…
- [ ] decidable
- [x] semi-decidable
- [ ] only able to talk about true/false symbols
- [ ] the same as propositional logic
> If KB ⊨ α a complete procedure finds the proof; if not, it may never stop.
see: concepts/propositional-and-first-order-logic.md

### unit3 | In Prolog, `parent(Hector, ana)` means…
- [ ] Hector (the constant) is a parent of ana
- [x] some X is a parent of ana (Hector is a variable)
- [ ] a syntax error
- [ ] ana is a parent of Hector
> Uppercase = variable, the opposite of the textbook's convention.
see: concepts/prolog.md

### unit3 | Result of `?- f(X, g(X)) = f(Y, g(a)).`
- [ ] false
- [ ] X = Y
- [x] X = a, Y = a
- [ ] X = g(a)
> X unifies with Y, then g(X) with g(a) forces X = a.
see: concepts/unification.md

### unit3 | `?- X = 2 + 3.` gives…
- [x] X = 2+3
- [ ] X = 5
- [ ] false
- [ ] an instantiation error
> `=` unifies terms and evaluates nothing; `is` evaluates.
see: concepts/unification.md

### unit3 | `?- X is Y + 1.` with Y unbound gives…
- [ ] X = Y+1
- [ ] false
- [x] an "arguments are not sufficiently instantiated" error
- [ ] X = 1
> `is/2` needs its right-hand side fully bound.
see: concepts/prolog.md

### unit3 | How does Prolog choose which goal and clause to try?
- [ ] Rightmost goal, last clause first
- [x] Leftmost goal, clauses top to bottom, depth-first with backtracking
- [ ] Breadth-first over all clauses
- [ ] Random choice
> SLD resolution with Prolog's search rule: depth-first, left to right.
see: concepts/prolog.md

### unit3 | Why can `path(X,Z) :- path(X,Y), link(Y,Z).` (written first) loop forever?
- [ ] link/2 is missing
- [x] It is left-recursive: path calls path before consuming anything
- [ ] Prolog has no recursion
- [ ] Because of the cut
> Put the base case first and recurse on the right, or use `:- table path/2.`
see: concepts/prolog.md

### unit3 | `\+ parent(X, ana)` with X unbound returns false because…
- [ ] nobody is ana's parent
- [x] some X is ana's parent, so the goal succeeds and its negation fails
- [ ] negation is not allowed in Prolog
- [ ] X must be uppercase
> Negation as failure only behaves like logical negation on ground (bound) goals.
see: concepts/prolog.md

### unit3 | Why is the naive fibo/2 slow?
- [ ] Prolog integers are slow
- [x] Each call makes two recursive calls and recomputes the same subproblems (exponential)
- [ ] It uses is/2
- [ ] It is tail-recursive
> An accumulator version is linear; tabling also fixes it.
see: concepts/prolog-recursion-and-lists.md

### unit3 | `isPerm([1,1,2],[1,2,2])` returns true because isPerm checks…
- [ ] length only
- [x] set equality (each element appears in the other list), not permutation
- [ ] sorted order
- [ ] nothing — it is correct
> Fix: `msort(X, S), msort(Y, S)`.
see: concepts/prolog-recursion-and-lists.md

### unit3 | `findall(D, ancestor(hector, D), L)` with the lecture's family.pl gives…
- [ ] [sofia, diego, ana, luis]
- [x] [ana, luis, sofia, diego]
- [ ] [ana, sofia, luis, diego]
- [ ] []
> The first ancestor clause (direct parent) gives the children first; the recursive clause adds the grandchildren.
see: study/practice-unit-3-logic.md

## Unit 4 — Optimization

### unit4 | Hill climbing gets stuck because of…
- [ ] its memory use
- [x] local maxima, ridges and plateaus
- [ ] its random moves
- [ ] its population size
> It never accepts a worse move; on random 8-queens it solves only 14% of instances.
see: concepts/local-search-hill-climbing.md

### unit4 | Simulated annealing accepts a worse move with probability…
- [ ] Δ / T
- [x] e^(−Δ/T)
- [ ] 1 − T
- [ ] always 0.5
> At high T almost everything is accepted; as T → 0 it becomes hill climbing.
see: concepts/simulated-annealing.md

### unit4 | Gradient descent on f = (x−2)² + (y+2)² from (0,0) with η = 0.1: the first step lands on…
- [ ] (0.2, −0.2)
- [x] (0.4, −0.4)
- [ ] (4, −4)
- [ ] (2, −2)
> ∇f(0,0) = (−4, 4); w ← w − 0.1·(−4, 4).
see: study/practice-unit-4-optimization.md

### unit4 | In a GA, which operator is mainly responsible for combining good building blocks?
- [ ] Mutation
- [x] Crossover
- [ ] Selection
- [ ] Elitism
> Holland: crossover recombines schemata; mutation is an insurance that keeps diversity.
see: concepts/genetic-algorithms.md

### unit4 | One-point crossover of 110|10110 and 001|11001 gives…
- [x] 11011001 and 00110110
- [ ] 11010110 and 00111001
- [ ] 00110110 and 11010110
- [ ] 11111111 and 00000000
> Swap the tails after position 3.
see: study/practice-unit-4-optimization.md

### unit4 | With 16 bits and a per-bit mutation rate of 0.1, how many bits flip per child on average?
- [ ] 0.1
- [ ] 1
- [x] 1.6
- [ ] 16
> L·p_m = 16 × 0.1. The usual choice is about 1/L.
see: concepts/ea-representation-and-variation.md

### unit4 | Which selection method is invariant to adding a constant to the fitness?
- [ ] Fitness-proportional (roulette)
- [x] Tournament selection
- [ ] Both
- [ ] Neither
> Tournaments only compare individuals; roulette probabilities change when f is shifted.
see: concepts/ea-selection-and-population-management.md

### unit4 | What does elitism guarantee?
- [ ] Faster mutation
- [x] The best fitness in the population never decreases
- [ ] More diversity
- [ ] That the global optimum is found
> The current best individual is always copied into the next generation.
see: concepts/ea-selection-and-population-management.md

### unit4 | Which operator keeps a permutation valid?
- [ ] One-point crossover
- [ ] Bit-flip mutation
- [x] Order crossover (OX)
- [ ] Arithmetic crossover
> Plain one-point crossover can duplicate values; OX, PMX, cycle and edge crossover are designed for permutations.
see: concepts/ea-representation-and-variation.md

### unit4 | In PSO, the term c₂·r₂·(g_best − x) is called…
- [ ] inertia
- [ ] the cognitive component
- [x] the social component
- [ ] mutation
> It pulls the particle toward the best position found by the whole swarm.
see: concepts/particle-swarm-optimization.md

### unit4 | What did Kennedy & Eberhart find when they removed the previous velocity (momentum) from the update?
- [ ] It converged faster
- [x] It became quite ineffective at finding global optima
- [ ] Nothing changed
- [ ] It became a genetic algorithm
> Momentum makes particles overshoot, which is how the swarm explores.
see: concepts/particle-swarm-optimization.md

### unit4 | In Ant System, an ant at city i moves to j with probability proportional to…
- [ ] d_ij
- [ ] τ_ij only
- [x] τ_ij^α · (1/d_ij)^β
- [ ] 1/L_k
> Pheromone (learned) times visibility (greedy heuristic), over the allowed cities.
see: concepts/ant-colony-optimization.md

### unit4 | Why does ACO evaporate pheromone?
- [ ] To save memory
- [x] To forget bad choices and avoid stagnation (unlimited accumulation)
- [ ] To speed up each ant
- [ ] Because ants die
> Positive feedback alone would make all ants follow the same early tour.
see: concepts/ant-colony-optimization.md

### unit4 | In Artificial Bee Colony, which bees provide exploration?
- [ ] Employed bees
- [ ] Onlooker bees
- [x] Scout bees
- [ ] Queen bees
> Scouts replace sources that have not improved for `limit` trials with random new ones.
see: concepts/artificial-bee-colony.md

### unit4 | Best choice for the shortest tour through 50 cities?
- [ ] Gradient descent
- [x] Ant colony optimization (or a GA with permutation operators)
- [ ] Perceptron training
- [ ] Minimax
> It is a combinatorial problem on a graph; 1/d is a natural heuristic.
see: study/metaheuristics-comparison.md

## Relacionado

- [Exam questions](exam-questions.md) · [Practice problems](practice-unit-2-search.md) · [Flashcards](flashcards.md)
