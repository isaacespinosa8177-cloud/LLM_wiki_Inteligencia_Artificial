---
title: EA Representation and Variation Operators
type: concept
tags: [optimization, evolutionary-computation, genetic-algorithms, mutation, crossover]
sources: [book-eiben-smith-evolutionary-computing, slides-04-optimization, book-russell-norvig-aima]
updated: 2026-10-07
---
# EA Representation and Variation Operators (Representación, mutación y recombinación)

> **Summary (EN):** The first and often hardest decision in an evolutionary algorithm is how to write a solution (its representation), and the mutation and crossover operators must match it so that children are always valid solutions. Eiben & Smith chapter 4 covers the standard cases: bits (bit-flip mutation; one-point, n-point and uniform crossover; Gray code), integers (random resetting, creep), real numbers (uniform and Gaussian mutation, self-adapting step sizes; discrete, arithmetic and blend crossover), permutations (swap, insert, scramble and inversion mutation; PMX, edge, order and cycle crossover) and trees (genetic programming).

> **En palabras simples (ES):** La forma de guardar una solución (bits, números reales o un orden) decide **cómo** se puede mezclar y cambiar sin romperla. Regla de oro: el hijo siempre debe ser una solución válida. Por ejemplo, en una ruta de ciudades no se puede repetir una ciudad, así que no sirve el corte simple de los bits. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Genotype / phenotype | Genotipo / fenotipo | La solución en "código" dentro del algoritmo / lo que significa (`10010` ↔ 18). |
| Encoding / decoding | Codificar / decodificar | Pasar de la solución al código / del código a la solución. |
| Locus, gene / allele | Posición, gen / alelo | Un lugar de la cadena / el valor en ese lugar. |
| Mutation rate p_m | Tasa de mutación | Probabilidad de cambiar cada gen (en permutaciones: cada cromosoma). |
| Crossover rate p_c | Tasa de cruce | Probabilidad de cruzar a dos padres (si no, los hijos son copias). |
| Arity | Aridad | Cuántos padres usa: 1 = mutación, 2 = cruce, más de 2 = multiparental. |
| Gray code | Código Gray | Forma de escribir números en bits donde dos números seguidos difieren en un solo bit. |
| Step size σ (sigma) | Tamaño de paso | Qué tan grandes son, en promedio, los cambios de la mutación gaussiana. |
| Self-adaptation | Autoadaptación | El propio σ va dentro de la solución y también evoluciona. |
| Permutation | Permutación | Un orden donde cada valor aparece una sola vez: [3 1 2]. |
| Respect | Respeto | Propiedad de un cruce: lo que los dos padres tienen en común pasa al hijo. |

## Explicación

### La regla de oro (Eiben & Smith §4.1)

Los operadores **nunca deben producir algo inválido**: el hijo de dos permutaciones debe ser una permutación. La **selección** solo mira la nota, así que funciona igual con cualquier representación; en cambio, la **mutación y el cruce dependen totalmente** de cómo se guarde la solución. Históricamente, el cruce fue el operador principal en los GA, la mutación el único en la programación evolutiva, y en la programación genética a veces solo se usa cruce.

### 1. Bits (§4.2)

- **Mutación por cambio de bit:** cada bit cambia con probabilidad p_m; en promedio cambian L·p_m bits por hijo (L = largo de la cadena). Se recomienda entre "un bit por generación" y "un bit por hijo".
- **El problema de los bits:** no todos los bits pesan igual. Para pasar de 7 (`0111`) a 8 (`1000`) hay que cambiar 4 bits, pero para pasar de 7 a 6 (`0110`) solo 1. Con **código Gray**, dos números seguidos siempre difieren en un bit. En general, usar bits para guardar números suele ser mala idea: es mejor usar directamente enteros o reales.
- **Cruce:**

| Operador | Cómo funciona | Efecto |
|---|---|---|
| Un punto (*one-point*) | Elige un punto r entre 1 y L−1 e intercambia los finales | Tiende a mantener juntos los genes cercanos; nunca junta los dos extremos |
| n puntos | Elige n puntos y alterna pedazos de cada padre | Parecido, con más mezcla |
| Uniforme | Para cada gen tira una moneda (p = 0.5) para decidir de qué padre viene; el otro hijo recibe lo contrario | No le importa la posición; cada hijo hereda ~50 % de cada padre |

### 2. Enteros (§4.3)

- Valores **ordinales** (tienen orden: 2 se parece a 3) vs. **cardinales** (sin orden: rojo, azul, amarillo).
- **Reasignación aleatoria** (*random resetting*): con probabilidad p_m, poner un valor permitido al azar. Sirve para cardinales.
- **Mutación por arrastre** (*creep*): sumar o restar un valor pequeño. Sirve para ordinales.
- Cruce: los mismos que con bits (promediar enteros no tiene sentido).

### 3. Números reales (§4.4)

