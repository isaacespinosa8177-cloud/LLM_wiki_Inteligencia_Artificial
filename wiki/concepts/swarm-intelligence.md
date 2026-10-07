---
title: Swarm Intelligence
type: concept
tags: [optimization, swarm-intelligence, bio-inspired, multi-agent]
sources: [slides-04-optimization, paper-kennedy-eberhart-1995-pso, paper-dorigo-1996-ant-system]
updated: 2026-10-07
---
# Swarm Intelligence (Inteligencia de enjambre)

> **Summary (EN):** Swarm intelligence is collective problem solving that emerges from many simple agents following local rules and sharing information — birds, fish, ants, bees. Millonas' five principles (proximity, quality, diverse response, stability, adaptability) characterize it. The course covers three algorithms: PSO (particles share best positions), ACO (ants communicate indirectly through pheromone, i.e., stigmergy) and ABC (bees divide labor between exploitation and exploration).

> **En palabras simples (ES):** Muchos agentes muy simples (pájaros, hormigas, abejas), cada uno siguiendo reglas sencillas y compartiendo un poco de información, logran juntos algo inteligente que ninguno logra solo, como encontrar el camino más corto a la comida. El curso usa tres algoritmos de este tipo: PSO (partículas como pájaros), ACO (hormigas con feromona) y ABC (abejas).

## Términos clave

| English | Español | Significado |
|---|---|---|
| Swarm | Enjambre | Población de agentes simples que interactúan. |
| Emergence | Emergencia | Comportamiento global que no está programado en ningún agente. |
| Stigmergy | Estigmergia | Comunicación indirecta modificando el entorno (feromona). |
| Positive feedback | Retroalimentación positiva | Lo bueno atrae más agentes y se refuerza. |
| Decentralized | Descentralizado | Sin líder ni control central. |

## Explicación

**Cinco principios de Millonas** (citados en el paper de PSO, §4):
1. **Proximidad:** la población puede hacer cálculos simples de espacio y tiempo.
2. **Calidad:** responde a factores de calidad del entorno.
3. **Respuesta diversa:** no concentra su actividad en canales demasiado estrechos.
4. **Estabilidad:** no cambia de modo cada vez que cambia el entorno.
5. **Adaptabilidad:** cambia de modo cuando vale la pena.

(4 y 5 son "dos caras de la misma moneda".)

**Idea social (Kennedy y Eberhart, citando a E. O. Wilson):** los miembros de un cardumen se benefician de los descubrimientos de todos; compartir información da ventaja evolutiva cuando los recursos están distribuidos de forma impredecible.

| Algoritmo | Inspiración | Cómo se comparte información | Problemas típicos |
|---|---|---|---|
| [PSO](particle-swarm-optimization.md) (1995) | Bandadas, cardúmenes | Directa: todos conocen g_best | Continuos |
| [ACO](ant-colony-optimization.md) (1996) | Hormigas buscando comida | Indirecta: feromona en las aristas | Combinatorios (TSP, rutas) |
| [ABC](artificial-bee-colony.md) (2007) | Abejas recolectoras | Danza: las observadoras eligen fuentes según su calidad | Continuos |

**Como sistema multiagente.** Cada partícula/hormiga/abeja es un [agente](intelligent-agents.md) muy simple en un entorno multiagente **cooperativo** ([Task Environments](task-environments.md)).

## Errores comunes y tips de examen

- La "inteligencia" está en la **interacción**, no en el individuo.
- PSO: comunicación directa (g_best). ACO: indirecta (estigmergia).

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
