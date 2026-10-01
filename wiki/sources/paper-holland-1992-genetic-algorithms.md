---
title: "Paper — Holland (1992), Genetic Algorithms (Scientific American)"
type: source
tags: [paper, evolutionary-computation, genetic-algorithms]
sources: [paper-holland-1992-genetic-algorithms]
updated: 2026-10-01
---
# Paper — Holland (1992), Genetic Algorithms

> **Summary (EN):** A popular-science article by the inventor of genetic algorithms (Scientific American 267(1):66–73, July 1992). Holland explains GAs as populations of bit strings that are selected by fitness, recombined by crossover and occasionally mutated. Their power comes from implicit parallelism: each string samples many "regions" (schemata such as `1***0*`) at once, and compact building blocks survive crossover and spread in proportion to their average fitness. Examples include classifier systems, evolving tit-for-tat in the Prisoner's Dilemma, gas-pipeline control and jet-engine turbine design.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/papers/Holland-GeneticAlgorithms-1992.pdf](../../raw/papers/Holland-GeneticAlgorithms-1992.pdf) |
| Autor | John H. Holland (Univ. of Michigan; Santa Fe Institute) |
| Publicación | *Scientific American*, vol. 267, no. 1, julio 1992, pp. 66–73 |
| Extensión | 9 páginas (incluye portada de JSTOR) |

## Resumen por secciones

- **Motivación.** Los organismos son resolvedores de problemas versátiles; la selección natural evita tener que especificar de antemano todas las características de un problema. Los GA "crían" programas que resuelven problemas que nadie entiende del todo.
- **Historia.** Intentos de finales de los 50 fallaron por depender solo de la mutación. Bremermann (60s) añadió una forma de apareamiento. Holland desarrolló el GA a mediados de los 60, con cruce y mutación, y luego los **classifier systems** (reglas condición→acción codificadas en bits; cualquier programa puede reescribirse como uno).
- **El algoritmo.** (1) evaluar cada cadena; (2) las de mayor rango se aparean: se elige un punto al azar y se intercambian los segmentos (**cruce de un punto**); los hijos reemplazan a las cadenas de baja aptitud (población constante); (3) **mutación** en una pequeña fracción (≈ 1 de cada 10 000 símbolos). La mutación sola no avanza la búsqueda, pero evita una población uniforme.
- **Paisaje de búsqueda.** El espacio de cadenas es un paisaje con valles y cumbres; hill climbing se atasca en paisajes con muchos picos. Ejemplo: ~10⁶⁰ estrategias de ajedrez.
- **Paralelismo implícito.** Una cadena como `11011001` pertenece a muchas regiones (`11******`, `1*******`, `**0**00*`, …). Una población de pocos miles de cadenas muestrea muchísimas más regiones; las regiones de alta aptitud reciben más muestras.
- **Building blocks.** Patrones cuyos bits definidos están cerca (compactos) sobreviven al cruce y se propagan en proporción a su aptitud media. La **inversión** puede reordenar genes para hacer bloques más compactos.
- **Exploración vs. explotación.** El cruce prueba bloques en nuevas combinaciones y contextos. Ejemplo del **Dilema del Prisionero**: Axelrod y Forrest evolucionaron estrategias que redescubrieron *tit for tat* (y temporalmente estrategias que lo explotaban).
- **Classifier systems.** Reglas compiten (subasta por fuerza) y se recompensan en cadena para metas de largo plazo; Goldberg las usó para controlar un gasoducto simulado.
- **Aplicaciones.** Diseño de turbinas de motores a reacción (General Electric), redes de comunicación, mercados y ecosistemas simulados en el Santa Fe Institute (*Echo*).

## Ideas clave

1. GA = selección + cruce + mutación sobre una población de cadenas.
2. **Schema / building block theory**: el GA asigna muestras a regiones en proporción a su aptitud estimada, "casi sin cómputo".
3. El cruce es el operador principal; la mutación es un seguro.

## Conceptos que alimenta

- [Genetic Algorithms](../concepts/genetic-algorithms.md)
- [Evolutionary Computation](../concepts/evolutionary-computation.md)
- [Optimization Basics](../concepts/optimization-basics.md) (exploración vs. explotación)

## Notas y discrepancias

- Las slides 04 fechan los GA en "1992"; la propuesta original es de 1975 (ver [slides-04](slides-04-optimization.md) y [errata](../study/errata.md)).
- El texto del PDF está en columnas mezcladas; las ilustraciones (cruce, tabla del Dilema del Prisionero) no se extrajeron.
