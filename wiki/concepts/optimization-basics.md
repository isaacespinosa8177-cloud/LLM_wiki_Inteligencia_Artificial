---
title: Optimization Basics
type: concept
tags: [optimization, local-search, metaheuristics]
sources: [slides-04-optimization, code-class-optimization, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, book-eiben-smith-evolutionary-computing, book-russell-norvig-aima]
updated: 2026-10-01
---
# Optimization Basics (Fundamentos de optimización)

> **Summary (EN):** Optimization looks for the input that maximizes or minimizes an objective (fitness) function, aiming for the global optimum without getting stuck in local optima. Unlike path search, only the final state matters. The course covers a gradient-based method (gradient descent), a single-solution stochastic method (simulated annealing) and population-based metaheuristics (GA, PSO, ACO, ABC). All of them balance exploration (trying new regions) against exploitation (refining good ones). Benchmark functions such as Rastrigin, Ackley and Schaffer f6 test that balance.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Objective / fitness function | Función objetivo / de aptitud | Lo que se quiere minimizar o maximizar. |
| Search space | Espacio de búsqueda | Conjunto de soluciones candidatas. |
| Global / local optimum | Óptimo global / local | Mejor punto de todo el espacio / mejor solo en su vecindad. |
| Local search | Búsqueda local | Mantiene una solución y la mueve a vecinas (hill climbing, SA). |
| Metaheuristic | Metaheurística | Estrategia general de búsqueda aplicable a muchos problemas (GA, PSO, ACO…). |
| Exploration / exploitation | Exploración / explotación | Probar regiones nuevas / refinar las buenas. |
| Premature convergence | Convergencia prematura | La población colapsa en un óptimo local. |
| Continuous / combinatorial | Continua / combinatoria | Variables reales / discretas (permutaciones, rutas). |

## Explicación

**Búsqueda de caminos vs. optimización.** En [A\*](a-star-search.md) importa el camino. En optimización solo importa **el estado final**: el punto (x, y) que minimiza f, el tour más corto, los pesos de una red.

**Óptimos locales y globales (slides 04, s3).** Una función puede tener muchos "valles" (mínimos locales) y "picos" (máximos locales). Optimizar es encontrar el global sin confundirlo con un local. Hill climbing (subir siempre a la mejor vecina) se atasca en el primer pico local (complemento, AIMA §4.1.1).

**Analogía evolutiva.** Cada punto del espacio es un "individuo" con una aptitud; si simulamos evolución, sobreviven los que convergen a los óptimos globales.

**Exploración vs. explotación** — el hilo conductor de la unidad:

| Algoritmo | Explora con… | Explota con… |
|---|---|---|
| [Gradient Descent](gradient-descent.md) | (casi nada; depende del punto inicial) | Seguir −∇f |
| [Simulated Annealing](simulated-annealing.md) | Aceptar empeoramientos cuando T es alta | Enfriar: T baja → solo mejoras |
| [Genetic Algorithms](genetic-algorithms.md) | Mutación, cruce entre regiones distintas | Selección de los más aptos, elitismo |
| [PSO](particle-swarm-optimization.md) | Inercia (sobrepasar), términos aleatorios | Atracción a p_best y g_best |
| [ACO](ant-colony-optimization.md) | Elección probabilística, evaporación | Refuerzo de feromona en buenos tours |
| [ABC](artificial-bee-colony.md) | Abejas exploradoras (*scouts*) | Abejas empleadas y observadoras |

Holland lo plantea como el problema de cuánto "hipotecar el presente por el futuro"; Kennedy y Eberhart citan su "asignación óptima de pruebas".

### Funciones de prueba del curso

| Función | Fórmula | Óptimo | Dificultad |
|---|---|---|---|
| Cuadrática (GD) | (x−2)² + (y+2)² | (2, −2), f = 0 | Convexa, un solo mínimo |
| Tareas GA/PSO | (x+2)² + (y−2)² + 10 | (−2, 2), f = 10 | Convexa |
| Rastrigin | 10n + Σ(xᵢ² − 10 cos 2πxᵢ) | 0, f = 0 | Muchísimos mínimos locales en rejilla |
| Ackley | −20 e^(−0.2√(½(x²+y²))) − e^(½(cos 2πx + cos 2πy)) + e + 20 | 0, f = 0 | Plana afuera, embudo con ruido |
| Schaffer f6 | (paper PSO) | 0 | Altamente no lineal, muchos óptimos locales |

## Errores comunes y tips de examen

- Las metaheurísticas **no garantizan** el óptimo global; son estocásticas: correr varias veces y reportar media/mejor.
- Una función convexa (como las de las tareas) se resuelve trivialmente con GD; las metaheurísticas brillan en funciones multimodales, discontinuas o combinatorias.
- Minimizar f equivale a maximizar −f (o 1/(1+f) para aptitudes positivas).

## Relacionado

- [Gradient Descent](gradient-descent.md) · [Simulated Annealing](simulated-annealing.md)
- [Evolutionary Computation](evolutionary-computation.md) · [Genetic Algorithms](genetic-algorithms.md)
- [Swarm Intelligence](swarm-intelligence.md) · [PSO](particle-swarm-optimization.md) · [ACO](ant-colony-optimization.md) · [ABC](artificial-bee-colony.md)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 3, 10.
- [Code — class optimization](../sources/code-class-optimization.md) (Rastrigin, Ackley, cuadrática).
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md); [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) §5–6.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 4; [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) cap. 1.
