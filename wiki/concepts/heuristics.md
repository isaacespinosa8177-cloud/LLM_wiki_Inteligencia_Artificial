---
title: Heuristics
type: concept
tags: [search, informed-search, heuristics]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Heuristics (Heurísticas)

> **Summary (EN):** A heuristic h(n) estimates the cost from node n to the goal (h(goal) = 0, h(n) ≥ 0). It encodes problem knowledge to guide search; it is an estimate, not a guarantee. A heuristic is admissible if it never overestimates the true cost and consistent if h(n) ≤ c(n, a, n') + h(n'). Classic examples from the course: straight-line distance (Romania), and Manhattan distance, Euclidean distance and misplaced tiles for sliding puzzles.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Heuristic function h(n) | Función heurística | Estimación del costo de n al objetivo. |
| Admissible | Admisible | Nunca sobreestima: h(n) ≤ h\*(n). |
| Consistent (monotone) | Consistente (monótona) | h(n) ≤ c(n,a,n') + h(n') (desigualdad triangular). |
| Dominance | Dominancia | h₂ domina a h₁ si h₂(n) ≥ h₁(n) para todo n (ambas admisibles). |
| Relaxed problem | Problema relajado | Versión con menos restricciones; su costo exacto es una heurística admisible. |
| Straight-line distance h_SLD | Distancia en línea recta | Heurística del mapa de Rumania. |

## Explicación

**Idea.** La búsqueda informada usa conocimiento adicional del problema, codificado en h(n). Una buena heurística **reduce drásticamente** los nodos explorados, pero no garantiza por sí sola el camino correcto: es una estimación.

Reglas básicas (slides 02, s11): h(n) = 0 si n es la meta; h(n) ≥ 0 siempre.

**Admisibilidad.** h nunca sobreestima el costo real restante (es *optimista*): h(n) ≤ h\*(n). Es lo que garantiza que [A\*](a-star-search.md) devuelva el óptimo. Ejemplo: la distancia en línea recta a Bucarest nunca es mayor que la distancia por carretera.

