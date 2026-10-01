---
title: "Paper — Kennedy & Eberhart (1995), Particle Swarm Optimization"
type: source
tags: [paper, swarm-intelligence, pso, optimization]
sources: [paper-kennedy-eberhart-1995-pso]
updated: 2026-10-01
---
# Paper — Kennedy & Eberhart (1995), Particle Swarm Optimization

> **Summary (EN):** The original PSO paper (IEEE ICNN 1995, pp. 1942–1948). It tells how a bird-flocking simulation (nearest-neighbor velocity matching + "craziness") turned into an optimizer once agents remembered their personal best (pbest) and knew the group best (gbest). After stripping away unneeded parts, the "current simplified version" updates velocities with `v += 2·rand()·(pbest − x) + 2·rand()·(gbest − x)`. PSO trained neural networks (XOR, Fisher Iris) as well as backpropagation and solved Schaffer's f6 benchmark; it sits conceptually between genetic algorithms and evolutionary programming.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/papers/2 - Particle_swarm_optimization.pdf](../../raw/papers/2%20-%20Particle_swarm_optimization.pdf) |
| Autores | James Kennedy (psicólogo social, Bureau of Labor Statistics) y Russell Eberhart (ingeniero eléctrico, Purdue) |
| Publicación | Proc. IEEE International Conference on Neural Networks, 1995, pp. 1942–1948 |
| Extensión | 7 páginas |

## Resumen por secciones

- **§1 Introducción.** Método para optimizar funciones continuas no lineales, descubierto simulando un modelo social simplificado. Raíces: vida artificial (bandadas, cardúmenes) y computación evolutiva. Muy simple: pocas líneas de código, operadores primitivos, barato en memoria y tiempo.
- **§2 Simular comportamiento social.** Reynolds y Heppner simularon bandadas. Cita de E. O. Wilson: los individuos de un cardumen se benefician de los descubrimientos de los demás → compartir información da ventaja evolutiva. En humanos, el "movimiento" es en un espacio abstracto de creencias, sin colisiones.
- **§3 Precursores (cómo nació el algoritmo).**
  - 3.1 *Nearest-neighbor velocity matching* + *craziness* (ruido) para evitar que la bandada se uniformice.
  - 3.2 *Cornfield vector*: cada agente recuerda su mejor posición (**pbest**) y conoce la mejor del grupo (**gbest**); ajusta su velocidad hacia ambas con incrementos aleatorios.
  - 3.3 Se eliminan variables auxiliares: sin craziness y sin velocity matching funciona igual o mejor. pbest ≈ "nostalgia" (memoria autobiográfica); gbest ≈ norma social. Si p-increment ≫ g-increment: individuos vagan aislados; si g ≫ p: convergencia prematura a mínimos locales.
  - 3.4 Búsqueda multidimensional: entrenar los 13 pesos de una red 2-3-1 para XOR; criterio e < 0.05 en 30.7 iteraciones promedio con 20 agentes.
  - 3.5 Aceleración por distancia: la velocidad cambia en proporción a la diferencia (pbest − x), no solo por el signo.
  - 3.6 **Versión simplificada actual:** `vx = vx + 2·rand()·(pbestx − presentx) + 2·rand()·(pbestx[gbest] − presentx)`. El factor 2 da media 1, así los agentes "sobrevuelan" el objetivo la mitad del tiempo.
  - 3.7 Variantes que no mejoraron: un solo término hacia el punto medio pbest/gbest (converge a ese punto aunque no sea óptimo); exploradores vs. colonos; **quitar el momentum** (la velocidad anterior) → mucho peor.
- **§4 Enjambres y partículas.** Cinco principios de inteligencia de enjambre de Millonas: proximidad, calidad, respuesta diversa, estabilidad, adaptabilidad. "Particle" porque tienen velocidad y aceleración.
- **§5 Pruebas.** Entrenó redes neuronales tan bien como backprop (Iris: 284 épocas promedio; EEG: 92 % vs. 89 % de backprop en test). En la función f6 de Schaffer encontró el óptimo global en cada corrida.
- **§6 Conclusiones.** PSO está entre los GA y la programación evolutiva; el ajuste hacia pbest/gbest es análogo al cruce. El *momentum* produce sobrepaso (exploración) y los factores aleatorios exploran entre regiones buenas — equilibrio exploración/explotación (cita a Holland, "optimum allocation of trials").

## Ideas clave

1. Dos memorias: **cognitiva** (pbest) y **social** (gbest).
2. La inercia/momentum de la velocidad es esencial; sin ella PSO falla.
3. La ecuación original **no tiene peso de inercia w** ni coeficientes c₁, c₂ distintos de 2; esos aparecen en trabajos posteriores (Shi & Eberhart 1998 introdujo w — conocimiento general).

## Conceptos que alimenta

- [Particle Swarm Optimization](../concepts/particle-swarm-optimization.md)
- [Swarm Intelligence](../concepts/swarm-intelligence.md)
- [Optimization Basics](../concepts/optimization-basics.md)
- [Neural Networks](../concepts/neural-networks.md)

## Notas y discrepancias

- La [tarea PSO](../assignments/pso-task.md) usa `w = 0.5`, `a1 = a2 = 1`: es la variante con peso de inercia, no la ecuación de 1995.
- La fórmula de evaluación del *cornfield* (§3.2) quedó ilegible en la extracción de texto.
