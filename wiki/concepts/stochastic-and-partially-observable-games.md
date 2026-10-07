---
title: Stochastic and Partially Observable Games
type: concept
tags: [games, adversarial-search, expectiminimax, uncertainty]
sources: [book-russell-norvig-aima]
updated: 2026-10-07
---
# Stochastic and Partially Observable Games (Juegos estocásticos y parcialmente observables)

> **Summary (EN):** Games of chance such as backgammon add chance nodes to the game tree; their value is the probability-weighted average of their children, giving expectiminimax, which costs O(bᵐ·nᵐ) for n distinct chance outcomes. Evaluation functions must then be a positive linear transformation of the probability of winning, because order-preserving changes can flip the decision. In partially observable games such as Kriegspiel, players reason over belief states; strategies map percept sequences to moves, and optimal play may require randomness.

> **En palabras simples (ES):** Cuando hay dados (azar), en los turnos del azar nadie elige: se calcula el **promedio** de lo que puede pasar, pesado por su probabilidad. Es minimax con un tercer tipo de nodo: el nodo de azar. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Chance node | Nodo de azar | Representa un evento aleatorio (tirar dados). |
| Expectiminimax | Expectiminimax | Minimax + nodos de azar que promedian. |
| Expected value | Valor esperado | Σ P(r)·valor(r). |
| Imperfect information | Información imperfecta | El jugador no ve todo el estado (póker, Kriegspiel). |
| Belief state | Estado de creencia | Conjunto de estados posibles dado lo percibido. |
| Guaranteed / probabilistic checkmate | Jaque mate garantizado / probabilístico | Funciona en todo estado del belief state / con probabilidad 1 gracias a jugadas aleatorias. |

## Explicación

**Juegos con azar (AIMA §6.5).** En backgammon el jugador no sabe qué dados sacará el rival, así que no puede construir un árbol minimax normal: se agregan **nodos de azar** con las tiradas posibles (36 combinaciones, 21 distintas: dobles con P = 1/36, el resto con P = 1/18).

```
EXPECTIMINIMAX(s) =
    UTILITY(s, MAX)                                  if IS-TERMINAL(s)
    max_a EXPECTIMINIMAX(RESULT(s, a))               if TO-MOVE(s) = MAX
    min_a EXPECTIMINIMAX(RESULT(s, a))               if TO-MOVE(s) = MIN
    Σ_r P(r) · EXPECTIMINIMAX(RESULT(s, r))          if TO-MOVE(s) = CHANCE
```

- **Costo:** O(bᵐ·nᵐ), n = número de resultados de azar distintos. En backgammon (n = 21, b ≈ 20) solo se pueden buscar ~3 plies.
- **Funciones de evaluación:** ya no basta con que respeten el orden. Con hojas [1, 2, 3, 4] la mejor jugada es a₁; con [1, 20, 30, 400] (mismo orden) es a₂. La evaluación debe ser una **transformación lineal positiva de la probabilidad de ganar**.
- **Poda:** alpha–beta se puede extender a nodos de azar si los valores de utilidad están **acotados** (así se acota un promedio sin ver todos los hijos). Alternativa: MCTS con tiradas aleatorias en las simulaciones.

**Juegos parcialmente observables (AIMA §6.6).** Ejemplo: **Kriegspiel** (ajedrez sin ver las piezas rivales; un árbitro anuncia capturas, jaques y jugadas ilegales). El jugador mantiene un **belief state** (tras la primera jugada de las negras, 20 posiciones posibles) y una estrategia asigna una jugada a cada **secuencia de percepciones**. Se buscan mates garantizados con **AND–OR search en el espacio de belief states** ([Search in Complex Environments](search-in-complex-environments.md)). Existen mates **probabilísticos** (moverse al azar termina encontrando al rey rival con probabilidad 1). Jugar de forma predecible **revela información**: el juego óptimo requiere cierta **aleatoriedad** (como las inspecciones sanitarias sorpresa).

**Límites de la búsqueda en juegos (AIMA §6.7).** (1) Alpha–beta es vulnerable a errores de la evaluación (en un árbol de 2 plies, si cada hoja tiene error σ = 5, la rama "peor" por 100 vs. 99 es en realidad mejor el 71 % de las veces). (2) Gasta tiempo calculando valores aunque una jugada sea obviamente la mejor → **metarazonamiento** (decidir qué vale la pena calcular). (3) Razona jugada a jugada, no con metas abstractas como un humano. (4) Integrar aprendizaje automático (AlphaZero).

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Cuando hay dados (azar), en los turnos del azar nadie elige: se calcula el **promedio** de lo que puede pasar, pesado por su probabilidad. Es minimax con un tercer tipo de nodo: el nodo de azar.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| Nodo de azar | el momento en que se tiran los dados | chance node |
| P(resultado) | la probabilidad de cada resultado (p. ej. 0.5 cada uno) | probability |
| Σ | "suma todo" | sum |
| Valor esperado | el promedio pesado: Σ P(resultado) × valor(resultado) | expected value |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Terminal state → return its utility.
   - *ES:* Si terminó, devuelve el puntaje.
2. MAX node → maximum over its children.
   - *ES:* Mi turno: el mayor.
3. MIN node → minimum over its children.
   - *ES:* Turno del rival: el menor.
4. CHANCE node → Σ P(outcome) × value(outcome).
   - *ES:* Turno del azar: multiplica cada resultado por su probabilidad y suma todo (promedio pesado).

**Ejemplo con números:** elijo a₁ o a₂; luego hay una moneda (50/50) y después juega el rival (MIN).
- a₁: moneda → MIN[2, 4] = 2 o MIN[7, 4] = 4 → 0.5·2 + 0.5·4 = **3**.
- a₂: moneda → MIN[10, 1] = 1 o MIN[8, 9] = 8 → 0.5·1 + 0.5·8 = **4.5**.
Elijo **a₂**. (Si tratara la moneda como un rival y tomara el mínimo, elegiría mal: a₁.)

**Say it in the exam (EN):** "Expectiminimax extends minimax with chance nodes, whose value is the probability-weighted average of their children. Its cost grows to O(b^m · n^m), where n is the number of chance outcomes. The evaluation function must be a positive linear transformation of the probability of winning, because with averages the size of the values matters, not just their order."

**Dilo así (ES):** "Expectiminimax agrega nodos de azar a minimax; su valor es el promedio pesado por la probabilidad. El costo sube a O(b^m · n^m), con n resultados del azar. La función de evaluación debe ser proporcional a la probabilidad de ganar, porque al promediar importa el tamaño de los valores, no solo su orden."

## Errores comunes y tips de examen

- En un nodo de azar se **promedia** (ponderado), no se maximiza ni minimiza.
- Una transformación que conserva el orden **no** conserva la decisión en expectiminimax (sí en minimax).

## Relacionado

- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Monte Carlo Tree Search](monte-carlo-tree-search.md)
- [Search in Complex Environments](search-in-complex-environments.md)
- [Task Environments](task-environments.md) (backgammon y póker en la Fig. 2.6)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.5–6.7 (Figs. 6.12–6.16).
