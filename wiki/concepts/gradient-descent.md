---
title: Gradient Descent
type: concept
tags: [optimization, continuous, gradient]
sources: [code-class-optimization, slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-07
---
# Gradient Descent (Descenso de gradiente)

> **Summary (EN):** Gradient descent minimizes a differentiable function by repeatedly stepping against the gradient: w ← w − η∇f(w). The learning rate η controls step size — too small is slow, too large overshoots or diverges. It converges to the global minimum on convex functions like the class example f(x,y) = (x−2)² + (y+2)², but only to a local minimum on multimodal ones. It is the engine behind backpropagation.

> **En palabras simples (ES):** Imagina que estás en una montaña con los ojos vendados y quieres bajar al valle. Tocas el suelo con el pie para sentir hacia dónde sube (eso es el gradiente) y das un paso **hacia el lado contrario**. Repites hasta que el suelo esté plano. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Gradient ∇f | Gradiente | Vector de derivadas parciales; apunta hacia donde f crece más rápido. |
| Learning rate η | Tasa de aprendizaje | Tamaño del paso. |
| Convex function | Función convexa | Un solo mínimo (global). |
| Convergence | Convergencia | Acercarse al mínimo con las iteraciones. |
| Divergence | Divergencia | Los pasos se alejan cada vez más. |

## Explicación

**Regla de actualización:**

```
w_{t+1} = w_t − η ∇f(w_t)
```

Como ∇f apunta "cuesta arriba", restar el gradiente baja por la pendiente más pronunciada.

**Ejemplo de clase (`gd_functions.py`).** f(x, y) = (x−2)² + (y+2)², ∇f = (2(x−2), 2(y+2)). Desde (0, 0) con η = 0.1:

```python
import numpy as np
def grad_f(w): return np.array([2*(w[0]-2), 2*(w[1]+2)])
w, eta = np.array([0.0, 0.0]), 0.1
for i in range(1000):
    w = w - eta * grad_f(w)
# w -> [2, -2], f(w) -> 0
```

Iteración 1: w = (0,0) − 0.1·(−4, 4) = (0.4, −0.4). En general la distancia al mínimo se multiplica por (1 − 2η) = 0.8 en cada paso → convergencia geométrica. Para esta función:
- 0 < η < 1 → converge (η = 0.5 llega en un paso).
- η = 1 → oscila para siempre; η > 1 → diverge.

`gd_steroids.py` usa η = 0.02 (factor 0.96, más lento) para que la animación 3-D se vea suave. ⚠️ Su superficie dibujada usa (y+1)² en lugar de (y+2)² — ver [bug](../sources/code-class-optimization.md).

**Limitaciones.** Necesita derivadas; en funciones multimodales (Rastrigin) termina en el mínimo local más cercano al punto inicial. Por eso existen [simulated annealing](simulated-annealing.md) y las metaheurísticas poblacionales.

**Conexión.** [Backpropagation](neural-networks.md) calcula ∇ de la pérdida respecto a los pesos; el descenso de gradiente los actualiza.

### Búsqueda local en espacios continuos (AIMA §4.2)

**Ejemplo de AIMA — 3 aeropuertos en Rumania.** Estado = (x₁, y₁, x₂, y₂, x₃, y₃) (6 variables). Objetivo: minimizar la suma de distancias al cuadrado de cada ciudad a su aeropuerto más cercano, f(x) = Σᵢ Σ_{c ∈ Cᵢ} (xᵢ − x_c)² + (yᵢ − y_c)². Un espacio continuo tiene **factor de ramificación infinito**, así que los algoritmos del cap. 3 no sirven directamente.

| Técnica | Idea |
|---|---|
| **Discretización** | Rejilla de paso δ: cada estado tiene 12 sucesores (±δ en cada variable); luego cualquier búsqueda local |
| **Empirical gradient** | Medir el cambio de f entre puntos cercanos = hill climbing en la versión discretizada |
| **Gradiente analítico** | ∇f da dirección y magnitud de la máxima pendiente; a veces se resuelve ∇f = 0 en forma cerrada (1 aeropuerto → la media de las ciudades) |
| **Paso de gradiente** | x ← x + α∇f(x) para maximizar (x ← x − α∇f(x) para minimizar); α = *step size* |
| **Line search** | Extender la dirección del gradiente duplicando α hasta que f empiece a empeorar |
| **Newton–Raphson** | x ← x − H_f(x)⁻¹ ∇f(x), con H la **Hessiana** (2.ª derivadas); ajusta una cuadrática y salta a su mínimo; caro en alta dimensión (n² entradas) |
| **Optimización con restricciones** | Soluciones deben cumplir restricciones (aeropuertos en tierra firme dentro de Rumania) |
| **Programación lineal / convexa** | Restricciones lineales (o región convexa) y objetivo lineal (o convexo) → **tiempo polinomial** |

El dilema de α: muy pequeño → demasiados pasos; muy grande → se pasa del máximo (lo mismo que se ve con η en `gd_functions.py`). Los métodos continuos sufren igual que los discretos con máximos locales, crestas y mesetas; ayudan los reinicios aleatorios y el recocido simulado.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Imagina que estás en una montaña con los ojos vendados y quieres bajar al valle. Tocas el suelo con el pie para sentir hacia dónde sube (eso es el gradiente) y das un paso **hacia el lado contrario**. Repites hasta que el suelo esté plano.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| w | el punto donde estoy, p. ej. w = (x, y) | current point (weights) |
| f(w) | qué tan alto estoy (el valor que quiero hacer pequeño) | function value |
| ∇f(w) | el **gradiente**: hacia dónde y qué tan rápido sube f. Se calcula con las derivadas de f respecto a cada variable | gradient |
| ∂f/∂x | la derivada de f respecto a x: cuánto cambia f si muevo solo x | partial derivative |
| η (eta) | la **tasa de aprendizaje**: el tamaño de cada paso | learning rate |
| w ← … | "el nuevo w es…" (actualizar) | update |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Start at some point w and choose a learning rate η.
   - *ES:* Elige un punto de partida y el tamaño del paso.
2. Compute the gradient ∇f(w): the derivative of f with respect to each variable.
   - *ES:* Calcula hacia dónde sube la función (una derivada por variable).
3. Move against it: w ← w − η · ∇f(w).
   - *ES:* Punto nuevo = punto actual − (tamaño del paso) × (gradiente). El signo "−" es para ir **cuesta abajo**.
4. Repeat steps 2–3 until the steps become tiny or you reach a maximum number of iterations. Return w.
   - *ES:* Repite hasta que casi no te muevas (llegaste al fondo).

**Ejemplo con números:** f(x, y) = (x − 2)² + (y + 2)², empiezo en (0, 0) con η = 0.1. El mínimo está en (2, −2).
1. Derivadas: ∂f/∂x = 2(x − 2) y ∂f/∂y = 2(y + 2). En (0, 0): ∇f = (2·(−2), 2·2) = (−4, 4).
2. Paso: (0, 0) − 0.1·(−4, 4) = (0 + 0.4, 0 − 0.4) = **(0.4, −0.4)**. f bajó de 8 a 5.12.
3. Siguiente paso: **(0.72, −0.72)**, f = 3.28. Luego **(0.976, −0.976)**, f ≈ 2.10. Se va acercando a (2, −2).
- Si η es muy grande (más de 1 aquí), los pasos se pasan del valle y se aleja (diverge). Si es muy pequeño, avanza lentísimo.

**Say it in the exam (EN):** "Gradient descent minimizes a function by repeatedly taking a small step against the gradient: w ← w − η∇f(w). The learning rate η matters: too small is slow, too large overshoots or diverges. It reaches the global minimum of convex (bowl-shaped) functions, but only a local minimum of functions with many valleys. Backpropagation computes the gradients that gradient descent uses to train neural networks."

**Dilo así (ES):** "El descenso de gradiente minimiza una función dando pasos pequeños en contra del gradiente: w ← w − η∇f(w). La tasa η importa: muy pequeña es lenta, muy grande se pasa o diverge. Llega al mínimo global si la función tiene un solo valle; si tiene muchos, solo a uno local. Backpropagation calcula los gradientes que se usan para entrenar redes neuronales."

## Errores comunes y tips de examen

- Es **menos** el gradiente (descenso); más el gradiente es ascenso.
- Elegir η: probar en escala logarítmica (0.001, 0.01, 0.1…).
- GD es determinista dado el punto inicial; SGD (estocástico) usa gradientes de muestras (complemento).

## Relacionado

- [Local Search and Hill Climbing](local-search-hill-climbing.md)
- [Optimization Basics](optimization-basics.md)
- [Simulated Annealing](simulated-annealing.md)
- [Neural Networks](neural-networks.md)

## Fuentes

- [Code — class optimization](../sources/code-class-optimization.md) (`gd_functions.py`, `gd_steroids.py`).
- [Slides 01](../sources/slides-01-introduction-to-ai.md), slide 11 (backprop).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.2 (ingestado: aeropuertos, gradiente empírico, line search, Newton–Raphson, optimización convexa).
