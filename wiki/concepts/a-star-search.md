---
title: A* Search
type: concept
tags: [search, informed-search, a-star]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-07
---
# A* Search (Búsqueda A*)

> **Summary (EN):** A* expands the node with the lowest f(n) = g(n) + h(n), where g is the actual cost so far and h the heuristic estimate to the goal; f estimates the total cost of the cheapest solution through n. With an admissible heuristic (tree search) or a consistent one (graph search), A* is complete and optimal. Its weakness is memory: it keeps every generated node, O(b^d). On the Romania map it finds the 418 km route Arad–Sibiu–Rimnicu Vilcea–Pitesti–Bucharest expanding 5 nodes, versus 9 for Dijkstra.

> **En palabras simples (ES):** A\* elige el lugar que tiene el **mejor total estimado del viaje**: lo que ya caminé (g) + lo que creo que me falta (h). Es como greedy, pero sin olvidar lo que ya pagaste. Si la estimación h nunca exagera, el primer camino a la meta que A\* **saca** de la lista es el más barato. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| g(n) | g(n) | Costo real acumulado desde el inicio hasta n. |
| h(n) | h(n) | Estimación heurística del menor costo de n a la meta. |
| f(n) = g(n) + h(n) | f(n) | Costo total estimado de la solución que pasa por n. |
| Admissible / Consistent | Admisible / Consistente | Ver [Heuristics](heuristics.md). |
| Optimally efficient | Óptimamente eficiente | Cualquier algoritmo que use la misma h y extienda caminos desde el inicio debe expandir al menos los nodos que A\* expande seguro. |
| Contour | Contorno | Región con f(n) ≤ c; A\* se expande en bandas de f creciente. |
| Weighted A\* | A\* ponderado | f = g + W·h, W > 1: más rápido, solución ≤ W·C\*. |
| IDA\*, RBFS, SMA\* | — | Versiones de A\* con memoria limitada. |

## Explicación

**Intuición.** A\* no solo mira qué tan cerca *parece* estar la meta (h, como greedy), sino también cuánto ya costó llegar (g, como Dijkstra). Combina lo mejor de ambos.

**Propiedades (slides 02, s14):**
- **Completo:** si existe solución y h es admisible (y además *b* finito, costos ≥ ε > 0).
- **Óptimo:** si h es admisible (AIMA 4e, cuyo best-first reabre estados cuando encuentra un camino más barato). Si la implementación **nunca reabre** estados ya expandidos (como la de la tarea), hace falta h **consistente**. Ver [Heuristics](heuristics.md).
- **Espacio:** O(b^d) — guarda todos los nodos en memoria. Es su principal limitación.
- **Tiempo:** depende de la calidad de h.

```
function A-STAR(problem, h):
    g[start] ← 0;  f[start] ← h(start)
    frontier ← {start};  explored ← ∅;  parent[start] ← None
    while frontier not empty:
        n ← node in frontier with lowest f
        if goal(n): return reconstruct_path(parent, n)
        frontier.remove(n);  explored.add(n)
        for (m, cost) in neighbors(n):
            if m in explored: continue
            if g[n] + cost < g[m]:
                g[m] ← g[n] + cost
                f[m] ← g[m] + h(m)
                parent[m] ← n
                frontier.add(m)
    return failure
```

Así está implementado `a_estrella()` en la tarea [A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md).

## Ejemplo — Arad → Bucarest (AIMA Fig. 3.18)

| Paso | Expande | f = g + h | Nuevos en la frontera (f) |
|---|---|---|---|
| 1 | Arad | 0 + 366 = 366 | Sibiu 393, Timisoara 447, Zerind 449 |
| 2 | Sibiu | 140 + 253 = 393 | Rimnicu V. 413, Fagaras 415, Oradea 671 (Arad ya explorado) |
| 3 | Rimnicu Vilcea | 220 + 193 = 413 | Pitesti 417, Craiova 526 |
| 4 | Fagaras | 239 + 176 = 415 | Bucharest 450 |
| 5 | Pitesti | 317 + 100 = 417 | **Bucharest mejora a 418** (Craiova sigue en 526) |
| 6 | Bucharest | 418 + 0 = 418 | ✅ meta |

Observa el paso 4–5: Bucarest entra con f = 450 vía Fagaras, pero A\* **no** se detiene al *generar* la meta; se detiene al *expandirla*. Antes expande Pitesti (417 < 450) y encuentra el camino de 418. Por eso es óptimo.

