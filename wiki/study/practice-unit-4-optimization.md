---
title: Practice problems — Unit 4 (Optimization)
type: study
tags: [study, practice, optimization, metaheuristics]
sources: [slides-04-optimization, code-class-optimization, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, book-eiben-smith-evolutionary-computing, book-russell-norvig-aima]
updated: 2026-10-07
---
# Practice problems — Unit 4: Optimization (Problemas de práctica — Unidad 4)

> **Summary (EN):** Hand-calculation exercises on gradient descent, simulated annealing, hill climbing with restarts, genetic-algorithm operators and selection, PSO velocity updates, ACO transition probabilities and pheromone updates, and choosing the right metaheuristic. All numbers were verified with code. Questions in English, solutions in Spanish with the English answer.

## Problem 1 — Gradient descent

Minimize f(x, y) = (x − 2)² + (y + 2)² from (0, 0) with η = 0.1. Give the first three iterates and f values. For which η does it converge?

> *En español:* Minimiza f(x, y) = (x − 2)² + (y + 2)² desde (0, 0) con η = 0.1. Da los tres primeros puntos y sus valores de f. ¿Con qué valores de η converge?

<details><summary>Solución</summary>

∇f = (2(x−2), 2(y+2)). En (0,0): ∇f = (−4, 4) → w₁ = (0,0) − 0.1·(−4, 4) = **(0.4, −0.4)**, f = 5.12.
w₂ = **(0.72, −0.72)**, f = 3.2768. w₃ = **(0.976, −0.976)**, f ≈ 2.097. (f₀ = 8.)

Cada paso multiplica la distancia al mínimo por (1 − 2η) = 0.8 y f por 0.64. Converge si |1 − 2η| < 1 → **0 < η < 1**; η = 0.5 llega en un paso; η = 1 oscila; η > 1 diverge.
</details>

## Problem 2 — Simulated annealing

A move worsens the cost by Δ = 2. Probability of accepting it at T = 10, T = 1 and T = 0.1? What happens to the algorithm as T → 0?

> *En español:* Un movimiento empeora el costo en Δ = 2. ¿Con qué probabilidad se acepta con T = 10, T = 1 y T = 0.1? ¿Qué pasa con el algoritmo cuando T → 0?

<details><summary>Solución</summary>

e^(−2/10) ≈ **0.819**; e^(−2/1) ≈ **0.135**; e^(−2/0.1) ≈ **2 × 10⁻⁹**. Con T → 0 ya no acepta empeoramientos: se vuelve **hill climbing**. Con T muy alta acepta casi todo: **caminata aleatoria**.
</details>

## Problem 3 — Random-restart hill climbing

One hill-climbing run on 8-queens succeeds with probability p = 0.14. Expected number of runs? If a success takes 4 steps and a failure 3, expected total steps?

> *En español:* Un intento de hill climbing en 8 reinas sale bien con probabilidad p = 0.14. ¿Cuántos intentos se necesitan en promedio? Si un éxito tarda 4 pasos y un fracaso 3, ¿cuántos pasos en total en promedio?

<details><summary>Solución</summary>

Reinicios esperados = 1/p ≈ **7.1** (≈ 6 fallos + 1 éxito). Pasos ≈ 4 + (1 − p)/p · 3 = 4 + 6.14·3 ≈ **22** (AIMA §4.1.1).
</details>

## Problem 4 — GA: decoding and fitness

The GA assignment uses 16 bits: bits 0–7 → x, 8–15 → y, sign-magnitude (first bit = sign, 1 = negative). Decode `1000001000000010` and compute f = (x + 2)² + (y − 2)² + 10. Is it optimal?

> *En español:* La tarea GA usa 16 bits: los bits 0–7 son x y los 8–15 son y, en signo-magnitud (primer bit = signo, 1 = negativo). Decodifica `1000001000000010` y calcula f = (x + 2)² + (y − 2)² + 10. ¿Es el óptimo?

<details><summary>Solución</summary>

x: `1 0000010` → signo −, magnitud 2 → **x = −2**. y: `0 0000010` → **y = 2**. f = 0 + 0 + 10 = **10** = el mínimo global → óptimo.
</details>

## Problem 5 — GA operators

(a) One-point crossover of P1 = `11010110` and P2 = `00111001` at point 3. (b) With L = 16 and p_m = 0.1, how many bits flip per child on average? (c) Swap mutation of the permutation [1 2 3 4 5 6] at positions 2 and 5.

> *En español:* (a) Cruce de un punto de P1 = `11010110` y P2 = `00111001` en el punto 3. (b) Con L = 16 bits y p_m = 0.1, ¿cuántos bits cambian por hijo en promedio? (c) Mutación por intercambio de la permutación [1 2 3 4 5 6] en las posiciones 2 y 5.

<details><summary>Solución</summary>

(a) `110|10110` × `001|11001` → hijo 1 = **`11011001`**, hijo 2 = **`00110110`**.
(b) L·p_m = 16 · 0.1 = **1.6** bits por hijo (lo típico sería ≈ 1/L = 0.0625 → 1 bit).
(c) **[1 5 3 4 2 6]** (una permutación válida; el cruce de un punto **no** sirve para permutaciones).
</details>

## Problem 6 — Selection

