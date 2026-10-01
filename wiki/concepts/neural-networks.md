---
title: Neural Networks
type: concept
tags: [machine-learning, neural-networks, history]
sources: [slides-01-introduction-to-ai, paper-kennedy-eberhart-1995-pso, book-russell-norvig-aima]
updated: 2026-10-01
---
# Neural Networks (Redes neuronales: perceptrón, backprop, SVM, deep learning)

> **Summary (EN):** The connectionist thread of AI as presented in the intro lecture: Rosenblatt's perceptron (1958) stores knowledge in synaptic weights learned from experience; backpropagation computes the gradient of the loss with respect to every weight, enabling multi-layer networks that solve XOR; SVMs (Vapnik, 1995) maximize the margin between classes; deep learning (Bengio, Hinton, LeCun) scales networks in depth. PSO was also shown to train network weights.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Perceptron | Perceptrón | Neurona artificial: suma ponderada + función umbral. |
| Synaptic weights | Pesos sinápticos | Parámetros donde se guarda el conocimiento aprendido. |
| Backpropagation | Retropropagación | Regla de la cadena para obtener ∂Loss/∂w en cada capa. |
| Loss function | Función de pérdida | Mide el error de la red; se minimiza. |
| XOR problem | Problema XOR | No es linealmente separable: un perceptrón solo no lo resuelve. |
| Margin | Margen | Distancia entre la frontera de decisión y los puntos más cercanos (SVM). |
| Deep learning | Aprendizaje profundo | Redes con muchas capas. |

## Explicación

**Perceptrón (1958).** Inspirado en neuronas biológicas. Una red neuronal es "un procesador paralelo distribuido formado por unidades simples que pueden almacenar conocimiento basado en experiencia" (slides 01, s8). El conocimiento se adquiere del entorno con un proceso de aprendizaje y se guarda en los **pesos**.

Complemento (conocimiento general): salida `y = step(w·x + b)`; regla de aprendizaje `w ← w + η (t − y) x`. Solo separa clases **linealmente separables**.

**Backpropagation.** Calcula el gradiente de la pérdida respecto a los pesos de cada neurona. Permite entrenar capas en serie con no linealidades, y así resolver XOR. Es [gradient descent](gradient-descent.md) aplicado a una red: `w ← w − η ∂L/∂w`.

**SVM (1995).** Clasificador lineal parecido al perceptrón, pero elige la frontera que **maximiza el margen** entre las dos clases (la fórmula está en imagen en la slide; en forma estándar: minimizar ½‖w‖² sujeto a yᵢ(w·xᵢ + b) ≥ 1).

**Deep learning.** Las herramientas existían desde los 60; el término aparece en 1986; Bengio, Hinton y LeCun mostraron cómo entrenar redes profundas con backprop modificado.

**Conexión con optimización.** Kennedy y Eberhart entrenaron con [PSO](particle-swarm-optimization.md) una red 2-3-1 para XOR (13 pesos) en ~31 iteraciones, y redes para Iris con resultados similares a backprop: los pesos de una red son solo un punto en un espacio continuo que cualquier optimizador puede buscar.

## Errores comunes y tips de examen

- Un perceptrón **simple no puede** aprender XOR; hace falta al menos una capa oculta + backprop.
- Backprop **no es** un algoritmo de aprendizaje completo por sí solo: calcula gradientes; el que actualiza es el descenso de gradiente.

## Relacionado

- [History of AI](history-of-ai.md)
- [Gradient Descent](gradient-descent.md)
- [Particle Swarm Optimization](particle-swarm-optimization.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 8, 11, 12, 13.
- [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md), §3.4 y §5.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 19–21 (pendiente de ingestar).
