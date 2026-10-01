---
title: "Slides 01 — Introduction to Artificial Intelligence"
type: source
tags: [slides, history, foundations]
sources: [slides-01-introduction-to-ai]
updated: 2026-10-01
---
# Slides 01 — Introduction to Artificial Intelligence (Introducción a la IA)

> **Summary (EN):** Opening lecture of the course (Daniel Riofrío, thanks to Luciana Valdivieso). It asks what "intelligence" and "artificial intelligence" mean and then walks a timeline from ancient automata (Talos, Antikythera mechanism) through the Mechanical Turk, the first computers, the Turing Test, LISP/FORTRAN, the 1956 Dartmouth workshop, the perceptron, Prolog, backpropagation, SVMs and deep learning, up to generative AI, LLMs and agents. It closes by contrasting statistical models with causal models (Judea Pearl).

## Ficha

| Campo | Valor |
|---|---|
| Archivo | [raw/slides/01_Introduction to Artificial Intelligence.pptx](../../raw/slides/01_Introduction%20to%20Artificial%20Intelligence.pptx) |
| Autor | Daniel Riofrío (agradecimiento a Luciana Valdivieso) |
| Tipo | Diapositivas de clase, 19 slides |
| Unidad | 1 — Fundamentos |

## Resumen por secciones

- **Slide 2 — Ideas iniciales.** Definiciones de inteligencia: capacidad de entender, de resolver problemas, conocimiento/comprensión, significado asignado a una proposición, habilidad y experiencia. Pregunta abierta: ¿qué entendemos por IA? Línea de tiempo 1700 → 2026 que termina en *Generative AI, LLMs, Agents*.
- **Slide 3 — Autómatas.** El Turco Mecánico (1770, Wolfgang von Kempelen): parecía jugar ajedrez, en realidad escondía a un humano. Autómatas de Pierre Jaquet-Droz (1768–1774): el músico, el dibujante y el escritor.
- **Slide 4 — Primeras computadoras.** Z1 de Konrad Zuse (1936, calculadora binaria con tarjetas perforadas, punto flotante, memoria). ENIAC (1945): una de las primeras computadoras de propósito general, programable, con tubos de vacío, 170 m², 27 toneladas.
- **Slide 5 — Test de Turing (1950).** Dos humanos y una computadora; el interrogador, aislado, hace preguntas por terminal de texto. Si no distingue a la máquina, se considera inteligente. Es un intento de definición *operacional* de inteligencia.
- **Slide 6 — Primeros lenguajes.** FORTRAN (1957, IBM, imperativo, cálculo numérico) y LISP (1958, John McCarthy, cálculo lambda y recursión, listas, notación prefija `(f a1 a2 a3)`).
- **Slide 7 — Nacimiento de la IA (Dartmouth, 1956).** Shannon, Minsky, Rochester, McCarthy. Cita de la propuesta: "every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it". Temas: computadoras automáticas, lenguaje, redes neuronales, tamaño de un cálculo, auto-mejora, abstracciones, aleatoriedad y creatividad.
- **Slide 8 — Perceptrón (1958, Frank Rosenblatt).** Modelo inspirado en neuronas; una red neuronal es un procesador paralelo distribuido que almacena conocimiento en pesos sinápticos aprendidos de la experiencia.
- **Slide 9 — Prolog (1970).** Programación lógica: *Algorithm = Logic + Control*; sistemas expertos; cláusulas positivas en notación similar a lógica de primer orden. ⚠️ Ver discrepancia abajo.
- **Slide 10 — ¿Qué es un modelo?** Descripción matemática de un fenómeno; hipótesis. Se construyen con **métodos formales** (cálculo de primer orden, cálculo lambda, lógica temporal, sistemas de reescritura, cálculo causal) o **métodos estadísticos** (regresión, clasificación, redes bayesianas, redes de Markov).
- **Slide 11 — Backpropagation (1975).** Calcula el gradiente de la pérdida respecto a cada peso; permitió entrenar neuronas en serie y resolver XOR.
- **Slide 12 — SVM (1995, Vapnik, AT&T Bell Labs).** Clasificador lineal que maximiza el margen entre dos subespacios (la fórmula está como imagen).
- **Slide 13 — Deep Learning (2000).** Término introducido en 1986; Bengio, Hinton y LeCun sentaron las bases para entrenar redes profundas con backpropagation modificado.
- **Slide 14 — Limitaciones de los modelos estadísticos** (solo imagen).
- **Slide 15 — Modelos causales.** Determinar si A causa B o B causa A (no ambos). Cálculo causal de Judea Pearl: relaciones causa-efecto codificadas en un grafo dirigido acíclico (DAG).
- **Slides 17–19 — Epílogo histórico.** Mecanismo de Anticitera (~200 a.C.): la computadora analógica más antigua conocida; predecía posiciones astronómicas y eclipses hasta 19 años adelante. Talos en la *Ilíada* (~800 a.C.?): gigante autómata de bronce que protegía Creta.

## Ideas clave

1. "Inteligencia" no tiene una sola definición; el Test de Turing propone una definición operacional (por comportamiento).
2. La IA nace formalmente en Dartmouth (1956) con la conjetura de que toda faceta de la inteligencia puede describirse con precisión suficiente para simularla.
3. Dos grandes tradiciones de modelado: **formal/simbólica** (lógica, Prolog, LISP) y **estadística/conexionista** (perceptrón, backprop, SVM, deep learning). La causalidad (Pearl) se propone como puente.

## Conceptos que alimenta

- [What Is AI?](../concepts/what-is-ai.md)
- [History of AI](../concepts/history-of-ai.md)
- [Neural Networks](../concepts/neural-networks.md)
- [Statistical vs. Causal Models](../concepts/statistical-vs-causal-models.md)
- [Prolog](../concepts/prolog.md)

## Notas y discrepancias

- ⚠️ **Slide 9 atribuye Prolog a "Dennis Ritchie at Bell Labs" y lo describe como "imperative, compiled language".** Esa descripción corresponde al lenguaje **C** (Ritchie, Bell Labs, ~1972). Prolog fue creado en Marsella en 1972 por **Alain Colmerauer y Philippe Roussel**, con teoría de **Robert Kowalski**, y es **declarativo**, como dice correctamente [slides XX](slides-xx-logic-programming-prolog.md) (slide 8). Ver [errata](../study/errata.md).
- Slide 4 pone "1936 First Computer (Z1)" y "1945 ENIAC" en un mismo slide; el Z1 se construyó entre 1936 y 1938.
- Varias slides (8, 11, 12, 14, 16) tienen el contenido principal en imágenes; las fórmulas (p. ej. el margen del SVM) no están en el texto extraído.
