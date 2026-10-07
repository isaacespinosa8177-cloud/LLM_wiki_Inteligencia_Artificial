---
title: EA Selection and Population Management
type: concept
tags: [optimization, evolutionary-computation, genetic-algorithms, selection]
sources: [book-eiben-smith-evolutionary-computing, slides-04-optimization]
updated: 2026-10-07
---
# EA Selection and Population Management (Selección y gestión de la población)

> **Summary (EN):** Selection is the force that pushes an evolutionary algorithm toward better solutions, and it happens twice: parent selection (who has children) and survivor selection (who goes on to the next generation). Eiben & Smith chapter 5 covers replacing the whole population vs. a few at a time; fitness-proportional (roulette) selection and its problems (converging too early, losing pressure, depending on how fitness is shifted) and fixes like windowing and sigma scaling; ranking and tournament selection; roulette vs. stochastic universal sampling; survivor schemes (by age, replace the worst, elitism, (μ+λ), (μ,λ)); how strong selection is (takeover time); and methods that keep diversity when there are several good peaks (fitness sharing, crowding, islands).

> **En palabras simples (ES):** La selección decide **quién tiene hijos** y **quién pasa a la siguiente generación**. Si eliges solo a los mejores, la población mejora rápido pero todos se vuelven parecidos (pierde variedad y puede atascarse). Si eliges casi al azar, conserva variedad pero mejora lento. Los métodos de selección regulan ese equilibrio. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| μ (mu) / λ (lambda) | — | Tamaño de la población / cantidad de hijos por generación. |
| Generational / steady-state | Generacional / estacionario | Se reemplaza toda la población / solo unos pocos cada vez. |
| Fitness proportional selection (FPS) | Selección proporcional a la aptitud | Ruleta: P(i) = nota de i / suma de todas las notas. |
| Ranking selection | Selección por ranking | La probabilidad depende del **puesto**, no del valor de la nota. |
| Tournament selection | Selección por torneo | Sacar k al azar y quedarse con el mejor. |
| Roulette wheel / SUS | Ruleta / muestreo universal estocástico | Girar una ruleta λ veces / girar una sola vez una ruleta con λ flechas repartidas. |
| Selection pressure | Presión de selección | Qué tanto se favorece a los mejores. |
| Takeover time τ\* | Tiempo de toma de control | Cuántas generaciones tarda el mejor en llenar toda la población con sus copias. |
| Elitism | Elitismo | El mejor siempre pasa a la siguiente generación. |
| (μ+λ) / (μ,λ) | — | Sobreviven los μ mejores entre padres **e** hijos / solo entre los hijos. |
| Premature convergence | Convergencia prematura | Todos se vuelven iguales demasiado pronto y se atasca. |
| Genetic drift | Deriva genética | Perder por puro azar una de varias buenas zonas, por tener una población finita. |
| Fitness sharing / crowding | Compartir aptitud / *crowding* | Métodos para mantener la variedad. |

## Explicación

### 1. Dos fuerzas y dos momentos de selección (Eiben & Smith §3.1–3.2)

- La **variación** (mutación y cruce) **crea variedad** y cosas nuevas.
- La **selección** **sube la calidad** promedio.

La selección ocurre dos veces:
1. **Selección de padres:** quién tiene hijos. Suele usar **azar**: los peores tienen una probabilidad pequeña pero no cero, para no ser demasiado codiciosos.
2. **Selección de supervivientes:** quién pasa a la siguiente generación. Suele ser **fija** (determinista).

**Dos formas de reemplazar (§5.1):** *generacional* (todos los hijos reemplazan a toda la población, como en el GA simple) o *estacionaria* (*steady-state*: se reemplazan solo unos pocos cada vez; en GENITOR, uno).

### 2. Selección de padres (§5.2)

