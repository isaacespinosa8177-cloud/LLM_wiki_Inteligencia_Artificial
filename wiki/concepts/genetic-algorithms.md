---
title: Genetic Algorithms
type: concept
tags: [optimization, evolutionary-computation, genetic-algorithms]
sources: [slides-04-optimization, paper-holland-1992-genetic-algorithms, book-eiben-smith-evolutionary-computing]
updated: 2026-10-01
---
# Genetic Algorithms (Algoritmos genéticos, GA)

> **Summary (EN):** A genetic algorithm evolves a population of chromosomes (classically bit strings) using selection by fitness, crossover between parents (single-, two- or k-point) and bit-flip mutation with a small probability. Holland's explanation of why it works is implicit parallelism: every string samples many schemata (regions like 1**0*) at once, and short, compact building blocks with above-average fitness survive crossover and multiply. In the course assignment, a 16-bit GA minimizes (x+2)² + (y−2)² + 10 and reaches the optimum (−2, 2).

## Términos clave

| English | Español | Significado |
|---|---|---|
| Chromosome / gene / allele | Cromosoma / gen / alelo | Cadena completa / posición / valor (0 o 1). |
| Encoding | Codificación | Cómo una solución se representa en bits. |
| Fitness function | Función de aptitud | Evalúa a cada individuo. |
| Selection (roulette, tournament, truncation) | Selección (ruleta, torneo, truncamiento) | Elegir padres según aptitud. |
| Crossover (single/two/k-point, uniform) | Cruce (uno/dos/k puntos, uniforme) | Intercambiar segmentos de bits entre padres. |
| Mutation (bit flip) | Mutación (inversión de bit) | Cada bit cambia con probabilidad p_m. |
| Elitism | Elitismo | Copiar los mejores sin cambios a la siguiente generación. |
| Schema / building block | Esquema / bloque constructor | Patrón como `1**0*`; región del espacio. |
| Implicit parallelism | Paralelismo implícito | Una población pequeña muestrea muchísimos esquemas. |

## Explicación

**Los tres principios (slides 04, s5):** variación, selección, herencia.
- **Individuos:** cadenas de bits (un número decimal en binario).
- **Evaluación:** función de aptitud que busca el valor más alto o más bajo.
- **Reproducción:** cruce.
- **Variación:** mutación = invertir un bit con cierta probabilidad.

**Cruce de un punto (s6, Holland):** los padres se alinean, se elige un punto al azar y se intercambian las partes:

```
parent1 = 1101|1001        child1 = 1101|0110
parent2 = 0010|0110   ->   child2 = 0010|1001
```

Se generaliza a dos puntos o k puntos.

**Mutación:** para cada bit, con probabilidad p_m, cambiarlo (Holland: ≈ 1 de cada 10 000 símbolos; en la práctica p_m ≈ 1/L). "La mutación sola no avanza la búsqueda, pero es un seguro contra una población uniforme."

```python
def genetic_algorithm():
    population = [random_bits(L) for _ in range(POP)]
    for generation in range(EPOCHS):
        parents = select(population, fitness)            # roulette / tournament / truncation
        next_pop = elites(population)                    # optional elitism
        while len(next_pop) < POP:
            p1, p2 = random.choice(parents), random.choice(parents)
            c1, c2 = crossover(p1, p2)                   # single-point
            next_pop += [mutate(c1), mutate(c2)]         # bit flip with p_m
        population = next_pop[:POP]
    return best(population, fitness)
```

**Codificar números reales en bits.** La tarea usa 8 bits por variable en **signo-magnitud**: 1 bit de signo + 7 bits de magnitud → rango [−127, 127] (con un "−0" redundante). Alternativas: binario con desplazamiento, **código Gray** (vecinos difieren en un bit), o representación real directa (Eiben & Smith cap. 4).

**Métodos de selección** (complemento, Eiben & Smith cap. 5):
- **Ruleta** (proporcional a la aptitud): sensible a la escala de f.
- **Torneo**: tomar k al azar y quedarse con el mejor; presión controlada por k.
- **Truncamiento**: quedarse con los K mejores (lo que hace la tarea: K = 10 de 100) — presión de selección muy alta.

**Por qué funciona — teoría de esquemas (Holland).** La cadena `11011001` pertenece a las regiones `11******`, `1*******`, `**0**00*`, etc. Una población de pocos miles de cadenas muestrea así un número enorme de regiones (**paralelismo implícito**); las regiones de mayor aptitud media reciben más descendencia. Los **bloques compactos** (bits definidos cercanos) tienen menos riesgo de ser cortados por el cruce y se propagan. Forma cuantitativa (Teorema de esquemas, complemento):

```
m(H, t+1) ≥ m(H, t) · f(H)/f̄ · [1 − p_c·δ(H)/(L−1) − o(H)·p_m]
```

δ(H) = longitud definida, o(H) = orden (nº de bits fijos).

**Aplicaciones (Holland 1992):** classifier systems, estrategias del Dilema del Prisionero (redescubrieron *tit for tat*), control de un gasoducto, diseño de turbinas de motores a reacción.

## Ejemplo del curso

[Tarea GA](../assignments/genetic-algorithm-task.md): población 100, 16 bits, 100 épocas, selección por truncamiento K = 10 + elitismo, cruce de un punto, p_m = 0.1 por bit. Con `random.seed(0)`, el mejor llegó a f = 11 en la época 1 y al óptimo (x, y) = (−2, 2), f = 10, en la época 20.

## Errores comunes y tips de examen

- Selección = **quién** se reproduce; cruce = **cómo** se combinan; mutación = **diversidad**.
- Elitismo garantiza que el mejor nunca empeora (curva de mejor aptitud monótona).
- p_m muy alta → búsqueda aleatoria; muy baja → convergencia prematura.
- La tarea minimiza: "fitness" más bajo = mejor (hay que decirlo explícitamente en el examen).

## Relacionado

- [Evolutionary Computation](evolutionary-computation.md)
- [Optimization Basics](optimization-basics.md)
- [Particle Swarm Optimization](particle-swarm-optimization.md) (comparación)
- [GA assignment](../assignments/genetic-algorithm-task.md)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 5–7.
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md).
- [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) caps. 4–5, 16 (selección y teorema de esquemas: complemento).
