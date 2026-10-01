---
title: "Homework 01 — Search Methods, Games and Heuristics"
type: assignment
tags: [assignment, search, games, csp, python]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Homework 01 — Search Methods, Games and Heuristics (Deber 1 — Búsqueda, juegos y heurísticas)

> **Summary (EN):** Homework 01 (USFQ, semester 202610) has one research question (Chess vs. Go: state of the art, algorithms, complexity, and whether BFS/DFS/minimax/alpha-beta apply) and six exercises: 8-tile (BFS, DFS, best-first with Euclidean, Manhattan and a free heuristic), 80-tile, N-Queens, farmer–wolf–goat–cabbage, missionaries–cannibals, and Sudoku (naive backtracking plus at least two of MRV, LCV and forward checking, with a metrics table and a solution counter). Isaac's Python file covers all six exercises. Run on the official boards, forward checking cut the hard board from 335,637 assignments (naive) to 309.

## Ficha

| Campo | Valor |
|---|---|
| Enunciado | [raw/assignments/001-HW01 (1) (1).pdf](../../raw/assignments/001-HW01%20%281%29%20%281%29.pdf) (4 páginas) |
| Código entregado | [raw/assignments/isaac_espinosa_deber1_ia_final (1).py](../../raw/assignments/isaac_espinosa_deber1_ia_final%20%281%29.py) (1257 líneas, export de Colab) |
| Ejercicio relacionado | [A\* vs. Dijkstra](astar-vs-dijkstra.md) |
| Unidad | 2 — Búsqueda, juegos, CSP |
| Evaluación | Informe 20 % + **defensa presencial 80 %** (en horas de oficina, una semana después de la entrega) |
| ⚠️ Política de IA | IA generativa **solo en modo chat**, con transcripción obligatoria. **Agentes de IA prohibidos para cualquier tarea → nota 0.** Esta página se completó *después* de calificada la tarea, por decisión de Isaac, como material de estudio. |

## Enunciado

**Pregunta de investigación — Chess vs. Go.** Estado del arte en ambos juegos, algoritmos más avanzados para jugar/entrenar, ¿qué es similar?, ¿qué es diferente?, complejidad computacional de cada uno, ¿se pueden usar BFS, DFS, minimax o alpha-beta?

**Ejercicios**

1. **8-Tile.** Generar el árbol/grafo de movimientos y encontrar el camino del estado inicial a la meta con (a) BFS, (b) DFS, (c) best-first con (i) distancia euclidiana, (ii) Manhattan, (iii) una heurística libre.
2. **80-Tile.** Tablero 9×9 de cuadrantes A–I con fichas 1–9 por cuadrante (no existe la ficha 9I: es el hueco). Llegar a la configuración final (cuadrantes en espiral `A B C / H I D / G F E`, y cada cuadrante ordenado `1 2 3 / 8 9 4 / 7 6 5`) con **el menor número de movimientos explorando la menor cantidad de estados**. Mostrar parte del árbol explorado, estados generados, estados analizados y longitud del camino.
3. **8-Queens.** Programa en un lenguaje imperativo que resuelva N reinas en N×N (backtracking).
4. **Granjero, lobo, cabra y col.** Modelar y encontrar los pasos que no violan las restricciones.
5. **Misioneros y caníbales.** 3 + 3, bote de capacidad 2; nunca menos misioneros que caníbales en una orilla (si hay misioneros).
6. **Sudoku como CSP.** Variables = celdas vacías, dominio {1..9}, restricciones de filas, columnas y cajas. Backtracking leyendo el tablero de un archivo (`0` o `.` = vacío). Resolver los dos tableros dados; implementar la versión ingenua y **al menos dos** de: (a) MRV, (b) Least Constraining Value, (c) forward checking y/o *naked/hidden singles*. Reportar asignaciones, backtracks, profundidad máxima y tiempo en una tabla y explicar por qué cambian. Responder: ¿cuántos tableros examinaría *generate-and-test* en el peor caso y por qué backtracking es mucho mejor? Contar todas las soluciones para verificar que cada tablero tiene exactamente una.

