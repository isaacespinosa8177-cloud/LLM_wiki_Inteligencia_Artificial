---
title: "Code — Class optimization scripts (gradient descent, simulated annealing)"
type: source
tags: [code, python, optimization]
sources: [code-class-optimization]
updated: 2026-10-01
---
# Code — Class optimization scripts (Scripts de optimización de clase)

> **Summary (EN):** Three Python scripts handed out in class (comments in Spanish). `gd_functions.py` runs plain gradient descent on f(x,y) = (x−2)² + (y+2)²; `gd_steroids.py` does the same with a 3-D matplotlib animation saved to MP4; `sa_functions.py` implements simulated annealing on the Rastrigin function (Ackley also defined). Reading notes below flag two bugs worth knowing.

## Ficha

| Archivo | Qué hace |
|---|---|
| [raw/code/class/gd_functions.py](../../raw/code/class/gd_functions.py) | Descenso de gradiente, η = 0.1, 1000 iteraciones, desde (0, 0); imprime cada paso. |
| [raw/code/class/gd_steroids.py](../../raw/code/class/gd_steroids.py) | Igual con η = 0.02, 200 iteraciones; anima la trayectoria sobre la superficie 3-D y guarda `descenso_gradiente-s.mp4` (requiere ffmpeg). |
| [raw/code/class/sa_functions.py](../../raw/code/class/sa_functions.py) | Simulated annealing genérico `simulated_annealing(func, bounds, max_iter, initial_temp, cooling_rate)`; Rastrigin 2-D en [−5.12, 5.12]², T₀ = 100, enfriamiento 0.8, 100 000 iteraciones. |

## Resumen

- **Gradient descent.** `w ← w − η ∇f(w)` con ∇f = (2(x−2), 2(y+2)). Mínimo en (2, −2), f = 0. Con η = 0.1 cada paso reduce la distancia al mínimo en un factor (1 − 2η) = 0.8, convergencia geométrica.
- **Simulated annealing.** Vecino = solución actual + ruido U(−1, 1) por dimensión, recortado a los límites. Acepta si Δ < 0 o con probabilidad e^(−Δ/T). T ← 0.8·T en cada iteración. Guarda la mejor solución vista.
- **Funciones de prueba.** Rastrigin `10n + Σ(xᵢ² − 10 cos 2πxᵢ)` (muchos mínimos locales, global en 0) y Ackley (global en 0). Ver [Optimization Basics](../concepts/optimization-basics.md).

## Conceptos que alimenta

- [Gradient Descent](../concepts/gradient-descent.md)
- [Simulated Annealing](../concepts/simulated-annealing.md)
- [Optimization Basics](../concepts/optimization-basics.md)

## Notas y discrepancias (revisión del código)

- 🐞 **`gd_steroids.py`: la superficie dibujada no es la función optimizada.** `objective` usa `(y + 2)**2`, pero la malla `Z` y la animación usan `(Y + 1)**2`. La trayectoria converge a (2, −2) mientras que el mínimo dibujado está en (2, −1).
- 🐞 **`sa_functions.py`: el enfriamiento es demasiado rápido para 100 000 iteraciones.** Con T ← 0.8·T, T < 10⁻⁸ tras ~105 iteraciones y llega a 0.0 (underflow) tras unas 3 400; desde ahí `np.exp(-delta / temperature)` divide por cero (RuntimeWarning) y el algoritmo se vuelve *hill climbing* puro. Para Rastrigin conviene un factor como 0.999–0.9999 o menos iteraciones.
- `objective_f2` (Ackley) está definida pero no se usa.
