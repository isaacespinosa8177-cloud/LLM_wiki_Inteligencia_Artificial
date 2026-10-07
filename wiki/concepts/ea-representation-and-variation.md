---
title: EA Representation and Variation Operators
type: concept
tags: [optimization, evolutionary-computation, genetic-algorithms, mutation, crossover]
sources: [book-eiben-smith-evolutionary-computing, slides-04-optimization, book-russell-norvig-aima]
updated: 2026-10-07
---
# EA Representation and Variation Operators (Representación, mutación y recombinación)

> **Summary (EN):** Choosing the genotype representation is the first and often hardest design step of an evolutionary algorithm, and the mutation and recombination operators must match it so that offspring stay valid. Eiben & Smith chapter 4 covers the standard families: binary (bit-flip mutation; one-point, n-point and uniform crossover, Gray code), integer (random resetting, creep), real-valued (uniform and Gaussian mutation, self-adaptive step sizes; discrete, arithmetic and blend recombination), permutation (swap, insert, scramble, inversion; PMX, edge, order and cycle crossover) and trees (genetic programming).

> **En palabras simples (ES):** La forma de guardar una solución (bits, números reales o un orden) decide **cómo** se puede mezclar y cambiar sin romperla. Regla de oro: el hijo siempre debe ser una solución válida. Por ejemplo, en una ruta de ciudades no se puede repetir una ciudad, así que no sirve el corte simple de los bits. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Genotype / phenotype | Genotipo / fenotipo | Codificación dentro del EA / solución real decodificada (10010 ↔ 18). |
| Encoding / decoding | Codificación / decodificación | Fenotipo → genotipo / genotipo → fenotipo. |
| Locus, gene / allele | Locus, gen / alelo | Posición / valor en esa posición. |
| Mutation rate p_m | Tasa de mutación | Probabilidad de mutar cada gen (o cada cromosoma en permutaciones). |
| Crossover rate p_c | Tasa de cruce | Probabilidad de recombinar (si no, se copian los padres). |
| Arity | Aridad | Nº de padres: 1 = mutación, 2 = cruce, > 2 = multiparental. |
| Positional / distributional bias | Sesgo posicional / distribucional | n-point tiende a mantener juntos genes cercanos / uniform tiende a heredar 50 % de cada padre. |
| Gray code | Código Gray | Enteros consecutivos difieren en un solo bit. |
| Step size σ / self-adaptation | Tamaño de paso / autoadaptación | Desviación de la mutación gaussiana; σ evoluciona dentro del cromosoma. |
| Respect | Respeto | Propiedad de un cruce: lo que comparten ambos padres pasa al hijo. |

## Explicación

**Regla de oro (Eiben & Smith §4.1):** los operadores deben **no salir del espacio de genotipos** (el hijo de dos permutaciones debe ser una permutación). La **selección** solo mira la aptitud y es independiente de la representación; los **operadores de variación** dependen totalmente de ella. Históricamente el cruce fue el operador principal en GA, la mutación el único en programación evolutiva, y en programación genética a veces solo se usa cruce.

### 1. Representación binaria (§4.2)

- **Mutación bit-flip:** cada bit cambia con probabilidad p_m; en promedio L·p_m bits por hijo. Se recomienda entre "un gen por generación" y "un gen por hijo".
- **Problema de los bits:** cada bit tiene distinto peso; de 7 (0111) a 8 (1000) hacen falta 4 cambios, pero a 6 (0110) solo 1 → usar **código Gray**. Usar bits para codificar números suele ser un error: mejor representación entera o real.
- **Cruce:**

| Operador | Cómo funciona | Sesgo |
|---|---|---|
| One-point | Punto r ∈ [1, L−1]; se intercambian las colas | Posicional fuerte (no junta genes de extremos opuestos) |
| n-point | n puntos; se alternan segmentos | Posicional |
| Uniform | Cada gen se hereda del padre 1 si U[0,1] < p (p = 0.5), si no del padre 2; el segundo hijo es el inverso | Sin sesgo posicional; sesgo distribucional (≈50 % de cada padre) |

### 2. Representación entera (§4.3)

- Atributos **ordinales** (2 se parece a 3) vs. **cardinales** (rojo/azul/amarillo, sin orden).
- **Random resetting:** con p_m, poner un valor permitido al azar (para cardinales).
- **Creep mutation:** sumar un valor pequeño ± (para ordinales).
- Cruce: los mismos que en binario (promediar enteros no tiene sentido).

### 3. Representación real (§4.4)

