---
marp: true
theme: ia-review
paginate: true
footer: "Unit 4 · Optimization & Metaheuristics · IA review"
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Unit 4 — Optimization & Metaheuristics

**Review deck for the test on Thu Oct 8**

*English for the exam · "ES:" tips in Spanish*
*Wiki: Optimization Basics · Gradient Descent · Simulated Annealing · Evolutionary Computation · GA · EA Representation & Selection · Swarm Intelligence · PSO · ACO · ABC*

---

## Optimization basics

- Find the input that **minimizes / maximizes** an objective (fitness) function. Only the **final state** matters (no path).
- Goal: the **global** optimum, without getting stuck in **local** optima.
- Every metaheuristic balances **exploration** (try new regions) and **exploitation** (refine good ones).
- Course function: **f(x, y) = (x + 2)² + (y − 2)² + 10** → minimum **f = 10 at (−2, 2)** (convex, one minimum).
- Benchmarks with many local minima: **Rastrigin, Ackley, Schaffer f6**.

> ES: buscamos el valle más profundo de la función sin quedarnos en uno pequeño.

---

<!-- _class: small -->

## The six algorithms at a glance

| | GD | SA | GA | PSO | ACO | ABC |
|---|---|---|---|---|---|---|
| Who / year | Cauchy, 19th c. | Kirkpatrick et al. 1983 | Holland 1975 | Kennedy & Eberhart 1995 | Dorigo et al. 1996 | Karaboga 2007 |
| Inspiration | calculus | annealing metals | evolution | bird flocks | ant pheromone | foraging bees |
| Solutions | 1 | 1 | population | swarm | colony | hive |
| Needs gradient | **yes** | no | no | no | no | no |
| Key operator | w ← w − η∇f | accept e^(−Δ/T) | selection, crossover, mutation | v ← w·v + c₁r₁(p−x) + c₂r₂(g−x) | p ∝ τ^α η^β | v = x + φ(x − x_k) |
| Typical problems | continuous, differentiable | both | both | continuous | **combinatorial** (TSP) | continuous |
| Global optimum guaranteed | only if convex | asymptotically (slow cooling) | no | no | no | no |

> ES: solo GD necesita derivadas; ACO es para rutas (combinatorio).

---

## Gradient descent

`w ← w − η · ∇f(w)`

Practice 1: f = (x − 2)² + (y + 2)², start (0, 0), η = 0.1
- ∇f = (2(x−2), 2(y+2)) = (−4, 4) → w₁ = **(0.4, −0.4)**, f = 5.12
- w₂ = **(0.72, −0.72)**, f = 3.2768 · w₃ = **(0.976, −0.976)**, f ≈ 2.097
- Each step multiplies the distance by (1 − 2η) → converges for **0 < η < 1**; η = 0.5 in one step; η = 1 oscillates; η > 1 diverges.

> ES: η pequeño = lento; η grande = se pasa o diverge. En funciones multimodales solo llega a un mínimo **local**.

---

## Simulated annealing

- Pick a random neighbor; Δ = cost(new) − cost(current).
- Δ < 0 → **always accept**; otherwise accept with probability **e^(−Δ/T)**.
- Cool down: T ← α·T.

| Δ = 2 | T = 10 | T = 1 | T = 0.1 |
|---|---|---|---|
| P(accept) | 0.819 | 0.135 | ≈ 2 × 10⁻⁹ |

High T → random walk (exploration) · T → 0 → hill climbing (exploitation).

> ES: bug B2 del script de clase: α = 0.8 con 100 000 iteraciones → T ≈ 0 en ~100 iteraciones. Usar α ≈ 0.9999.

---
<!-- _class: small -->
## The evolutionary loop

```text
initialize population randomly
evaluate fitness of each individual
repeat until a stop condition:
    select parents            (fitter → more likely)
    recombine (crossover)     → offspring
    mutate offspring          (small random changes)
    evaluate offspring
    select survivors          → next generation
```

Dialects: **evolutionary programming** (L. Fogel, 1960s) · **evolution strategies** (Rechenberg & Schwefel, 1970s, real-valued) · **genetic algorithms** (Holland, 1975, bit strings).

> ES: elegir padres → mezclarlos → cambiar un poco a los hijos → quedarse con los mejores → repetir.

---

## GA: encoding and operators

