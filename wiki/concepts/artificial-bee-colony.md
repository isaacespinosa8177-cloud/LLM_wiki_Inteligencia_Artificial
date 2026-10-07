---
title: Artificial Bee Colony
type: concept
tags: [optimization, swarm-intelligence, abc, continuous]
sources: [slides-04-optimization]
updated: 2026-10-07
---
# Artificial Bee Colony (Colonia artificial de abejas, ABC)

> **Summary (EN):** ABC (Karaboga, 2007) imitates honeybee foraging. Food sources are candidate solutions; employed bees exploit their own source by trying a nearby position, onlooker bees pick sources with probability proportional to quality and exploit them too, and scout bees abandon sources that have not improved for `limit` trials and search randomly — they provide exploration. Control parameters: number of food sources (= employed bees = onlooker bees), limit, and maximum cycle number (MCN).

> **En palabras simples (ES):** Imita a las abejas buscando flores. Cada **fuente de comida** es una solución. Las abejas **empleadas** trabajan cada una su fuente probando un lugar cercano. Las **observadoras** van más seguido a las fuentes buenas. Si una fuente no mejora después de varios intentos, se abandona y una abeja **exploradora** busca una fuente nueva al azar. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

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

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Imita a las abejas buscando flores. Cada **fuente de comida** es una solución. Las abejas **empleadas** trabajan cada una su fuente probando un lugar cercano. Las **observadoras** van más seguido a las fuentes buenas. Si una fuente no mejora después de varios intentos, se abandona y una abeja **exploradora** busca una fuente nueva al azar.

**Antes de empezar: qué significa cada cosa**

| Símbolo / palabra | Qué es (en simple) | English |
|---|---|---|
| Fuente de comida x | una solución candidata | food source |
| Calidad | qué tan buena es la solución (su nota) | fitness / nectar amount |
| SN | cuántas fuentes hay (= número de empleadas = número de observadoras) | number of food sources |
| x_k | otra fuente elegida al azar, para compararse | random partner source |
| φ (phi) | un número al azar entre −1 y 1 | random factor |
| v = x + φ(x − x_k) | la posición vecina que se prueba: moverse un poco acercándose o alejándose de otra fuente | neighbor solution |
| trials | cuántas veces seguidas no mejoró una fuente | failure counter |
| limit | cuántos fracasos se aceptan antes de abandonar la fuente | abandonment limit |
| MCN | número máximo de ciclos | maximum cycle number |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Create SN random food sources (solutions); set every trial counter to 0.
   - *ES:* Crea fuentes al azar; ninguna ha fallado todavía.
2. Employed bees: for each source x, try a neighbor v = x + φ·(x − x_k) on one variable. If v is better, keep it; otherwise add 1 to its trial counter.
   - *ES:* Cada empleada prueba un lugar cerca de su fuente (moviéndose un poco respecto a otra fuente al azar). Si es mejor, se queda ahí; si no, cuenta un fracaso.
3. Onlooker bees: choose sources with probability proportional to their quality and do the same neighbor test on them.
   - *ES:* Las observadoras eligen fuentes, prefiriendo las buenas, y también prueban vecinos. Así las fuentes buenas se mejoran más.
4. Scout bees: any source with more failures than the limit is abandoned and replaced by a new random source.
   - *ES:* Si una fuente falló demasiadas veces seguidas, se abandona y una exploradora busca una nueva al azar (esto es la exploración).
5. Remember the best source. Repeat steps 2–5 for MCN cycles and return it.
   - *ES:* Guarda la mejor fuente y repite muchos ciclos.

**Ejemplo con números:** fuente x = 2, fuente compañera al azar x_k = 5, número al azar φ = −0.5. Vecino: v = 2 + (−0.5)·(2 − 5) = 2 + 1.5 = **3.5**. Si f(3.5) es mejor que f(2), la abeja se mueve a 3.5 y su contador vuelve a 0; si no, su contador sube a 1. Con limit = 10, después de 10 fracasos seguidos la fuente se abandona.

**Say it in the exam (EN):** "Artificial Bee Colony imitates honeybee foraging. Each food source is a candidate solution. Employed bees try a nearby position for their source; onlooker bees choose good sources more often and improve them too; both exploit. Scout bees replace sources that have not improved after a set number of trials (the limit) with random new ones, which provides exploration. The parameters are the number of food sources, the limit and the maximum number of cycles."

**Dilo así (ES):** "ABC imita a las abejas buscando comida. Cada fuente es una solución. Las empleadas prueban un lugar cercano a su fuente y las observadoras eligen más seguido las fuentes buenas; ambas explotan. Las exploradoras reemplazan las fuentes que no mejoraron después de 'limit' intentos por otras al azar; eso es la exploración. Los parámetros son el número de fuentes, el límite y el máximo de ciclos."

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
