---
marp: true
theme: ia-review
paginate: true
footer: "Unit 1 · Foundations & Agents · IA review"
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Unit 1 — Foundations & Intelligent Agents

**Review deck for the test on Thu Oct 8**

*English for the exam · "ES:" tips in Spanish*
*Wiki: What is AI · History of AI · Intelligent Agents · Task Environments · Agent Types · State Representation*

---

## What is AI?

- No single definition of *intelligence*; the course lists **understanding, problem solving, knowledge, meaning, skill**.
- **Turing Test (1950):** an operational, behavior-based definition — can a machine pass as human in conversation?
- **Dartmouth (1956):** "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."
- **AIMA's view:** AI = building **rational agents**.

> ES: si preguntan "¿qué es IA?", responde con *rational agent* + menciona Turing y Dartmouth.

---

## Timeline you must know

| Year | Who | What |
|---|---|---|
| 1950 | Alan Turing | Turing Test |
| 1956 | McCarthy, Minsky, Rochester, Shannon | Dartmouth workshop, "AI" named |
| 1958 | Frank Rosenblatt | Perceptron |
| 1972 | Colmerauer & Roussel (Kowalski's theory) | **Prolog**, Marseille |
| 1975 | John Holland | Genetic algorithms |
| 1995 | Kennedy & Eberhart | Particle swarm optimization |
| 1996 | Dorigo, Maniezzo & Colorni | Ant System (ACO) |
| 2007 | Karaboga | Artificial bee colony |

> ES: trampas de las slides → Prolog **no** es de Dennis Ritchie (eso es C); GA = **1975**, no 1992.

---

## Agent, agent function, agent program

- **Agent:** perceives the environment through **sensors**, acts through **actuators**.
- **Agent function:** maps the whole *percept history* → action (abstract, possibly infinite table).
- **Agent program:** the concrete code that implements the function compactly.
- **Rational agent:** chooses the action that maximizes the **expected** value of the performance measure, given the percepts so far and its built-in knowledge.

> ES: racional ≠ omnisciente. Maximiza el desempeño **esperado**, no el real. Cruzar la calle tras mirar es racional aunque luego caiga una puerta de avión.

---

## Performance measures: "you get what you ask for"

- A vacuum robot rewarded **+1 per unit of dirt vacuumed** could dump dirt and vacuum it again.
- Better: **+1 per clean square per time step** (minus energy/noise penalties).

**Say it in the exam:** "Design performance measures according to what one actually wants in the environment, not according to how one thinks the agent should behave."

> ES: la nota debe premiar el resultado que quieres (piso limpio), no la acción que imaginas (aspirar).

---

## PEAS — specify the task environment first

| | Performance | Environment | Actuators | Sensors |
|---|---|---|---|---|
| Sudoku app | correct board, time | 9×9 board with clues | write digits, show solution | file / camera |
| Robot soccer | goals for − against | field, ball, teammates, rivals | legs/wheels, kicker | camera, odometry, touch |
| Shopping assistant | price, quality, user satisfaction | web shops, products, user | show products, buy, ask | web pages, user input |

> ES: PEAS es siempre el primer paso para diseñar un agente.

---

## Six environment dimensions

1. **Fully** vs. **partially** observable
2. **Deterministic** vs. **non-deterministic (stochastic)**
3. **Episodic** vs. **sequential**
4. **Static** vs. **dynamic** (*semidynamic*: the world doesn't change but the score does with time)
5. **Discrete** vs. **continuous**
6. **Single-agent** vs. **multi-agent** (competitive / cooperative)

Classical search assumes: *fully observable, deterministic, static, discrete, known*.

> ES: siete preguntas sobre el mundo del agente: ¿ve todo?, ¿hay azar?, ¿las decisiones se conectan?, ¿cambia mientras piensa?, ¿se puede contar?, ¿hay otros jugadores?, ¿conoce las reglas?

---

## Classify these (practice U1 #2)

| Task | Obs. | Det. | Episodic | Static | Discrete | Agents |
|---|---|---|---|---|---|---|
| Crossword | full | det. | seq. | static | discrete | single |
| Poker | partial | stoch. | seq. | static | discrete | multi |
| 4×4 tic-tac-toe | full | det. | seq. | static | discrete | multi (comp.) |
| Image classification | full | det. | **episodic** | semi | continuous | single |
| Delivery drone | partial | stoch. | seq. | dynamic | continuous | multi |

> ES: clasificar imágenes es **episódico**: cada imagen no depende de la anterior.

---

## Four agent architectures (+ learning)

| Type | Uses | Example |
|---|---|---|
| **Simple reflex** | condition–action rules on the *current* percept | thermostat |
| **Model-based reflex** | internal state + transition model | vacuum that maps the house |
| **Goal-based** | search / planning toward a goal | GPS route planner |
| **Utility-based** | maximizes expected utility; trades off conflicting goals | self-driving taxi |

**Learning agent:** any of the above + learning element, critic, problem generator (e.g., a chess program that improves by self-play).

> ES: cada tipo agrega algo al anterior: reacciona → recuerda → planifica → compara qué tan bueno es cada resultado.

---

## Is the vacuum agent rational? (AIMA §2.2)

- Two squares; rule: *if dirty → Suck, else move to the other square*.
- Measure **+1 per clean square per step** → **rational** (no agent does better in expectation).
- Add **−1 per move** → **not rational**: it keeps oscillating when everything is clean.
- Fix: a **model-based** agent that remembers both squares are clean and does *NoOp*.

> ES: si moverse no cuesta, la aspiradora reflejo es racional; si cuesta, pierde puntos yendo y viniendo cuando todo ya está limpio.

---

## State representations

| Representation | What a state is | Course example |
|---|---|---|
| **Atomic** | an indivisible black box | "Sibiu" in Romania route finding |
| **Factored** | a vector of variables with values | 8-puzzle tuple, Sudoku as a CSP, (x, y) in optimization |
| **Structured** | objects and relations | `parent(hector, ana).` in Prolog / FOL |

More expressive → more reasoning possible → more expensive.

> ES: atómico = solo un nombre; factorizado = lista de valores; estructurado = objetos y relaciones.

---

## Statistical vs. causal models

- **Model:** a mathematical description of a system / hypothesis.
- **Statistical** (regression, classification, Bayesian/Markov networks): capture **correlation**.
- **Causal** (Judea Pearl's causal calculus): cause → effect in a **DAG**; presented as the bridge between ML and AI.

> ES: "correlación no implica causalidad" — el modelo causal permite preguntar "¿qué pasa si intervengo?".

---

<!-- _class: lead -->

## Self-check (answer aloud, in English)

1. Define a rational agent in one sentence.
2. Why is a rational agent not always successful?
3. PEAS for an automated taxi.
4. Which agent type is a GPS app, and why?
5. Is poker episodic? Is it fully observable?
6. Who created Prolog, and when?

*Answers: wiki `study/practice-unit-1-agents.md` · more drills in the Exam Drill quiz*
