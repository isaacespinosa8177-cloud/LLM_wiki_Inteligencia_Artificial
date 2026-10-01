---
title: Constraint Satisfaction Problems
type: concept
tags: [search, csp]
sources: [slides-02-problem-solving, book-russell-norvig-aima]
updated: 2026-10-01
---
# Constraint Satisfaction Problems (Problemas de satisfacción de restricciones, CSP)

> **Summary (EN):** A CSP opens up the "black-box" state: variables X₁…Xₙ, domains D₁…Dₙ and constraints C; a solution is a complete and consistent assignment. Because the structure is visible, general (domain-independent) techniques work: constraint propagation (node, arc, path, k-consistency; AC-3), backtracking search with MRV/degree variable ordering and least-constraining-value ordering, forward checking or MAC during search, conflict-directed backjumping, min-conflicts local search, and exploiting graph structure (tree-structured CSPs are solvable in O(nd²)). Examples: map coloring, Sudoku, N-Queens, job-shop scheduling.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Variables X / Domains D / Constraints C | Variables / dominios / restricciones | Lo que se asigna / valores posibles / condiciones. |
| Constraint ⟨scope, rel⟩ | Restricción | Tupla de variables + relación permitida, p. ej. ⟨(X₁, X₂), X₁ > X₂⟩. |
| Consistent / complete assignment | Asignación consistente / completa | No viola restricciones / todas las variables tienen valor. |
| Constraint graph | Grafo de restricciones | Nodos = variables, aristas = restricciones binarias. |
| Unary / binary / global constraint | Restricción unaria / binaria / global | 1 variable / 2 variables / número arbitrario (p. ej. **Alldiff**). |
| Node / arc / path / k-consistency | Consistencia de nodo / arco / camino / k | Niveles de propagación local. |
| AC-3 | AC-3 | Algoritmo clásico de consistencia de arcos. |
| MRV / degree heuristic | Mínimos valores restantes / heurística de grado | Qué variable asignar primero. |
| Least-constraining value (LCV) | Valor menos restrictivo | Qué valor probar primero. |
| Forward checking / MAC | Comprobación hacia adelante / mantener consistencia de arcos | Inferencia durante la búsqueda. |
| Backjumping | Salto atrás | Retroceder a la variable culpable, no a la última. |
| Min-conflicts | Mínimos conflictos | Búsqueda local para CSP. |
| Cycle cutset | Conjunto de corte de ciclos | Variables cuya eliminación deja un árbol. |

## Explicación

**Por qué formular algo como CSP** (AIMA §5.1). En búsqueda atómica solo se puede preguntar "¿es esto la meta?". En un CSP, en cuanto una asignación parcial viola una restricción se descartan **de una vez todas sus extensiones**, y se sabe **qué** variables causan el problema. Ejemplo: tras fijar SA = blue en el mapa de Australia, los 5 vecinos pasan de 3⁵ = 243 combinaciones a 2⁵ = 32 (−87 %). Resolver CSPs es NP-completo en general.

**Ejemplos.**
- **Coloreo del mapa de Australia:** X = {WA, NT, Q, NSW, V, SA, T}, D = {red, green, blue}, restricciones SA ≠ WA, SA ≠ NT, … (9 fronteras).
- **Sudoku:** 81 variables, dominio {1..9}, **27 Alldiff** (9 filas, 9 columnas, 9 cajas).
- **N-Reinas:** Qᵢ = fila de la reina de la columna i ([N-Queens](n-queens.md)).
- **Job-shop scheduling:** variable = tiempo de inicio de cada tarea; restricciones de precedencia (`AxleF + 10 ≤ WheelRF`) y disyuntivas (dos tareas no usan la misma herramienta a la vez).
- **Criptoaritmética:** TWO + TWO = FOUR con Alldiff(F, T, U, W, R, O) y variables auxiliares de acarreo.

**Variantes:** dominios discretos finitos (lo usual), infinitos (enteros: restricciones lineales tienen algoritmos; no lineales son indecidibles), continuos (programación lineal). Restricciones **absolutas** vs. **de preferencia** (→ problema de optimización con restricciones, COP).

### 1. Propagación de restricciones (AIMA §5.2)

