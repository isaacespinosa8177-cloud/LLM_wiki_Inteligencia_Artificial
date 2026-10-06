---
title: "Tic-tac-toe 4×4 with depth-limited Minimax"
type: assignment
tags: [assignment, games, minimax, python]
sources: [slides-02-problem-solving]
updated: 2026-10-01
---
# Tic-tac-toe 4×4 with depth-limited Minimax (Tres en raya 4×4 con Minimax)

> **Summary (EN):** An interactive 4×4 tic-tac-toe where the human plays O and the AI plays X using Minimax cut off at depth 4 with an open-lines heuristic, "because full minimax is too large". The game works, but terminal wins are scored ±1 while the heuristic can exceed 1, so the AI sometimes prefers a "promising" position over an immediate win — confirmed in 2 of 54 random test positions. Scoring wins as ±1000 fixes it; alpha–beta pruning would allow deeper search.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/assignments/tic_tac_toe_4x4_isaac (2).py](../../raw/assignments/tic_tac_toe_4x4_isaac%20%282%29.py) |
| Lenguaje | Python 3 (export de Colab), identificadores en español |
| Unidad | 2 — Búsqueda adversarial |
| ⚠️ Política de IA | Desconocida: el enunciado no está en `raw/`. Revisión añadida tras la entrega (2026-10-01). Si agregas el enunciado, la IA debe verificar su política. |

## Qué se implementó

- Tablero de 16 casillas; 10 líneas ganadoras (4 filas, 4 columnas, 2 diagonales).
- `evaluar`: +1 si gana X, −1 si gana O, 0 si no.
- `evaluar_heuristica`: por cada línea que solo tiene X suma el nº de X; si solo tiene O, resta el nº de O (rango aproximado −30…+30).
- `minimax(tablero, es_turno_de_X, profundidad)` con corte en `MAX_PROFUNDIDAD = 4`, devuelve (valor, movimiento).
- Bucle de juego con validación de entrada (1–16).

## Resultados (prueba automática, 2026-10-01)

Se generaron posiciones aleatorias (4 O, 3 X, turno de X) en las que X **puede ganar en una jugada**:

| Posiciones probadas | La IA no tomó la victoria |
|---|---|
| 54 | **2** |

Ejemplo: tablero `OO.X..X.O...XO..` (fila por fila, `.` = vacío). Ganar en la casilla 9 vale +1, pero la IA eligió la 5 con valor heurístico **2**.

## Revisión

**Fortalezas**
- Estructura clara (mostrar, ganador, lleno, evaluar, minimax, jugar).
- Buena idea de heurística (líneas abiertas) y corte por profundidad justificado en un comentario.
- Manejo de entrada inválida.

**Bug principal: escala de valores**
Los valores terminales deben dominar a cualquier valor heurístico ([Minimax](../concepts/adversarial-search-minimax.md)). Arreglo mínimo:

```python
WIN = 1000

def evaluar(tablero):
    ganador = hay_ganador(tablero)
    if ganador == 'X': return WIN
    if ganador == 'O': return -WIN
    return 0

# in minimax: check  abs(puntaje) == WIN  instead of == 1 / == -1,
# and optionally return WIN - (MAX_PROFUNDIDAD - profundidad) to prefer faster wins
```

**Otras mejoras**
1. Añadir [alpha–beta](../concepts/alpha-beta-pruning.md): mismo resultado, permite profundidad ~6–8 en el mismo tiempo.
2. Ordenar movimientos (centro primero) para que la poda sea más efectiva.
3. Preferir victorias rápidas y derrotas lentas (restar/sumar la profundidad).

## Conceptos relacionados

- [Adversarial Search and Minimax](../concepts/adversarial-search-minimax.md)
- [Alpha–Beta Pruning](../concepts/alpha-beta-pruning.md)
- [Heuristics](../concepts/heuristics.md)