**Consistencia (= monotonía).** Para todo n y sucesor n': h(n) ≤ c(n, a, n') + h(n') — es la **desigualdad triangular**. Toda heurística consistente es admisible (no al revés). Con consistencia:
- f = g + h **nunca decrece** a lo largo de un camino (f es monótona ⇔ h es consistente);
- la primera vez que A\* alcanza un estado ya es por un camino óptimo, así que nunca hay que reabrirlo.

> **¿Cuándo basta admisible y cuándo hace falta consistente?** En el BEST-FIRST-SEARCH de AIMA 4e, que **vuelve a agregar** un estado a la frontera si encuentra un camino más barato, basta con admisible. En implementaciones que **nunca reabren** un estado ya expandido (lista cerrada clásica, como `a_estrella` de la tarea, que salta los vecinos en `visitados`), hace falta **consistente** para garantizar el óptimo. h\_SLD es consistente, así que la tarea es correcta.

**Heurísticas para el 8-puzzle** (implementadas en [Deber 1](../assignments/deber-1-search-problems.md)):

| Heurística | Definición | ¿Admisible? |
|---|---|---|
| Misplaced tiles h₁ | Nº de fichas fuera de lugar (sin contar el hueco) | Sí: cada ficha mal ubicada necesita ≥ 1 movimiento |
| Manhattan h₂ | Σ \|fila − fila_meta\| + \|col − col_meta\| por ficha | Sí: cada movimiento mueve una ficha una casilla |
| Euclidean | Σ distancia euclidiana por ficha | Sí, pero más débil: Euclid ≤ Manhattan |

Manhattan **domina** a misplaced tiles y a la euclidiana → es la más informada de las tres. Resultado real: greedy best-first generó 15 estados con Manhattan y 20 con las otras dos.

### Calidad de una heurística: factor de ramificación efectivo (AIMA §3.6.1)

Si A\* genera N nodos para una solución de profundidad d, el **factor de ramificación efectivo** b\* es el que tendría un árbol uniforme de profundidad d con N + 1 nodos: N + 1 = 1 + b\* + (b\*)² + … + (b\*)^d. Ejemplo: d = 5 con 52 nodos → b\* = 1.92. Cuanto más cerca de 1, mejor la heurística.

Experimento de AIMA (Fig. 3.26, promedio de 100 8-puzzles por longitud):

| d | BFS nodos | A\*(h₁) nodos | A\*(h₂) nodos | b\* BFS | b\* h₁ | b\* h₂ |
|---|---|---|---|---|---|---|
| 14 | 6 783 | 678 | 174 | 1.77 | 1.47 | 1.31 |
| 20 | 91 493 | 9 905 | 1 318 | 1.69 | 1.50 | 1.34 |
| 26 | 395 355 | 110 372 | 10 080 | 1.58 | 1.50 | 1.35 |

**Dominancia.** h₂(n) ≥ h₁(n) para todo n → A\* con h₂ **nunca expande más** nodos que con h₁ (salvo empates). Razón: todo nodo con f(n) < C\* se expande seguro, es decir h(n) < C\* − g(n); con una h más grande, menos nodos cumplen eso.

### Cómo inventar heurísticas (AIMA §3.6.2–3.6.4)

**1. Problemas relajados.** Un problema con menos restricciones agrega aristas al grafo; su costo óptimo es una heurística **admisible y consistente** para el original. Regla del 8-puzzle: *"A tile can move from square X to square Y if X is adjacent to Y and Y is blank."* Quitando condiciones:
- (a) "si X es adyacente a Y" → **Manhattan** (h₂).
- (b) "si Y está vacío" → heurística de Gaschnig (ejercicio del libro).
- (c) "de X a Y" sin condiciones → **misplaced tiles** (h₁).

El problema relajado debe poder resolverse **sin búsqueda** (aquí se descompone en 8 subproblemas independientes), si no la heurística sería cara.

**2. Máximo de heurísticas.** h(n) = max{h₁(n), …, h_k(n)}: admisible si todas lo son, consistente si todas lo son, y domina a cada componente. Costo: más tiempo de cálculo.

**3. Pattern databases.** Guardar el costo exacto de resolver un **subproblema** (p. ej. colocar las fichas 1-2-3-4 y el hueco: 9·8·7·6·5 = 15 120 patrones), calculado hacia atrás desde la meta. Combinadas con max reducen los nodos ×1000 en el 15-puzzle; las **disjoint pattern databases** (contando solo los movimientos de las fichas del patrón) permiten *sumar* y reducen ×10 000.

**4. Landmarks.** Precalcular costos óptimos a unos pocos puntos de referencia L: h\_L(n) = min_L C\*(n, L) + C\*(L, meta) (no admisible, pero muy precisa; así funcionan los servicios de rutas).

**h\_SLD a Bucarest** (usada en la tarea A\* vs Dijkstra): Arad 366, Bucharest 0, Craiova 160, Fagaras 176, Oradea 380, Pitesti 100, Rimnicu Vilcea 193, Sibiu 253, Timisoara 329, Zerind 374.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** una buena heurística es el costo exacto de una versión **más fácil** del problema; así nunca sobreestima.

```text
DESIGN AN ADMISSIBLE HEURISTIC:
1. Write the rules of the problem (e.g., "a tile moves to an adjacent blank square").
2. Remove a restriction to get a relaxed problem
   (drop "blank" → Manhattan distance; drop both → misplaced tiles).
3. Use the exact cost of the relaxed problem as h(n).

CHECK A HEURISTIC:
1. h(goal) = 0 and h(n) ≥ 0?
2. Admissible: for every n, is h(n) ≤ the real cheapest cost to the goal?
3. Consistent: for every edge n → n', is h(n) ≤ cost(n, n') + h(n')?
4. Compare two admissible heuristics: the one that is always ≥ (dominates) is better.
```

**Say it in the exam (EN):** "h(n) estimates the cost from n to the goal. Admissible means it never overestimates; consistent means it satisfies the triangle inequality, which implies admissible. A dominating admissible heuristic expands fewer nodes; on the 8-puzzle Manhattan distance dominates misplaced tiles."

## Errores comunes y tips de examen

- Admisible **no implica** consistente (al revés sí).
- h = 0 es admisible y consistente, pero no informa nada: A\* se convierte en UCS/Dijkstra.
- Entre dos heurísticas admisibles, usar la **mayor** (la que domina): expande menos nodos.
- Contar el hueco en *misplaced tiles* puede volverla no admisible (AIMA define h₁ *blank not included*).
- Ejemplo de AIMA Fig. 3.25: h₁ = 8, h₂ = 18, costo real 26 → ambas subestiman, como deben.

## Relacionado

- [A* Search](a-star-search.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Uninformed Search](uninformed-search.md)
- [State Representation](state-representation.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 11, 14, 16 (s16 está en imagen).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5–3.6 (ingestado: consistencia, b\*, Fig. 3.26, dominancia, relajación, pattern databases, landmarks).
- [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md), [Deber 1](../assignments/deber-1-search-problems.md).