**Mutación:**
- **Uniforme:** x'ᵢ ~ U[Lᵢ, Uᵢ].
- **Gaussiana (no uniforme):** x'ᵢ = xᵢ + N(0, σ), recortada a [Lᵢ, Uᵢ]; ~2/3 de los cambios están en ±σ. σ = **tamaño de paso de mutación**. (Cauchy = colas más gruesas.)
- **Autoadaptativa** (estrategias evolutivas): σ va **dentro** del cromosoma y evoluciona. Primero se muta σ y luego x con el nuevo σ:
  - Un σ: σ' = σ · e^(τ·N(0,1)), x'ᵢ = xᵢ + σ'·Nᵢ(0,1), con τ ∝ 1/√n y un mínimo ε₀ para σ (contornos de mutación = **círculos**).
  - n σ: σ'ᵢ = σᵢ · e^(τ'·N(0,1) + τ·Nᵢ(0,1)) (contornos = **elipses** alineadas con los ejes).
  - Correlacionada: además n(n−1)/2 ángulos de rotación (elipses **rotadas**, matriz de covarianza).
  - Teoría y experimentos coinciden: σ debe **decrecer** con el tiempo (explorar al inicio, afinar al final).

**Recombinación (padres x e y, hijo z):**

| Tipo | Fórmula | Nota |
|---|---|---|
| Discreta | zᵢ = xᵢ o yᵢ con igual probabilidad | Solo la mutación crea valores nuevos |
| Simple arithmetic | Primeros k genes de x; el resto α·yᵢ + (1−α)·xᵢ | — |
| Single arithmetic | Solo el gen k se promedia | — |
| Whole arithmetic (la más usada) | z = α·x + (1−α)·y | Con α = ½ los dos hijos son iguales; reduce el rango de valores |
| Blend (BLX-α) | zᵢ en un intervalo que **excede** el de los padres | Crea material nuevo sin reducir el rango |

### 4. Permutaciones (§4.5)

Dos clases de problemas: **orden** (scheduling: importa qué va antes) y **adyacencia** (TSP: importan los enlaces; [1,2,3,4] ≡ [2,3,4,1]). Para n = 30 ciudades hay ~10³² tours. Aquí p_m es la probabilidad de mutar **el cromosoma**, no cada gen.

| Mutación | Qué hace (ejemplo sobre [1 2 3 4 5 6 7 8 9]) |
|---|---|
| Swap | Intercambia dos posiciones (2 y 5 → [1 5 3 4 2 6 7 8 9]) |
| Insert | Mueve un alelo junto a otro (5 junto a 2 → [1 2 5 3 4 6 7 8 9]) |
| Scramble | Desordena un subconjunto de posiciones |
| Inversion | Invierte un segmento (2..5 → [1 5 4 3 2 6 7 8 9]); rompe solo 2 enlaces → base del **2-opt** para TSP |

| Cruce | Idea | Para |
|---|---|---|
| **PMX** (Partially Mapped) | Copia un segmento de P1 y ubica los valores del segmento de P2 siguiendo el "mapeo" entre ambos segmentos; el resto de P2 | Adyacencia (TSP) |
| **Edge (edge-3)** | Tabla de vecinos de cada ciudad en ambos padres; preferir aristas comunes y la lista más corta | Adyacencia; preserva aristas comunes (*respect*) |
| **Order (OX, Davis)** | Copia un segmento de P1; completa con los valores restantes en el orden en que aparecen en P2 desde el segundo punto (circular) | Orden |
| **Cycle** | Divide en ciclos de posiciones y alterna ciclos de cada padre | Posición absoluta |

**Ejemplo de Eiben & Smith (§3.4.1) — 8 reinas como permutación:** igual que en el curso ([N-Queens](n-queens.md)), el genotipo es una permutación de 1..8 (fila de la reina en cada columna) → filas y columnas nunca chocan; solo hay que minimizar los ataques diagonales. Mutación = **swap**; cruce = **cut-and-crossfill** (copiar la primera parte de P1 y rellenar con los valores de P2 en orden, saltando los repetidos).

### 5. Árboles (§4.6)

En **programación genética** el individuo es un árbol de sintaxis (un programa o fórmula). Mutación = reemplazar un subárbol por uno aleatorio; cruce = intercambiar subárboles entre padres.

## Pseudocódigo

```
BIT-FLIP-MUTATION(x, pm):           for i in 1..L: if rand() < pm: x[i] ← 1 − x[i]
ONE-POINT-CROSSOVER(p1, p2):        r ← randint(1, L−1)
                                    return p1[:r] + p2[r:],  p2[:r] + p1[r:]
UNIFORM-CROSSOVER(p1, p2, p=0.5):   for i: if rand() < p: c1[i]←p1[i]; c2[i]←p2[i]
                                               else:        c1[i]←p2[i]; c2[i]←p1[i]
GAUSSIAN-MUTATION(x, σ):            for i: x[i] ← clip(x[i] + σ·N(0,1), L[i], U[i])
WHOLE-ARITHMETIC(x, y, α):          return α·x + (1−α)·y,  α·y + (1−α)·x
SWAP-MUTATION(perm):                pick i ≠ j;  swap perm[i], perm[j]
ORDER-CROSSOVER(p1, p2):            copy p1[a..b] into child;
                                    fill remaining slots, starting after b and wrapping,
                                    with p2's values in p2's order (from position b+1), skipping used ones
```

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** La forma de guardar una solución (bits, números reales o un orden) decide **cómo** se puede mezclar y cambiar sin romperla. Regla de oro: el hijo siempre debe ser una solución válida. Por ejemplo, en una ruta de ciudades no se puede repetir una ciudad, así que no sirve el corte simple de los bits.

