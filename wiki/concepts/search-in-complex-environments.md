---
title: Search in Complex Environments
type: concept
tags: [search, nondeterminism, partial-observability, online-search]
sources: [book-russell-norvig-aima]
updated: 2026-10-07
---
# Search in Complex Environments (Búsqueda en entornos complejos)

> **Summary (EN):** Classical search assumes a fully observable, deterministic, known environment, so the agent can plan a fixed action sequence and execute it "with its eyes closed". AIMA chapter 4 relaxes each assumption: with nondeterministic actions the solution becomes a conditional (contingency) plan found by AND–OR search; with partial observability the agent searches over belief states (sets of possible states); and in unknown environments online search agents must act to explore, learning heuristic estimates as they go (LRTA*).

> **En palabras simples (ES):** Cuando una acción puede salir de varias formas (no es segura), un plan simple como "haz A, luego B" no sirve. Necesitas un plan con **"si pasa esto, haz aquello"** para cada resultado posible, como un plan con respuestas para cada caso. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Nondeterministic action | Acción no determinista | Puede tener varios resultados posibles. |
| Conditional / contingency plan | Plan condicional / de contingencia | Plan con "if-then-else" según lo que se perciba. |
| AND–OR tree | Árbol Y–O | Nodos OR = elección del agente; nodos AND = resultados posibles del entorno (hay que cubrirlos todos). |
| Cyclic solution | Solución cíclica | Plan con `while`: "seguir intentando hasta que funcione". |
| Belief state | Estado de creencia | Conjunto de estados físicos en que el agente cree que puede estar. |
| Sensorless (conformant) problem | Problema sin sensores (conformante) | El agente no percibe nada; la solución es una secuencia fija. |
| Online search | Búsqueda en línea | Intercalar computación y acción en un entorno desconocido. |
| LRTA\* | LRTA\* | Agente en línea que actualiza sus estimaciones heurísticas con la experiencia. |

## Explicación

**1. Acciones no deterministas → planes condicionales (§4.3).** En el *erratic vacuum world*, `Suck` en un cuadro sucio a veces limpia también el cuadro vecino y, en uno limpio, a veces lo ensucia. La solución ya no es una secuencia sino un plan como `[Suck, if State = 5 then [Right, Suck] else []]`. Se busca con **AND–OR search**: en los nodos **OR** el agente elige una acción (basta una que funcione); en los nodos **AND** el entorno elige el resultado (el plan debe funcionar para **todos**). En un *slippery vacuum world* (moverse a veces falla) no hay solución acíclica, pero sí una **cíclica**: `[Suck, while State = 5 do Right, Suck]`.

**2. Observabilidad parcial → estados de creencia (§4.4).** El agente razona sobre el conjunto de estados posibles. En el problema **sin sensores**, la aspiradora empieza en el *belief state* {1, …, 8} y aun así puede resolverlo con una secuencia fija (p. ej. Right, Suck, Left, Suck) porque las acciones reducen la incertidumbre. Con N estados físicos hay hasta 2^N estados de creencia; se puede aplicar cualquier algoritmo del cap. 3 sobre ese espacio. Con sensores, se combina con AND–OR search.

**3. Entornos desconocidos → búsqueda en línea (§4.5).** El agente no conoce los estados ni las acciones: debe **actuar para explorar** (como un robot en un edificio nuevo). Si el entorno es *safely explorable* (sin callejones sin salida irreversibles) puede construir un mapa y encontrar la meta. **LRTA\*** actualiza la estimación de costo de cada estado visitado con lo aprendido, lo que le permite escapar de mínimos locales.

## Relación con el curso

- Es el puente entre [Problem Formulation](problem-formulation.md) (supuestos clásicos) y [Task Environments](task-environments.md) (todas las dimensiones).
- El árbol AND–OR es el mismo concepto que el **grafo Y–O** de las [cláusulas de Horn](horn-clauses-and-backward-chaining.md) y es primo de los árboles de [Minimax](adversarial-search-minimax.md) (MAX ≈ OR, MIN ≈ AND).

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Cuando una acción puede salir de varias formas (no es segura), un plan simple como "haz A, luego B" no sirve. Necesitas un plan con **"si pasa esto, haz aquello"** para cada resultado posible, como un plan con respuestas para cada caso.

**Antes de empezar: qué significa cada cosa**

| Palabra | Qué es (en simple) | English |
|---|---|---|
| Acción no determinista | la misma acción puede dar resultados distintos | nondeterministic action |
| Nodo OR | donde **yo** elijo: basta que **alguna** acción funcione | OR node |
| Nodo AND | donde **la naturaleza** elige el resultado: deben funcionar **todos** los resultados | AND node |
| Plan condicional | plan con "si… entonces…" | conditional (contingency) plan |
| Estado de creencia | el conjunto de estados en los que **podría** estar cuando no veo todo | belief state |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. At an OR node (my choice): succeed if SOME action leads to a working plan.
   - *ES:* Cuando me toca elegir, me basta encontrar una acción que funcione.
2. At an AND node (nature's choice): succeed only if EVERY possible outcome has a working plan.
   - *ES:* Cuando el resultado no depende de mí, necesito un plan para cada resultado posible.
3. The solution is a conditional plan: [action, if outcome A then … else …].
   - *ES:* La respuesta es un plan con casos: "haz esto; si sale así, haz aquello; si no, lo otro".
4. If I cannot see everything, search over belief states (sets of possible states) instead of single states.
   - *ES:* Si no veo todo, trabajo con "todos los estados en los que podría estar".

**Ejemplo con números:** aspiradora "torpe": a veces, al aspirar, el cuadro queda limpio y a veces no. Plan condicional: "Aspira; **si** el cuadro quedó limpio → muévete; **si no** → vuelve a aspirar".

**Say it in the exam (EN):** "When actions are nondeterministic, the solution is a conditional plan found by AND–OR search: at OR nodes the agent chooses one action, at AND nodes the plan must handle every possible outcome. With partial observability the agent searches over belief states, the sets of states it might be in. In unknown environments it must act and explore online."

**Dilo así (ES):** "Si las acciones no son seguras, la solución es un plan condicional que se encuentra con búsqueda AND–OR: en los nodos OR el agente elige una acción y en los AND el plan debe cubrir todos los resultados. Si el agente no ve todo, busca sobre estados de creencia. En entornos desconocidos debe actuar y explorar a la vez."

## Errores comunes y tips de examen

- En un nodo AND hay que tener plan para **cada** resultado; en un nodo OR basta **una** acción.
- Problema sin sensores: la solución es una **secuencia** (no hay nada que percibir), pero se busca en el espacio de **belief states**.

## Relacionado

- [Problem Formulation](problem-formulation.md)
- [Task Environments](task-environments.md)
- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Local Search and Hill Climbing](local-search-hill-climbing.md)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.3–4.5 (resumen del capítulo y secciones; detalle de algoritmos pendiente si el curso lo cubre).
