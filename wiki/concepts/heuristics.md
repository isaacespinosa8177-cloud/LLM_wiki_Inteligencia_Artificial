---
title: Heuristics
type: concept
tags: [search, informed-search, heuristics]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# Heuristics (Heurísticas)

> **Summary (EN):** A heuristic h(n) is an estimate of the remaining cost from node n to the goal, such as the straight-line distance on a map (h(goal) = 0, h(n) ≥ 0). It is a guess, not a guarantee, but a good one makes search much faster. A heuristic is admissible if it never overestimates the real remaining cost, and consistent if h(n) ≤ c(n, a, n') + h(n') for every step. Course examples: straight-line distance (Romania), and Manhattan distance, Euclidean distance and misplaced tiles for the 8-puzzle.

> **En palabras simples (ES):** Una heurística es una **estimación** de cuánto falta para llegar a la meta, como la distancia en línea recta en un mapa: no es exacta, pero orienta. La mejor forma de inventar una es resolver una versión **más fácil** del problema (quitando una regla); así la estimación nunca exagera. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Heuristic function h(n) | Función heurística | Mi estimación de cuánto falta desde n hasta la meta. |
| h\*(n) | Costo real restante | Lo que de verdad falta por el mejor camino. |
| Admissible | Admisible | Nunca exagera: h(n) ≤ h\*(n). Es "optimista". |
| Consistent (monotone) | Consistente (monótona) | Al dar un paso, la estimación no baja más que el costo de ese paso: h(n) ≤ c(n,a,n') + h(n'). |
| Dominance | Dominancia | Entre dos admisibles, la que siempre da números más altos (más cerca de la realidad) es mejor. |
| Relaxed problem | Problema relajado | El mismo problema con alguna regla eliminada, más fácil de resolver. |
| Straight-line distance h_SLD | Distancia en línea recta | La heurística del mapa de Rumania: distancia "a vuelo de pájaro" a Bucarest. |

## Explicación

### 1. ¿Qué es una heurística?

La búsqueda "informada" usa una **pista**: un número h(n) que estima cuánto falta desde n hasta la meta. Es como preguntar "¿cuánto falta para llegar?" y que te digan "unos 300 km en línea recta". No es exacto (la carretera da vueltas), pero te orienta.

Dos reglas básicas (slides 02, s11): **h(meta) = 0** (si ya llegaste, no falta nada) y **h(n) ≥ 0** (nunca falta una cantidad negativa).

Una buena heurística **reduce muchísimo** los nodos que se revisan, pero no garantiza el camino correcto por sí sola: es una estimación.

### 2. Admisible: nunca exagera

Una heurística es **admisible** si **nunca dice que falta más de lo que de verdad falta**: h(n) ≤ h\*(n). Es "optimista".

- Ejemplo: la distancia en línea recta a Bucarest **nunca** es mayor que la distancia por carretera, porque la línea recta es el camino más corto posible. Desde Arad: línea recta 366 km, carretera 418 km → 366 ≤ 418 ✓.
- ¿Por qué importa? Porque así [A\*](a-star-search.md) garantiza encontrar el camino más barato.

### 3. Consistente: no "salta" al avanzar

Una heurística es **consistente** si, al dar un paso de n a su vecino n', la estimación no baja más de lo que costó ese paso:

h(n) ≤ c(n, a, n') + h(n')

En palabras: "lo que estimo desde aquí" ≤ "lo que cuesta el paso" + "lo que estimo desde el siguiente". Es la **desigualdad del triángulo**: ir directo nunca es más largo que ir pasando por otro punto.

- Ejemplo: de Arad a Sibiu cuesta 140. h(Arad) = 366 ≤ 140 + h(Sibiu) = 140 + 253 = 393 ✓.
- **Toda heurística consistente es admisible** (pero no al revés).
- Con una h consistente: el valor f = g + h **nunca baja** a lo largo de un camino, y la primera vez que A\* saca un estado ya llegó por el mejor camino (nunca necesita "reabrirlo").

> **¿Cuándo basta admisible y cuándo hace falta consistente?** Si el algoritmo **vuelve a meter** un estado en la frontera cuando encuentra un camino más barato (como el BEST-FIRST-SEARCH de AIMA 4e), basta con **admisible**. Si el algoritmo **nunca vuelve a revisar** un estado ya expandido (lista cerrada clásica, como `a_estrella` de la tarea, que salta los vecinos en `visitados`), hace falta **consistente**. Como h\_SLD es consistente, la tarea es correcta.

### 4. Heurísticas para el 8-puzzle

