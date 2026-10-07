---
title: Optimization Basics
type: concept
tags: [optimization, local-search, metaheuristics]
sources: [slides-04-optimization, code-class-optimization, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, book-eiben-smith-evolutionary-computing, book-russell-norvig-aima]
updated: 2026-10-07
---
# Optimization Basics (Fundamentos de optimización)

> **Summary (EN):** Optimization looks for the input that maximizes or minimizes an objective (fitness) function, aiming for the global optimum without getting stuck in local optima. Unlike path search, only the final state matters. The course covers a gradient-based method (gradient descent), a single-solution stochastic method (simulated annealing) and population-based metaheuristics (GA, PSO, ACO, ABC). All of them balance exploration (trying new regions) against exploitation (refining good ones). Benchmark functions such as Rastrigin, Ackley and Schaffer f6 test that balance.

> **En palabras simples (ES):** Optimizar es buscar **el mejor valor posible** de una función, por ejemplo el punto más bajo de un valle. No importa el camino, solo el punto final. El peligro es quedarse en un "valle pequeño" (óptimo local) creyendo que es el más profundo (óptimo global). Para elegir algoritmo, haz estas preguntas. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

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

**Óptimos locales y globales (slides 04, s3).** Una función puede tener muchos "valles" (mínimos locales) y "picos" (máximos locales). Optimizar es encontrar el global sin confundirlo con un local. Hill climbing (subir siempre a la mejor vecina) se atasca en máximos locales, crestas y mesetas — en 8 reinas aleatorias resuelve solo el 14 % (ver [Local Search and Hill Climbing](local-search-hill-climbing.md)). AIMA llama **búsqueda local** a estos métodos: guardan solo el estado actual (o unos pocos), usan una **formulación de estado completo** y no recuerdan caminos.

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

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Optimizar es buscar **el mejor valor posible** de una función, por ejemplo el punto más bajo de un valle. No importa el camino, solo el punto final. El peligro es quedarse en un "valle pequeño" (óptimo local) creyendo que es el más profundo (óptimo global). Para elegir algoritmo, haz estas preguntas.

**Antes de empezar: qué significa cada cosa**

| Palabra / símbolo | Qué es (en simple) | English |
|---|---|---|
| f(x, y) | la función que queremos hacer lo más pequeña (o grande) posible; su valor es la "nota" de una solución | objective / fitness function |
| Minimizar / maximizar | buscar el valor más bajo / más alto | minimize / maximize |
| Óptimo global | el mejor punto de **toda** la función | global optimum |
| Óptimo local | el mejor punto **de su zona**, pero no de todas | local optimum |
| Gradiente | la dirección en que la función sube más rápido (necesita derivadas) | gradient |
| Continuo / combinatorio | los valores pueden ser cualquier número / son elecciones contables (rutas, órdenes) | continuous / combinatorial |
| Explorar / explotar | buscar en zonas nuevas / mejorar alrededor de lo bueno que ya tengo | exploration / exploitation |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Is f differentiable and (almost) bowl-shaped (convex)? → gradient descent.
   - *ES:* ¿Puedo calcular derivadas y la función tiene un solo valle? → descenso de gradiente.
2. Only one solution at a time and many local optima? → simulated annealing or random-restart hill climbing.
   - *ES:* ¿Quiero mejorar una sola solución pero hay muchos valles? → recocido simulado o reiniciar varias veces.
3. Continuous variables and no gradient? → PSO, ABC, real-valued GA or evolution strategies.
   - *ES:* ¿Números reales sin derivadas? → enjambre de partículas, abejas o un algoritmo evolutivo.
4. Combinatorial problem (routes, orders, schedules)? → ACO, GA with permutation operators, local search.
   - *ES:* ¿Rutas u órdenes? → hormigas o un GA para permutaciones.
5. Always run several times (results are random), keep the best, and balance exploration and exploitation.
   - *ES:* Estos algoritmos usan azar: córrelos varias veces y quédate con el mejor resultado.

**Ejemplo con números:** la función del curso f(x, y) = (x + 2)² + (y − 2)² + 10 tiene un solo valle. Su mínimo es **f = 10 en (−2, 2)**, porque ahí los dos cuadrados valen 0. Cualquier algoritmo la resuelve. Rastrigin, en cambio, tiene muchísimos valles pequeños: ahí sí se nota qué algoritmo explora mejor.

**Say it in the exam (EN):** "In optimization only the final solution matters, not the path. The goal is the global optimum, and the danger is getting stuck in a local optimum. Every metaheuristic balances exploration (searching new regions) and exploitation (improving good solutions): mutation and selection in GAs, inertia and attraction to the bests in PSO, evaporation and reinforcement in ACO, scouts and employed bees in ABC, and temperature in simulated annealing."

**Dilo así (ES):** "En optimización solo importa la solución final, no el camino. Se busca el óptimo global y el peligro es quedarse en uno local. Toda metaheurística equilibra explorar (zonas nuevas) y explotar (mejorar lo bueno): mutación y selección en GA, inercia y atracción en PSO, evaporación y refuerzo en ACO, exploradoras y empleadas en ABC, y temperatura en el recocido simulado."

## Errores comunes y tips de examen

- Las metaheurísticas **no garantizan** el óptimo global; son estocásticas: correr varias veces y reportar media/mejor.
- Una función convexa (como las de las tareas) se resuelve trivialmente con GD; las metaheurísticas brillan en funciones multimodales, discontinuas o combinatorias.
- Minimizar f equivale a maximizar −f (o 1/(1+f) para aptitudes positivas).

## Relacionado

- [Local Search and Hill Climbing](local-search-hill-climbing.md)
- [Gradient Descent](gradient-descent.md) · [Simulated Annealing](simulated-annealing.md)
- [Evolutionary Computation](evolutionary-computation.md) · [Genetic Algorithms](genetic-algorithms.md)
- [Swarm Intelligence](swarm-intelligence.md) · [PSO](particle-swarm-optimization.md) · [ACO](ant-colony-optimization.md) · [ABC](artificial-bee-colony.md)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 3, 10.
- [Code — class optimization](../sources/code-class-optimization.md) (Rastrigin, Ackley, cuadrática).
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md); [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) §5–6.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.1–4.2 (ingestado); [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) cap. 1.
