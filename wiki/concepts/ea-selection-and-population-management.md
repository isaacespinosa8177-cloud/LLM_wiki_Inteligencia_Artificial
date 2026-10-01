---
title: EA Selection and Population Management
type: concept
tags: [optimization, evolutionary-computation, genetic-algorithms, selection]
sources: [book-eiben-smith-evolutionary-computing, slides-04-optimization]
updated: 2026-10-01
---
# EA Selection and Population Management (Selección y gestión de la población)

> **Summary (EN):** Selection is the fitness-based force that pushes an evolutionary algorithm towards better solutions, and it acts twice: parent selection (who reproduces) and survivor selection (who enters the next generation). Eiben & Smith chapter 5 covers generational vs. steady-state models; fitness-proportional selection and its problems (premature convergence, loss of pressure, sensitivity to shifting f), fixes like windowing and sigma scaling, ranking and tournament selection, roulette-wheel vs. stochastic universal sampling; survivor schemes (age-based, replace-worst, elitism, (μ+λ), (μ,λ)); selection pressure measured by takeover time; and diversity-preserving methods for multimodal problems (fitness sharing, crowding, island models).

## Términos clave

| English | Español | Significado |
|---|---|---|
| μ / λ | μ / λ | Tamaño de la población / número de hijos. |
| Generational / steady-state model | Modelo generacional / estacionario | Se reemplaza toda la población / solo λ < μ individuos. |
| Generational gap λ/μ | Brecha generacional | Proporción de la población que se reemplaza. |
| Fitness proportional selection (FPS) | Selección proporcional a la aptitud | P(i) = fᵢ / Σⱼ fⱼ (ruleta). |
| Ranking selection | Selección por ranking | La probabilidad depende de la posición, no del valor. |
| Tournament selection | Selección por torneo | Tomar k al azar y elegir el mejor. |
| Roulette wheel / SUS | Ruleta / muestreo universal estocástico | λ giros de un brazo / un giro con λ brazos equiespaciados. |
| Selection pressure | Presión de selección | Cuánto se favorece a los mejores. |
| Takeover time τ\* | Tiempo de toma de control | Generaciones hasta que el mejor llena la población. |
| Elitism | Elitismo | Conservar siempre al mejor individuo. |
| (μ+λ) / (μ,λ) | (μ+λ) / (μ,λ) | Sobreviven los μ mejores de padres + hijos / solo de los hijos. |
| Genetic drift | Deriva genética | Pérdida aleatoria de nichos por población finita. |
| Fitness sharing / crowding | Compartición de aptitud / *crowding* | Métodos explícitos para mantener diversidad. |

## Explicación

### Esquema general (Eiben & Smith §3.1–3.2)

Dos fuerzas: **variación** (mutación y recombinación) crea **diversidad/novedad**; **selección** sube la **calidad media**. Componentes de un EA: representación, función de evaluación, población, **selección de padres**, operadores de variación, **selección de supervivientes**, inicialización y condición de terminación. La selección de padres suele ser **estocástica** (los débiles tienen una probabilidad pequeña pero positiva, para no ser demasiado *greedy*); la de supervivientes suele ser **determinista**.

**Modelos de población (§5.1):** *generacional* (la población entera se reemplaza por los hijos; GA simple) o *steady-state* (se reemplazan λ < μ por iteración, p. ej. λ = 1 en GENITOR).

### Selección de padres (§5.2)

**1. Proporcional a la aptitud (FPS, ruleta):** P(i) = fᵢ / Σⱼ fⱼ. Problemas:
- **Convergencia prematura:** un individuo sobresaliente toma la población muy rápido.
- **Pérdida de presión** cuando todas las aptitudes son parecidas (final de la corrida).
- **Sensible a trasladar f** (Tabla 5.1):

| Ind. | f | P(f) | f + 10 | P(f+10) | f + 100 | P(f+100) |
|---|---|---|---|---|---|---|
| A | 1 | 0.10 | 11 | 0.275 | 101 | 0.326 |
| B | 4 | 0.40 | 14 | 0.350 | 104 | 0.335 |
| C | 5 | 0.50 | 15 | 0.375 | 105 | 0.339 |

Soluciones: **windowing** (restar la peor aptitud actual) y **sigma scaling**: f'(x) = max(f(x) − (f̄ − c·σ_f), 0), con c ≈ 2.

**2. Ranking:** ordenar y asignar probabilidad por posición i (peor = 0, mejor = μ−1). **Lineal** con parámetro s ∈ (1, 2]:

```
P_lin-rank(i) = (2 − s)/μ  +  2·i·(s − 1) / (μ·(μ − 1))
```

Ejemplo (Tabla 5.2, μ = 3): fitness A = 1, B = 5, C = 4 → rangos 0, 2, 1. FPS: 0.1 / 0.5 / 0.4. Lineal s = 2: 0 / 0.67 / 0.33. Lineal s = 1.5: 0.167 / 0.5 / 0.333. Para más presión: ranking **exponencial**, P(i) = (1 − e^(−i)) / c.

