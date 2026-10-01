---
title: Alpha–Beta Pruning
type: concept
tags: [search, games, adversarial-search]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Alpha–Beta Pruning (Poda alfa–beta)

> **Summary (EN):** Alpha–beta pruning returns exactly the same decision as Minimax while skipping branches that cannot influence it. α is the best value found so far for MAX (a lower bound) and β the best for MIN (an upper bound); a branch is pruned when its value can no longer fall inside (α, β). With perfect move ordering the time drops from O(b^m) to O(b^(m/2)), effectively doubling the searchable depth.

## Términos clave

| English | Español | Significado |
|---|---|---|
| α (alpha) | α | Mejor valor garantizado para MAX en el camino actual (cota inferior). |
| β (beta) | β | Mejor valor garantizado para MIN en el camino actual (cota superior). |
| Pruning | Poda | No explorar ramas que no pueden cambiar la decisión. |
| Move ordering | Orden de movimientos | Explorar primero las mejores jugadas maximiza la poda. |

## Explicación

**Reglas de poda (slides 02, s20):**
- En un nodo **MIN**, si su valor cae **por debajo de α** → podar (MAX nunca elegiría este camino; ya tiene algo mejor).
- En un nodo **MAX**, si su valor sube **por encima de β** → podar (MIN nunca dejaría llegar aquí).
- Formalmente se poda cuando α ≥ β.

```python
def alphabeta(state, depth, alpha, beta, maximizing):
    if terminal(state) or depth == 0:
        return evaluate(state)
    if maximizing:
        value = float('-inf')
        for a in actions(state):
            value = max(value, alphabeta(result(state, a), depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break            # beta cut-off
        return value
    else:
        value = float('inf')
        for a in actions(state):
            value = min(value, alphabeta(result(state, a), depth-1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break            # alpha cut-off
        return value

# call: alphabeta(root, D, float('-inf'), float('inf'), True)
```

**Intuición (AIMA §6.2.3):** α = "**at least**" (lo mínimo que MAX ya tiene asegurado), β = "**at most**" (lo máximo que MIN dejará). Si un jugador ya tiene una opción mejor en el mismo nivel o más arriba, nunca irá a n; en cuanto sabemos lo suficiente de n para concluirlo, lo podamos.

**Ejemplo de AIMA (Fig. 6.5), el mismo árbol de minimax:** B = {3, 12, 8} → B = 3, la raíz vale ≥ 3. En C la primera hoja vale 2 → C ≤ 2 < 3 → **se podan las otras dos hojas de C**. En D: 14 (D ≤ 14, seguir), 5 (D ≤ 5, seguir), 2 → D = 2. Raíz = max(3, ≤2, 2) = 3. Formalmente: MINIMAX(raíz) = max(min(3,12,8), min(2,x,y), min(14,5,2)) = max(3, z, 2) con z ≤ 2 → no depende de x ni y.

**Ejemplo mínimo.** MAX tiene dos hijos MIN, A y B. A tiene hojas {3, 12, 8} → A = 3, así α = 3. En B la primera hoja vale 2 → B ≤ 2 < α = 3 → las demás hojas de B se podan; MAX elige A sin mirarlas.

**Orden de jugadas y complejidad (AIMA §6.2.4).**
- Orden perfecto: **O(b^(m/2))** → factor de ramificación efectivo **√b** (en ajedrez ~6 en vez de 35): se busca el **doble de profundidad** en el mismo tiempo.
- Orden aleatorio: ≈ O(b^(3m/4)).
- En el ejemplo de la Fig. 6.5 no se pudo podar D porque sus peores hijos (para MIN) salieron primero; si el 2 hubiera salido primero, se podaban los otros dos.
- Ordenamiento simple en ajedrez (capturas, luego amenazas, avances, retrocesos) queda a un factor ~2 del óptimo.
- **Killer move heuristic:** probar primero las jugadas que resultaron mejores antes (por ejemplo en la iteración anterior de *iterative deepening*).
- **Transposition table:** guardar el valor de posiciones ya evaluadas que se alcanzan por distintos órdenes de jugadas (transposiciones); en ajedrez duplica la profundidad alcanzable.

**Aplicación a la tarea.** El tic-tac-toe 4×4 usa minimax puro con profundidad 4 "because full minimax is too large". Con alpha-beta y buen orden se podría buscar a ~profundidad 8 con el mismo costo.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** deja de mirar una rama en cuanto sabes que el rival nunca te dejaría llegar ahí (o que tú nunca la elegirías).

```text
ALPHA-BETA(state, α = −∞, β = +∞):
α = best value MAX can already guarantee ("at least")
β = best value MIN can already guarantee ("at most")
1. Terminal or depth limit → return utility / EVAL.
2. MAX node: v = −∞; for each child:
       v = max(v, ALPHA-BETA(child, α, β)); α = max(α, v);
       if α ≥ β → STOP (prune the remaining children).
   return v
3. MIN node: v = +∞; for each child:
       v = min(v, ALPHA-BETA(child, α, β)); β = min(β, v);
       if α ≥ β → STOP (prune the remaining children).
   return v
```

**Say it in the exam (EN):** "Alpha–beta returns exactly the minimax decision while skipping branches that cannot change it. With perfect move ordering it examines O(b^(m/2)) nodes, so it can search about twice as deep; with random ordering about O(b^(3m/4))."

## Errores comunes y tips de examen

- Alpha–beta **no cambia el resultado** de minimax, solo ahorra trabajo.
- α solo se actualiza en nodos MAX y β en nodos MIN; ambos se **pasan hacia abajo**.
- En el examen, al trazar a mano: escribir [α, β] en cada nodo y tachar las ramas podadas.

## Relacionado

- [Monte Carlo Tree Search](monte-carlo-tree-search.md)
- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Tic-tac-toe 4×4 assignment](../assignments/tic-tac-toe-4x4-minimax.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 20–22.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.2.3–6.2.4 (ingestado: Fig. 6.5, α/β, orden de jugadas, killer moves, tablas de transposición).
