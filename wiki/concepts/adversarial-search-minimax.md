---
title: Adversarial Search and Minimax
type: concept
tags: [search, games, adversarial-search, minimax]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Adversarial Search and Minimax (Búsqueda adversarial y Minimax)

> **Summary (EN):** In games, two or more agents have opposing goals, so the task is to find an optimal strategy assuming the opponent also plays optimally. For two-player, zero-sum, deterministic, perfect-information games, Minimax defines the value of a node recursively: utility at terminal states, max over successors on MAX's turn and min on MIN's turn. It explores the full tree (time O(b^m), space O(b·m)); real games cut off at a depth limit and use a heuristic evaluation function.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Adversarial search | Búsqueda adversarial | Búsqueda con oponente. |
| MAX / MIN | MAX / MIN | Jugador que maximiza / minimiza el valor. |
| Zero-sum | Suma cero | Lo que gana uno lo pierde el otro. |
| Perfect information | Información perfecta | Entorno totalmente observable. |
| Utility / terminal test | Utilidad / prueba terminal | Valor de un estado final / ¿terminó el juego? |
| Ply | Ply (media jugada) | Un movimiento de un jugador. |
| Evaluation function | Función de evaluación | Estimación heurística del valor de un estado no terminal. |
| Cutoff / depth limit | Corte / límite de profundidad | Dejar de buscar a cierta profundidad. |

## Explicación

**De caminos a estrategias.** Hasta ahora un solo agente buscaba un camino. En un juego, el resultado depende también de lo que haga el rival; buscamos la **mejor jugada suponiendo que el rival juega óptimamente**.

**Valor minimax:**

```
MINIMAX(s) =
    UTILITY(s)                                   if TERMINAL(s)
    max over a of MINIMAX(RESULT(s, a))          if PLAYER(s) = MAX
    min over a of MINIMAX(RESULT(s, a))          if PLAYER(s) = MIN
```

```python
def minimax(state, maximizing, depth):
    if terminal(state):  return utility(state)
    if depth == 0:       return evaluate(state)       # heuristic cutoff
    values = [minimax(result(state, a), not maximizing, depth - 1)
              for a in actions(state)]
    return max(values) if maximizing else min(values)
```

- Supone que ambos juegan de forma óptima.
- Explora el árbol completo hasta los nodos terminales: tiempo **O(b^m)**, espacio **O(b·m)** (DFS).
- Para juegos reales (ajedrez b ≈ 35, m ≈ 80) es imposible: se corta a una profundidad y se usa una **función de evaluación** (complemento, AIMA §6.3).

**Función de evaluación del tic-tac-toe 4×4 (tarea):** para cada línea (4 filas, 4 columnas, 2 diagonales), si solo tiene X suma el número de X; si solo tiene O, resta el número de O. Es la idea clásica de "líneas abiertas".

⚠️ **Regla de oro:** los valores terminales deben **dominar** a cualquier valor heurístico. Si ganar vale +1 pero una posición no terminal puede valer +2, el agente prefiere la posición "prometedora" a ganar. Esto ocurre en la [tarea 4×4](../assignments/tic-tac-toe-4x4-minimax.md) (verificado: la IA no tomó una victoria inmediata en 2 de 54 posiciones de prueba). Solución: ganar = +1000 (o +1000 − profundidad para preferir victorias rápidas).

## Errores comunes y tips de examen

- Minimax es **DFS**: por eso el espacio es lineal O(b·m) aunque el tiempo sea exponencial.
- MAX elige el máximo **de los valores de sus hijos**, que son nodos MIN (y viceversa).
- Con corte por profundidad, el resultado ya no es el minimax "verdadero", sino una aproximación que depende de la evaluación.
- Mejora directa: [Alpha–Beta Pruning](alpha-beta-pruning.md) (mismo resultado, menos nodos).

## Relacionado

- [Alpha–Beta Pruning](alpha-beta-pruning.md)
- [Tic-tac-toe 4×4 assignment](../assignments/tic-tac-toe-4x4-minimax.md)
- [Task Environments](task-environments.md) (multiagente competitivo)
- [Uninformed Search](uninformed-search.md) (DFS)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 17–19.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.1–6.3 (función de evaluación y corte: complemento).
