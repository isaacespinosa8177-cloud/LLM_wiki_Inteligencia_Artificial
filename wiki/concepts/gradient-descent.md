---
title: Gradient Descent
type: concept
tags: [optimization, continuous, gradient]
sources: [code-class-optimization, slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-01
---
# Gradient Descent (Descenso de gradiente)

> **Summary (EN):** Gradient descent minimizes a differentiable function by repeatedly stepping against the gradient: w ← w − η∇f(w). The learning rate η controls step size — too small is slow, too large overshoots or diverges. It converges to the global minimum on convex functions like the class example f(x,y) = (x−2)² + (y+2)², but only to a local minimum on multimodal ones. It is the engine behind backpropagation.

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

## Errores comunes y tips de examen

- Es **menos** el gradiente (descenso); más el gradiente es ascenso.
- Elegir η: probar en escala logarítmica (0.001, 0.01, 0.1…).
- GD es determinista dado el punto inicial; SGD (estocástico) usa gradientes de muestras (complemento).

## Relacionado

- [Optimization Basics](optimization-basics.md)
- [Simulated Annealing](simulated-annealing.md)
- [Neural Networks](neural-networks.md)

## Fuentes

- [Code — class optimization](../sources/code-class-optimization.md) (`gd_functions.py`, `gd_steroids.py`).
- [Slides 01](../sources/slides-01-introduction-to-ai.md), slide 11 (backprop).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.2 (complemento).