Resultado real de la tarea: A\* 5 nodos expandidos, Dijkstra 9, ambos con costo 418.


## Por qué A\* es óptimo (prueba de AIMA §3.5.2)

Supón que A\* devuelve un camino de costo C > C\*. Entonces hay un nodo n en el camino óptimo que no fue expandido. Con g\*(n) y h\*(n) los costos óptimos desde el inicio y hasta la meta:

```
f(n) > C*                 (si no, n se habría expandido antes que la meta de costo C)
f(n) = g(n) + h(n)        (definición)
f(n) = g*(n) + h(n)       (n está en el camino óptimo)
f(n) ≤ g*(n) + h*(n)      (admisibilidad: h(n) ≤ h*(n))
f(n) ≤ C*                 (C* = g*(n) + h*(n))
```

La primera y la última línea se contradicen → A\* solo devuelve caminos óptimos.

## Contornos y eficiencia óptima (AIMA §3.5.3)

- A\* se expande en **bandas concéntricas de f** (contornos 380, 400, 420 en Rumania). UCS tiene contornos "circulares" de g alrededor del inicio; con una buena h, los contornos de A\* se **estiran hacia la meta**.
- A\* expande **todos** los nodos con f(n) < C\* (*surely expanded*), quizá algunos con f(n) = C\*, y **ninguno** con f(n) > C\*.
- Por eso **poda**: Timisoara (447) y Zerind (449) son hijos de Arad pero nunca se expanden, porque la solución de 418 aparece antes.
- Con h consistente, A\* es **óptimamente eficiente**. Pero el número de nodos aún puede ser exponencial en la longitud de la solución.

## Variantes (AIMA §3.5.4–3.5.6)

| Variante | Idea | Garantía |
|---|---|---|
| **Weighted A\*** | f = g + W·h, W > 1 | Solución entre C\* y W·C\*; mucho más rápida (Fig. 3.21: 7× menos estados, camino 5 % más caro) |
| **Beam search** | Mantener solo los k mejores nodos de la frontera | Incompleta y subóptima, pero rápida |
| **IDA\*** | Iterative deepening con límite de **f** (no de profundidad); el nuevo límite es el menor f que excedió el anterior | Óptima, memoria lineal; ≤ C\* iteraciones con costos enteros (≤ 31 en el 8-puzzle) |
| **RBFS** | DFS recursiva que recuerda el f de la mejor alternativa y "retrocede" si lo supera, guardando valores *backed-up* | Óptima con h admisible, memoria lineal; cambia de opinión a menudo |
| **SMA\*** | A\* hasta llenar la memoria; luego borra la hoja con peor f y guarda su valor en el padre | Completa si la solución cabe en memoria; óptima si la óptima es alcanzable |
| **Bidirectional A\*** | Dos fronteras con f₂(n) = max(2g(n), g(n)+h(n)) | Completa y óptima con h admisible; a veces más eficiente |

**Familia de best-first** según la función de evaluación:

| Algoritmo | f(n) | W |
|---|---|---|
| Uniform-cost search | g(n) | 0 |
| A\* | g(n) + h(n) | 1 |
| Weighted A\* | g(n) + W·h(n) | 1 < W < ∞ |
| Greedy best-first | h(n) | ∞ |

### Diagrama

Subgrafo de Rumania usado en la tarea (costos en km; h\_SLD entre paréntesis). Camino óptimo en negrita: 140 + 80 + 97 + 101 = **418**.