El 8-puzzle es una cuadrícula de 3×3 con 8 fichas numeradas y un hueco; hay que ordenar las fichas moviéndolas al hueco. Implementadas en [Deber 1](../assignments/deber-1-search-problems.md):

| Heurística | Cómo se calcula (en simple) | ¿Admisible? |
|---|---|---|
| Fichas mal colocadas h₁ (*misplaced tiles*) | Cuenta cuántas fichas no están en su lugar (sin contar el hueco) | Sí: cada ficha mal ubicada necesita al menos 1 movimiento |
| Manhattan h₂ | Para cada ficha suma cuántas filas + cuántas columnas le faltan para llegar a su lugar | Sí: cada movimiento mueve una ficha una sola casilla |
| Euclidiana | Para cada ficha, la distancia en línea recta a su lugar | Sí, pero da números más bajos que Manhattan (es más débil) |

Ejemplo: una ficha que está 2 casillas a la derecha de su lugar suma **1** en h₁ y **2** en Manhattan. Manhattan siempre da números iguales o más altos → **domina** a las otras dos, es la más útil. En la tarea, greedy generó 15 estados con Manhattan y 20 con las otras.

### 5. ¿Cómo saber si una heurística es buena? (AIMA §3.6.1)

**Factor de ramificación efectivo b\*:** si A\* revisó N nodos para una solución de d pasos, b\* es "cuántos hijos por nodo tendría un árbol perfecto de profundidad d con ese mismo número de nodos" (N + 1 = 1 + b\* + (b\*)² + … + (b\*)^d). Ejemplo: d = 5 con 52 nodos → b\* = 1.92. **Cuanto más cerca de 1, mejor la heurística** (significa que casi va directo).

Experimento de AIMA (Fig. 3.26, promedio de 100 8-puzzles por longitud):

| d (pasos) | Nodos BFS | Nodos A\*(h₁) | Nodos A\*(h₂) | b\* BFS | b\* h₁ | b\* h₂ |
|---|---|---|---|---|---|---|
| 14 | 6 783 | 678 | 174 | 1.77 | 1.47 | 1.31 |
| 20 | 91 493 | 9 905 | 1 318 | 1.69 | 1.50 | 1.34 |
| 26 | 395 355 | 110 372 | 10 080 | 1.58 | 1.50 | 1.35 |

**Dominancia:** si h₂(n) ≥ h₁(n) en todos los estados (y las dos son admisibles), A\* con h₂ **nunca revisa más nodos** que con h₁ (salvo empates). La razón: A\* revisa seguro todo nodo con f(n) menor que el costo óptimo; con una h más grande, menos nodos cumplen eso.

### 6. Cómo inventar heurísticas (AIMA §3.6.2–3.6.4)

**1. Problemas relajados (el truco principal).** Quita una regla del problema y resuelve esa versión más fácil; su costo exacto es una heurística **admisible y consistente**. La regla del 8-puzzle es: *"A tile can move from square X to square Y if X is adjacent to Y and Y is blank"* (una ficha se mueve de X a Y si son vecinas y Y está vacía). Quitando partes:
- quitar "si Y está vacía" → cada ficha camina directo a su lugar → **Manhattan** (h₂);
- quitar "si X es vecina de Y" → heurística de Gaschnig (ejercicio del libro);
- quitar las dos condiciones → cada ficha salta directo a su lugar en 1 movimiento → **fichas mal colocadas** (h₁).

El problema fácil tiene que poder resolverse **sin buscar** (aquí son 8 problemas de una ficha cada uno), si no, calcular la heurística costaría demasiado.

**2. Tomar el máximo.** h(n) = el mayor valor entre varias heurísticas. Si todas son admisibles, el máximo también, y es mejor que cada una. El precio: tarda más en calcularse.

**3. Bases de datos de patrones (*pattern databases*)** *(extra).* Guardar el costo exacto de resolver una **parte** del problema (por ejemplo, colocar solo las fichas 1, 2, 3, 4 y el hueco: 15 120 casos), calculado desde la meta hacia atrás. En el 15-puzzle reduce los nodos unas 1000 veces; si las partes no se pisan, se pueden **sumar** y reduce unas 10 000 veces.

**4. Puntos de referencia (*landmarks*)** *(extra).* Precalcular las distancias a unos pocos lugares de referencia. No es admisible, pero es muy precisa; así funcionan los servicios de mapas.