**Mutación:**
- **Uniforme:** reemplazar el valor por cualquier número al azar dentro de sus límites [Lᵢ, Uᵢ].
- **Gaussiana:** x'ᵢ = xᵢ + N(0, σ), recortado a sus límites. N(0, σ) es un número al azar que casi siempre es pequeño: unos 2 de cada 3 cambios quedan entre −σ y +σ. (La versión Cauchy a veces da saltos más grandes.)
- **Autoadaptativa** (estrategias evolutivas): el tamaño de paso σ va **dentro** de la solución y también evoluciona. Primero se cambia σ y después x con el nuevo σ:
  - Un solo σ: σ' = σ · e^(τ·N(0,1)) y x'ᵢ = xᵢ + σ'·Nᵢ(0,1), con τ ∝ 1/√n y un valor mínimo para σ. Los cambios se reparten en **círculos**.
  - Un σ por variable: σ'ᵢ = σᵢ · e^(τ'·N(0,1) + τ·Nᵢ(0,1)). Los cambios se reparten en **elipses** alineadas con los ejes.
  - Con ángulos de rotación: elipses **inclinadas**.
  - Tanto la teoría como los experimentos dicen que σ debe **ir bajando**: pasos grandes al inicio (explorar) y pequeños al final (afinar).

**Cruce (padres x e y, hijo z):**

| Tipo | Fórmula | Comentario |
|---|---|---|
| Discreto | Cada zᵢ se copia de x o de y, al azar | Solo la mutación crea valores nuevos |
| Aritmético simple | Primeros k genes de x; el resto α·yᵢ + (1−α)·xᵢ | — |
| Aritmético de un gen | Solo se promedia el gen k | — |
| Aritmético completo (el más usado) | z = α·x + (1−α)·y | Promedio pesado; con α = ½ los dos hijos son iguales; los valores se van juntando |
| Blend (BLX-α) | zᵢ al azar en un rango un poco **más ancho** que el de los padres | Crea valores nuevos sin que todo se junte |

Ejemplo: padres 2 y 6 con α = 0.5 → hijo = 0.5·2 + 0.5·6 = 4.

### 4. Permutaciones (§4.5)

Hay dos tipos de problemas:
- **De orden** (horarios): importa qué va **antes** de qué.
- **De adyacencia** (TSP, el viajante): importa qué ciudad está **al lado** de cuál ([1,2,3,4] es el mismo recorrido que [2,3,4,1]).

Con 30 ciudades hay unos 10³² recorridos. Aquí p_m es la probabilidad de mutar **la solución entera**, no cada gen.

| Mutación | Qué hace (ejemplo sobre [1 2 3 4 5 6 7 8 9]) |
|---|---|
| Intercambio (*swap*) | Intercambia dos posiciones (2 y 5 → [1 5 3 4 2 6 7 8 9]) |
| Inserción (*insert*) | Mueve un valor junto a otro (el 5 junto al 2 → [1 2 5 3 4 6 7 8 9]) |
| Revolver (*scramble*) | Desordena algunas posiciones |
| Inversión (*inversion*) | Da vuelta un tramo (de 2 a 5 → [1 5 4 3 2 6 7 8 9]); solo rompe 2 enlaces, por eso es la base del **2-opt** para el TSP |

| Cruce | Idea (en simple) | Sirve para |
|---|---|---|
| **PMX** (*Partially Mapped*) | Copia un tramo de P1; los valores del mismo tramo en P2 se ubican siguiendo la "correspondencia" entre ambos tramos; el resto viene de P2 | Adyacencia (TSP) |
| **Edge (edge-3)** | Hace una tabla con los vecinos de cada ciudad en los dos padres y prefiere los enlaces que tienen en común | Adyacencia; conserva los enlaces comunes |
| **Order (OX, Davis)** | Copia un tramo de P1 y completa con los valores que faltan, en el orden en que aparecen en P2 empezando después del segundo corte (dando la vuelta) | Orden |
| **Cycle** | Divide las posiciones en "ciclos" y toma un ciclo de cada padre alternadamente | Posición exacta |

**Ejemplo de Eiben & Smith (§3.4.1), 8 reinas como permutación:** igual que en el curso ([N-Queens](n-queens.md)), la solución es una permutación de 1..8 (la fila de la reina de cada columna), así que nunca chocan en filas ni columnas; solo hay que reducir los choques en diagonal. Mutación = **intercambio**; cruce = **cut-and-crossfill** (copiar la primera parte de P1 y completar con los valores de P2 en su orden, saltando los repetidos).

### 5. Árboles (§4.6)

En la **programación genética**, cada solución es un árbol que representa un programa o una fórmula. Mutar = reemplazar una rama por otra al azar; cruzar = intercambiar ramas entre los padres.

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

- El cruce de un punto aplicado a **permutaciones** da hijos inválidos (con valores repetidos) → usar PMX, OX, cycle o edge.
- Guardar números reales en bits es posible (lo hace la tarea GA), pero suele funcionar peor que guardar los reales directamente con mutación gaussiana.
- En el cruce de un punto, el corte se elige entre 1 y L−1 para que no quede antes del primer gen ni después del último.
- En la tarea GA: 16 bits en signo-magnitud, cruce de un punto y cambio de bit con p_m = 0.1 ([tarea](../assignments/genetic-algorithm-task.md)).

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