**Antes de empezar: qué significa cada cosa**

| Símbolo / palabra | Qué es (en simple) | English |
|---|---|---|
| Representación | cómo se guarda una solución: bits, números reales, un orden (permutación) | representation |
| Gen | una posición de la solución (un bit, un número) | gene |
| P1, P2 | padre 1 y padre 2 | parents |
| p_m | probabilidad de mutar cada gen | mutation rate |
| N(0, σ) | un número al azar "normal": casi siempre cerca de 0; σ dice qué tan lejos puede ir | Gaussian noise |
| α | un peso entre 0 y 1 para promediar a los padres | weight |
| Permutación | un orden donde cada valor aparece una sola vez: [1 2 3 4 5 6] | permutation |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Bits — one-point crossover: cut both parents at the same random point; child 1 = start of P1 + end of P2, child 2 = start of P2 + end of P1.
   - *ES:* Corta los dos en el mismo lugar e intercambia los finales.
2. Bits — uniform crossover: for each gene, flip a coin to decide which parent it comes from.
   - *ES:* Para cada posición, una moneda decide de qué padre viene.
3. Bits — bit-flip mutation: flip each bit with probability p_m.
   - *ES:* Cada bit puede cambiar de 0 a 1 (o al revés) con probabilidad pequeña.
4. Real numbers — Gaussian mutation: add a small random number N(0, σ) to each value and keep it inside its limits.
   - *ES:* Suma a cada número un poquito de "ruido" al azar.
5. Real numbers — arithmetic crossover: child = α·P1 + (1 − α)·P2.
   - *ES:* El hijo es un promedio pesado de los padres (con α = 0.5, el punto medio).
6. Permutations — swap mutation: exchange two positions. Inversion mutation: reverse a random segment.
   - *ES:* Intercambia dos posiciones, o da vuelta a un tramo. Así no se repite ningún valor.
7. Permutations — order crossover: copy a segment from P1, then fill the empty places with the missing values in the order they appear in P2.
   - *ES:* Copia un tramo del padre 1 y completa con los valores que faltan, en el orden en que aparecen en el padre 2.

**Ejemplo con números:**
- Bits: `110|10110` × `001|11001` → **`11011001`** y **`00110110`**.
- Reales: P1 = 2, P2 = 6, α = 0.5 → hijo = 0.5·2 + 0.5·6 = **4**. Mutación gaussiana: 4 + 0.3 = 4.3.
- Permutación: [1 2 3 4 5 6], intercambio de las posiciones 2 y 5 → **[1 5 3 4 2 6]**. Cada número sigue apareciendo una vez.

**Say it in the exam (EN):** "The representation decides the variation operators, because the children must stay valid. Bit strings use bit-flip mutation and one-point, n-point or uniform crossover. Real-valued vectors use Gaussian mutation and arithmetic recombination. Permutations, as in the TSP, need special operators such as swap or inversion mutation and order or PMX crossover; one-point crossover would repeat values."

**Dilo así (ES):** "La representación decide los operadores, porque los hijos deben ser válidos. Con bits se usa mutación por inversión de bits y cruce de uno o varios puntos o uniforme. Con números reales, mutación gaussiana y cruce aritmético. Con permutaciones, como en el TSP, se necesitan operadores especiales como intercambio, inversión, order crossover o PMX; el cruce de un punto repetiría valores."

## Errores comunes y tips de examen

- Aplicar cruce de un punto a **permutaciones** produce hijos inválidos (valores repetidos) → usar PMX, OX, cycle o edge.
- Representar reales con bits es posible (tarea GA) pero suele ser peor que la representación real + mutación gaussiana.
- One-point crossover: el punto se elige en [1, L−1] para que no quede antes del primer gen ni después del último.
- En la tarea GA: 16 bits en signo-magnitud, cruce de un punto y bit-flip con p_m = 0.1 ([tarea](../assignments/genetic-algorithm-task.md)).

## Relacionado

- [Genetic Algorithms](genetic-algorithms.md)
- [EA Selection and Population Management](ea-selection-and-population-management.md)
- [Evolutionary Computation](evolutionary-computation.md)
- [N-Queens](n-queens.md)
- [Ant Colony Optimization](ant-colony-optimization.md) (otra forma de atacar el TSP)

## Fuentes

- [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) cap. 4 completo y §3.4.1 (ingestado).
- [Slides 04](../sources/slides-04-optimization.md), slide 6 (cruce de un punto y mutación).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.1.4.
