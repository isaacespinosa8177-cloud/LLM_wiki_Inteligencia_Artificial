---
title: Monte Carlo Tree Search
type: concept
tags: [games, adversarial-search, mcts, go, chess]
sources: [book-russell-norvig-aima]
updated: 2026-10-01
---
# Monte Carlo Tree Search (Búsqueda de árbol Monte Carlo, MCTS)

> **Summary (EN):** MCTS estimates the value of a game state not with a heuristic evaluation function but by averaging the results of many complete simulated games (playouts) from that state. It grows a search tree with four repeated steps — selection, expansion, simulation, back-propagation — using a selection policy such as UCT (UCB1) that balances exploitation of moves with high win rates against exploration of rarely tried moves. It replaced alpha–beta in Go, where the branching factor (≈361 at the start) and the lack of a good evaluation function defeat heuristic minimax; AlphaGo and AlphaZero combine MCTS with neural networks trained by self-play.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Playout / rollout / simulation | Simulación | Jugar una partida completa desde un estado hasta el final. |
| Playout policy | Política de simulación | Cómo se eligen las jugadas en la simulación (al azar o sesgadas a buenas jugadas). |
| Selection policy | Política de selección | Cómo bajar por el árbol eligiendo hijos. |
| UCT / UCB1 | UCT / UCB1 | *Upper Confidence bounds applied to Trees*: fórmula que balancea explotación y exploración. |
| Back-propagation | Retropropagación | Actualizar victorias/simulaciones desde la hoja hasta la raíz. |
| Pure Monte Carlo search | Monte Carlo puro | N simulaciones desde el estado actual, sin árbol. |
| Type A / Type B strategy (Shannon) | Estrategia tipo A / tipo B | A: todas las jugadas hasta cierta profundidad + evaluación (amplio y poco profundo). B: solo jugadas prometedoras, lo más profundo posible (estrecho y profundo). |

## Explicación

**Problema con alpha–beta en Go** (AIMA §6.4): (1) factor de ramificación inicial **361** → alpha–beta solo llega a 4–5 plies; (2) es muy difícil escribir una **función de evaluación** para Go (el material no indica quién gana y las posiciones cambian hasta el final).

**Idea:** el valor de un estado = **promedio de los resultados** de muchas partidas simuladas desde él, usando las **reglas del juego** (no una heurística falible) para ver quién ganó. Si las jugadas de la simulación fueran totalmente aleatorias responderíamos "¿cuál es la mejor jugada si ambos juegan al azar?"; por eso se usa una **playout policy** sesgada a buenas jugadas (aprendida con redes neuronales por auto-juego en Go).

**Los cuatro pasos (AIMA Fig. 6.10), repetidos hasta que se acabe el tiempo:**

1. **Selection:** desde la raíz, bajar eligiendo hijos con la política de selección (UCT) hasta una hoja del árbol.
2. **Expansion:** agregar un hijo nuevo (0/0) a esa hoja.
3. **Simulation:** jugar una partida desde el hijo nuevo con la playout policy (estas jugadas **no** se guardan en el árbol).
4. **Back-propagation:** subir actualizando cada nodo del camino: +1 simulación a todos, +1 victoria a los nodos del jugador que ganó.

Al final se devuelve la jugada con **más simulaciones** (no la de mejor porcentaje: 65/100 es más confiable que 2/3).

**UCB1** para un nodo n:

```
UCB1(n) = U(n) / N(n)  +  C · sqrt( ln N(PARENT(n)) / N(n) )
          └ exploitation ┘   └──────── exploration ────────┘
```

U(n) = utilidad total (victorias) de las simulaciones por n, N(n) = número de simulaciones por n. El término de exploración es grande para nodos poco visitados. La teoría sugiere C = √2; en la práctica se ajusta. AlphaZero agrega un término con la probabilidad de la jugada dada por una red neuronal.

**Ejemplo verificado (AIMA Fig. 6.10, raíz con 100 simulaciones, ln 100 ≈ 4.605):**

