---
title: Constraint Satisfaction Problems
type: concept
tags: [search, csp]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Constraint Satisfaction Problems (Problemas de satisfacción de restricciones, CSP)

> **Summary (EN):** In a CSP, states have internal structure: variables X₁…Xₙ, domains D₁…Dₙ and constraints C. A solution is a complete and consistent assignment. Unlike black-box search, CSP solvers exploit this structure: backtracking search assigns one variable at a time, and constraint propagation (forward checking, arc consistency) plus ordering heuristics such as Minimum Remaining Values prune the domains before failures happen. Examples: Sudoku, school timetables, N-Queens.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Variables X | Variables | Lo que hay que asignar. |
| Domains D | Dominios | Valores posibles de cada variable. |
| Constraints C | Restricciones | Condiciones que deben cumplir las asignaciones. |
| Consistent assignment | Asignación consistente | No viola ninguna restricción. |
| Complete assignment | Asignación completa | Toda variable tiene valor. |
| Backtracking search | Búsqueda con retroceso | DFS que asigna una variable por nivel y retrocede al fallar. |
| Forward checking | Comprobación hacia adelante | Al asignar X, quitar valores incompatibles de los vecinos. |
| Arc consistency (AC-3) | Consistencia de arcos | Para cada valor de Xᵢ existe un valor compatible en Xⱼ. |
| Minimum Remaining Values (MRV) | Mínimos valores restantes | Elegir primero la variable con menos valores posibles. |

## Explicación

**Diferencia con la búsqueda estándar.** En búsqueda clásica los estados son cajas negras; solo importa llegar a la meta. En un CSP los estados tienen **estructura** (representación [factorizada](state-representation.md)) y la meta es: todas las variables asignadas, sin violar restricciones.

**Ejemplos de la clase.** Sudoku (los números no se repiten en filas, columnas ni cajas); horario escolar (deportes no después del almuerzo). Del curso: [N-Reinas](n-queens.md) — variables = columna de la reina de cada fila, dominio = {1..N}, restricciones = no misma columna ni diagonal.

**Backtracking (complemento, AIMA §5.3).**

```
function BACKTRACK(assignment, csp):
    if assignment is complete: return assignment
    var ← SELECT-UNASSIGNED-VARIABLE(csp)          # e.g. MRV
    for value in ORDER-DOMAIN-VALUES(var):          # e.g. least-constraining value
        if value is consistent with assignment:
            assignment[var] ← value
            inferences ← INFERENCE(csp, var)        # forward checking / AC-3
            if inferences ≠ failure:
                result ← BACKTRACK(assignment, csp)
                if result ≠ failure: return result
            remove var (and inferences) from assignment
    return failure
```

El `solve(chessboard, column, n)` de la tarea de N-Reinas es exactamente este esquema sin propagación.

**Propagación de restricciones** (reducir dominios *antes* de asignar):
- **Forward checking:** al asignar una variable, se eliminan de los vecinos los valores incompatibles; si un dominio queda vacío, se retrocede ya.
- **Arc consistency:** se hace consistente cada arco Xᵢ → Xⱼ; detecta fallos antes que forward checking.
- **MRV:** asignar primero la variable más restringida (*fail-first*).

## Errores comunes y tips de examen

- MRV elige **variable**; *least-constraining value* (complemento) elige **valor**.
- Forward checking no detecta todos los conflictos entre variables aún no asignadas; arc consistency sí detecta más.
- "Generate & test" (generar asignaciones completas y luego comprobar) es mucho peor que "test as you go" — ver la tabla de inferencias en [N-Queens](n-queens.md).

## Relacionado

- [N-Queens](n-queens.md)
- [State Representation](state-representation.md)
- [Uninformed Search](uninformed-search.md) (DFS)
- [Prolog](prolog.md) (Prolog hace backtracking automáticamente)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 23–24.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 5 (pseudocódigo: complemento).
