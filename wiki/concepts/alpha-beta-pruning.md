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

**Ejemplo mínimo.** MAX tiene dos hijos MIN, A y B. A tiene hojas {3, 12, 8} → A = 3, así α = 3. En B la primera hoja vale 2 → B ≤ 2 < α = 3 → las demás hojas de B se podan; MAX elige A sin mirarlas.

**Complejidad.** Con orden perfecto O(b^(m/2)); con orden aleatorio ≈ O(b^(3m/4)) (complemento AIMA §6.2.4). El orden de los movimientos importa mucho.

**Aplicación a la tarea.** El tic-tac-toe 4×4 usa minimax puro con profundidad 4 "because full minimax is too large". Con alpha-beta y buen orden se podría buscar a ~profundidad 8 con el mismo costo.

## Errores comunes y tips de examen

- Alpha–beta **no cambia el resultado** de minimax, solo ahorra trabajo.
- α solo se actualiza en nodos MAX y β en nodos MIN; ambos se **pasan hacia abajo**.
- En el examen, al trazar a mano: escribir [α, β] en cada nodo y tachar las ramas podadas.

## Relacionado

- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Tic-tac-toe 4×4 assignment](../assignments/tic-tac-toe-4x4-minimax.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 20–22.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.2.3–6.2.4 (pseudocódigo y orden: complemento).