**a) Proporcional a la aptitud (ruleta).** Cada individuo recibe un pedazo de ruleta proporcional a su nota: P(i) = fᵢ / Σⱼ fⱼ (su nota dividida para la suma de todas). Problemas:
- **Convergencia prematura:** si uno es muchísimo mejor que los demás, se queda con casi toda la ruleta y llena la población enseguida.
- **Pérdida de presión:** al final, cuando todos tienen notas parecidas, la ruleta reparte casi igual y ya no favorece a nadie.
- **Depende de sumar una constante** a la nota (Tabla 5.1):

| Individuo | f | P(f) | f + 10 | P(f+10) | f + 100 | P(f+100) |
|---|---|---|---|---|---|---|
| A | 1 | 0.10 | 11 | 0.275 | 101 | 0.326 |
| B | 4 | 0.40 | 14 | 0.350 | 104 | 0.335 |
| C | 5 | 0.50 | 15 | 0.375 | 105 | 0.339 |

Con solo sumar 100 a todas las notas, C pasa de tener 50 % a casi lo mismo que A. Arreglos: **windowing** (restar a todos la peor nota actual) y **sigma scaling**: f'(x) = max(f(x) − (f̄ − c·σ_f), 0), con c ≈ 2 (f̄ = promedio, σ_f = cuánto varían las notas).

**b) Por ranking (por puesto).** Se ordenan y la probabilidad depende del **puesto** i (el peor es 0, el mejor es μ−1). Versión **lineal**, con un parámetro s entre 1 y 2 que dice cuánto se favorece al mejor:

```
P_lin-rank(i) = (2 − s)/μ  +  2·i·(s − 1) / (μ·(μ − 1))
```

Ejemplo (Tabla 5.2, μ = 3): notas A = 1, B = 5, C = 4 → puestos A = 0, C = 1, B = 2.
- Ruleta: A 0.1 · B 0.5 · C 0.4.
- Ranking lineal con s = 2: A 0 · B 0.67 · C 0.33.
- Ranking lineal con s = 1.5: A 0.167 · B 0.5 · C 0.333.

Para favorecer aún más a los mejores existe el ranking **exponencial**: P(i) = (1 − e^(−i)) / c.

**Cómo hacer el sorteo:** la **ruleta** (girar λ veces) puede dar resultados muy dispares por mala suerte. **SUS** gira una sola vez una ruleta con λ flechas repartidas a la misma distancia; así cada individuo recibe casi exactamente las copias que le tocan (entre ⌊λ·P(i)⌋ y ⌊λ·P(i)⌋ + 1).

**c) Por torneo.** Repite λ veces: saca **k individuos al azar** y quédate con **el mejor**.
- No necesita conocer a toda la población ni un número de nota: basta con poder **comparar** dos soluciones (útil en juegos o en arte).
- Con **k más grande** → más presión (los mejores ganan más seguido). Si el mejor gana solo con probabilidad p < 1 → menos presión.
- Si se sacan sin reemplazo, los k−1 peores nunca pueden ganar.
- Es el más usado en GA porque es simple y fácil de controlar.

**d) Uniforme.** Todos con la misma probabilidad 1/μ (en estrategias evolutivas y programación evolutiva); ahí la presión la pone la selección de supervivientes. Para poblaciones enormes (programación genética) se usa *overselection*: el 80 % de los padres sale del mejor grupo.

### 3. Selección de supervivientes (§5.3)

| Esquema | Regla (en simple) | Comentario |
|---|---|---|
| **Por edad** | Cada uno vive un tiempo fijo (en el GA simple, todos los hijos reemplazan a todos los padres) | La mejor nota puede bajar de una generación a otra |
| **Reemplazar al peor (GENITOR)** | Los hijos reemplazan a los λ peores | Mejora rápido pero se puede atascar pronto |
| **Elitismo** | El mejor actual nunca se pierde | Se combina con los otros esquemas |
| **Todos contra todos (*round-robin*)** | Cada uno compite con q rivales (q = 10); sobreviven los μ con más victorias | Programación evolutiva |
| **(μ+λ)** | Se juntan padres e hijos y quedan los μ mejores | Es elitista por construcción |
| **(μ,λ)** | Se descartan todos los padres; quedan los μ mejores de λ > μ hijos (λ/μ ≈ 5–7) | Preferido en estrategias evolutivas: escapa de valles pequeños y sigue óptimos que se mueven |

