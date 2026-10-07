---
title: Local Search and Hill Climbing
type: concept
tags: [optimization, local-search, hill-climbing, search]
sources: [book-russell-norvig-aima, code-class-optimization]
updated: 2026-10-07
---
# Local Search and Hill Climbing (Búsqueda local y ascenso de colinas)

> **Summary (EN):** Local search keeps only the current state (or a few), moves to neighboring states and never remembers paths, so it uses almost no memory and works in huge or infinite spaces where only the final state matters. Hill climbing always moves to the best neighbor and stops at a peak, so it gets stuck on local maxima, ridges and plateaus — on random 8-queens it solves only 14% of instances. Sideways moves, stochastic and first-choice variants, random restarts, local beam search and simulated annealing are the standard fixes; evolutionary algorithms extend stochastic beam search with recombination.

> **En palabras simples (ES):** Es como subir una montaña con niebla: no ves la cima, solo lo que está a un paso. Miras alrededor, das el paso que más sube, y repites. Cuando ningún paso sube, paras. El problema: puedes quedarte en una colina pequeña creyendo que es la montaña más alta. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Local search | Búsqueda local | Va de un estado a sus vecinos sin guardar caminos ni estados alcanzados. |
| State-space landscape | Paisaje del espacio de estados | Cada estado tiene una "elevación" = valor de la función objetivo. |
| Complete-state formulation | Formulación de estado completo | Cada estado ya es una solución candidata completa (8 reinas en el tablero). |
| Hill climbing (steepest ascent) | Ascenso de colinas (máxima pendiente) | Moverse siempre al mejor vecino. |
| Local maximum | Máximo local | Pico más alto que sus vecinos pero no el global. |
| Ridge | Cresta | Secuencia de máximos locales no conectados directamente. |
| Plateau / shoulder | Meseta / hombro | Zona plana; el hombro permite seguir avanzando. |
| Sideways move | Movimiento lateral | Moverse a un vecino de igual valor. |
| Random-restart | Reinicio aleatorio | Repetir hill climbing desde estados iniciales aleatorios. |
| Local beam search | Búsqueda local en haz | Mantener k estados y quedarse con los k mejores sucesores. |

## Explicación

**¿Cuándo sirve?** Cuando solo importa el **estado final**, no el camino: 8 reinas, diseño de circuitos, distribución de fábricas, *scheduling*, optimización de redes, portafolios. Dos ventajas: (1) memoria mínima; (2) encuentra soluciones razonables en espacios enormes o infinitos. Desventaja: **no es sistemática**, puede no explorar la región donde está la solución.

Si la elevación es un valor a maximizar, buscamos el **máximo global** (hill climbing); si es un costo, el **mínimo global** ([gradient descent](gradient-descent.md)).

**Hill climbing** ("subir el Everest con niebla espesa y amnesia"): mantiene un estado y se mueve al vecino de mayor valor; se detiene cuando ningún vecino es mejor. También se llama **greedy local search**.

**Ejemplo de AIMA — 8 reinas (§4.1.1):** estado = 8 reinas, una por columna; sucesores = mover una reina dentro de su columna (8 × 7 = **56 sucesores**); h = número de pares de reinas que se atacan (0 = solución). Desde un estado con h = 17, en 5 pasos llega a h = 1 (casi solución), pero ese estado es un **mínimo local**: cualquier movimiento empeora.

**Por qué se atasca:** máximos locales, crestas (*ridges*) y mesetas (*plateaus*: máximo local plano u *hombro*).

| Variante (8 reinas aleatorias) | Éxito | Pasos promedio |
|---|---|---|
| Steepest-ascent hill climbing | **14 %** | 4 al tener éxito, 3 al atascarse |
| + hasta 100 movimientos laterales seguidos | **94 %** | 21 al tener éxito, 64 al fallar |
| Random-restart (sin laterales) | ~100 % | ≈ 7 reinicios (1/p, p ≈ 0.14), ≈ 22 pasos |
| Random-restart (con laterales) | ~100 % | ≈ 1.06 reinicios, ≈ 25 pasos |

Con reinicios aleatorios, AIMA resuelve **3 millones de reinas** en segundos. El número esperado de reinicios es **1/p**.

**Variantes:**
- **Stochastic hill climbing:** elige al azar entre los movimientos que suben (probabilidad según la pendiente).
- **First-choice hill climbing:** genera sucesores al azar hasta encontrar uno mejor (útil con miles de sucesores).
- **Random-restart:** "If at first you don't succeed, try, try again"; completo con probabilidad 1.
- **[Simulated annealing](simulated-annealing.md):** combina hill climbing con caminata aleatoria aceptando a veces empeoramientos.
- **Local beam search:** k estados; genera todos los sucesores de todos y se queda con los k mejores. No es lo mismo que k reinicios en paralelo: la información se comparte ("¡vengan aquí, el pasto es más verde!"). Problema: pérdida de diversidad → **stochastic beam search** elige sucesores con probabilidad proporcional a su valor.
- **[Evolutionary algorithms](genetic-algorithms.md):** stochastic beam search + **recombinación** de varios padres.

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

Paisaje de una dimensión (AIMA Fig. 4.1): hill climbing desde la izquierda se queda en el máximo local.

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

Estados 1–3: subida hasta un **máximo local**; 5–7: **hombro** (zona plana desde la que aún se puede subir); 10: **máximo global**.

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

- Hill climbing **no guarda** frontera ni explorados: memoria O(1).
- "Óptimo local" depende del vecindario elegido: cambiar los movimientos cambia los óptimos locales.
- Local beam search ≠ k reinicios independientes (comparte información).
- NP-difíciles suelen tener un número exponencial de máximos locales, pero unos pocos reinicios suelen dar uno bueno.

## Relacionado

- [Optimization Basics](optimization-basics.md)
- [Simulated Annealing](simulated-annealing.md)
- [Genetic Algorithms](genetic-algorithms.md)
- [Gradient Descent](gradient-descent.md)
- [N-Queens](n-queens.md)
- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md) (min-conflicts)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.1 (Figs. 4.1–4.3; estadísticas de 8 reinas).
