---
title: Search in Complex Environments
type: concept
tags: [search, nondeterminism, partial-observability, online-search]
sources: [book-russell-norvig-aima]
updated: 2026-10-07
---
# Search in Complex Environments (Búsqueda en entornos complejos)

> **Summary (EN):** Classical search assumes the agent sees everything, actions always do the same thing, and the world is known, so it can plan a fixed sequence and follow it "with its eyes closed". AIMA chapter 4 removes each assumption: if actions can have several outcomes, the solution is a conditional plan found by AND–OR search; if the agent cannot see everything, it searches over belief states (sets of states it might be in); if the world is unknown, it must act and explore at the same time (online search, e.g. LRTA*).

> **En palabras simples (ES):** Cuando una acción puede salir de varias formas (no es segura), un plan simple como "haz A, luego B" no sirve. Necesitas un plan con **"si pasa esto, haz aquello"** para cada resultado posible, como un plan con respuestas para cada caso. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Nondeterministic action | Acción no determinista | La misma acción puede dar resultados distintos. |
| Conditional / contingency plan | Plan condicional / de contingencia | Plan con "si… entonces… si no…". |
| AND–OR tree | Árbol Y–O | Árbol con dos tipos de nodos: OR (yo elijo; basta una opción que funcione) y AND (el entorno elige; deben funcionar todas). |
| Cyclic solution | Solución cíclica | Plan con "repite hasta que funcione". |
| Belief state | Estado de creencia | El conjunto de estados en los que **podría** estar, cuando no veo todo. |
| Sensorless (conformant) problem | Problema sin sensores | El agente no percibe nada; igual debe resolverlo con una secuencia fija. |
| Online search | Búsqueda en línea | Pensar y actuar a la vez en un lugar desconocido. |
| LRTA\* | LRTA\* | Agente en línea que va corrigiendo sus estimaciones con la experiencia. |

## Explicación

La búsqueda clásica funciona cuando el agente lo ve todo, sus acciones siempre hacen lo mismo y conoce el mapa. Este capítulo responde: **¿qué pasa si eso no se cumple?** Hay tres casos.

### 1. Acciones no seguras → planes con "si… entonces…" (§4.3)

**Ejemplo: la aspiradora torpe (*erratic vacuum world*).** Cuando aspira un cuadro sucio, a veces también limpia el cuadro vecino. Cuando aspira un cuadro limpio, a veces lo ensucia. Como no sabe qué va a pasar, una lista fija de pasos no sirve. La solución es un plan con casos:

`[Suck, if State = 5 then [Right, Suck] else []]` → "aspira; **si** quedaste en el estado 5, ve a la derecha y aspira; **si no**, ya terminaste".

Ese plan se busca con **búsqueda AND–OR**:
- En los nodos **OR** decido **yo**: me basta encontrar **una** acción que funcione.
- En los nodos **AND** decide **el entorno**: el plan debe funcionar para **todos** los resultados posibles.

**Aspiradora resbalosa (*slippery vacuum world*):** a veces, al intentar moverse, se queda en el mismo lugar. No hay un plan que termine seguro en un número fijo de pasos, pero sí uno **cíclico**: `[Suck, while State = 5 do Right, Suck]` → "aspira; **mientras** sigas en el estado 5, intenta ir a la derecha; luego aspira".

### 2. No ve todo → estados de creencia (§4.4)

Si el agente no sabe exactamente dónde está, razona sobre **todos los estados en los que podría estar** (su estado de creencia).

**Ejemplo sin sensores:** la aspiradora no percibe nada; al empezar podría estar en cualquiera de los 8 estados {1, …, 8}. Aun así lo resuelve con una secuencia fija, por ejemplo Right, Suck, Left, Suck: cada acción va **reduciendo la duda** (después de ir a la derecha, seguro está en el cuadro derecho, esté sucio o no).

Con N estados reales hay hasta 2^N estados de creencia posibles, pero se puede usar cualquier algoritmo del capítulo 3 sobre ese nuevo "mapa". Si el agente tiene algunos sensores, se combina con la búsqueda AND–OR.

### 3. Mundo desconocido → búsqueda en línea (§4.5)

El agente **no conoce el mapa**: tiene que moverse para descubrirlo, como un robot en un edificio nuevo. Si no hay callejones sin salida de los que no se pueda volver (*safely explorable*), puede ir armando el mapa y encontrar la meta.

**LRTA\*** es un agente así: cada vez que visita un lugar, corrige su estimación de "cuánto falta desde aquí" con lo que aprendió. Eso le permite salir de zonas donde se habría quedado atascado.

## Relación con el curso

- Es el puente entre [Problem Formulation](problem-formulation.md) (el caso fácil) y [Task Environments](task-environments.md) (todas las propiedades del entorno).
- El árbol AND–OR es la misma idea que el **grafo Y–O** de las [cláusulas de Horn](horn-clauses-and-backward-chaining.md), y se parece al árbol de [Minimax](adversarial-search-minimax.md): mi turno ≈ OR, turno del rival ≈ AND.

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

- En un nodo AND hace falta un plan para **cada** resultado; en un nodo OR basta **una** acción que funcione.
- Problema sin sensores: la solución es una **secuencia fija** (no hay nada que percibir), pero se busca en el espacio de **estados de creencia**.

## Relacionado

- [Problem Formulation](problem-formulation.md)
- [Task Environments](task-environments.md)
- [Adversarial Search and Minimax](adversarial-search-minimax.md)
- [Local Search and Hill Climbing](local-search-hill-climbing.md)

## Fuentes

- [AIMA 4e](../sources/book-russell-norvig-aima.md) §4.3–4.5 (resumen del capítulo y secciones; detalle de algoritmos pendiente si el curso lo cubre).