| Nivel | Definición | Ejemplo |
|---|---|---|
| **Node consistency** | Todo valor cumple las restricciones unarias | Si SA no puede ser verde, D_SA = {red, blue} |
| **Arc consistency** | Para cada valor de Xᵢ existe un valor de Xⱼ compatible | Y = X² con dígitos: X ∈ {0,1,2,3}, Y ∈ {0,1,4,9} |
| **Path consistency** | Para cada asignación consistente de {Xᵢ, Xⱼ} existe un valor de Xₘ compatible con ambos | Detecta que Australia con 2 colores es imposible (WA, SA, NT se tocan) — arc consistency no lo detecta |
| **k-consistency** | Para k−1 variables consistentes siempre hay valor para la k-ésima | 1 = nodo, 2 = arco, 3 = camino (binario). Fuertemente n-consistente → se resuelve sin backtracking en O(n²d), pero establecerlo es exponencial |

**AC-3:** cola con todos los arcos (cada restricción binaria da dos). Saca un arco (Xᵢ, Xⱼ) y **REVISE**: borra de Dᵢ los valores sin soporte en Dⱼ. Si Dᵢ cambió, vuelve a encolar los arcos (Xₖ, Xᵢ) de sus vecinos. Si un dominio queda vacío → no hay solución. Complejidad **O(c·d³)** (c arcos, dominio d). AC-3 resuelve Sudokus fáciles por sí solo; los difíciles requieren búsqueda.

**Restricciones globales:** Alldiff con m variables y n valores disponibles en total es imposible si m > n (detecta que {WA = red, NSW = red} falla). **Atmost / bounds propagation** para recursos: F₁ ∈ [0, 165], F₂ ∈ [0, 385], F₁ + F₂ = 420 → F₁ ∈ [35, 165], F₂ ∈ [255, 385].

### 2. Backtracking search (AIMA §5.3)

Una búsqueda en profundidad ingenua tendría n!·dⁿ hojas; como los CSP son **conmutativos** (el orden de asignación no importa), basta asignar **una variable por nivel** → dⁿ hojas.

**Ordenar variables y valores:**
- **MRV** (*most constrained variable*, *fail-first*): la variable con menos valores legales. Si alguna tiene 0, el fallo se detecta ya.
- **Degree heuristic** (desempate): la variable con más restricciones sobre variables no asignadas (SA tiene grado 5 en Australia).
- **LCV**: el valor que elimina menos opciones de los vecinos (*fail-last*).
- ¿Por qué variable *fail-first* y valor *fail-last*? Toda variable debe asignarse igual, así que conviene fallar pronto; pero solo necesitamos **una** solución, así que conviene probar primero el valor más prometedor.

**Inferencia durante la búsqueda:**
- **Forward checking:** al asignar X, establece consistencia de arco *solo para X*: borra de cada vecino no asignado los valores incompatibles. Detecta {WA = red, Q = green, V = blue} como inconsistente (SA se queda sin valores). **No** detecta que NT y SA quedan ambos con solo {blue} siendo vecinos.
- **MAC (Maintaining Arc Consistency):** tras asignar Xᵢ llama a AC-3 empezando por los arcos (Xⱼ, Xᵢ) y **propaga recursivamente**: estrictamente más fuerte que forward checking.

**Backtracking inteligente:** el *backtracking cronológico* vuelve a la última variable (¡recolorear Tasmania no arregla SA!). **Backjumping** vuelve a la variable más reciente del **conflict set**; **conflict-directed backjumping** usa conjuntos de conflicto más profundos. Todo lo que poda el backjumping simple ya lo poda forward checking. **Constraint learning** guarda los conflictos encontrados (*no-goods*) para no repetirlos.

### 3. Búsqueda local: min-conflicts (AIMA §5.4)

Empieza con una asignación **completa** (con conflictos); repite: elegir una variable en conflicto al azar y darle el valor que **minimiza el número de conflictos**. Resuelve el problema del **millón de reinas en ~50 pasos** (sin contar la asignación inicial) y redujo la planificación semanal del telescopio Hubble de 3 semanas a ~10 minutos. Mejoras: búsqueda en mesetas, tabu search, **constraint weighting**. Sirve para "reparar" un plan cuando cambia el problema.

