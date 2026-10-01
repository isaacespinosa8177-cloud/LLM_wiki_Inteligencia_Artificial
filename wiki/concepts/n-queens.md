---
title: N-Queens
type: concept
tags: [csp, backtracking, prolog, worked-example]
sources: [slides-xx-logic-programming-prolog, slides-02-problem-solving, code-prolog-examples]
updated: 2026-10-01
---
# N-Queens (El problema de las N reinas)

> **Summary (EN):** Place N queens on an N×N board so that no two attack each other. It appears twice in the course — in Prolog (queens.pl, select/3 + threat/2) and in Python (backtracking in Homework 1) — and it is the canonical CSP example. Representing the board as a permutation of 1..N guarantees one queen per row and column, leaving only diagonals to check. Solution counts: N=4→2, 5→10, 6→4, 7→40, 8→92, 9→352, 10→724; N=2 and N=3 have none.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Queen attack | Ataque de reina | Misma fila, columna o diagonal. |
| Permutation encoding | Codificación por permutación | `Qs[i]` = columna de la reina de la fila i. |
| Diagonal test | Prueba de diagonal | \|Qᵢ − Qⱼ\| = \|i − j\|. |
| Generate and test | Generar y probar | Construir el tablero completo y luego verificar. |
| Test as you go | Probar mientras se construye | Verificar cada reina al colocarla (backtracking). |

## Explicación

**Como CSP.** Variables: la reina de cada fila (o columna). Dominio: {1..N}. Restricciones: distinta columna y distinta diagonal. Ver [CSP](constraint-satisfaction-problems.md).

**La representación hace la mitad del trabajo.** Si `Qs` es una permutación de 1..N, hay una reina por fila (posición en la lista) y una por columna (valores distintos). Solo quedan las diagonales.

### Versión Prolog (`queens.pl`, slides XX s25)

```prolog
queens(N, Qs) :- range(1, N, Ns), queens(Ns, [], Qs).

queens([], Qs, Qs).
queens(UnplacedQs, SafeQs, Qs) :-
    select(Q, UnplacedQs, NewUnplaced),     % choice point
    \+ threat(Q, SafeQs),                   % test as you go
    queens(NewUnplaced, [Q|SafeQs], Qs).

threat(X, Xs) :- threat(X, 1, Xs).
threat(X, N, [Y|_]) :- X is Y + N ; X is Y - N.   % same diagonal
threat(X, N, [_|Ys]) :- N1 is N + 1, threat(X, N1, Ys).
```

`?- queens(8, Qs).` → `Qs = [4,2,7,3,6,8,5,1]`; `findall` cuenta 92 soluciones.

### Versión Python (Deber 1, backtracking por columnas)

```python
def validate(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(board, col, n):
    if col == n: return True
    for row in range(n):
        if validate(board, row, col):
            board[col] = row
            if solve(board, col + 1, n): return True
    return False
```

### Generate & test vs. test as you go (slides XX s27)

Inferencias para enumerar todas las soluciones (SWI-Prolog 9.2.9):

| N | Generate & test | Interleaved | Ratio |
|---|---|---|---|
| 4 | 425 | 200 | 2.1× |
| 6 | 15 358 | 3 090 | 5.0× |
| 8 | 1 058 230 | 61 770 | 17.1× |
| 10 | 113 230 594 | 1 468 869 | **77.1×** |

Misma lógica; la segunda **poda** antes un tablero malo. Es "Algorithm = Logic + Control" en acción.

## Errores comunes y tips de examen

- La prueba de diagonal es `|Δfila| == |Δcolumna|`.
- N = 2 y N = 3 no tienen solución; N = 6 tiene menos (4) que N = 5 (10).
- En Prolog, `select/3` es el punto de elección: el *backtracking* lo hace el motor, no el programador.

## Relacionado

- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md)
- [Prolog](prolog.md)
- [State Representation](state-representation.md)
- [Deber 1](../assignments/deber-1-search-problems.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 25–27.
- [Code — Prolog examples](../sources/code-prolog-examples.md) (`queens.pl`).
- [Deber 1](../assignments/deber-1-search-problems.md) (versión Python).
