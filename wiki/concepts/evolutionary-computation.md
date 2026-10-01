---
title: Evolutionary Computation
type: concept
tags: [optimization, evolutionary-computation, bio-inspired]
sources: [slides-04-optimization, paper-holland-1992-genetic-algorithms, book-eiben-smith-evolutionary-computing]
updated: 2026-10-01
---
# Evolutionary Computation (Computación evolutiva)

> **Summary (EN):** Evolutionary computation applies the mechanisms of biological evolution — variation, selection and heredity — to optimization. It has several historical dialects: evolutionary programming (Lawrence Fogel, 1960s, evolving finite-state machines), evolution strategies (Rechenberg and Schwefel, 1970s, real-valued parameter optimization) and genetic algorithms (John Holland, 1975, bit strings with crossover). All share the same loop: initialize a population, evaluate fitness, select parents, recombine and mutate, select survivors, repeat.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Population | Población | Conjunto de soluciones candidatas (individuos). |
| Individual / chromosome / genotype | Individuo / cromosoma / genotipo | Una solución codificada. |
| Phenotype | Fenotipo | La solución decodificada (p. ej. (x, y)). |
| Fitness | Aptitud | Calidad de un individuo. |
| Parent / survivor selection | Selección de padres / supervivientes | Quién se reproduce / quién pasa a la siguiente generación. |
| Recombination (crossover) | Recombinación (cruce) | Combinar dos padres. |
| Mutation | Mutación | Cambio aleatorio pequeño. |
| Generation / epoch | Generación / época | Una iteración del ciclo. |

## Explicación

**Principios biológicos (slides 04, s3):** *adaptación* (sobrevivir y comportarse bien en el entorno), *herencia* (pasar rasgos a la siguiente generación), *selección natural* (los más aptos tienen más probabilidad de pasar sus rasgos).

**Esquema general de un algoritmo evolutivo** (complemento: Eiben & Smith cap. 3):

```
initialize population with random candidates
evaluate each candidate
repeat until termination:
    select parents
    recombine pairs of parents  -> offspring
    mutate offspring
    evaluate offspring
    select individuals for the next generation
```

**Dialectos históricos:**

| Dialecto | Origen | Representación típica | Operador principal |
|---|---|---|---|
| Evolutionary programming | L. J. Fogel, 1960 | Máquinas de estados finitos | Mutación |
| Evolution strategies | Rechenberg y Schwefel, 1970 | Vectores reales | Mutación gaussiana auto-adaptativa |
| [Genetic algorithms](genetic-algorithms.md) | J. H. Holland, 1975 | Cadenas de bits | Cruce (+ mutación) |
| Genetic programming | Koza, ~1990 (complemento) | Árboles (programas) | Cruce de subárboles |

Holland (1992) explica por qué los primeros intentos de finales de los 50 fallaron: dependían solo de la **mutación**; la clave fue añadir **apareamiento (cruce)**.

**Relación con la inteligencia de enjambre.** [PSO](particle-swarm-optimization.md) también usa una población y una medida de aptitud, pero no hay selección ni reproducción: las mismas partículas se mueven. Kennedy y Eberhart lo ubican "entre los GA y la programación evolutiva".

## Errores comunes y tips de examen

- Fogel → 1960 (EP); Rechenberg/Schwefel → 1970 (ES); Holland → **1975** (GA).
- Genotipo (código) ≠ fenotipo (solución decodificada).

## Relacionado

- [Genetic Algorithms](genetic-algorithms.md)
- [Swarm Intelligence](swarm-intelligence.md)
- [Optimization Basics](optimization-basics.md)
- [History of AI](history-of-ai.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 2–3.
- [Holland 1992](../sources/paper-holland-1992-genetic-algorithms.md).
- [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) caps. 2–3, 6 (pendiente de ingestar).