**Tableros oficiales** (`.` = vacío):

```
Board 1 (30 givens)        Board 2 (22 givens)
53..7....                  85...24..
6..195...                  72......9
.98....6.                  ..4......
8...6...3                  ...1.7..2
4..8.3..1                  3.5...9..
7...2...6                  .4.......
.6....28.                  ....8..7.
...419..5                  .17......
....8..79                  ....36.4.
```

## Qué se implementó (cobertura del enunciado)

| Parte | Pedido | Implementado | ✓ |
|---|---|---|---|
| Investigación | Chess vs. Go | No está en el código (iba en el PDF del informe, no incluido en `raw/`) | — |
| 1 | BFS, DFS, best-first ×3 | BFS, DFS (límite 10), best-first con Euclidean, Manhattan y **misplaced tiles** (heurística libre) | ✅ |
| 2 | Camino corto con pocos estados; árbol parcial y métricas | Greedy best-first + Manhattan; imprime los primeros 20 nodos explorados, generados, analizados y el camino | ✅ (greedy no garantiza el camino más corto) |
| 3 | N reinas genérico | Backtracking por columnas, N por `input()` | ✅ |
| 4 | Granjero | BFS con `safe` | ✅ |
| 5 | Misioneros | BFS | ✅ |
| 6 | Sudoku ingenuo + ≥2 mejoras + métricas + conteo | Ingenuo, MRV, forward checking (+MRV), conteo de soluciones, lectura desde archivo | ✅ |

## Resultados (ejecutado el 2026-10-01)

**8-tile** — inicio `(2,4,3,1,0,6,7,5,8)`, meta `(1,2,3,4,5,6,7,8,0)`

| Algoritmo | Movimientos | Estados generados |
|---|---|---|
| BFS | 6 (óptimo) | 135 |
| DFS (max_depth = 10) | 10 | 484 |
| Best-first Manhattan | 6 | **15** |
| Best-first Euclidean | 6 | 20 |
| Best-first misplaced tiles | 6 | 20 |

**80-tile:** la instancia es resoluble (verificado por paridad), pero no terminó en 90 s.

**Granjero:** 7 cruces (óptimo). **Misioneros y caníbales:** 11 cruces (óptimo).

**Sudoku — tableros oficiales**

| Tablero | Método | Asignaciones | Backtracks | Prof. máx. | Tiempo |
|---|---|---|---|---|---|
| 1 (30 dados, 51 vacías) | Ingenuo | 4 208 | 4 157 | 51 | 27 ms |
| 1 | MRV | 51 | 0 | 51 | 9 ms |
| 1 | Forward checking (+MRV) | 51 | 0 | 51 | 1 ms |
| 2 (22 dados, 59 vacías) | Ingenuo | **335 637** | 335 578 | 59 | 2 094 ms |
| 2 | MRV | 4 036 | 3 977 | 59 | 914 ms |
| 2 | Forward checking (+MRV) | **309** | 250 | 59 | **4 ms** |

Ambos tableros: exactamente **1 solución** (contador de soluciones).

## Respuestas de estudio (para la defensa y el examen)

**¿Por qué cambian los números?**
- *Ingenuo* elige la siguiente celda vacía en orden fijo: si se equivoca temprano, descubre el error muchos niveles después → enormes subárboles inútiles.
- *MRV* (*fail-first*) asigna primero la celda más restringida; en el tablero 1 siempre hay una celda con un único valor legal, por eso 0 backtracks.
- *Forward checking* elimina valores de los vecinos tras cada asignación y detecta un dominio vacío **antes** de bajar en la recursión → poda ramas enteras. Además, mantener los dominios evita recalcular los valores legales, por eso es el más rápido.
- La profundidad máxima = número de celdas vacías (51 y 59): toda solución asigna cada variable una vez.

