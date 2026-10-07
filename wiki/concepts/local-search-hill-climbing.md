---
title: Local Search and Hill Climbing
type: concept
tags: [optimization, local-search, hill-climbing, search]
sources: [book-russell-norvig-aima, code-class-optimization]
updated: 2026-10-07
---
# Local Search and Hill Climbing (Búsqueda local y ascenso de colinas)

> **Summary (EN):** Local search keeps only the current solution (or a few), moves to nearby solutions and never remembers paths, so it uses almost no memory and works in huge spaces where only the final answer matters. Hill climbing always moves to the best neighbor and stops when none is better, so it gets stuck on local maxima, ridges and plateaus; on random 8-queens it solves only 14% of cases. Sideways moves, random variants, random restarts, local beam search and simulated annealing fix this; evolutionary algorithms extend beam search by mixing solutions.

> **En palabras simples (ES):** Es como subir una montaña con niebla: no ves la cima, solo lo que está a un paso. Miras alrededor, das el paso que más sube, y repites. Cuando ningún paso sube, paras. El problema: puedes quedarte en una colina pequeña creyendo que es la montaña más alta. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Local search | Búsqueda local | Ir de una solución a otra parecida, sin guardar caminos. |
| Neighbor | Vecino | Una solución que se obtiene con un cambio pequeño (mover una reina). |
| State-space landscape | Paisaje del espacio de estados | Imaginar cada solución como un punto en un terreno; su altura es qué tan buena es. |
| Complete-state formulation | Formulación de estado completo | Cada estado ya es una solución completa (las 8 reinas ya están en el tablero), aunque sea mala. |
| Hill climbing (steepest ascent) | Ascenso de colinas | Moverse siempre al mejor vecino. |
| Local maximum | Máximo local | Una cima pequeña: más alta que sus vecinos, pero no la más alta de todas. |
| Ridge | Cresta | Una fila de cimas pequeñas difícil de recorrer con pasos simples. |
| Plateau / shoulder | Meseta / hombro | Zona plana; en un hombro todavía se puede seguir subiendo más adelante. |
| Sideways move | Movimiento lateral | Moverse a un vecino igual de bueno (para cruzar zonas planas). |
| Random restart | Reinicio aleatorio | Empezar de nuevo en otro punto al azar. |
| Local beam search | Búsqueda local en haz | Llevar k soluciones a la vez y quedarse con las k mejores. |

## Explicación

### 1. ¿Cuándo sirve la búsqueda local?

Cuando **solo importa la respuesta final, no el camino**: colocar 8 reinas, diseñar circuitos, distribuir una fábrica, hacer horarios, optimizar redes o portafolios.

- **Ventajas:** usa muy poca memoria y encuentra soluciones razonables en espacios gigantes.
- **Desventaja:** no revisa todo de forma ordenada, así que puede no pasar nunca por la zona donde está la solución.

Imagina un terreno: cada punto es una solución y su **altura** es qué tan buena es. Si la altura es algo a **maximizar**, buscamos la cima más alta (hill climbing). Si es un **costo**, buscamos el valle más profundo ([gradient descent](gradient-descent.md)).

### 2. Hill climbing (ascenso de colinas)

El libro lo describe como "subir el Everest con niebla espesa y amnesia": solo ves a un paso y no recuerdas por dónde viniste. Se queda con una solución y se mueve al **vecino de mayor valor**; para cuando ningún vecino es mejor. También se llama **búsqueda local voraz**.

**Ejemplo de AIMA — 8 reinas (§4.1.1):**
- **Estado:** las 8 reinas en el tablero, una por columna.
- **Vecinos:** mover una reina a otra fila **dentro de su columna**: 8 columnas × 7 filas nuevas = **56 vecinos**.
- **h:** número de pares de reinas que se atacan (h = 0 es una solución).
- Desde un tablero con h = 17, en 5 pasos llega a h = 1 (casi resuelto), pero ahí **cualquier movimiento empeora**: se quedó atascado en una cima pequeña.

### 3. ¿Por qué se atasca?

- **Máximos locales:** cimas pequeñas; desde ahí todo baja.
- **Crestas:** filas de cimas pequeñas que no se pueden recorrer con un paso simple.
- **Mesetas:** zonas planas donde todos los vecinos valen igual y no sabe hacia dónde ir. Si es un **hombro**, más adelante se puede volver a subir.

| Versión (8 reinas al azar) | Lo resuelve… | Pasos promedio |
|---|---|---|
| Hill climbing normal | **14 %** de las veces | 4 cuando lo logra, 3 cuando se atasca |
| + hasta 100 movimientos laterales seguidos | **94 %** | 21 cuando lo logra, 64 cuando falla |
| Con reinicios aleatorios (sin laterales) | ~100 % | ≈ 7 reinicios (1/p con p ≈ 0.14), ≈ 22 pasos |
| Con reinicios aleatorios (con laterales) | ~100 % | ≈ 1.06 reinicios, ≈ 25 pasos |

Con reinicios aleatorios, AIMA resuelve **3 millones de reinas** en segundos. Si un intento sale bien con probabilidad p, en promedio necesitas **1/p** intentos.

### 4. Variantes para no atascarse

