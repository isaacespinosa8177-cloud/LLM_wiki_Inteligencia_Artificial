---
title: "Genetic algorithm — minimize (x+2)² + (y−2)² + 10"
type: assignment
tags: [assignment, optimization, genetic-algorithms, python]
sources: [slides-04-optimization, paper-holland-1992-genetic-algorithms]
updated: 2026-10-01
---
# Genetic algorithm task (Tarea: algoritmo genético)

> **Summary (EN):** A 16-bit genetic algorithm (8 bits per variable, sign-magnitude) that minimizes f(x, y) = (x+2)² + (y−2)² + 10. Population 100, 100 epochs, truncation selection of the best 10 with elitism, single-point crossover and per-bit mutation rate 0.1; it plots best fitness per epoch. With random seed 0 it reaches f = 11 at epoch 1 and the exact optimum (−2, 2), f = 10, at epoch 20.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/assignments/Genetic_algorithm (1).py](../../raw/assignments/Genetic_algorithm%20%281%29.py) |
| Autor | Isaac Espinosa (00342611) |
| Lenguaje | Python 3 + matplotlib (export de Colab) |
| Unidad | 4 — Optimización |
| ⚠️ Política de IA | Desconocida: el enunciado no está en `raw/`. Revisión añadida tras la entrega (2026-10-01). Si agregas el enunciado, la IA debe verificar su política. |

## Qué se implementó

| Componente | Implementación |
|---|---|
| Codificación | 16 bits: bits 0–7 → x, 8–15 → y; primer bit = signo, 7 bits = magnitud → x, y ∈ [−127, 127] |
| Aptitud | f(x, y) = (x+2)² + (y−2)² + 10 (minimizar; óptimo f = 10 en (−2, 2)) |
| Selección | Truncamiento: ordenar y tomar los K = 10 mejores |
| Elitismo | Los 10 seleccionados pasan copiados |
| Cruce | Un punto, `randint(1, 15)` |
| Mutación | Cada bit se invierte con p = 0.1 |
| Parámetros | Población 100, 100 épocas |
| Salida | Mejor individuo por época + gráfica de f(best) vs. época |

## Resultados (`random.seed(0)`, 2026-10-01)

- Época 1: `1000000100000010` → x = −1, y = 2, f = 11.
- Época 20: `1000001000000010` → **x = −2, y = 2, f = 10** (óptimo global). Se mantiene hasta la época 100 gracias al elitismo.

## Revisión

**Fortalezas**
- Código claro y modular (una función por operador), con elitismo correcto (copias `ind[:]`, sin *aliasing*).
- Encuentra el óptimo exacto rápidamente; la gráfica muestra la convergencia.

**Puntos a mejorar**
1. **Presión de selección muy alta:** truncamiento al 10 % + elitismo puede hacer perder diversidad (convergencia prematura en funciones multimodales). Probar torneo (k = 2–3) o ruleta y comparar.
2. **Mutación alta:** 0.1 por bit ≈ 1.6 bits por hijo; lo habitual es ≈ 1/L = 0.0625. Buen experimento: graficar convergencia con p_m ∈ {0.01, 0.06, 0.1, 0.2}.
3. **Signo-magnitud** tiene dos ceros (+0 y −0) y saltos grandes entre vecinos; **código Gray** hace que valores vecinos difieran en un bit.
4. El rango [−127, 127] es mucho mayor que lo necesario; para una función continua se podría mapear los bits a [a, b] con resolución fija o usar representación real.
5. `fitness()` se recalcula muchas veces (ordenar, `min`, imprimir); cachear valores ahorra tiempo en problemas más caros.
6. La función es convexa: GD lo resuelve trivialmente. Para lucir el GA, probar Rastrigin o Ackley (ya están en [sa_functions.py](../sources/code-class-optimization.md)).

## Conceptos relacionados

- [Genetic Algorithms](../concepts/genetic-algorithms.md)
- [Evolutionary Computation](../concepts/evolutionary-computation.md)
- [Optimization Basics](../concepts/optimization-basics.md)
- [PSO task](pso-task.md) (misma función)
