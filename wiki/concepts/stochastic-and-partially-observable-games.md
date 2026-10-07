---
title: Stochastic and Partially Observable Games
type: concept
tags: [games, adversarial-search, expectiminimax, uncertainty]
sources: [book-russell-norvig-aima]
updated: 2026-10-07
---
# Stochastic and Partially Observable Games (Juegos estocásticos y parcialmente observables)

> **Summary (EN):** Games with dice, like backgammon, add chance nodes to the game tree; a chance node's value is the average of its children weighted by their probabilities. This is expectiminimax, and it costs O(b^m · n^m) for n possible chance outcomes. Evaluation functions must then be proportional to the probability of winning, because with averages the size of the values matters, not only their order. In games where players cannot see everything, like Kriegspiel, players reason over belief states, and the best play may need some randomness.

> **En palabras simples (ES):** Cuando hay dados (azar), en los turnos del azar nadie elige: se calcula el **promedio** de lo que puede pasar, pesado por su probabilidad. Es minimax con un tercer tipo de nodo: el nodo de azar. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Chance node | Nodo de azar | El momento en que se tiran los dados. |
| Expectiminimax | Expectiminimax | Minimax + nodos de azar que promedian. |
| Expected value | Valor esperado | El promedio pesado: Σ P(resultado) × valor(resultado). |
| P(r) | Probabilidad | Qué tan probable es cada resultado r (por ejemplo, 1/36). |
| Imperfect information | Información imperfecta | El jugador no ve todo (cartas ocultas en el póker). |
| Belief state | Estado de creencia | El conjunto de situaciones posibles según lo que he visto. |
| Guaranteed / probabilistic checkmate | Jaque mate garantizado / probabilístico | Gana sea cual sea la situación real / gana casi seguro gracias a jugadas al azar. |

## Explicación

### 1. Juegos con dados: expectiminimax (AIMA §6.5)

En el backgammon no sabes qué dados va a sacar el rival, así que no puedes armar un árbol minimax normal. La solución es agregar **nodos de azar** con todas las tiradas posibles. Con dos dados hay 36 combinaciones, pero solo 21 distintas: los dobles tienen probabilidad 1/36 y las demás 1/18 (porque 3-5 y 5-3 son lo mismo).

```
EXPECTIMINIMAX(s) =
    UTILITY(s, MAX)                                  if IS-TERMINAL(s)
    max_a EXPECTIMINIMAX(RESULT(s, a))               if TO-MOVE(s) = MAX
    min_a EXPECTIMINIMAX(RESULT(s, a))               if TO-MOVE(s) = MIN
    Σ_r P(r) · EXPECTIMINIMAX(RESULT(s, r))          if TO-MOVE(s) = CHANCE
```

En palabras: igual que minimax, más una regla nueva. En un nodo de azar, **multiplica el valor de cada resultado por su probabilidad y suma todo**.

- **Costo:** O(b^m · n^m), donde n es la cantidad de resultados distintos del azar. En backgammon (n = 21, unas 20 jugadas por turno) solo se puede mirar unas 3 jugadas adelante.
- **Cuidado con la función de evaluación:** ya no basta con que ordene bien las posiciones. Ejemplo del libro: con valores [1, 2, 3, 4] la mejor jugada es a₁, pero con [1, 20, 30, 400] (mismo orden) la mejor es a₂, porque al promediar importan los **tamaños**. La evaluación debe ser **proporcional a la probabilidad de ganar** (una "transformación lineal positiva").
- **Poda:** alfa–beta se puede usar con nodos de azar si los puntajes tienen un máximo y un mínimo conocidos (así se puede acotar un promedio sin ver todos los hijos). Otra opción es MCTS con tiradas al azar en las partidas rápidas.

### 2. Juegos donde no se ve todo (AIMA §6.6)

**Ejemplo: Kriegspiel**, un ajedrez en el que no ves las piezas del rival; un árbitro solo anuncia capturas, jaques y jugadas ilegales.

- El jugador lleva la cuenta de **todas las posiciones en las que podría estar el tablero** (su estado de creencia). Después de la primera jugada de las negras hay 20 posibles.
- Su estrategia dice qué jugar según **todo lo que ha percibido** hasta ahora.
- Se buscan mates **garantizados** (que funcionen en todas las posiciones posibles) con búsqueda AND–OR sobre estados de creencia ([Search in Complex Environments](search-in-complex-environments.md)).
- También hay mates **probabilísticos**: moviéndose al azar, tarde o temprano se encuentra al rey rival.
- Jugar siempre igual **le da información al rival**. Por eso, a veces lo mejor es jugar con algo de **azar**, como las inspecciones sanitarias sorpresa.

### 3. Límites de la búsqueda en juegos (AIMA §6.7)

1. Alfa–beta depende mucho de la función de evaluación: si cada hoja tiene un pequeño error, una rama que parece peor (100 vs. 99) en realidad es mejor el 71 % de las veces.
2. Pierde tiempo calculando aunque una jugada sea obviamente la mejor. Pensar en qué vale la pena calcular se llama **metarazonamiento**.
3. Piensa jugada por jugada, no con planes generales como un humano.
4. Le falta aprender de la experiencia; eso es lo que agregó AlphaZero.

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

- En un nodo de azar se **promedia** (con las probabilidades como pesos); no se toma el máximo ni el mínimo.
- Cambiar los valores manteniendo su orden **no** cambia la decisión en minimax, pero **sí** puede cambiarla en expectiminimax.

## Relacionado

- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Monte Carlo Tree Search](monte-carlo-tree-search.md)
- [Search in Complex Environments](search-in-complex-environments.md)
- [Task Environments](task-environments.md) (backgammon y póker en la Fig. 2.6)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.5–6.7 (Figs. 6.12–6.16).
