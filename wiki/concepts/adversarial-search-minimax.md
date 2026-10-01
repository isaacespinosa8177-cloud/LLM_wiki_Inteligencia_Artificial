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

**Definición formal de un juego (AIMA §6.1):** S₀ (estado inicial), TO-MOVE(s) (a quién le toca), ACTIONS(s), RESULT(s, a), IS-TERMINAL(s) (prueba terminal) y UTILITY(s, p) (en ajedrez 1, 0 o ½). Los juegos más estudiados son **deterministas, de dos jugadores, por turnos, de información perfecta y de suma cero**. El árbol de tic-tac-toe tiene < 9! = 362 880 hojas (5 478 estados distintos); el de ajedrez > 10⁴⁰ nodos.

**De caminos a estrategias.** Hasta ahora un solo agente buscaba un camino. En un juego, el resultado depende también de lo que haga el rival; buscamos la **mejor jugada suponiendo que el rival juega óptimamente**.

**Valor minimax:**

```
MINIMAX(s) =
    UTILITY(s, MAX)                              if IS-TERMINAL(s)
    max_a MINIMAX(RESULT(s, a))                  if TO-MOVE(s) = MAX
    min_a MINIMAX(RESULT(s, a))                  if TO-MOVE(s) = MIN
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
- Para juegos reales es imposible: ajedrez b ≈ 35, ~80 plies → 35⁸⁰ ≈ **10¹²³** estados.
- La estrategia de MAX es un **plan condicional** (una respuesta para cada jugada de MIN): minimax generaliza el [AND–OR search](search-in-complex-environments.md) (MAX ≈ OR, MIN ≈ AND).
- Si MIN no juega óptimo, MAX obtiene **al menos** el valor minimax (puede ser mejor arriesgar contra un rival débil).

**Ejemplo de AIMA (Fig. 6.2), árbol de 2 plies:** MAX tiene a₁, a₂, a₃ que llevan a nodos MIN B, C, D con hojas B = {3, 12, 8}, C = {2, 4, 6}, D = {14, 5, 2}. Valores MIN: B = 3, C = 2, D = 2 → la raíz vale max(3, 2, 2) = **3** y la decisión minimax es **a₁**.

**Juegos de más de dos jugadores (§6.2.2):** cada nodo guarda un **vector** de utilidades ⟨v_A, v_B, v_C⟩ y cada jugador elige el hijo que maximiza su componente. Surgen **alianzas** de forma natural (dos débiles contra uno fuerte).

### Heuristic minimax: cortar y evaluar (AIMA §6.3)

```
H-MINIMAX(s, d) =
    EVAL(s, MAX)                                   if IS-CUTOFF(s, d)
    max_a H-MINIMAX(RESULT(s, a), d + 1)           if TO-MOVE(s) = MAX
    min_a H-MINIMAX(RESULT(s, a), d + 1)           if TO-MOVE(s) = MIN
```

- **Función de evaluación:** rápida de calcular, fuertemente correlacionada con la probabilidad de ganar, EVAL = UTILITY en estados terminales y, en los demás, entre perder y ganar. La forma típica es una **función lineal ponderada**: EVAL(s) = w₁f₁(s) + … + wₙfₙ(s) (en ajedrez: peón 1, caballo/alfil 3, torre 5, reina 9). Supone que las características son **independientes**; los programas modernos usan combinaciones no lineales y pesos aprendidos.
- **Valor esperado por categorías:** si 82 % de los finales "2 peones vs 1" se ganan, 2 % se pierden y 16 % son tablas: 0.82·1 + 0.02·0 + 0.16·½ = **0.90**.
- **Cutoff test:** profundidad fija o, mejor, **iterative deepening** (devuelve la jugada de la búsqueda completa más profunda cuando se acaba el tiempo).
- **Quiescence search:** solo evaluar posiciones **quietas** (sin una captura pendiente que cambie todo); si no, seguir buscando (p. ej. solo capturas).
- **Horizon effect:** el programa "empuja" una pérdida inevitable más allá de su horizonte con jugadas dilatorias (sacrificar peones para salvar un alfil condenado). Mitigación: **singular extensions**.
- **Forward pruning (Type B):** descartar jugadas que parecen malas (beam search, **ProbCut**, *late move reduction*); ahorra tiempo pero puede errar. Alpha–beta, en cambio, solo poda lo que *demostradamente* no importa.
- **Tablas de aperturas y finales:** en vez de buscar, consultar. Los finales con ≤ 7 piezas están resueltos por **análisis retrógrado**.

Rendimiento en ajedrez (AIMA): minimax con 10⁶ nodos/s llega a ~5 plies (lo vence un jugador promedio); alpha–beta + tabla de transposiciones llega a ~14 plies (nivel experto); Stockfish supera los 30 plies.

**Función de evaluación del tic-tac-toe 4×4 (tarea):** para cada línea (4 filas, 4 columnas, 2 diagonales), si solo tiene X suma el número de X; si solo tiene O, resta el número de O. Es la idea clásica de "líneas abiertas".

⚠️ **Regla de oro:** los valores terminales deben **dominar** a cualquier valor heurístico. Si ganar vale +1 pero una posición no terminal puede valer +2, el agente prefiere la posición "prometedora" a ganar. Esto ocurre en la [tarea 4×4](../assignments/tic-tac-toe-4x4-minimax.md) (verificado: la IA no tomó una victoria inmediata en 2 de 54 posiciones de prueba). Solución: ganar = +1000 (o +1000 − profundidad para preferir victorias rápidas).

## Errores comunes y tips de examen

- Minimax es **DFS**: por eso el espacio es lineal O(b·m) aunque el tiempo sea exponencial.
- MAX elige el máximo **de los valores de sus hijos**, que son nodos MIN (y viceversa).
- Con corte por profundidad, el resultado ya no es el minimax "verdadero", sino una aproximación que depende de la evaluación.
- Mejora directa: [Alpha–Beta Pruning](alpha-beta-pruning.md) (mismo resultado, menos nodos). Alternativa sin evaluación: [MCTS](monte-carlo-tree-search.md).
- El espacio es O(b·m) si se generan todas las acciones a la vez, **O(m)** si se generan de a una (backtracking).
- "Zero-sum" en ajedrez: técnicamente *constant-sum* (1 + 0 o ½ + ½).

## Relacionado

- [Monte Carlo Tree Search](monte-carlo-tree-search.md)
- [Stochastic and Partially Observable Games](stochastic-and-partially-observable-games.md)
- [Alpha–Beta Pruning](alpha-beta-pruning.md)
- [Tic-tac-toe 4×4 assignment](../assignments/tic-tac-toe-4x4-minimax.md)
- [Task Environments](task-environments.md) (multiagente competitivo)
- [Uninformed Search](uninformed-search.md) (DFS)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 17–19.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.1–6.3 (ingestado: definición de juego, Fig. 6.2, multijugador, H-MINIMAX, evaluación, quiescence, horizonte, forward pruning, tablas).
