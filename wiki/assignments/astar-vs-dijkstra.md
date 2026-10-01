---
title: "A* vs. Dijkstra on the Romania map"
type: assignment
tags: [assignment, search, a-star, dijkstra, python]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# A* vs. Dijkstra on the Romania map (A* vs. Dijkstra en el mapa de Rumania)

> **Summary (EN):** A Python exercise (comments in Spanish) comparing Dijkstra and A* from Arad to Bucharest on the 10-city subgraph of AIMA's Romania map (Figs. 3.16 and 3.18), using straight-line distances as the heuristic. Both find the optimal route Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest with cost 418; Dijkstra expands 9 nodes and A* only 5, because h_SLD is admissible and steers the search toward the goal.

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/assignments/deber_1_IA (1).py](../../raw/assignments/deber_1_IA%20%281%29.py) |
| Lenguaje | Python 3 (export de Colab) |
| Unidad | 2 — Búsqueda informada |
| Datos | Grafo y h\_SLD tomados de AIMA cap. 3.5 (Figs. 3.16 y 3.18), "sin agregar ni cambiar datos" |

## Enunciado (inferido del código)

Comparar Dijkstra y A\* en el ejemplo de Rumania: camino encontrado, costo, nodos expandidos, y conclusión sobre complejidad y eficiencia.

## Qué se implementó

- `dijkstra(grafo, inicio, objetivo, mostrar_pasos)` — frontera = conjunto; elige el menor g; expande; relaja vecinos. Opción para imprimir cada paso.
- `a_estrella(grafo, heuristica, inicio, objetivo)` — igual, pero elige el menor f = g + h.
- `nodo_de_menor_f` (búsqueda lineal del mínimo), `reconstruir_camino` (sigue los padres).
- Ambos prueban la meta **al expandir**, no al generar (correcto para optimalidad).

## Resultados (ejecutado el 2026-10-01)

| | Camino | Costo | Nodos expandidos |
|---|---|---|---|
| Dijkstra | Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 418 | 9 |
| A\* | Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 418 | **5** |

Traza completa de A\* en [A* Search](../concepts/a-star-search.md#ejemplo--arad--bucarest-aima-fig-318).

## Revisión

**Fortalezas**
- Implementaciones limpias, legibles y correctas; misma estructura en ambos algoritmos, lo que hace la comparación justa.
- La conclusión escrita es correcta: Dijkstra explora según g sin saber dónde está la meta (visita Zerind, Timisoara, Oradea, Craiova); A\* usa una h admisible y llega al mismo óptimo explorando menos.

**Puntos a mejorar**
1. La complejidad con esta implementación es O(V²) (búsqueda lineal del mínimo). Con `heapq` sería O((V + E) log V) — mencionarlo enriquece la conclusión.
2. Se podría mostrar que h\_SLD también es **consistente** (necesario para optimalidad en búsqueda en grafo con conjunto de visitados).
3. El grafo es un subgrafo (10 de 20 ciudades), por eso Dijkstra expande solo 9 nodos; en el mapa completo la diferencia sería mayor.

## Conceptos relacionados

- [A* Search](../concepts/a-star-search.md)
- [Uninformed Search](../concepts/uninformed-search.md) (UCS/Dijkstra)
- [Heuristics](../concepts/heuristics.md)
