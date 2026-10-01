---
title: Artificial Bee Colony
type: concept
tags: [optimization, swarm-intelligence, abc, continuous]
sources: [slides-04-optimization]
updated: 2026-10-01
---
# Artificial Bee Colony (Colonia artificial de abejas, ABC)

> **Summary (EN):** ABC (Karaboga, 2007) imitates honeybee foraging. Food sources are candidate solutions; employed bees exploit their own source by trying a nearby position, onlooker bees pick sources with probability proportional to quality and exploit them too, and scout bees abandon sources that have not improved for `limit` trials and search randomly — they provide exploration. Control parameters: number of food sources (= employed bees = onlooker bees), limit, and maximum cycle number (MCN).

## Términos clave

| English | Español | Significado |
|---|---|---|
| Food source | Fuente de comida | Una solución candidata; su "néctar" = aptitud. |
| Employed bee | Abeja empleada | Explota una fuente asignada. |
| Onlooker bee | Abeja observadora | Elige una fuente según la información compartida (danza). |
| Scout bee | Abeja exploradora | Busca fuentes nuevas al azar. |
| Limit | Límite | Intentos sin mejora antes de abandonar una fuente. |
| MCN | Número máximo de ciclos | Criterio de parada. |
| Recruitment rate | Tasa de reclutamiento | Qué tan rápido la colonia encuentra y explota una fuente nueva. |

## Explicación

**División del trabajo (slides 04, s17).** Como en una colmena real, el éxito depende de descubrir rápido y usar bien los mejores recursos:
- Empleadas + observadoras → **explotación**.
- Exploradoras → **exploración**.

**Ciclo del algoritmo** (ecuaciones reconstruidas de Karaboga 2007, conocimiento general; en las slides están como imagen):

```
initialize SN food sources x_i uniformly in the bounds; trials_i = 0
repeat MCN cycles:
    # employed bee phase
    for each source i:
        pick random k ≠ i and random dimension j
        v_ij = x_ij + φ_ij · (x_ij − x_kj),   φ_ij ~ U[−1, 1]
        if fitness(v) better than fitness(x_i): x_i = v; trials_i = 0  else trials_i += 1
    # onlooker bee phase
    p_i = fit_i / Σ fit          # fit_i = 1/(1+f_i) if f_i ≥ 0 else 1+|f_i|
    each onlooker chooses source i with probability p_i and does the same local move
    # scout bee phase
    if some trials_i > limit: replace x_i with a random point  (x_j = min_j + rand·(max_j − min_j))
    remember best solution
```

Slide 18: "k ∈ {1, 2, …, BN} y j ∈ {1, 2, …, D} son índices elegidos al azar" — corresponde a la ecuación de v_ij.

**Parámetros (s18).** Número de fuentes de comida (= número de empleadas BN = número de observadoras SN), `limit`, MCN.

## Errores comunes y tips de examen

- Solo **una** dimensión j cambia en cada movimiento de una abeja.
- La selección greedy (quedarse con el mejor entre x_i y v) se hace en las fases de empleadas y observadoras.
- Las exploradoras son el mecanismo anti-estancamiento (análogo a la mutación en GA o la evaporación en ACO).

## Relacionado

- [Swarm Intelligence](swarm-intelligence.md)
- [Particle Swarm Optimization](particle-swarm-optimization.md)
- [Optimization Basics](optimization-basics.md)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 16–19.
- Karaboga & Basturk (2007), *J. Global Optimization* 39:459–471 — **no está en raw/**; las fórmulas son conocimiento general. Buen candidato para añadir como fuente.