- **Estocástico:** elige al azar entre los movimientos que suben (los que suben más tienen más probabilidad).
- **Primera opción (*first-choice*):** genera vecinos al azar hasta encontrar uno mejor; útil cuando hay miles de vecinos.
- **Reinicio aleatorio:** "si no funciona, inténtalo otra vez desde otro lugar". Termina encontrando la solución con probabilidad 1.
- **[Recocido simulado](simulated-annealing.md):** a veces acepta bajar para poder salir de una cima pequeña.
- **Búsqueda en haz (*local beam search*):** lleva **k** soluciones a la vez; genera todos sus vecinos y se queda con las k mejores. No es lo mismo que k intentos separados: las soluciones **comparten información** ("¡vengan aquí, el pasto es más verde!"). Problema: todas pueden terminar en el mismo lugar → la versión **estocástica** elige vecinos con probabilidad proporcional a qué tan buenos son.
- **[Algoritmos evolutivos](genetic-algorithms.md):** son una búsqueda en haz estocástica que además **mezcla** soluciones (cruce).

## Pseudocódigo

```
function HILL-CLIMBING(problem) returns a state that is a local maximum
    current ← problem.INITIAL
    while true:
        neighbor ← a highest-valued successor of current
        if VALUE(neighbor) ≤ VALUE(current): return current
        current ← neighbor
```

### Diagrama

Terreno de una dimensión (AIMA Fig. 4.1): hill climbing que empieza a la izquierda se queda en la cima pequeña.

```text
objective
  9 |                               * <- global maximum
  8 |                            *     *
  7 |                         *
  6 |       * <- local maximum
  5 |    *     *           *              *
  4 | *           * * * <- shoulder (flat, but you can still climb later)
  2 *
    +--1--2--3--4--5--6--7--8--9--10--11--12--> state
Hill climbing that starts at state 1 climbs to state 3 and stops there.
```

Estados 1–3: subida hasta un **máximo local** (cima pequeña); 5–7: **hombro** (zona plana desde la que aún se puede subir); 10: **máximo global** (la cima más alta).

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Es como subir una montaña con niebla: no ves la cima, solo lo que está a un paso. Miras alrededor, das el paso que más sube, y repites. Cuando ningún paso sube, paras. El problema: puedes quedarte en una colina pequeña creyendo que es la montaña más alta.

**Antes de empezar: qué significa cada cosa**

| Palabra / símbolo | Qué es (en simple) | English |
|---|---|---|
| Estado actual | la solución donde estoy ahora | current state |
| Vecino | una solución que se obtiene con un cambio pequeño (mover una reina, sumar 1) | neighbor |
| Valor | qué tan buena es una solución (más alto = mejor) | value / objective |
| Máximo local | una cima pequeña: ningún vecino es mejor, pero hay cimas más altas | local maximum |
| Meseta | zona plana: todos los vecinos valen lo mismo | plateau |
| p | probabilidad de que un intento termine bien | success probability |
| k | cuántas soluciones guardo a la vez (búsqueda en haz) | beam width |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

*Hill climbing*

1. Start from some state (often random).
   - *ES:* Empieza en cualquier punto.
2. Look at all neighbors of the current state.
   - *ES:* Mira todos los cambios pequeños posibles.
3. If none is better → stop and return the current state (it is a peak, maybe only a local one).
   - *ES:* Si ninguno mejora, paras: estás en una cima (quizá pequeña).
4. Otherwise move to the best neighbor and go back to step 2.
   - *ES:* Si alguno mejora, ve al mejor y repite.

*Random-restart hill climbing*

1. Repeat hill climbing from new random starting points until you find a goal (or time runs out). On average you need 1/p tries.
   - *ES:* Si te quedas atascado, empieza de nuevo en otro lugar al azar. Si cada intento sale bien con probabilidad p, necesitas en promedio 1/p intentos.

*Local beam search*

1. Keep k states; generate all their neighbors; keep the k best; repeat.
   - *ES:* En vez de una solución, lleva k a la vez y quédate siempre con las k mejores.

**Ejemplo con números:** maximizar f(x) = −(x − 3)², donde x es un entero y los vecinos son x − 1 y x + 1. Empiezo en x = 0 (f = −9) → paso a 1 (f = −4) → a 2 (f = −1) → a 3 (f = 0). Los vecinos 2 y 4 valen −1, no mejoran → **paro en x = 3**. En las 8 reinas al azar, hill climbing solo resuelve el **14 %** de los casos: el resto se atasca en cimas pequeñas. Con reinicios, se necesitan en promedio 1/0.14 ≈ 7 intentos.

**Say it in the exam (EN):** "Hill climbing keeps only the current state and always moves to the best neighbor, stopping when no neighbor is better. It uses almost no memory, but it gets stuck on local maxima, ridges and plateaus — it solves only 14% of random 8-queens instances. Fixes include sideways moves, random restarts, simulated annealing and local beam search."

**Dilo así (ES):** "Hill climbing guarda solo la solución actual y siempre va al mejor vecino; para cuando ninguno es mejor. Usa poquísima memoria, pero se atasca en máximos locales, crestas y mesetas: resuelve solo el 14 % de las 8 reinas al azar. Se mejora con movimientos laterales, reinicios aleatorios, recocido simulado o búsqueda en haz."

## Errores comunes y tips de examen

- Hill climbing **no guarda** frontera ni lista de visitados: memoria casi nula, O(1).
- Qué es una "cima pequeña" depende de qué cuentas como vecino: si cambias los movimientos permitidos, cambian las cimas.
- La búsqueda en haz **no** es lo mismo que k reinicios separados: comparte información entre las k soluciones.
- Los problemas difíciles suelen tener muchísimas cimas pequeñas, pero con unos pocos reinicios normalmente se encuentra una buena.

## Relacionado

- [Optimization Basics](optimization-basics.md)
- [Simulated Annealing](simulated-annealing.md)
- [Genetic Algorithms](genetic-algorithms.md)
- [Gradient Descent](gradient-descent.md)
- [N-Queens](n-queens.md)
- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md) (min-conflicts)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.1 (Figs. 4.1–4.3; estadísticas de 8 reinas).