```mermaid
flowchart LR
    Arad["Arad (366)"] -- 140 --> Sibiu["Sibiu (253)"]
    Arad -- 118 --> Tim["Timisoara (329)"]
    Arad -- 75 --> Zer["Zerind (374)"]
    Sibiu -- 99 --> Fag["Fagaras (176)"]
    Sibiu -- 151 --> Ora["Oradea (380)"]
    Sibiu -- 80 --> RV["Rimnicu Vilcea (193)"]
    RV -- 146 --> Cra["Craiova (160)"]
    RV -- 97 --> Pit["Pitesti (100)"]
    Cra -- 138 --> Pit
    Fag -- 211 --> Buc["Bucharest (0)"]
    Pit -- 101 --> Buc
    linkStyle 0,5,7,10 stroke-width:4px
```

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** A\* elige el lugar que tiene el **mejor total estimado del viaje**: lo que ya caminé (g) + lo que creo que me falta (h). Es como greedy, pero sin olvidar lo que ya pagaste. Si la estimación h nunca exagera, el primer camino a la meta que A\* **saca** de la lista es el más barato.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| g(n) | lo que ya pagué desde el inicio hasta n (km recorridos) | path cost so far |
| h(n) | lo que creo que falta desde n hasta la meta (línea recta) | heuristic estimate |
| f(n) = g(n) + h(n) | el costo total estimado del viaje si paso por n | estimated total cost |
| Cola de prioridad | lista donde siempre sale el de menor f | priority queue |
| Padre | de qué nodo vine, para reconstruir el camino | parent |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Put the start in a priority queue with g = 0 and f = h(start).
   - *ES:* Pon el inicio; su g es 0, así que su f es solo la estimación.
2. Take the node with the SMALLEST f.
   - *ES:* Saca el que tiene el mejor total estimado.
3. If it is the goal → return the path. Test the goal when you take it out, not when you add it.
   - *ES:* Si es la meta, termina. Ojo: la meta se revisa al **sacarla**; puede estar en la lista con un costo alto y luego aparecer un camino más barato.
4. For each neighbor: new_g = g(node) + step cost. If the neighbor is new or new_g is smaller than its old g → save new_g, f = new_g + h, and the parent; add it to the queue.
   - *ES:* Para cada vecino calcula lo que costaría llegar por aquí. Si es nuevo o es más barato que antes, guárdalo con su nuevo total y anota de dónde vino.
5. Go back to step 2.
   - *ES:* Repite.

**Ejemplo con números:** Arad → Bucarest (f = g + h):
1. Saca Arad: f = 0 + 366 = 366.
2. Saca Sibiu: f = 140 + 253 = 393.
3. Saca Rimnicu Vilcea: f = 220 + 193 = 413.
4. Saca Fagaras: f = 239 + 176 = 415. Aquí aparece Bucarest con f = 450 + 0 = **450**, pero A\* **no** para todavía.
5. Saca Pitesti: f = 317 + 100 = 417. Bucarest mejora a f = 418 + 0 = **418**.
6. Saca Bucarest con 418 → termina. Camino Arad–Sibiu–Rimnicu Vilcea–Pitesti–Bucarest = **418 km** (el óptimo).

**Say it in the exam (EN):** "A* expands the node with the lowest f(n) = g(n) + h(n), where g is the cost already paid and h the estimated cost to the goal, so f estimates the total cost of the best path through n. It is complete and optimal if h is admissible (and consistent when states are never reopened). Its weakness is memory: it keeps every node, O(b^d). On Romania it finds the optimal 418 km route expanding only 5 nodes."

**Dilo así (ES):** "A\* expande el nodo con menor f = g + h: lo ya pagado más lo que se estima que falta. Es completo y óptimo si h es admisible (y consistente si no reabre estados). Su debilidad es la memoria, porque guarda todos los nodos. En Rumania encuentra la ruta óptima de 418 km expandiendo solo 5 nodos."

## Errores comunes y tips de examen

- **Probar la meta al expandir, no al generar** — si no, se pierde la optimalidad (el 450 vía Fagaras).
- Con h = 0, A\* = UCS/Dijkstra. Con f = h, es greedy.
- Si h sobreestima, A\* puede devolver una solución subóptima (pero a veces más rápido: *weighted A\**).
- Complejidad espacial exponencial → variantes con memoria limitada: IDA\*, RBFS, SMA\* (tabla arriba).
- Si te piden *probar* la optimalidad, usa la contradicción de 5 líneas de arriba.

## Relacionado

- [Heuristics](heuristics.md)
- [Greedy Best-First Search](greedy-best-first-search.md)
- [Uninformed Search](uninformed-search.md) (UCS/Dijkstra)
- [A* vs Dijkstra assignment](../assignments/astar-vs-dijkstra.md)
- [Search algorithms comparison](../study/search-algorithms-comparison.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 14–15.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §3.5 y Fig. 3.18 (ingestado: prueba de optimalidad, contornos, eficiencia óptima, weighted A\*, IDA\*, RBFS, SMA\*, bidireccional; traza verificada ejecutando la tarea).