**Cómo muestrear:** la **ruleta** (λ giros de un brazo) tiene mucha varianza; **SUS** (un giro con λ brazos equiespaciados, r ~ U[0, 1/λ] e incrementos de 1/λ) garantiza que cada individuo recibe entre ⌊λ·P(i)⌋ y ⌊λ·P(i)⌋ + 1 copias.

**3. Torneo:** repetir λ veces: tomar k individuos al azar y elegir el mejor. No necesita conocer toda la población ni un valor numérico de aptitud (solo poder **comparar**, útil en juegos o arte). Mayor **k** → más presión; elegir al mejor con probabilidad p < 1 → menos presión; sin reemplazo, los k−1 peores nunca se eligen. Es el más usado en GA por simple y fácil de controlar.

**4. Uniforme:** P = 1/μ (estrategias evolutivas, programación evolutiva); la presión viene de la selección de supervivientes. **Overselection** para poblaciones enormes (GP): 80 % de los padres del x % superior.

### Selección de supervivientes (§5.3)

| Esquema | Regla | Comentario |
|---|---|---|
| **Age-based** | Cada individuo vive un número fijo de iteraciones (GA simple: todos los hijos reemplazan a todos los padres; o FIFO) | La mejor aptitud puede bajar entre generaciones |
| **Replace worst (GENITOR)** | Reemplazar a los λ peores | Mejora rápida pero riesgo de convergencia prematura |
| **Elitism** | El mejor actual nunca se pierde | Se combina con age-based o estocástico |
| **Round-robin** | Cada uno compite con q rivales (q = 10); sobreviven los μ con más victorias | Programación evolutiva |
| **(μ+λ)** | Unir padres e hijos y quedarse con los μ mejores | Generaliza GENITOR |
| **(μ,λ)** | Descartar a todos los padres; quedarse con los μ mejores de λ > μ hijos (λ/μ ≈ 5–7) | Preferida en ES: escapa de óptimos locales, sigue óptimos móviles, favorece la autoadaptación |

### Presión de selección (§5.4)

**Takeover time τ\***: generaciones hasta que el mejor llena la población partiendo de una copia. Para (μ,λ): τ\* = ln λ / ln(λ/μ) → μ = 15, λ = 100 da **τ\* ≈ 2**. Para FPS en un GA: τ\* = λ·ln λ → λ = 100 da **τ\* ≈ 460**. Es decir, la selección de las ES es muchísimo más agresiva.

### Diversidad en problemas multimodales (§5.5)

Con población finita y apareamiento libre (*panmictic*) aparece **deriva genética**: dos nichos igual de buenos empiezan 50/50, por azar pasan a 49/51 y la diferencia se amplifica hasta que queda uno solo. Soluciones:
- **Explícitas:** **fitness sharing** (dividir la aptitud entre los vecinos a distancia < σ_share; distribuye individuos entre picos **en proporción a su aptitud**), **crowding** (el hijo reemplaza al individuo más parecido; *deterministic crowding*: cada hijo compite con su padre más similar; reparte la población **por igual** entre picos), especiación.
- **Implícitas:** **island model** (subpoblaciones con migración ocasional), EAs celulares.

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

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** la selección decide quién se reproduce y quién sobrevive; más presión = converge más rápido pero pierde diversidad.

```text
ROULETTE WHEEL (fitness proportional):
1. P(i) = f_i / sum of all f.  2. Spin: pick a random r in [0,1] and walk the
   cumulative probabilities until passing r. Repeat for each parent.
TOURNAMENT (size k):
1. Pick k individuals at random.  2. The best one becomes a parent. Repeat.
ELITISM:
Always copy the current best individual into the next generation.
(μ, λ) SURVIVOR SELECTION:
From λ children keep the best μ; discard all parents.
(μ + λ) SURVIVOR SELECTION:
Merge parents and children; keep the best μ.
```

**Say it in the exam (EN):** "Fitness-proportional selection causes premature convergence early and loses pressure late, and it changes if f is shifted. Ranking and tournament selection fix this; tournament size k controls the pressure. Elitism guarantees the best fitness never decreases. Takeover time measures selection pressure."

## Errores comunes y tips de examen

- La selección es **independiente de la representación**; los operadores de variación no.
- FPS no funciona con aptitudes negativas ni cuando se minimiza sin transformar f (Eiben usa, p. ej., M − q(p)).
- Torneo y ranking son **invariantes** a trasladar o escalar f; FPS no.
- La tarea GA usa **truncamiento** (los 10 mejores de 100) + elitismo: presión muy alta (ver [tarea](../assignments/genetic-algorithm-task.md)).
- (μ,λ) puede perder al mejor; (μ+λ) es elitista por construcción.

## Relacionado

- [Genetic Algorithms](genetic-algorithms.md)
- [EA Representation and Variation Operators](ea-representation-and-variation.md)
- [Evolutionary Computation](evolutionary-computation.md)
- [Optimization Basics](optimization-basics.md) (exploración vs. explotación)

## Fuentes

- [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) §3.1–3.2, cap. 5 completo (ingestado; Tablas 5.1–5.2 verificadas a mano).
