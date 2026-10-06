---
title: "Code — Prolog examples (01_Code)"
type: source
tags: [code, prolog]
sources: [code-prolog-examples, slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# Code — Prolog examples from the lecture (Ejemplos de Prolog, `01_Code`)

> **Summary (EN):** The eight Prolog programs shown in the Prolog lecture, originally in `01_Code (1).zip` (macOS metadata dropped when unzipping). `family.pl` is the starting point for Prolog Lab 01; the others illustrate recursion, lists, mutual recursion, a buggy permutation check, a binary search tree and N-Queens.

## Ficha

| Archivo | Contenido | Slide |
|---|---|---|
| [family.pl](../../raw/code/prolog_examples/family.pl) | Hechos `parent/2`, `male/1`, `female/1`; reglas `father`, `grandparent`, `sibling`, `ancestor`; consultas sugeridas | 12–13, 29 |
| [factorial.pl](../../raw/code/prolog_examples/factorial.pl) | `factorial/2` recursivo | 17 |
| [fibonacci.pl](../../raw/code/prolog_examples/fibonacci.pl) | `fibo/2` ingenuo (exponencial) | 18 |
| [isEven.pl](../../raw/code/prolog_examples/isEven.pl) | `isEven/2` e `isOdd/2` mutuamente recursivos sobre la longitud de una lista | 20 |
| [isPerm.pl](../../raw/code/prolog_examples/isPerm.pl) | `isPerm/2` vía inclusión mutua (bug: es igualdad de conjuntos) | 21 |
| [predicates.pl](../../raw/code/prolog_examples/predicates.pl) | `isEven`, `isOdd`, `isPerm`, `isInc`, `isMember`, más `isMerged/3` e `isTail/2` (intercalar listas) | — |
| [binaryTree.pl](../../raw/code/prolog_examples/binaryTree.pl) | Árbol binario de búsqueda: `member2/2`, `insert/3` | 22 |
| [queens.pl](../../raw/code/prolog_examples/queens.pl) | N-Reinas con `select/3` y `threat/2` | 25–26 |

## Conceptos que alimenta

- [Prolog](../concepts/prolog.md)
- [Recursion and Lists in Prolog](../concepts/prolog-recursion-and-lists.md)
- [N-Queens](../concepts/n-queens.md)
- [Prolog Lab 01](../assignments/prolog-lab-01-family.md)

## Notas

- `predicates.pl` incluye `isMerged/3` e `isTail/2`, que no se explican en las slides; generan *singleton warnings* (`Y`, `XS`) igual que `isEven`.
- Los archivos datan de 2011 y 2023 (código heredado del curso); `family.pl` fue actualizado en 2026 para el laboratorio.