(a) Roulette-wheel probabilities for fitness [24, 23, 20, 11] (AIMA's 8-queens GA). (b) Linear ranking with μ = 3, s = 2 for fitness A = 1, B = 5, C = 4. (c) Why can fitness-proportional selection cause premature convergence?

> *En español:* (a) Probabilidades de la ruleta para las notas [24, 23, 20, 11] (GA de 8 reinas de AIMA). (b) Ranking lineal con μ = 3 y s = 2 para las notas A = 1, B = 5, C = 4. (c) ¿Por qué la selección por ruleta puede hacer que la población converja demasiado pronto?

<details><summary>Solución</summary>

(a) Suma 78 → **0.31, 0.29, 0.26, 0.14**.
(b) Rangos A = 0, C = 1, B = 2; P(i) = (2 − s)/μ + 2i(s − 1)/(μ(μ − 1)) = i/3 → A **0**, C **0.33**, B **0.67**.
(c) Al inicio, un individuo mucho mejor que el resto recibe casi toda la probabilidad y sus copias llenan la población antes de que se explore lo suficiente (**convergencia prematura**). Más tarde, cuando todas las aptitudes se parecen, las probabilidades se igualan y la **presión de selección desaparece**. Además, sumar una constante a f cambia las probabilidades. Ranking y torneo evitan estos problemas.
</details>

## Problem 7 — PSO update

f(x, y) = (x + 2)² + (y − 2)² + 10. A particle at x = (1, 1) with v = (0.5, −0.5); p_best = (0, 2); g_best = (−2, 2); w = 0.5, c₁ = c₂ = 1, r₁ = 0.5, r₂ = 0.2. Compute the new velocity, position and f. Did it improve?

> *En español:* f(x, y) = (x + 2)² + (y − 2)² + 10. Una partícula está en x = (1, 1) con v = (0.5, −0.5); su mejor lugar p_best = (0, 2); el mejor del grupo g_best = (−2, 2); w = 0.5, c₁ = c₂ = 1, r₁ = 0.5, r₂ = 0.2. Calcula la nueva velocidad, la nueva posición y su f. ¿Mejoró?

<details><summary>Solución</summary>

- Inercia: 0.5·(0.5, −0.5) = (0.25, −0.25)
- Cognitivo: 1·0.5·((0, 2) − (1, 1)) = (−0.5, 0.5)
- Social: 1·0.2·((−2, 2) − (1, 1)) = (−0.6, 0.2)
- **v = (−0.85, 0.45)**, **x = (0.15, 1.45)**
- f(1, 1) = 9 + 1 + 10 = 20 → f(0.15, 1.45) = 4.6225 + 0.3025 + 10 = **14.925** → mejoró; p_best no cambia porque f(p_best) = 4 + 0 + 10 = 14 < 14.925.
</details>

## Problem 8 — ACO

An ant is in city A; unvisited cities B, C, D. Pheromone τ: AB = 1, AC = 2, AD = 1; distances: AB = 2, AC = 4, AD = 1. With α = 1, β = 2: (a) transition probabilities. (b) After a cycle, ρ = 0.5 (persistence), Q = 100, and two ants used edge AB in tours of length 10 and 20. New τ_AB?

> *En español:* Una hormiga está en la ciudad A; le faltan B, C y D. Feromona τ: AB = 1, AC = 2, AD = 1; distancias: AB = 2, AC = 4, AD = 1. Con α = 1 y β = 2: (a) probabilidades de ir a cada ciudad. (b) Después de un ciclo, con ρ = 0.5 (lo que se conserva), Q = 100, y dos hormigas que usaron el camino AB en recorridos de largo 10 y 20, ¿cuánto vale el nuevo τ_AB?

<details><summary>Solución</summary>

(a) Pesos τ^α·(1/d)^β: B = 1·(1/2)² = 0.25; C = 2·(1/4)² = 0.125; D = 1·1² = 1 → suma 1.375 → **P(B) = 0.18, P(C) = 0.09, P(D) = 0.73**. (D gana por estar muy cerca: β = 2 pesa la distancia.)
(b) τ_AB = ρ·τ + Σ Q/L_k = 0.5·1 + 100/10 + 100/20 = 0.5 + 10 + 5 = **15.5**.
</details>

## Problem 9 — Which algorithm?

Pick an algorithm and justify: (a) train the weights of a neural network with a differentiable loss, (b) shortest route visiting 50 cities, (c) minimize the Rastrigin function (many local minima, no gradient given), (d) a timetable with hard constraints that changed slightly this week.

> *En español:* Elige un algoritmo y justifica: (a) entrenar los pesos de una red neuronal con una función de error derivable, (b) la ruta más corta que visite 50 ciudades, (c) minimizar la función de Rastrigin (muchos mínimos locales, sin gradiente), (d) un horario con reglas obligatorias que cambió un poco esta semana.

<details><summary>Solución</summary>

(a) **Gradient descent / backprop** (diferenciable, muchas dimensiones). (b) **ACO** o GA con operadores de permutación (problema combinatorio en grafo; η = 1/d es una heurística natural). (c) **PSO**, SA o un EA real (continuo, multimodal, sin gradiente). (d) **Min-conflicts** / búsqueda local partiendo del horario anterior (reparar con pocos cambios), o un CSP con backtracking + forward checking.
</details>

## Relacionado

- [Metaheuristics comparison](metaheuristics-comparison.md) · [Exam questions](exam-questions.md)
- [GA](../concepts/genetic-algorithms.md) · [EA Selection](../concepts/ea-selection-and-population-management.md) · [PSO](../concepts/particle-swarm-optimization.md) · [ACO](../concepts/ant-colony-optimization.md) · [SA](../concepts/simulated-annealing.md) · [Gradient Descent](../concepts/gradient-descent.md)
