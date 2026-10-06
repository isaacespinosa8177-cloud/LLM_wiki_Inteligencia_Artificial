---
title: "Paper — Dorigo, Maniezzo & Colorni (1996), Ant System"
type: source
tags: [paper, swarm-intelligence, aco, combinatorial-optimization, tsp]
sources: [paper-dorigo-1996-ant-system]
updated: 2026-10-01
---
# Paper — Dorigo, Maniezzo & Colorni (1996), Ant System: Optimization by a Colony of Cooperating Agents

> **Summary (EN):** The founding Ant Colony Optimization paper (IEEE Trans. SMC-B 26(1):29–41). Artificial ants build Traveling Salesman tours step by step, choosing the next town with probability proportional to τ^α·η^β (pheromone trail × visibility 1/d). After each cycle, trails evaporate (factor ρ) and each ant deposits Q/L_k on the edges of its tour. The main ingredients are positive feedback, distributed computation and a constructive greedy heuristic. Ant-cycle beat ant-density and ant-quantity; best parameters α=1, β=5, ρ=0.5, m=n ants. AS was competitive with tabu search and simulated annealing and was applied to ATSP, QAP and job-shop scheduling.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/papers/3 - dorigo1996.pdf](../../raw/papers/3%20-%20dorigo1996.pdf) |
| Autores | Marco Dorigo, Vittorio Maniezzo, Alberto Colorni (Politecnico di Milano) |
| Publicación | IEEE Transactions on Systems, Man, and Cybernetics — Part B, vol. 26, no. 1, feb. 1996, pp. 29–41 |
| Extensión | 13 páginas |

## Resumen por secciones

- **§I Introducción.** Heurística general para optimización combinatoria: versátil (TSP → ATSP), robusta (QAP, JSP), poblacional (retroalimentación positiva, paralelizable). Hormigas reales casi ciegas encuentran el camino más corto gracias a la **feromona**: proceso autocatalítico (más hormigas → más feromona → más atractivo). Ejemplo del obstáculo: el camino corto acumula feromona más rápido. Las hormigas artificiales tienen memoria, no son totalmente ciegas y viven en tiempo discreto.
- **§II Ant System para TSP.**
  - Cada hormiga elige la siguiente ciudad con probabilidad función de la distancia y la feromona; una **tabu list** impide repetir ciudades hasta completar el tour.
  - Visibilidad: η_ij = 1/d_ij.
  - Probabilidad de transición: p_ij^k = [τ_ij]^α [η_ij]^β / Σ_{l ∈ allowed_k} [τ_il]^α [η_il]^β.
  - Actualización tras cada ciclo (n pasos): τ_ij(t+n) = ρ·τ_ij(t) + Δτ_ij, con Δτ_ij = Σ_k Δτ_ij^k y Δτ_ij^k = Q/L_k si la hormiga k usó la arista (i, j). (1 − ρ) es la **evaporación**.
- **§III Algoritmos.** *Ant-cycle* (deposita al final del tour, Q/L_k — información global), *ant-density* (deposita Q en cada paso) y *ant-quantity* (deposita Q/d_ij en cada paso) — estos dos usan información local. Complejidad de ant-cycle: O(NC·n²·m) = O(NC·n³) con m ≈ n. Con α = 0 se obtiene un greedy estocástico con múltiples inicios.
- **§IV Parámetros (Oliver30).** Valores probados α ∈ {0, 0.5, 1, 2, 5}, β ∈ {0, 1, 2, 5}, ρ ∈ {0.3 … 0.999}, Q ∈ {1, 100, 10000}. Mejor: **α = 1, β = 5, ρ = 0.5**; Q casi no influye. Ant-cycle encontró un tour de 423.741 (mejor que el 424.635 de los GA). α alto → **estancamiento** (todas las hormigas hacen el mismo tour); α bajo / β alto → greedy sin cooperación.
- **§V** Número de hormigas: relación lineal con número de ciudades (m = n); estrategia **elitista** (hormigas extra que refuerzan el mejor tour encontrado).
- **§VI** Comparado con tabu search y simulated annealing: competitivo en los problemas probados.
- **§VII** Generalización: ATSP, Quadratic Assignment Problem, Job-Shop Scheduling.
- **§VIII–IX** Características: revisión global de una estructura de datos compartida (feromona), comunicación distribuida, transiciones probabilísticas; sinergia entre hormigas.

## Ideas clave

1. **Estigmergia**: comunicación indirecta modificando el entorno (la feromona).
2. Retroalimentación positiva + evaporación = explotación con olvido controlado.
3. La heurística greedy (visibilidad) guía al inicio; la feromona domina después.

## Conceptos que alimenta

- [Ant Colony Optimization](../concepts/ant-colony-optimization.md)
- [Swarm Intelligence](../concepts/swarm-intelligence.md)
- [Simulated Annealing](../concepts/simulated-annealing.md) (comparación)
- [Optimization Basics](../concepts/optimization-basics.md)

## Notas y discrepancias

- Las slides llaman al método "Ant Colony Optimization (1996)"; el paper lo llama **Ant System** (AS). El nombre ACO como metaheurística general se formalizó después (Dorigo & Di Caro 1999 — conocimiento general).
- Las ecuaciones se reconstruyeron del texto extraído (las fórmulas del PDF salieron parcialmente ilegibles).