- Assignment: 16 bits, sign-magnitude; `1000001000000010` → x = **−2**, y = **2**, f = **10** (optimal).
- One-point crossover at 3: `110|10110` × `001|11001` → **`11011001`**, **`00110110`**.
- Bit-flip mutation: expected flips = L·p_m (typical p_m ≈ 1/L).
- **Representation must match the operators:** permutations need swap / insert / scramble / inversion mutation and PMX / order / cycle / edge crossover — one-point crossover breaks permutations.
- Holland: **schemata** (e.g., `1**0*`) and **implicit parallelism** — short, fit building blocks multiply.

> ES: el cruce corta a dos padres en el mismo punto e intercambia los finales; la mutación cambia bits al azar.

---

## Selection

- **Fitness-proportional (roulette):** fitness [24, 23, 20, 11] → **0.31, 0.29, 0.26, 0.14**.
  Problems: premature convergence early, lost pressure late, changes if you add a constant to f.
- **Linear ranking:** P(i) = (2 − s)/μ + 2i(s − 1)/(μ(μ − 1)).
- **Tournament (size k):** pick k at random, keep the best — simple, no global fitness needed.
- **SUS:** one spin with λ equally spaced arms (less variance than roulette).
- **Survivors:** generational, steady-state, **elitism**, (μ+λ) parents + offspring, (μ,λ) offspring only.

> ES: ruleta = probabilidad según la nota; torneo = el mejor de k al azar; elitismo = el mejor siempre sigue.

---

## PSO — particle swarm optimization

```text
v ← w·v + c₁·r₁·(p_best − x) + c₂·r₂·(g_best − x)
x ← x + v
```

inertia (momentum) + **cognitive** (own memory) + **social** (swarm's best)

Practice 7: x = (1, 1), v = (0.5, −0.5), p = (0, 2), g = (−2, 2), w = 0.5, c₁ = c₂ = 1, r₁ = 0.5, r₂ = 0.2
→ **v = (−0.85, 0.45)**, **x = (0.15, 1.45)**, f: 20 → **14.925** (improved).

> ES: el paper de 1995 no tiene w (coef. 2); la tarea usa la versión con inercia → di cuál usas (errata #7).

---

## ACO — Ant System (Dorigo 1996)

- Probability of the next city: **p_ij ∝ τ_ij^α · η_ij^β**, η = 1/d; tabu list = visited cities.
- Update after all ants: **τ_ij ← ρ·τ_ij + Σ_k Q/L_k** (ρ = persistence, 1 − ρ = evaporation).
- Paper's best: **α = 1, β = 5, ρ = 0.5**, one ant per city.

Practice 8 (α = 1, β = 2): weights B 0.25, C 0.125, D 1 → **P = 0.18, 0.09, 0.73**.
τ_AB = 0.5·1 + 100/10 + 100/20 = **15.5**.

> ES: *stigmergy* = comunicación indirecta a través del entorno (la feromona).

---

## ABC and swarm intelligence

**Artificial bee colony (Karaboga 2007):**
- **Employed bees** exploit their food source (try a nearby position).
- **Onlookers** choose sources ∝ quality and exploit them.
- **Scouts** abandon a source after `limit` failed trials → random search (**exploration**).
- Parameters: number of sources (SN), limit, MCN.

**Swarm intelligence:** simple agents + local rules + information sharing → collective behavior. Millonas' 5 principles: proximity, quality, diverse response, stability, adaptability.

> ES: empleadas y observadoras mejoran las fuentes buenas; las exploradoras buscan fuentes nuevas al azar.

---

## Which algorithm? (practice 9)

| Problem | Choice | Why |
|---|---|---|
| Train neural-network weights | **Gradient descent / backprop** | differentiable, many dimensions |
| Shortest tour of 50 cities | **ACO** (or GA with permutations) | combinatorial graph problem |
| Minimize Rastrigin, no gradient | **PSO**, SA, real-valued EA | continuous, multimodal |
| Repair this week's timetable | **Min-conflicts** local search / CSP | few changes from a good start |

> ES: mutación, evaporación y abejas exploradoras cumplen el mismo papel: **mantener diversidad**.

---

<!-- _class: lead -->

## Self-check (answer aloud, in English)

1. Write the PSO update and name each term.
2. What does SA do when T is very high? When T → 0?
3. Why can't one-point crossover be used on permutations?
4. Why can roulette selection cause premature convergence?
5. Write the ACO transition rule; what do α and β control?
6. Which algorithms need a gradient?

*Answers: wiki `study/practice-unit-4-optimization.md` · Algorithm Lab (Optimization tab) · Exam Drill quiz*
