---
title: Gradient Descent
type: concept
tags: [optimization, continuous, gradient]
sources: [code-class-optimization, slides-01-introduction-to-ai, book-russell-norvig-aima]
updated: 2026-10-07
---
# Gradient Descent (Descenso de gradiente)

> **Summary (EN):** Gradient descent minimizes a function by repeatedly taking a small step in the direction where it goes down fastest, the opposite of the gradient: w ← w − η∇f(w). The learning rate η sets the step size: too small is slow, too large overshoots or diverges. It reaches the global minimum of bowl-shaped (convex) functions like the class example f(x,y) = (x−2)² + (y+2)², but only a local minimum of functions with many valleys. It is the engine behind backpropagation.

> **En palabras simples (ES):** Imagina que estás en una montaña con los ojos vendados y quieres bajar al valle. Tocas el suelo con el pie para sentir hacia dónde sube (eso es el gradiente) y das un paso **hacia el lado contrario**. Repites hasta que el suelo esté plano. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Derivative ∂f/∂x | Derivada parcial | Cuánto cambia f si mueves solo x un poquito. |
| Gradient ∇f | Gradiente | La lista de derivadas, una por variable: apunta hacia donde f **sube** más rápido. |
| Learning rate η (eta) | Tasa de aprendizaje | El tamaño de cada paso. |
| Convex function | Función convexa | Con forma de tazón: un solo valle (el mínimo global). |
| Convergence / divergence | Convergencia / divergencia | Acercarse al mínimo / alejarse cada vez más. |

## Explicación

### 1. La regla

```
w_{t+1} = w_t − η ∇f(w_t)
```

En palabras: **punto nuevo = punto actual − (tamaño del paso) × (gradiente)**. Como el gradiente apunta cuesta **arriba**, restarlo te lleva cuesta **abajo** por la pendiente más inclinada.

### 2. Ejemplo de clase (`gd_functions.py`)

Función: f(x, y) = (x−2)² + (y+2)². Su valle está en (2, −2), donde f = 0.

**Gradiente:** derivando cada variable, ∇f = (2(x−2), 2(y+2)).

```python
import numpy as np
def grad_f(w): return np.array([2*(w[0]-2), 2*(w[1]+2)])
w, eta = np.array([0.0, 0.0]), 0.1
for i in range(1000):
    w = w - eta * grad_f(w)
# w -> [2, -2], f(w) -> 0
```

**Primer paso a mano**, desde (0, 0) con η = 0.1:
1. Gradiente en (0, 0): (2·(0−2), 2·(0+2)) = (−4, 4).
2. Paso: (0, 0) − 0.1·(−4, 4) = (0 + 0.4, 0 − 0.4) = **(0.4, −0.4)**. Se acercó a (2, −2).

En cada paso la distancia al mínimo se multiplica por (1 − 2η) = 0.8, o sea, se acorta un 20 %. Para esta función:
- Si 0 < η < 1 → **llega** al mínimo (con η = 0.5 llega en un solo paso).
- Si η = 1 → **rebota** de un lado al otro para siempre.
- Si η > 1 → los pasos se pasan cada vez más y se **aleja** (diverge).

`gd_steroids.py` usa η = 0.02 (avanza solo un 4 % por paso) para que la animación en 3-D se vea suave. ⚠️ La superficie que dibuja usa (y+1)² en lugar de (y+2)² — ver [bug](../sources/code-class-optimization.md).

### 3. Límites

- Necesita poder calcular **derivadas**.
- Si la función tiene muchos valles (Rastrigin), termina en el valle **más cercano** a donde empezó, que puede no ser el mejor. Por eso existen el [recocido simulado](simulated-annealing.md) y los métodos con poblaciones.

**Conexión con redes neuronales:** [backpropagation](neural-networks.md) calcula el gradiente del error respecto a cada peso, y el descenso de gradiente usa ese gradiente para corregir los pesos.

### 4. Optimizar con números reales (AIMA §4.2) *(extra)*

**Ejemplo del libro: 3 aeropuertos en Rumania.** Hay que ubicar 3 aeropuertos, cada uno con coordenadas (x, y): 6 números en total. Queremos que la suma de las distancias (al cuadrado) de cada ciudad a su aeropuerto más cercano sea mínima. Como cada coordenada puede ser cualquier número real, hay **infinitos vecinos**, y los algoritmos del capítulo 3 no sirven directamente.

| Técnica | Idea (en simple) |
|---|---|
| **Discretizar** | Usar una cuadrícula: moverse solo ±δ en cada variable (12 vecinos) y aplicar búsqueda local normal |
| **Gradiente empírico** | Medir cuánto cambia f probando puntos muy cercanos (sin fórmula de derivada) |
| **Gradiente con fórmula** | Calcular las derivadas; a veces se puede resolver ∇f = 0 directamente (con 1 aeropuerto, el mejor lugar es el promedio de las ciudades) |
| **Paso de gradiente** | x ← x + α∇f(x) para maximizar, o x ← x − α∇f(x) para minimizar; α es el tamaño del paso |
| **Búsqueda en línea** (*line search*) | Seguir en la dirección del gradiente duplicando el paso hasta que f empiece a empeorar |
| **Newton–Raphson** | Usar también las segundas derivadas (la matriz Hessiana) para saltar directo al fondo de una parábola; es caro con muchas variables |
| **Optimización con restricciones** | Las soluciones deben cumplir reglas (los aeropuertos deben quedar dentro de Rumania) |
| **Programación lineal / convexa** | Si las reglas y la función son "rectas" (lineales) o con forma de tazón (convexas), se resuelve rápido |

El dilema del tamaño de paso α es el mismo que con η: muy pequeño → demasiados pasos; muy grande → se pasa del objetivo. Los métodos con números reales también se atascan en valles pequeños, crestas y zonas planas; ayudan los reinicios aleatorios y el recocido simulado.

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

- Es **menos** el gradiente (para bajar). Más el gradiente sería subir (ascenso de gradiente).
- Para elegir η, prueba valores en escala de 10: 0.001, 0.01, 0.1…
- Con el mismo punto de inicio, el descenso de gradiente siempre da el mismo resultado (no usa azar). La versión estocástica (SGD) usa el gradiente de solo algunos datos cada vez (complemento).

## Relacionado

- [Local Search and Hill Climbing](local-search-hill-climbing.md)
- [Optimization Basics](optimization-basics.md)
- [Simulated Annealing](simulated-annealing.md)
- [Neural Networks](neural-networks.md)

## Fuentes

- [Code — class optimization](../sources/code-class-optimization.md) (`gd_functions.py`, `gd_steroids.py`).
- [Slides 01](../sources/slides-01-introduction-to-ai.md), slide 11 (backprop).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.2 (ingestado: aeropuertos, gradiente empírico, line search, Newton–Raphson, optimización convexa).