**Generate-and-test en el peor caso:** 9^(celdas vacías) tableros → tablero 1: 9⁵¹ ≈ 4.6 × 10⁴⁸; tablero 2: 9⁵⁹ ≈ 2.0 × 10⁵⁶. Backtracking es mejor porque **comprueba las restricciones en cada asignación parcial** y descarta de una vez todos los tableros que comparten un prefijo inválido (si una asignación parcial viola una restricción, se eliminan 9^(restantes) tableros sin generarlos). Es la misma diferencia "generate & test vs. test as you go" de [N-Queens](../concepts/n-queens.md).

**Chess vs. Go (resumen de conceptos; conocimiento general, a confirmar con AIMA cap. 6):**

| | Ajedrez | Go (19×19) |
|---|---|---|
| Factor de ramificación | ~35 | ~250 |
| Longitud típica | ~80 plies | ~150–200 jugadas |
| Espacio de estados | ~10⁴⁴–10⁴⁷ posiciones | ~2.1 × 10¹⁷⁰ posiciones legales |
| Árbol de juego | ~10¹²³ (número de Shannon ~10¹²⁰) | ~10³⁶⁰ |
| Hito | Deep Blue vence a Kasparov (1997): alpha-beta + evaluación manual + hardware dedicado | AlphaGo vence a Lee Sedol (2016): MCTS + redes de política y valor |
| Estado del arte | Stockfish (alpha-beta + red NNUE); AlphaZero / Leela (MCTS + red profunda, auto-juego) | AlphaGo Zero, AlphaZero, MuZero, KataGo (MCTS + redes, aprendizaje por refuerzo) |

- *Similar:* ambos son de suma cero, deterministas, de información perfecta → en teoría minimax los resuelve.
- *Diferente:* en Go el factor de ramificación y la dificultad de escribir una buena función de evaluación hacen inviable alpha-beta con profundidad útil; por eso triunfó MCTS + redes neuronales.
- *¿BFS/DFS/minimax/alpha-beta?* En principio sí (juegos finitos), en la práctica no hasta el final: BFS/DFS no modelan al rival; minimax completo es O(b^m) ≈ imposible. En ajedrez funciona **alpha-beta con corte de profundidad + función de evaluación**; en Go hace falta **MCTS**.

## Revisión

**Fortalezas**
- Cubre los seis ejercicios y compara algoritmos con métricas reales, como pide el enunciado.
- El Sudoku cumple todo: lectura desde archivo, ingenuo + 2 mejoras, tabla de métricas y conteo de soluciones; los números muestran claramente el efecto de MRV y forward checking.

**Puntos a mejorar**
1. **80-tile:** el enunciado pide el **camino más corto** con pocos estados; greedy best-first no garantiza el más corto. A\* (óptimo, más estados) o A\* ponderado / IDA\* con Manhattan + *linear conflict* responden mejor al pedido. Además, guardar el camino completo en cada nodo (`camino_actual + [mov]`) consume mucha memoria; mejor un diccionario de padres.
2. **DFS con límite + `visited` global puede perder soluciones** dentro del límite (un estado visto primero a mayor profundidad bloquea un camino más corto). Solución: guardar la profundidad mínima de cada estado o chequear ciclos solo en el camino actual (como IDS).
3. **Best-first recorre toda la frontera** en cada paso (O(n)); con `heapq` es O(log n).
4. Funciones redefinidas (`get_successors`, `bfs`, `main`) por concatenar celdas de Colab; N-Reinas usa `input()` y bloquea la ejecución no interactiva.

## Conceptos relacionados

- [Problem Formulation](../concepts/problem-formulation.md)
- [Uninformed Search](../concepts/uninformed-search.md)
- [Heuristics](../concepts/heuristics.md)
- [Greedy Best-First Search](../concepts/greedy-best-first-search.md)
- [A* Search](../concepts/a-star-search.md)
- [Adversarial Search and Minimax](../concepts/adversarial-search-minimax.md)
- [Constraint Satisfaction Problems](../concepts/constraint-satisfaction-problems.md)
- [N-Queens](../concepts/n-queens.md)