### 4. ¿Qué tan fuerte es la selección? (§5.4)

**Takeover time τ\*:** cuántas generaciones tarda el mejor en llenar toda la población, empezando con una sola copia.
- (μ,λ): τ\* = ln λ / ln(λ/μ) → con μ = 15 y λ = 100, **τ\* ≈ 2** generaciones.
- Ruleta en un GA: τ\* = λ·ln λ → con λ = 100, **τ\* ≈ 460** generaciones.

O sea: la selección de las estrategias evolutivas es muchísimo más agresiva.

### 5. Mantener la variedad cuando hay varios picos buenos (§5.5)

Con una población finita donde todos se cruzan con todos, aparece la **deriva genética**: si hay dos zonas igual de buenas y la población empieza 50/50, por puro azar pasa a 49/51, y esa diferencia se va agrandando hasta que una zona desaparece. Soluciones:
- **Explícitas:**
  - **Compartir aptitud (*fitness sharing*):** la nota de cada uno se divide entre los vecinos que tiene cerca (a menos de σ_share). Así los individuos se reparten entre los picos **según qué tan buenos son**.
  - **Crowding:** cada hijo reemplaza al individuo **más parecido** a él (en *deterministic crowding*, compite con su padre más parecido). Reparte la población **por igual** entre los picos.
  - **Especiación:** solo se cruzan los parecidos.
- **Implícitas:** **islas** (varias subpoblaciones separadas que de vez en cuando intercambian individuos) y algoritmos celulares (cada uno solo se cruza con sus vecinos).

## Pseudocódigo

```
function EVOLUTIONARY-ALGORITHM():            # Eiben & Smith Fig. 3.1
    INITIALISE population with random candidate solutions
    EVALUATE each candidate
    repeat until TERMINATION-CONDITION:
        SELECT parents
        RECOMBINE pairs of parents
        MUTATE the resulting offspring
        EVALUATE new candidates
        SELECT individuals for the next generation

function TOURNAMENT-SELECTION(population, λ, k):
    pool ← []
    repeat λ times:
        contestants ← k individuals chosen at random
        append the best of contestants to pool
    return pool

function ROULETTE-WHEEL(population, a, λ):    # a = cumulative probabilities, a[μ] = 1
    repeat λ times:
        r ← U[0, 1];  i ← 1
        while a[i] < r: i ← i + 1
        append population[i] to pool

function SUS(population, a, λ):
    r ← U[0, 1/λ];  i ← 1
    repeat λ times:
        while r > a[i]: i ← i + 1
        append population[i] to pool;  r ← r + 1/λ
```

Cómo leer la ruleta: `a` es la lista de probabilidades **acumuladas** (por ejemplo, 0.31, 0.60, 0.86, 1.00). Se saca un número al azar r entre 0 y 1 y se avanza hasta el primer individuo cuya probabilidad acumulada pase r.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** La selección decide **quién tiene hijos** y **quién pasa a la siguiente generación**. Si eliges solo a los mejores, la población mejora rápido pero todos se vuelven parecidos (pierde variedad y puede atascarse). Si eliges casi al azar, conserva variedad pero mejora lento. Los métodos de selección regulan ese equilibrio.

**Antes de empezar: qué significa cada cosa**

