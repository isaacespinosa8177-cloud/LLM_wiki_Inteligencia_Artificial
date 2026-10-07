---
title: N-Queens
type: concept
tags: [csp, backtracking, prolog, worked-example]
sources: [slides-xx-logic-programming-prolog, slides-02-problem-solving, code-prolog-examples]
updated: 2026-10-07
---
# N-Queens (El problema de las N reinas)

> **Summary (EN):** Place N queens on an N×N chessboard so that no two attack each other (a queen attacks along its row, column and diagonals). It appears twice in the course, in Prolog (queens.pl with select/3 and threat/2) and in Python (backtracking in Homework 1), and it is the classic CSP example. Storing the board as a permutation of 1..N (one different row per column) already guarantees one queen per row and column, so only diagonals must be checked. Number of solutions: N=4→2, 5→10, 6→4, 7→40, 8→92, 9→352, 10→724; N=2 and N=3 have none.

> **En palabras simples (ES):** Hay que poner N reinas en un tablero de N×N sin que ninguna ataque a otra (una reina ataca en su fila, su columna y sus diagonales). Se colocan **una por columna**: si la nueva reina choca con alguna anterior, pruebas otra fila; si ninguna fila sirve, regresas a la columna anterior y mueves esa reina. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Queen attack | Ataque de reina | Dos reinas chocan si están en la misma fila, columna o diagonal. |
| Permutation encoding | Codificación por permutación | Una lista donde la posición i dice dónde está la reina i, y no hay números repetidos. |
| Diagonal test | Prueba de diagonal | Dos reinas están en diagonal si \|diferencia de filas\| = \|diferencia de columnas\|. |
| Generate and test | Generar y probar | Armar el tablero completo y recién al final revisar si sirve. |
| Test as you go | Probar mientras se construye | Revisar cada reina en el momento de ponerla (backtracking). |

## Explicación

### 1. Como CSP

- **Variables:** la posición de la reina de cada columna (o de cada fila).
- **Dominio:** {1..N}, las filas posibles.
- **Reglas:** dos reinas no pueden compartir fila ni diagonal. Ver [CSP](constraint-satisfaction-problems.md).

### 2. Una buena representación hace la mitad del trabajo

Si guardas el tablero como una **permutación** de 1..N, por ejemplo `[2, 4, 1, 3]`:
- la posición en la lista es la columna → **una reina por columna**;
- todos los números son distintos → **una reina por fila**.

Solo queda revisar las **diagonales**: dos reinas chocan en diagonal si la diferencia de filas es igual a la diferencia de columnas. Ejemplo: reinas en (columna 1, fila 2) y (columna 3, fila 4): diferencia de columnas 2, diferencia de filas 2 → **chocan**.

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

Cómo leerlo: `select/3` elige una fila Q que todavía no se usó (si después falla, Prolog vuelve y elige otra); `\+ threat(Q, SafeQs)` comprueba que Q no esté en diagonal con las reinas ya puestas; si todo va bien, sigue con las que faltan. `threat` revisa si alguna reina ya puesta está a N columnas de distancia y a N filas de diferencia (X = Y + N o X = Y − N).

`?- queens(8, Qs).` → `Qs = [4,2,7,3,6,8,5,1]`; con `findall` se cuentan las 92 soluciones.

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

Cómo leerlo: `validate` revisa que ninguna reina anterior esté en la misma fila ni en diagonal. `solve` pone una reina en la columna `col`, prueba cada fila segura y sigue con la siguiente columna; si ninguna fila funciona, devuelve `False` y la columna anterior prueba otra fila.

### 3. Generar todo vs. probar mientras construyes (slides XX s27)

Número de pasos de inferencia de Prolog para encontrar **todas** las soluciones (SWI-Prolog 9.2.9):

| N | Generar y probar | Probar mientras se construye | Cuántas veces más rápido |
|---|---|---|---|
| 4 | 425 | 200 | 2.1× |
| 6 | 15 358 | 3 090 | 5.0× |
| 8 | 1 058 230 | 61 770 | 17.1× |
| 10 | 113 230 594 | 1 468 869 | **77.1×** |