| Nodo | U/N | Explotación | Exploración (C = 1.4) | UCB1 (C = 1.4) | UCB1 (C = 1.5) |
|---|---|---|---|---|---|
| 60/79 | 0.759 | 0.759 | 1.4·√(4.605/79) = 0.338 | **1.097** | 1.121 |
| 1/10 | 0.100 | 0.100 | 1.4·√(4.605/10) = 0.950 | 1.050 | 1.118 |
| 2/11 | 0.182 | 0.182 | 1.4·√(4.605/11) = 0.906 | 1.088 | **1.152** |

Con C = 1.4 se elige 60/79 (explotación); con C = 1.5, el 2/11 (exploración) — exactamente lo que dice el libro.

**Comparación con alpha–beta (AIMA §6.4):** con b = 32, partidas de 100 plies y presupuesto de 10⁹ estados: minimax llega a 6 plies, alpha–beta con orden perfecto a 12, y MCTS hace 10 millones de simulaciones. Una simulación cuesta tiempo **lineal** en la profundidad (una jugada por nivel).

| | Heuristic alpha–beta | MCTS |
|---|---|---|
| Evaluación de hojas | Función de evaluación | Promedio de simulaciones |
| Mejor cuando | b moderado y buena evaluación (ajedrez) | b alto o evaluación difícil (Go), juegos nuevos |
| Debilidad | Un error de la evaluación en un nodo puede decidir la jugada | Puede no explorar una jugada única decisiva (poda tipo B); lento para confirmar posiciones "obviamente" ganadas |

## Pseudocódigo

```
function MONTE-CARLO-TREE-SEARCH(state) returns an action
    tree ← NODE(state)
    while IS-TIME-REMAINING():
        leaf  ← SELECT(tree)              # follow UCB1 down to a leaf
        child ← EXPAND(leaf)              # add a new child node
        result ← SIMULATE(child)          # playout to a terminal state
        BACK-PROPAGATE(result, child)     # update wins/playouts up to the root
    return the move in ACTIONS(state) whose node has the highest number of playouts
```

## Ajedrez vs. Go (conecta con HW01)

- **Ajedrez:** Deep Blue venció a Kasparov en 1997 con alpha–beta (> 100 millones de posiciones/s, extensiones singulares hasta 40 plies). Stockfish y similares reducen el factor de ramificación efectivo a < 3 (de 35) con *null move* y *futility pruning*. En 2017 **AlphaZero** (MCTS + red neuronal, auto-juego) venció a Stockfish 155–6 en 1000 partidas.
- **Go:** hasta 2015 los programas eran de nivel amateur. **AlphaGo** (Silver et al., 2016) combinó reconocimiento visual de patrones, aprendizaje por refuerzo, redes neuronales y MCTS para vencer a Lee Sedol 4–1 (marzo de 2016; AIMA dice "2015", ver [errata](../study/errata.md)) y a Ke Jie 3–0 (2017).
- Kasparov sobre AlphaZero: se acerca al enfoque humano **Type B** soñado por Shannon y Turing, en lugar de la fuerza bruta.

## Errores comunes y tips de examen

- MCTS **no necesita** función de evaluación (solo las reglas), pero puede combinarse con ella (cortar la simulación y evaluar).
- La jugada devuelta es la de **más simulaciones**, no la de mejor porcentaje.
- UCB1: el término de exploración usa el **logaritmo** de las visitas del **padre** dividido por las visitas del **hijo**.
- Es otra instancia de **exploración vs. explotación**, igual que en [optimización](optimization-basics.md).

## Relacionado

- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Alpha–Beta Pruning](alpha-beta-pruning.md)
- [Stochastic and Partially Observable Games](stochastic-and-partially-observable-games.md)
- [Neural Networks](neural-networks.md)
- [HW01 (Chess vs. Go)](../assignments/deber-1-search-problems.md)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §6.4 (MCTS, UCT, Fig. 6.10–6.11) y notas históricas del cap. 6 (Deep Blue, Stockfish, AlphaGo, AlphaZero).
