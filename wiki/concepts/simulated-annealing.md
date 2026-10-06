---
title: Simulated Annealing
type: concept
tags: [optimization, local-search, stochastic]
sources: [code-class-optimization, paper-dorigo-1996-ant-system, book-russell-norvig-aima]
updated: 2026-10-01
---
# Simulated Annealing (Recocido simulado)

> **Summary (EN):** Simulated annealing is local search that sometimes accepts worse moves to escape local optima. A neighbor with cost change Δ is always accepted if Δ < 0 and otherwise with probability e^(−Δ/T). The temperature T starts high (lots of exploration, almost a random walk) and is lowered by a cooling schedule until the search becomes greedy hill climbing. The class script applies it to the Rastrigin function; Dorigo et al. use it as a baseline for Ant System.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Annealing | Recocido | Calentar un metal y enfriarlo lentamente para que alcance un estado de baja energía. |
| Temperature T | Temperatura | Controla cuánto empeoramiento se acepta. |
| Cooling schedule | Esquema de enfriamiento | Cómo baja T (p. ej. geométrico T ← αT). |
| Metropolis criterion | Criterio de Metropolis | Aceptar con probabilidad e^(−Δ/T). |
| Energy Δ | Diferencia de energía | f(nuevo) − f(actual) al minimizar. |

## Explicación

**Intuición.** Hill climbing se queda en el primer valle. SA permite "subir colinas" de vez en cuando: al principio (T alta) acepta casi cualquier movimiento; al final (T baja) casi solo mejoras. Si T baja lo suficientemente despacio, la probabilidad de terminar en el óptimo global tiende a 1 (complemento AIMA §4.1.2).

**Probabilidad de aceptación** (al minimizar):

| Δ | T alta (100) | T baja (0.1) |
|---|---|---|
| −1 (mejora) | 1 | 1 |
| +1 | e^(−0.01) ≈ 0.99 | e^(−10) ≈ 0.00005 |
| +10 | e^(−0.1) ≈ 0.90 | ≈ 0 |

**Código de clase (`sa_functions.py`, resumido):**

```python
def simulated_annealing(func, bounds, max_iter, initial_temp, cooling_rate):
    current = random point in bounds;  best = current;  T = initial_temp
    for i in range(max_iter):
        new = clip(current + uniform(-1, 1, size=dim), bounds)
        delta = func(new) - func(current)
        if delta < 0 or random() < exp(-delta / T):
            current = new
            if func(new) < func(best): best = new
        T *= cooling_rate
    return best
```

Aplicado a Rastrigin 2-D en [−5.12, 5.12]², T₀ = 100, α = 0.8, 100 000 iteraciones.

⚠️ **Enfriamiento demasiado rápido.** Con α = 0.8, T < 10⁻⁸ tras ~105 iteraciones: el 99.9 % de las iteraciones son hill climbing puro (y T llega a 0.0 tras ~3 400, causando divisiones por cero). Valores típicos de α: 0.95–0.9999, o ajustar α para que T llegue a ~10⁻³ al final: α = (T_final/T₀)^(1/max_iter).

### La versión de AIMA (§4.1.2)

AIMA la presenta como un punto medio entre hill climbing (nunca baja → se atasca) y la caminata aleatoria (encuentra el óptimo pero de forma ineficiente). **Analogía:** meter una pelota de ping-pong en la grieta más profunda de una superficie llena de baches: si solo la dejas rodar queda en un mínimo local; si **sacudes** la superficie, salta a otros. Hay que sacudir fuerte al inicio (T alta) y cada vez menos (T baja).

```
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
    current ← problem.INITIAL
    for t = 1 to ∞ do
        T ← schedule(t)
        if T = 0 then return current
        next ← a randomly selected successor of current
        ΔE ← VALUE(current) – VALUE(next)          # here VALUE is a COST (minimize)
        if ΔE > 0 then current ← next
        else current ← next only with probability e^(ΔE/T)
```

⚠️ **Convención de signos.** En esta figura AIMA 4e cambia al punto de vista de *gradient descent* (minimizar un costo): ΔE = VALUE(current) − VALUE(next) > 0 significa que `next` es **mejor** → se acepta siempre; si ΔE < 0 (empeora), se acepta con probabilidad e^(ΔE/T) < 1. El código de clase usa Δ = f(nuevo) − f(actual) = −ΔE y e^(−Δ/T): **es la misma regla** — siempre aceptar mejoras; aceptar empeoramientos con probabilidad e^(−|empeoramiento|/T).

Propiedad clave: si el esquema baja T **lo suficientemente lento**, por la distribución de Boltzmann toda la probabilidad se concentra en los óptimos globales, que se encuentran con probabilidad → 1. Usos: diseño de circuitos VLSI desde los 80, *scheduling* de fábricas.

### Diagrama

```mermaid
flowchart TD
    I[current = random, T = T0] --> N[next = random neighbor]
    N --> D{"Δ = f(next) − f(current) < 0 ?"}
    D -- yes --> A[accept next]
    D -- no --> P{"rand() < e^(−Δ/T) ?"}
    P -- yes --> A
    P -- no --> K[keep current]
    A --> C[T = α·T]
    K --> C
    C --> X{T ≈ 0 or budget over?}
    X -- no --> N
    X -- yes --> R[return best]
```

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** como hill climbing, pero a veces aceptas empeorar; al principio mucho (temperatura alta) y al final casi nunca.

```text
SIMULATED ANNEALING (minimizing f):
1. current ← random solution; best ← current; T ← T0 (high).
2. Repeat until T is (almost) 0 or the step budget ends:
   a. next ← a random neighbor of current.
   b. Δ = f(next) − f(current).
   c. If Δ < 0 (better) → accept next.
      Else accept next with probability e^(−Δ / T).
   d. If current is better than best → best ← current.
   e. Cool down: T ← α · T (e.g., α = 0.99).
3. Return best.
```

**Say it in the exam (EN):** "Simulated annealing escapes local optima by accepting worse moves with probability e^(−Δ/T). High temperature means exploration (almost a random walk); low temperature means exploitation (hill climbing). If T decreases slowly enough, it finds the global optimum with probability approaching 1."

## Errores comunes y tips de examen

- SA mantiene **una** solución (no es poblacional), pero es estocástico.
- Con T → ∞ es caminata aleatoria; con T = 0 es hill climbing.
- Guardar siempre la **mejor** solución vista: la actual puede empeorar.

## Relacionado

- [Local Search and Hill Climbing](local-search-hill-climbing.md)
- [Optimization Basics](optimization-basics.md)
- [Gradient Descent](gradient-descent.md)
- [Ant Colony Optimization](ant-colony-optimization.md) (comparado con SA en el paper)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Code — class optimization](../sources/code-class-optimization.md) (`sa_functions.py`).
- [Dorigo et al. 1996](../sources/paper-dorigo-1996-ant-system.md) §VI (comparación).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.1.2 (ingestado: pseudocódigo, analogía, convergencia).