### 4. Estructura del problema (AIMA §5.5)

- **Subproblemas independientes** (componentes conexas, como Tasmania): trabajo O(dᶜ·n/c), lineal en n.
- **CSP con grafo árbol:** ordenar topológicamente, hacer *directional arc consistency* de hojas a raíz y asignar de raíz a hojas **sin backtracking**: **O(n·d²)**.
- **Cutset conditioning:** asignar un *cycle cutset* S (quitar SA deja un árbol) y resolver el árbol para cada asignación de S: O(d^c·(n−c)·d²).
- **Tree decomposition:** agrupar variables en nodos que forman un árbol; eficiente si el *tree width* es pequeño.

## Pseudocódigo

```
function BACKTRACKING-SEARCH(csp) returns a solution or failure
    return BACKTRACK(csp, {})

function BACKTRACK(csp, assignment) returns a solution or failure
    if assignment is complete: return assignment
    var ← SELECT-UNASSIGNED-VARIABLE(csp, assignment)          # MRV, degree
    for each value in ORDER-DOMAIN-VALUES(csp, var, assignment): # LCV
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences ← INFERENCE(csp, var, assignment)        # forward checking / MAC
            if inferences ≠ failure:
                add inferences to csp
                result ← BACKTRACK(csp, assignment)
                if result ≠ failure: return result
                remove inferences from csp
            remove {var = value} from assignment
    return failure

function AC-3(csp) returns false if an inconsistency is found, true otherwise
    queue ← all arcs in csp
    while queue not empty:
        (Xi, Xj) ← POP(queue)
        if REVISE(csp, Xi, Xj):
            if size of Di = 0: return false
            for each Xk in NEIGHBORS(Xi) − {Xj}: add (Xk, Xi) to queue
    return true

function REVISE(csp, Xi, Xj) returns true iff Di was revised
    revised ← false
    for each x in Di:
        if no value y in Dj satisfies the constraint between Xi and Xj:
            delete x from Di;  revised ← true
    return revised

function MIN-CONFLICTS(csp, max_steps) returns a solution or failure
    current ← an initial complete assignment
    for i = 1 to max_steps:
        if current is a solution: return current
        var ← a randomly chosen conflicted variable
        value ← the value v for var that minimizes CONFLICTS(csp, var, v, current)
        set var = value in current
    return failure
```

## Ejemplo — Sudoku de la tarea (HW01, tableros oficiales)

| Tablero | Ingenuo | MRV | Forward checking + MRV |
|---|---|---|---|
| 1 (30 dados) | 4 208 asignaciones | 51 | 51 |
| 2 (22 dados) | 335 637 | 4 036 | **309** |

Lectura con la teoría: MRV es *fail-first*; forward checking detecta dominios vacíos antes de bajar en la recursión. Ver [HW01](../assignments/deber-1-search-problems.md).

## Errores comunes y tips de examen

- MRV elige **variable**; LCV elige **valor**; degree es el desempate de MRV.
- Forward checking ≠ arc consistency completa: solo revisa los vecinos de la variable recién asignada, sin propagar.
- Arc consistency no resuelve "Australia con 2 colores"; path consistency sí.
- Árbol → O(nd²) sin backtracking. Es una pregunta típica de "¿por qué la estructura importa?".
- "Generate & test" vs. backtracking: ver la tabla de inferencias en [N-Queens](n-queens.md) y el cálculo 9⁵⁹ del Sudoku en HW01.

## Relacionado

- [N-Queens](n-queens.md)
- [State Representation](state-representation.md)
- [Uninformed Search](uninformed-search.md) (DFS, backtracking)
- [Local Search and Hill Climbing](local-search-hill-climbing.md) (min-conflicts)
- [Prolog](prolog.md) (Prolog hace backtracking automáticamente)
- [HW01](../assignments/deber-1-search-problems.md)

## Fuentes

- [Slides 02](../sources/slides-02-problem-solving.md), slides 23–24.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 5 completo (ingestado: §5.1 definiciones y ejemplos, §5.2 AC-3 y consistencias, §5.3 backtracking/heurísticas/FC/MAC/backjumping, §5.4 min-conflicts, §5.5 estructura).
