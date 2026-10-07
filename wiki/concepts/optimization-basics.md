---
title: Optimization Basics
type: concept
tags: [optimization, local-search, metaheuristics]
sources: [slides-04-optimization, code-class-optimization, paper-holland-1992-genetic-algorithms, paper-kennedy-eberhart-1995-pso, book-eiben-smith-evolutionary-computing, book-russell-norvig-aima]
updated: 2026-10-07
---
# Optimization Basics (Fundamentos de optimización)

> **Summary (EN):** Optimization looks for the input that makes a function as small (or as large) as possible, for example the lowest point of a valley; only the final answer matters, not the path. The danger is getting stuck in a local optimum (a small valley) instead of the global one (the deepest). The course covers gradient descent (uses derivatives), simulated annealing (one solution, with randomness) and population methods (GA, PSO, ACO, ABC). All of them balance exploration (trying new regions) and exploitation (improving good ones). Test functions like Rastrigin, Ackley and Schaffer f6 check that balance.

> **En palabras simples (ES):** Optimizar es buscar **el mejor valor posible** de una función, por ejemplo el punto más bajo de un valle. No importa el camino, solo el punto final. El peligro es quedarse en un "valle pequeño" (óptimo local) creyendo que es el más profundo (óptimo global). Para elegir algoritmo, haz estas preguntas. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Objective / fitness function | Función objetivo / de aptitud | La "nota" de una solución: lo que queremos hacer lo más pequeño (o grande) posible. |
| Search space | Espacio de búsqueda | Todas las soluciones posibles. |
| Global optimum | Óptimo global | La mejor solución de **todas**. |
| Local optimum | Óptimo local | La mejor solución **de su zona**, pero no de todas (un valle pequeño). |
| Local search | Búsqueda local | Mejorar una solución haciéndole cambios pequeños (hill climbing, recocido simulado). |
| Metaheuristic | Metaheurística | Una estrategia general de búsqueda que sirve para muchos problemas (GA, PSO, ACO…). |
| Exploration / exploitation | Exploración / explotación | Probar zonas nuevas / mejorar alrededor de lo bueno que ya tengo. |
| Premature convergence | Convergencia prematura | Todas las soluciones se juntan demasiado pronto en un valle pequeño. |
| Continuous / combinatorial | Continuo / combinatorio | Los valores son números reales / son elecciones que se pueden contar (rutas, órdenes). |

## Explicación

### 1. Buscar un camino vs. optimizar

En [A\*](a-star-search.md) importa el **camino** (por dónde vas a Bucarest). En optimización solo importa **la respuesta final**: el punto (x, y) donde f es mínima, la ruta más corta o los pesos de una red neuronal.

### 2. Óptimos locales y globales (slides 04, s3)

Imagina el gráfico de f como un terreno con muchos **valles** (mínimos locales) y **picos** (máximos locales). Optimizar es encontrar el valle **más profundo** sin confundirlo con uno pequeño.

- **Hill climbing** (ir siempre al mejor vecino) se atasca en cimas pequeñas, crestas y zonas planas. En 8 reinas al azar solo resuelve el 14 % (ver [Local Search and Hill Climbing](local-search-hill-climbing.md)).
- El libro llama **búsqueda local** a estos métodos: guardan solo la solución actual (o unas pocas), cada estado ya es una solución completa y no recuerdan el camino.

**Analogía de la evolución:** cada punto del terreno es un "individuo" con su nota (aptitud). Si simulamos la evolución, sobreviven los que llegan a los mejores valles.

### 3. Explorar vs. explotar: la idea que une toda la unidad

Todo algoritmo de optimización tiene que equilibrar dos cosas:
- **Explorar:** buscar en zonas nuevas, por si hay un valle mejor en otro lado.
- **Explotar:** mejorar alrededor de lo bueno que ya encontré.

Si solo explotas, te quedas en el primer valle. Si solo exploras, nunca afinas la respuesta.

| Algoritmo | Explora con… | Explota con… |
|---|---|---|
| [Gradient Descent](gradient-descent.md) | casi nada (depende de dónde empiezas) | ir siempre cuesta abajo (−∇f) |
| [Simulated Annealing](simulated-annealing.md) | aceptar empeorar cuando la temperatura T es alta | enfriar: con T baja solo acepta mejoras |
| [Genetic Algorithms](genetic-algorithms.md) | mutación y cruce entre soluciones distintas | elegir a los mejores como padres, elitismo |
| [PSO](particle-swarm-optimization.md) | la inercia (pasarse de largo) y los números al azar | la atracción a su mejor lugar y al mejor del grupo |
| [ACO](ant-colony-optimization.md) | elegir caminos al azar, evaporación de feromona | reforzar con feromona los buenos recorridos |
| [ABC](artificial-bee-colony.md) | abejas exploradoras (*scouts*) | abejas empleadas y observadoras |

Holland lo describe como decidir cuánto "hipotecar el presente por el futuro" (gastar intentos explorando para ganar después). Kennedy y Eberhart citan esa misma idea.

### 4. Funciones de prueba del curso

| Función | Fórmula | Dónde está el mínimo | ¿Qué tan difícil? |
|---|---|---|---|
| Cuadrática (descenso de gradiente) | (x−2)² + (y+2)² | (2, −2), f = 0 | Fácil: un solo valle |
| Tareas GA/PSO | (x+2)² + (y−2)² + 10 | (−2, 2), f = 10 | Fácil: un solo valle |
| Rastrigin | 10n + Σ(xᵢ² − 10 cos 2πxᵢ) | en 0, f = 0 | Difícil: muchísimos valles pequeños en cuadrícula |
| Ackley | −20 e^(−0.2√(½(x²+y²))) − e^(½(cos 2πx + cos 2πy)) + e + 20 | en 0, f = 0 | Plana por fuera y un embudo con "ruido" en el centro |
| Schaffer f6 | (en el paper de PSO) | en 0 | Muy irregular, con muchos valles |

¿Por qué la de las tareas vale 10 en (−2, 2)? Porque ahí (x+2)² = 0 y (y−2)² = 0, y solo queda el +10.

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

- Las metaheurísticas **no garantizan** encontrar el óptimo global y usan azar: hay que correrlas varias veces y reportar el promedio y el mejor resultado.
- Una función con un solo valle (como las de las tareas) se resuelve fácil con descenso de gradiente; las metaheurísticas sirven más en funciones con muchos valles, con saltos o en problemas combinatorios.
- Minimizar f es lo mismo que maximizar −f (o 1/(1+f) si se necesita una aptitud positiva).

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
