---
title: Swarm Intelligence
type: concept
tags: [optimization, swarm-intelligence, bio-inspired, multi-agent]
sources: [slides-04-optimization, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system]
updated: 2026-10-07
---
# Swarm Intelligence (Inteligencia de enjambre)

> **Summary (EN):** Swarm intelligence is problem solving that appears when many simple agents (birds, fish, ants, bees) follow local rules and share a little information; the group finds solutions no single agent could. Millonas' five principles (proximity, quality, diverse response, stability, adaptability) describe it. The course covers three algorithms: PSO (particles share their best positions), ACO (ants communicate indirectly by leaving pheromone, called stigmergy) and ABC (bees split the work between exploiting good sources and exploring new ones).

> **En palabras simples (ES):** Muchos agentes muy simples (pájaros, hormigas, abejas), cada uno siguiendo reglas sencillas y compartiendo un poco de información, logran juntos algo inteligente que ninguno logra solo, como encontrar el camino más corto a la comida. El curso usa tres algoritmos de este tipo: PSO (partículas como pájaros), ACO (hormigas con feromona) y ABC (abejas).

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Swarm | Enjambre | Un grupo de muchos agentes simples que se influyen entre sí. |
| Emergence | Emergencia | Un comportamiento del grupo que nadie programó en cada individuo. |
| Stigmergy | Estigmergia | Comunicarse dejando señales en el entorno (como la feromona de las hormigas). |
| Positive feedback | Retroalimentación positiva | Lo bueno atrae a más agentes, y así se refuerza más. |
| Decentralized | Descentralizado | No hay jefe ni control central. |

## Explicación

### 1. La idea

Una hormiga sola no sabe cuál es el camino más corto a la comida, pero **la colonia sí lo encuentra**. Nadie le dio esa instrucción a ninguna hormiga: el resultado **emerge** de muchas acciones simples y de la información que comparten. Eso es la inteligencia de enjambre.

### 2. Los cinco principios de Millonas (citados en el paper de PSO, §4)

1. **Proximidad:** el grupo puede hacer cálculos simples de espacio y tiempo ("¿qué tan lejos está?, ¿cuánto tardo?").
2. **Calidad:** responde a qué tan buenas son las cosas del entorno (más comida, mejor lugar).
3. **Respuesta diversa:** no pone todo su esfuerzo en un solo lugar.
4. **Estabilidad:** no cambia de comportamiento cada vez que cambia algo pequeño.
5. **Adaptabilidad:** sí cambia cuando vale la pena.

(Los principios 4 y 5 son "dos caras de la misma moneda": no cambiar por cualquier cosa, pero sí cuando conviene.)

### 3. ¿Por qué compartir información ayuda?

Kennedy y Eberhart citan a E. O. Wilson: los peces de un cardumen se benefician de lo que **cualquiera** de ellos descubre. Cuando la comida está repartida de forma impredecible, compartir información da ventaja para sobrevivir.

### 4. Los tres algoritmos del curso

| Algoritmo | Inspirado en | Cómo comparten información | Tipo de problema |
|---|---|---|---|
| [PSO](particle-swarm-optimization.md) (1995) | Bandadas de pájaros, cardúmenes | **Directa:** todos conocen el mejor lugar del grupo (g_best) | Continuos (números reales) |
| [ACO](ant-colony-optimization.md) (1996) | Hormigas buscando comida | **Indirecta:** dejan feromona en los caminos | Combinatorios (rutas, TSP) |
| [ABC](artificial-bee-colony.md) (2007) | Abejas buscando flores | **Danza:** las observadoras eligen fuentes según qué tan buenas son | Continuos |

**Visto como agentes:** cada partícula, hormiga o abeja es un [agente](intelligent-agents.md) muy simple dentro de un entorno multiagente **cooperativo** ([Task Environments](task-environments.md)).

## Errores comunes y tips de examen

- La "inteligencia" está en la **interacción** entre los agentes, no en cada individuo.
- PSO comparte información de forma directa (g_best). ACO, de forma indirecta (estigmergia: la feromona).

## Relacionado

- [Particle Swarm Optimization](particle-swarm-optimization.md)
- [Ant Colony Optimization](ant-colony-optimization.md)
- [Artificial Bee Colony](artificial-bee-colony.md)
- [Evolutionary Computation](evolutionary-computation.md)
- [Optimization Basics](optimization-basics.md)

## Fuentes

- [Slides 04](../sources/slides-04-optimization.md), slides 4, 8–18.
- [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) §2, §4.
- [Dorigo et al. 1996](../sources/paper-dorigo-1996-ant-system.md) §I.
