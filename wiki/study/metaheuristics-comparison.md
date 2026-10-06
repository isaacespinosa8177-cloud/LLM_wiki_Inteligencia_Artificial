---
title: Metaheuristics comparison
type: study
tags: [study, optimization, comparison, cheat-sheet]
sources: [slides-04-optimization, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system, code-class-optimization]
updated: 2026-10-01
---
# Metaheuristics comparison (Comparación de metaheurísticas)

> **Summary (EN):** Side-by-side cheat sheet for Unit 4: gradient descent, simulated annealing, genetic algorithms, PSO, ACO and ABC — inspiration, representation, key operators and parameters, how each explores and exploits, and the problems each suits.

## Tabla maestra

| | [Gradient Descent](../concepts/gradient-descent.md) | [Simulated Annealing](../concepts/simulated-annealing.md) | [GA](../concepts/genetic-algorithms.md) | [PSO](../concepts/particle-swarm-optimization.md) | [ACO](../concepts/ant-colony-optimization.md) | [ABC](../concepts/artificial-bee-colony.md) |
|---|---|---|---|---|---|---|
| Autor / año | (Cauchy, s. XIX) | Kirkpatrick et al., 1983 | Holland, 1975 | Kennedy & Eberhart, 1995 | Dorigo et al., 1996 | Karaboga, 2007 |
| Inspiración | Cálculo | Recocido de metales | Evolución natural | Bandadas, cardúmenes | Hormigas y feromona | Abejas recolectoras |
| Nº de soluciones | 1 | 1 | Población | Enjambre | Colonia | Colmena |
| Representación | Vector real | Cualquiera con vecindad | Bits (o reales) | Vector real + velocidad | Tour / camino en grafo | Vector real |
| Necesita gradiente | **Sí** | No | No | No | No | No |
| Operador clave | w ← w − η∇f | Aceptar con e^(−Δ/T) | Selección, cruce, mutación | v ← w·v + c₁φ₁(p−x) + c₂φ₂(g−x) | p ∝ τ^α η^β; evaporación + depósito | v = x + φ(x − x_k) |
| Parámetros | η | T₀, enfriamiento | Tamaño, p_c, p_m, selección | N, w, c₁, c₂ | m, α, β, ρ, Q | SN, limit, MCN |
| Exploración | Ninguna | T alta | Mutación, cruce | Inercia, aleatorios | Probabilidades, evaporación | Exploradoras |
| Explotación | Seguir −∇f | T baja | Selección, elitismo | p_best, g_best | Refuerzo de feromona | Empleadas, observadoras |
| Problemas típicos | Continuos, diferenciables (redes neuronales) | Combinatorios y continuos | Combinatorios y continuos | Continuos | **Combinatorios** (TSP, rutas, scheduling) | Continuos |
| Garantía de óptimo global | Solo si convexa | Asintótica (enfriamiento lento) | No | No | No | No |

## Lo que cada paper/código demuestra

- **Holland 1992:** el cruce + selección asigna muestras a regiones según su aptitud (paralelismo implícito).
- **Kennedy & Eberhart 1995:** sin momentum PSO falla; p y g balanceados funcionan mejor.
- **Dorigo et al. 1996:** α = 1, β = 5, ρ = 0.5; α alto → estancamiento; información global (Q/L_k) > local.
- **sa_functions.py:** el esquema de enfriamiento importa (0.8 es demasiado rápido para 100 000 iteraciones).
- **Tareas GA y PSO:** ambas encuentran (−2, 2), f = 10; la función es convexa, así que no diferencia a los métodos.

## Preguntas de comparación típicas

1. ¿Por qué PSO no necesita selección? → Las partículas no mueren: se mueven; la "selección" está implícita en p_best/g_best.
2. ¿Cuál usarías para el TSP y por qué? → ACO (o GA con permutaciones): problema combinatorio en un grafo; η = 1/d da una heurística natural.
3. ¿Qué tienen en común la mutación, la evaporación y las abejas exploradoras? → Mantienen la **diversidad** / exploración y evitan la convergencia prematura.

## Relacionado

- [Optimization Basics](../concepts/optimization-basics.md)
- [Swarm Intelligence](../concepts/swarm-intelligence.md)
- [Evolutionary Computation](../concepts/evolutionary-computation.md)
- [Exam questions](exam-questions.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md); [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md); [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md); [Dorigo et al. 1996](../sources/paper-dorigo-1996-ant-system.md); [Code — class optimization](../sources/code-class-optimization.md).
- Autores/años de GD y SA: conocimiento general.
