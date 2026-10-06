---
title: Interactive study tools (quiz and algorithm lab)
type: study
tags: [study, quiz, visualizer, interactive]
sources: [slides-02-problem-solving, slides-04-optimization, book-russell-norvig-aima, paper-kennedy-eberhart-1995-pso]
updated: 2026-10-01
---
# Interactive study tools (Herramientas interactivas)

> **Summary (EN):** Two browser pages built from this wiki. The **Exam Drill** is a multiple-choice quiz (61 questions from the [quiz bank](quiz-bank.md)) that grades you per unit and can replay only your mistakes. The **Algorithm Lab** lets you step through search on the Romania map, minimax/alpha–beta on game trees, and PSO/GA/SA/GD on 2-D functions. Both work on a phone.

## Dónde abrirlas

| Herramienta | Enlace publicado (privado, tu cuenta de Claude) | Archivo en el repo |
|---|---|---|
| **IA Exam Drill** (quiz) | https://claude.ai/artifact/9hSKYonRePXtWC6XArdtQU | [`study-tools/web/quiz.html`](../../study-tools/web/quiz.html) (generado) |
| **Algorithm Lab** (visualizadores) | https://claude.ai/artifact/UGK26c8fFaBuEY4ADznnvC | [`study-tools/web/visualizer.html`](../../study-tools/web/visualizer.html) |

Los enlaces publicados son privados: solo tú (o quien compartas desde el menú *Share*) los puede abrir. Los archivos `.html` también funcionan sin internet: descárgalos y ábrelos en el navegador (sin internet solo cambian las fuentes).

## IA Exam Drill (quiz)

- Elige unidades (chips), cantidad (10 / 20 / todas) y pulsa *Start*. Teclas **1–4** para responder, **Enter** para seguir.
- Al final: puntaje por unidad y lista de repaso con la explicación y el enlace a la página de la wiki.
- **Only my mistakes:** repite solo las preguntas que fallaste (se guarda en tu navegador).
- Las preguntas están en inglés, como en el examen; la explicación remite a la página de la wiki, que está en español.
- Para agregar preguntas: edita [quiz-bank.md](quiz-bank.md) (formato en su resumen) y ejecuta `python3 tools/build_study.py`. Las mismas preguntas también entran al mazo de [Anki](flashcards.md) con el tag `quiz`.

## Algorithm Lab (visualizadores)

Úsalo así: pulsa **Step** y, *antes* de volver a pulsar, di en voz alta (en inglés) qué nodo se expande y por qué. Esa es exactamente la explicación que piden en el examen.

| Pestaña | Qué muestra | Qué observar |
|---|---|---|
| **Search · Romania** | BFS, DFS, UCS, greedy y A\* desde cualquier ciudad hasta Bucharest, con la frontera (g, h, f) y el camino final | Desde Arad, greedy y BFS devuelven Sibiu→Fagaras (450 km) y A\*/UCS devuelven Rimnicu→Pitesti (418 km). A\* expande 5 nodos y UCS 12 en el mapa completo de 20 ciudades (en el subgrafo de 10 ciudades de la [tarea A\* vs Dijkstra](../assignments/astar-vs-dijkstra.md) eran 9). BFS aplica el *goal test* al **generar** y A\* al **expandir**: por eso A\* ve Bucharest con f = 450 en la frontera y aun así sigue hasta encontrar 418. |
| **Games · minimax & α–β** | El árbol de AIMA Fig. 6.2 y los problemas 5 y 6 de [Práctica U2](practice-unit-2-search.md), más árboles aleatorios; muestra [α, β] en cada nodo y las ramas podadas en gris | AIMA: raíz 3, se podan 2 hojas. Práctica 5: se podan 7, 1 y 5. Práctica 6: raíz 5, se podan la hoja 9 y el subárbol G. Cambia a *Plain minimax* para ver que el valor de la raíz no cambia. |
| **Optimization** | PSO, GA binario, SA y GD sobre la función del curso f = (x+2)² + (y−2)² + 10, Rastrigin y Ackley; mapa de calor (más claro = mejor) y curva del mejor f | En la función del curso todos llegan a (−2, 2) con f = 10. En Rastrigin (muchos mínimos locales), PSO llega a f = 0, mientras que GD con η = 0.002 se detiene en el mínimo local más cercano (por ejemplo, f ≈ 2 en (1, −1)) y con η = 0.1 rebota sin converger. Con SA y α = 0.8 se ve el enfriamiento demasiado rápido del script de clase. Con PSO y w = 0 se pierde el impulso (*momentum*). |

Los resultados de la pestaña de búsqueda y de juegos se verificaron contra la [comparación de búsqueda](search-algorithms-comparison.md) y las soluciones de la práctica; los valores coinciden.

## Relacionado

- [A* Search](../concepts/a-star-search.md) · [Uninformed Search](../concepts/uninformed-search.md) · [Alpha–Beta Pruning](../concepts/alpha-beta-pruning.md)
- [Particle Swarm Optimization](../concepts/particle-swarm-optimization.md) · [Genetic Algorithms](../concepts/genetic-algorithms.md) · [Simulated Annealing](../concepts/simulated-annealing.md) · [Gradient Descent](../concepts/gradient-descent.md)
- [Study plan](study-plan.md) · [Flashcards](flashcards.md) · [Quiz bank](quiz-bank.md)

## Fuentes

- Mapa de Rumania, distancias y h_SLD: AIMA 4e Fig. 3.1 y Fig. 3.16 ([book-russell-norvig-aima](../sources/book-russell-norvig-aima.md)); también [slides-02](../sources/slides-02-problem-solving.md).
- Árbol de juego: AIMA 4e Fig. 6.2 / Fig. 6.5.
- Ecuación de PSO: [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md) con inercia w (Shi & Eberhart 1998, conocimiento general); función del curso: [slides-04](../sources/slides-04-optimization.md).