Las dos versiones tienen **la misma lógica**; la segunda descarta antes un tablero malo, sin terminar de armarlo. Es "Algoritmo = Lógica + Control" en acción: cambiar solo el control (el orden) ahorra muchísimo trabajo.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Hay que poner N reinas en un tablero de N×N sin que ninguna ataque a otra (una reina ataca en su fila, su columna y sus diagonales). Se colocan **una por columna**: si la nueva reina choca con alguna anterior, pruebas otra fila; si ninguna fila sirve, regresas a la columna anterior y mueves esa reina.

**Antes de empezar: qué significa cada cosa**

| Palabra / símbolo | Qué es (en simple) | English |
|---|---|---|
| Fila, columna | posición de la reina en el tablero | row, column |
| Diagonal | dos reinas están en diagonal si la diferencia de filas es igual a la diferencia de columnas | diagonal |
| \|a − b\| | valor absoluto: la diferencia sin signo (\|2 − 5\| = 3) | absolute value |
| Permutación | una lista con cada número una sola vez, p. ej. (2, 4, 1, 3): la reina de la columna 1 va en la fila 2, etc. | permutation |
| Backtracking | deshacer la última reina y probar otra posición | backtracking |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Place queens column by column, starting with the first column.
   - *ES:* Empieza por la primera columna.
2. In the current column, try each row. A row is safe if no earlier queen is in the same row and none is on a diagonal (|row difference| = |column difference|).
   - *ES:* Prueba cada fila. Es segura si ninguna reina anterior está en esa fila ni en diagonal.
3. If the row is safe → place the queen and go to the next column. If that later fails → remove the queen and try the next row.
   - *ES:* Si es segura, pon la reina y sigue con la siguiente columna. Si más adelante no hay salida, quítala y prueba la fila siguiente.
4. If no row works → go back to the previous column (backtrack).
   - *ES:* Si ninguna fila sirve, regresa a la columna anterior y mueve esa reina.
5. When all N columns have a queen → that is a solution.
   - *ES:* Cuando todas las columnas tienen reina, encontraste una solución.

**Ejemplo con números:** N = 4. Si empiezo con la reina de la columna 1 en la fila 1, después de probar todo no hay salida y regreso hasta la columna 1. Con la reina de la columna 1 en la fila 2 sale la solución **(2, 4, 1, 3)**. Comprobación de una pareja: columnas 1 y 3 → filas 2 y 1 → diferencia de filas 1, diferencia de columnas 2 → no están en diagonal ✓.

**Say it in the exam (EN):** "N-queens places N queens on an N×N board so that none attack each other. Representing the board as a permutation (one row number per column, all different) guarantees one queen per row and per column, so only the diagonals must be checked: two queens attack diagonally when |row difference| = |column difference|. Backtracking checks each queen as it is placed and undoes the last queen when no row is safe."

**Dilo así (ES):** "N-reinas pone N reinas en un tablero N×N sin que se ataquen. Si el tablero es una permutación (un número de fila distinto por columna), ya hay una reina por fila y por columna, y solo hay que revisar diagonales: dos reinas chocan en diagonal si la diferencia de filas es igual a la de columnas. Backtracking revisa cada reina al colocarla y deshace la última cuando ninguna fila sirve."

## Errores comunes y tips de examen

- La prueba de diagonal es `|diferencia de filas| == |diferencia de columnas|`.
- N = 2 y N = 3 no tienen solución; N = 6 tiene menos soluciones (4) que N = 5 (10).
- En Prolog, `select/3` es el punto donde se elige: el *backtracking* lo hace Prolog solo, no el programador.

## Relacionado

- [Constraint Satisfaction Problems](constraint-satisfaction-problems.md)
- [Prolog](prolog.md)
- [State Representation](state-representation.md)
- [Deber 1](../assignments/deber-1-search-problems.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 25–27.
- [Code — Prolog examples](../sources/code-prolog-examples.md) (`queens.pl`).
- [Deber 1](../assignments/deber-1-search-problems.md) (versión Python).