**h\_SLD a Bucarest** (usada en la tarea A\* vs Dijkstra): Arad 366, Bucharest 0, Craiova 160, Fagaras 176, Oradea 380, Pitesti 100, Rimnicu Vilcea 193, Sibiu 253, Timisoara 329, Zerind 374.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Una heurística es una **estimación** de cuánto falta para llegar a la meta, como la distancia en línea recta en un mapa: no es exacta, pero orienta. La mejor forma de inventar una es resolver una versión **más fácil** del problema (quitando una regla); así la estimación nunca exagera.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| h(n) | cuánto **creo** que falta desde n hasta la meta | heuristic estimate |
| h\*(n) | cuánto falta **de verdad** (el costo real más barato) | true remaining cost |
| c(n, n') | costo de ir de n a su vecino n' | step cost |
| Admisible | nunca exagera: h(n) ≤ h\*(n) | admissible |
| Consistente | al dar un paso, la estimación no baja más de lo que cuesta ese paso: h(n) ≤ c(n, n') + h(n') | consistent |
| Domina | entre dos admisibles, la que siempre da valores más altos (más cerca de la realidad) | dominates |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

*How to invent an admissible heuristic*

1. Write the rules of the problem (8-puzzle: a tile can move to an adjacent square only if it is empty).
   - *ES:* Escribe las reglas del problema.
2. Remove a rule to get an easier (relaxed) problem.
   - *ES:* Quita una regla. Si las fichas se pueden mover aunque la casilla esté ocupada → cada ficha necesita tantos pasos como su distancia horizontal + vertical (**Manhattan**). Si además pueden saltar a cualquier lugar → cada ficha mal ubicada necesita 1 paso (**fichas mal colocadas**).
3. Use the exact cost of the easier problem as h(n).
   - *ES:* El costo exacto del problema fácil es tu heurística. Nunca exagera, porque el problema real es más difícil.

*How to check a heuristic*

1. Check that h(goal) = 0 and h(n) ≥ 0.
   - *ES:* En la meta debe valer 0 y nunca ser negativa.
2. Admissible: h(n) ≤ the real cheapest cost from n, for every n.
   - *ES:* ¿Nunca dice que falta **más** de lo que de verdad falta? Si nunca exagera, es admisible.
3. Consistent: h(n) ≤ c(n, n') + h(n') for every step from n to n'.
   - *ES:* Al avanzar un paso, la estimación no puede bajar más que lo que costó ese paso (como la desigualdad del triángulo).
4. Between two admissible heuristics, prefer the one that is always larger (it dominates).
   - *ES:* Entre dos admisibles, usa la más alta: se acerca más a la realidad y A\* revisa menos nodos.

**Ejemplo con números:** Rumania, h = distancia en línea recta a Bucarest. h(Arad) = 366 km y el camino real más corto mide 418 km → 366 ≤ 418, **admisible**. Consistencia en el paso Arad → Sibiu (140 km): 366 ≤ 140 + 253 = 393 ✓. En el 8-puzzle, una ficha que está a 2 casillas de su lugar suma 1 en "mal colocadas" y 2 en Manhattan: Manhattan es más alta, por eso domina.

**Say it in the exam (EN):** "A heuristic h(n) estimates the cost from n to the goal. It is admissible if it never overestimates the real cost, and consistent if h(n) ≤ c(n, n') + h(n') for every step; consistent implies admissible. A good way to build one is to solve a relaxed problem with fewer rules. Between two admissible heuristics, the one that dominates (is always larger) makes A* expand fewer nodes; on the 8-puzzle, Manhattan distance dominates misplaced tiles."

**Dilo así (ES):** "Una heurística h(n) estima cuánto falta desde n hasta la meta. Es admisible si nunca exagera, y consistente si al dar un paso no baja más que el costo de ese paso; consistente implica admisible. Se construye resolviendo una versión más fácil del problema. Entre dos admisibles, la más alta hace que A\* revise menos nodos; en el 8-puzzle, Manhattan domina a fichas mal colocadas."

## Errores comunes y tips de examen

- Admisible **no implica** consistente (al revés sí).
- h = 0 en todos lados es admisible y consistente, pero no ayuda nada: A\* se vuelve UCS/Dijkstra.
- Entre dos heurísticas admisibles, usa la **mayor** (la que domina): revisa menos nodos.
- Si en *fichas mal colocadas* cuentas también el hueco, puede dejar de ser admisible (AIMA define h₁ sin contar el hueco).
- Ejemplo de AIMA Fig. 3.25: h₁ = 8, h₂ = 18 y el costo real es 26 → las dos se quedan cortas, como debe ser.

## Relacionado

- [A* Search](a-star-search.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Uninformed Search](uninformed-search.md)
- [State Representation](state-representation.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 11, 14, 16 (s16 está en imagen).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5–3.6 (ingestado: consistencia, b\*, Fig. 3.26, dominancia, relajación, pattern databases, landmarks).
- [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md), [Deber 1](../assignments/deber-1-search-problems.md).
