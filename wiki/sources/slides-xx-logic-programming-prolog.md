---
title: "Slides XX — Logic Programming with Prolog"
type: source
tags: [slides, logic, prolog]
sources: [slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# Slides XX — Logic Programming with Prolog (Programación lógica con Prolog)

> **Summary (EN):** A 31-slide lecture that goes from propositional and first-order logic to Horn clauses, backward chaining and Prolog ("Algorithm = Logic + Control", Kowalski 1979). It teaches SWI-Prolog hands-on: terms, facts, rules, queries, unification, SLD resolution, arithmetic with is/2, recursion (factorial, Fibonacci with accumulators), lists, negation as failure and the cut, useful built-ins, an N-Queens case study, debugging, and the Prolog Lab 01 assignment (family knowledge base with plunit tests).

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/slides/XX_Logic Programming with Prolog (1).pptx](../../raw/slides/XX_Logic%20Programming%20with%20Prolog%20%281%29.pptx) |
| Tipo | Diapositivas de clase, 31 slides (mucho código) |
| Unidad | 3 — Lógica y programación lógica |
| Código asociado | [code-prolog-examples](code-prolog-examples.md) |
| Tarea | [Prolog Lab 01](../assignments/prolog-lab-01-family.md) |
| Lecturas | AIMA 4e §7.5 y §9.4; Luger 6e §14.2–14.3; Bratko; Sterling & Shapiro |

## Resumen por secciones

- **Slide 2 — Dónde estamos.** Lógica proposicional (decidible, no puede decir "todo") → primer orden (objetos y cuantificadores, indecidible) → cláusulas de Horn (inferencia barata) → Prolog (Horn + backward chaining + unificación).
- **Slide 3 — CNF.** Literal, cláusula (disyunción de literales), CNF (conjunción de cláusulas). La resolución es refutation-complete y necesita forma clausal (AIMA Fig. 7.12).
- **Slides 4–5 — Cláusulas de Horn.** A lo sumo un literal positivo. Definite clause (regla), fact, goal clause (consulta). Ventajas: se leen como implicaciones, permiten encadenamiento, entailment lineal en KB proposicional. `P ∨ Q` no tiene forma de Horn. Grafo AND–OR (AIMA Fig. 7.16).
- **Slide 6 — Backward chaining.** Desde la consulta, probar el cuerpo de una cláusula que coincide; profundidad primero, izquierda a derecha. Árbol de prueba de `Criminal(West)` (AIMA Fig. 9.7).
- **Slide 7 — De FOL a Prolog.** Implicación escrita al revés (`C :- A, B.`), mayúscula = variable, cuantificadores implícitos (universales), coma = "y", punto y coma = "o", punto final. Ejemplo completo del crimen de West.
- **Slide 8 — Qué es Prolog.** *Programmation en logique*, Marsella 1972 (Colmerauer y Roussel), teoría de Kowalski (Edimburgo). Se declara qué es verdad; el intérprete busca la prueba.
- **Slides 9–11 — SWI-Prolog.** Instalación (brew / winget / apt), `swipl`, SWISH en el navegador, primera sesión, prompts `?-` y `|:`, `;` para más soluciones.
- **Slides 12–13 — Anatomía y consultas.** Átomos, números, variables, términos compuestos; hechos, reglas, consultas; nombre/aridad (`father/2`). `family.pl`. `findall/3` vs `setof/3`, `\+`.
- **Slide 14 — Unificación.** Pattern matching bidireccional; sin *occurs check* (`X = f(X)` crea término cíclico).
- **Slide 15 — Ejecución (SLD resolution).** Meta más a la izquierda, cláusulas en orden de archivo, backtracking. El orden de cláusulas/metas cambia el comportamiento; la recursión por la izquierda causa *stack overflow*; `:- table path/2.` lo arregla.
- **Slide 16 — Aritmética.** `=/2` unifica, `is/2` evalúa; `=:=`, `=\=`, `=<`, `>=`, `==`, `\=`.
- **Slides 17–18 — Recursión.** Factorial; Fibonacci ingenuo (exponencial) vs. con acumulador (lineal) vs. tabling.
- **Slides 19–22 — Listas y ejemplos.** `[H|T]`, `append/3` en reversa, `mymember`, `myappend`, `mylen`; `isEven/isOdd` (warnings de singleton); `isPerm` y su bug (igualdad de conjuntos ≠ permutación); árbol binario de búsqueda.
- **Slide 23 — Negación por fallo y corte.** `\+` bajo supuesto de mundo cerrado; solo negar metas con variables ligadas. `!` compromete elecciones; el bug clásico de `max/3`; preferir `( C -> T ; E )`.
- **Slide 24 — Built-ins.** `findall`, `bagof`, `setof`, `aggregate_all`, `forall`, `between`, `select`, `permutation`, `length`, `msort`, `format`, `time`, `listing`, `make`.
- **Slides 25–27 — N-Reinas.** Representación como permutación; `select/3` como punto de elección; conteo de soluciones (N=8 → 92); *generate & test* vs. *test as you go* (77× menos inferencias para N=10).
- **Slide 28 — Depuración.** `trace/0` con los cuatro puertos (Call, Exit, Redo, Fail). Errores típicos.
- **Slides 29–30 — Prolog Lab 01.** Ver [página de la tarea](../assignments/prolog-lab-01-family.md).
- **Slide 31 — Lecturas.** AIMA cap. 7.5 y 9.4; Luger 14.2–14.3; Bratko; Sterling & Shapiro; swi-prolog.org, SWISH, learnprolognow.org, metalevel.at/prolog.

## Ideas clave

1. **Algorithm = Logic + Control**: el programador da la lógica (cláusulas), Prolog da el control (SLD, profundidad primero).
2. SLD resolution es completa, pero la **estrategia de búsqueda de Prolog no lo es** (bucles por recursión izquierda).
3. La representación hace la mitad del trabajo (N-Reinas como permutación).

## Conceptos que alimenta

- [Propositional and First-Order Logic](../concepts/propositional-and-first-order-logic.md)
- [Horn Clauses and Backward Chaining](../concepts/horn-clauses-and-backward-chaining.md)
- [Unification](../concepts/unification.md)
- [Prolog](../concepts/prolog.md)
- [Recursion and Lists in Prolog](../concepts/prolog-recursion-and-lists.md)
- [N-Queens](../concepts/n-queens.md)

## Notas y discrepancias

- Contradice la slide 9 de [slides 01](slides-01-introduction-to-ai.md), que atribuye Prolog a Dennis Ritchie. Esta presentación (slide 8) es la correcta. Ver [errata](../study/errata.md).
- Slide 22 menciona que `binaryTree.pl` original en `01_Code` tiene cláusulas extra para hijos vacíos que son innecesarias.
