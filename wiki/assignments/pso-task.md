---
title: "Particle Swarm Optimization — minimize (x+2)² + (y−2)² + 10"
type: assignment
tags: [assignment, optimization, pso, python]
sources: [slides-04-optimization, paper-kennedy-eberhart-1995-pso]
updated: 2026-10-01
---
# PSO task (Tarea: optimización por enjambre de partículas)

> **Summary (EN):** A vectorized NumPy implementation of PSO (`swalgorithm`) that follows the pseudocode from class step by step: initialize swarm S and personal bests P, update velocities with inertia w = 0.5 and coefficients a₁ = a₂ = 1, clip positions to [−10, 10], update P and the global-best index g. With 20 particles, 100 iterations and seed 0 it finds x ≈ (−2.00000001, 1.99999998), f = 10.0 — the same function and optimum as the GA task.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/assignments/swalgorithm (2).py](../../raw/assignments/swalgorithm%20%282%29.py) |
| Autor | Isaac Espinosa (00342611) |
| Lenguaje | Python 3 + NumPy (export de Colab) |
| Unidad | 4 — Optimización |

## Qué se implementó

```python
V = w*V + a1*phi_1*(P - S) + a2*phi_2*(P[g] - S)   # phi ~ U[0,1], shape (N, D)
S = np.clip(S + V, lower, upper)
improved = f_S < f_P
P[improved] = S[improved]; f_P[improved] = f_S[improved]
g = np.argmin(f_P)
```

Parámetros: N = 20, D = 2, límites (−10, 10), max_iter = 100, w = 0.5, a₁ = a₂ = 1.

## Resultados (`np.random.seed(0)`, 2026-10-01)

```
Best x: [-2.00000001  1.99999998]
f(x): 10.0
```

## Revisión

**Fortalezas**
- Vectorizado (sin bucles por partícula), compacto y fiel al pseudocódigo (comentarios "Set t ← 0", "Update S"…).
- Velocidad inicial cero y P = S, como en el algoritmo estándar.

**Puntos a mejorar**
1. Es la variante **con peso de inercia** (w), no la ecuación original de 1995 (sin w, coeficientes 2). Vale la pena decirlo en el informe ([paper](../sources/paper-kennedy-eberhart-1995-pso.md)).
2. Se recortan las posiciones pero no las velocidades; es común limitar |v| ≤ v_max para evitar explosiones en funciones con límites amplios.
3. El comentario `#genetic algorithm function` sobre `f` viene del GA; aquí es la función objetivo.
4. Buen experimento: comparar convergencia con w ∈ {0, 0.5, 0.9} — el paper muestra que sin momentum PSO pierde capacidad de encontrar el óptimo global.

## Conceptos relacionados

- [Particle Swarm Optimization](../concepts/particle-swarm-optimization.md)
- [Swarm Intelligence](../concepts/swarm-intelligence.md)
- [Optimization Basics](../concepts/optimization-basics.md)
- [GA task](genetic-algorithm-task.md) (misma función)
