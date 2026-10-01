---
title: Particle Swarm Optimization
type: concept
tags: [optimization, swarm-intelligence, pso, continuous]
sources: [slides-04-optimization, paper-kennedy-eberhart-1995-pso]
updated: 2026-10-01
---
# Particle Swarm Optimization (Optimización por enjambre de partículas, PSO)

> **Summary (EN):** PSO (Kennedy & Eberhart, 1995) keeps a swarm of particles, each with a position x (a candidate solution), a velocity v and a personal best p_best; the swarm shares a global best g_best. Each step, velocity is pulled toward p_best (cognitive term) and g_best (social term) with random weights, and the particle moves: x ← x + v. The original update is v ← v + 2·rand·(p_best − x) + 2·rand·(g_best − x); later versions add an inertia weight w. Momentum causes overshooting (exploration) while the attraction terms exploit good regions.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Particle | Partícula | Solución candidata que se mueve en el espacio. |
| Position x_t / velocity v_t | Posición / velocidad | Dónde está / cómo se mueve. |
| Personal best p_best | Mejor personal | Mejor posición que visitó esa partícula ("nostalgia"). |
| Global best g_best | Mejor global | Mejor posición encontrada por el enjambre ("norma social"). |
| Cognitive / social term | Término cognitivo / social | Atracción hacia p_best / g_best. |
| Inertia weight w | Peso de inercia | Cuánto conserva de su velocidad anterior (variante posterior). |
| φ₁, φ₂ | φ₁, φ₂ | Números aleatorios ~ U[0, 1]. |

## Explicación

**Origen (paper §3).** Empezó como simulación de bandadas: *velocity matching* con el vecino + "craziness". Al añadir un "campo de maíz" (*cornfield*), cada agente recordaba su mejor posición (p_best) y conocía la mejor del grupo (g_best). Luego se eliminó lo innecesario (craziness, vecinos) y la bandada se volvió un **enjambre** que encuentra el óptimo.

**Ecuaciones.**

Versión original (1995, §3.6):
```
v ← v + 2·rand()·(p_best − x) + 2·rand()·(g_best − x)
x ← x + v
```
El factor 2 da media 1: las partículas "sobrevuelan" el objetivo la mitad del tiempo.

Versión con inercia (la de la tarea; Shi & Eberhart 1998, complemento):
```
v ← w·v + a₁·φ₁·(p_best − x) + a₂·φ₂·(g_best − x),   φ₁, φ₂ ~ U[0,1]
x ← x + v
```

**Algoritmo (tal como en la [tarea PSO](../assignments/pso-task.md)):**

```python
S = uniform(lower, upper, (N, D)); V = zeros((N, D)); P = S.copy()
f_P = [f(p) for p in P];  g = argmin(f_P)
for t in range(max_iter):
    phi1, phi2 = rand(N, D), rand(N, D)
    V = w*V + a1*phi1*(P - S) + a2*phi2*(P[g] - S)
    S = clip(S + V, lower, upper)
    f_S = [f(s) for s in S]
    improved = f_S < f_P
    P[improved], f_P[improved] = S[improved], f_S[improved]
    g = argmin(f_P)
return P[g], f_P[g]
```

**Exploración vs. explotación (slide 10).**
- p_increment ≫ g_increment → individuos vagan aislados (demasiada exploración).
- g_increment ≫ p_increment → el enjambre corre prematuramente a un mínimo local.
- Valores aproximadamente iguales funcionan mejor.
- **Quitar el momentum** (la velocidad anterior) hace al algoritmo "bastante ineficaz" para óptimos globales: la inercia es lo que explora.

**Resultados del paper.** Entrenó una red XOR 2-3-1 (13 pesos) en 30.7 iteraciones con 20 agentes; Iris tan bien como backprop; EEG 92 % vs. 89 %; encontró el óptimo global de Schaffer f6 en cada corrida.

## Ejemplo del curso

Tarea: N = 20 partículas, D = 2, límites [−10, 10], 100 iteraciones, w = 0.5, a₁ = a₂ = 1, minimizar (x+2)² + (y−2)² + 10. Con `np.random.seed(0)`: mejor x = (−2.00000001, 1.99999998), f = 10.0.

## Errores comunes y tips de examen

- PSO **no** tiene selección, cruce ni mutación: las mismas partículas sobreviven y se mueven.
- p_best es por partícula; g_best es uno para todo el enjambre (en la variante *global*; existe *lbest* con vecindarios — complemento).
- La ecuación original no tiene w; si en el examen aparece w, es la variante con inercia.
- Relación con GA: el ajuste hacia p_best/g_best es "conceptualmente similar al cruce" (paper §6).

## Relacionado

- [Swarm Intelligence](swarm-intelligence.md)
- [Genetic Algorithms](genetic-algorithms.md)
- [Optimization Basics](optimization-basics.md)
- [Neural Networks](neural-networks.md)
- [PSO assignment](../assignments/pso-task.md)
- [Metaheuristics comparison](../study/metaheuristics-comparison.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 8–11.
- [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) §3–6.