| Símbolo / palabra | Qué es (en simple) | English |
|---|---|---|
| f_i | la aptitud (nota) del individuo i; aquí más alta = mejor | fitness of individual i |
| P(i) | la probabilidad de que i sea elegido | selection probability |
| Ruleta | cada individuo recibe un pedazo de ruleta proporcional a su nota | roulette wheel |
| Torneo de tamaño k | eliges k individuos al azar y gana el mejor | tournament |
| Elitismo | el mejor pasa siempre a la siguiente generación | elitism |
| μ (mu), λ (lambda) | cantidad de padres / cantidad de hijos | parents / offspring |
| Presión de selección | qué tanto se favorece a los mejores | selection pressure |
| Convergencia prematura | todos se parecen demasiado pronto y la búsqueda se atasca | premature convergence |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Roulette wheel: P(i) = f_i / (sum of all fitness values). Spin: pick a random number between 0 and 1 and see in which slice it falls. Repeat for each parent.
   - *ES:* Ruleta: tu probabilidad es tu nota dividida para la suma de todas las notas. Gira la ruleta una vez por cada padre que necesites.
2. Tournament of size k: pick k individuals at random; the best one becomes a parent. Repeat.
   - *ES:* Torneo: saca k al azar y gana el mejor. Con k más grande, los mejores ganan más seguido (más presión).
3. Elitism: always copy the best individual into the next generation.
   - *ES:* Elitismo: el mejor siempre pasa, así la mejor nota nunca empeora.
4. (μ, λ) survivor selection: from the λ children keep the best μ; all parents are discarded.
   - *ES:* (μ, λ): de los λ hijos se quedan los μ mejores; los padres se descartan todos.
5. (μ + λ) survivor selection: put parents and children together and keep the best μ.
   - *ES:* (μ + λ): se juntan padres e hijos y se quedan los μ mejores.

**Ejemplo con números:** notas [24, 23, 20, 11] (más alta = mejor). Suma = 78. Ruleta: 24/78 = **0.31**, 23/78 = **0.29**, 20/78 = **0.26**, 11/78 = **0.14**. El peor todavía tiene un 14 % de probabilidad, lo que conserva variedad. Torneo con k = 2: si salen el de 20 y el de 11, gana el de **20**.

**Say it in the exam (EN):** "Selection decides who reproduces and who survives. Fitness-proportional (roulette) selection gives each individual a probability equal to its fitness divided by the total; it can converge too early when one individual is much better, and it loses pressure when everyone is similar. Ranking and tournament selection avoid this; in a tournament, the size k controls the pressure. Elitism guarantees the best solution is never lost. (μ, λ) keeps only the best children; (μ + λ) keeps the best of parents and children."

**Dilo así (ES):** "La selección decide quién se reproduce y quién sobrevive. La ruleta da a cada individuo una probabilidad igual a su nota dividida para el total; puede converger demasiado pronto si uno es mucho mejor, y pierde presión cuando todos se parecen. El ranking y el torneo lo evitan; en el torneo, k controla la presión. El elitismo asegura que nunca se pierda el mejor. (μ, λ) guarda solo a los mejores hijos; (μ + λ), a los mejores entre padres e hijos."

## Errores comunes y tips de examen

- La selección **no depende de la representación**; la mutación y el cruce sí.
- La ruleta no funciona con notas negativas ni cuando se minimiza sin transformar la nota antes (Eiben usa, por ejemplo, M − q(p)).
- El torneo y el ranking dan lo mismo aunque sumes una constante a todas las notas o las multipliques; la ruleta no.
- La tarea GA usa **truncamiento** (los 10 mejores de 100) + elitismo: favorece muchísimo a los mejores (ver [tarea](../assignments/genetic-algorithm-task.md)).
- (μ,λ) puede perder al mejor individuo; (μ+λ) nunca lo pierde.

## Relacionado

- [Genetic Algorithms](genetic-algorithms.md)
- [EA Representation and Variation Operators](ea-representation-and-variation.md)
- [Evolutionary Computation](evolutionary-computation.md)
- [Optimization Basics](optimization-basics.md) (exploración vs. explotación)

## Fuentes

- [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) §3.1–3.2, cap. 5 completo (ingestado; Tablas 5.1–5.2 verificadas a mano).
