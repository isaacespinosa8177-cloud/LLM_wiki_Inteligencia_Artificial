---
title: Neural Networks
type: concept
tags: [machine-learning, neural-networks, history]
sources: [slides-01-introduction-to-ai, paper-kennedy-eberhart-1995-pso, book-russell-norvig-aima]
updated: 2026-10-07
---
# Neural Networks (Redes neuronales: perceptrón, backprop, SVM, deep learning)

> **Summary (EN):** The "learning from data" side of AI as shown in the intro lecture. Rosenblatt's perceptron (1958) is an artificial neuron that stores what it learns in its weights. Backpropagation computes how much each weight of a multilayer network contributed to the error, so gradient descent can fix it; this lets networks learn XOR. SVMs (Vapnik, 1995) separate two classes leaving the widest possible gap. Deep learning (Bengio, Hinton, LeCun) uses networks with many layers. PSO can also train network weights.

> **En palabras simples (ES):** Un perceptrón es una "balanza" que suma las entradas, cada una multiplicada por su importancia (peso). Si la suma pasa de cero, dice "sí" (1); si no, dice "no" (0). Cuando se equivoca, ajusta un poco las importancias para no repetir el error. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Perceptron | Perceptrón | Una neurona artificial: multiplica cada entrada por un peso, suma, y responde 1 o 0. |
| Weights | Pesos (sinápticos) | Números que dicen cuánto importa cada entrada; ahí se guarda lo aprendido. |
| Bias | Sesgo | Un número extra que facilita o dificulta que la neurona diga "sí". |
| Loss function | Función de pérdida | Mide qué tan equivocada está la red; se quiere hacer pequeña. |
| Backpropagation | Retropropagación | Método para calcular cuánta "culpa" tiene cada peso en el error. |
| Linearly separable | Linealmente separable | Datos que se pueden separar con una línea recta. |
| XOR problem | Problema XOR | Un caso que **no** se separa con una línea recta: un perceptrón solo no lo aprende. |
| Margin | Margen | El espacio libre entre la línea que separa y los puntos más cercanos (SVM). |
| Deep learning | Aprendizaje profundo | Redes con muchas capas de neuronas. |

## Explicación

### 1. El perceptrón (1958): una neurona artificial

Está inspirado en las neuronas del cerebro. La clase la define como "un procesador paralelo distribuido formado por unidades simples que pueden almacenar conocimiento basado en experiencia" (slides 01, s8). En simple: muchas unidades pequeñas que aprenden de ejemplos y guardan lo aprendido en sus **pesos**.

**Cómo decide** (complemento: conocimiento general):

1. Multiplica cada entrada por su peso y suma todo, más el sesgo: `w·x + b`.
2. Si el resultado es mayor que 0 → responde **1**; si no → responde **0**.

**Cómo aprende:** si se equivoca, corrige los pesos con `w ← w + η (t − y) x`, es decir: peso nuevo = peso viejo + (tamaño del paso) × (error) × (entrada). Si acierta, el error es 0 y no cambia nada.

**Su límite:** solo puede separar datos con **una línea recta**. Por eso no aprende **XOR**: en XOR, los puntos (0,0) y (1,1) dan 0, y los puntos (0,1) y (1,0) dan 1; ninguna línea recta separa unos de otros.

### 2. Backpropagation: entrenar redes de varias capas

Si pones neuronas en **varias capas**, la red sí puede aprender XOR. El problema es saber cómo corregir los pesos de las capas de en medio. **Backpropagation** calcula, yendo de la salida hacia atrás, **cuánto contribuyó cada peso al error** (eso es el gradiente, ∂L/∂w). Después, el [descenso de gradiente](gradient-descent.md) corrige cada peso un poquito: `w ← w − η ∂L/∂w`.

### 3. SVM (1995): la línea con más espacio

Una SVM también separa dos grupos con una línea (o un plano), como el perceptrón. Pero de todas las líneas posibles elige la que **deja el mayor espacio libre (margen)** entre los dos grupos, como trazar una carretera lo más ancha posible entre dos pueblos. La fórmula está como imagen en la slide; en su forma estándar es: minimizar ½‖w‖² cumpliendo yᵢ(w·xᵢ + b) ≥ 1 (complemento: conocimiento general).

### 4. Deep learning

Las ideas existían desde los años 60. El término "deep learning" aparece en 1986. Bengio, Hinton y LeCun mostraron cómo entrenar redes con **muchas capas** usando versiones mejoradas de backpropagation.

### 5. Conexión con la unidad de optimización

Los pesos de una red son simplemente **una lista de números**, así que cualquier optimizador puede buscarlos. Kennedy y Eberhart entrenaron con [PSO](particle-swarm-optimization.md) una red pequeña (2 entradas, 3 neuronas ocultas, 1 salida: 13 pesos) para resolver XOR en unas 31 iteraciones, y redes para el conjunto de flores Iris con resultados parecidos a backpropagation.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Un perceptrón es una "balanza" que suma las entradas, cada una multiplicada por su importancia (peso). Si la suma pasa de cero, dice "sí" (1); si no, dice "no" (0). Cuando se equivoca, ajusta un poco las importancias para no repetir el error.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Qué es (en simple) | English |
|---|---|---|
| x | las entradas del ejemplo (los datos que recibe), p. ej. x = (1, 1) | inputs |
| w | los **pesos**: un número por entrada que dice cuánto importa esa entrada | weights |
| b | el **sesgo**: un número extra que facilita o dificulta decir "sí" | bias |
| w·x | multiplicar cada entrada por su peso y sumar todo: w₁·x₁ + w₂·x₂ | dot product |
| y | la respuesta que da el perceptrón (0 o 1) | output |
| t | la respuesta correcta que debía dar (0 o 1) | target |
| t − y | el error: 0 si acertó, +1 si dijo 0 y era 1, −1 si dijo 1 y era 0 | error |
| η (eta) | la **tasa de aprendizaje**: qué tan grande es cada corrección (p. ej. 0.1 o 1) | learning rate |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

*Perceptron training*

1. Start with small random weights w and bias b.
   - *ES:* Empieza con pesos y sesgo pequeños al azar (o en cero).
2. Take one training example x with its correct answer t.
   - *ES:* Toma un ejemplo de entrenamiento y su respuesta correcta.
3. Compute the output: y = 1 if w·x + b > 0, otherwise y = 0.
   - *ES:* Suma cada entrada por su peso, más el sesgo. Si da más de 0, responde 1; si no, 0.
4. Update the weights: w ← w + η·(t − y)·x and b ← b + η·(t − y).
   - *ES:* Corrige: peso nuevo = peso viejo + (tasa) × (error) × (entrada). Si acertó, el error es 0 y nada cambia. Si se equivocó, los pesos se mueven hacia la respuesta correcta.
5. Repeat with every example, again and again, until there are no errors.
   - *ES:* Pasa por todos los ejemplos varias veces hasta que no falle ninguno. Esto solo termina si los datos se pueden separar con una línea recta (*linearly separable*).

*Backpropagation (training a network with several layers)*

1. Forward pass: compute the output of each layer, from input to output.
   - *ES:* Pasa los datos por la red, capa por capa, hasta obtener la respuesta.
2. Compute the loss: how wrong the output is.
   - *ES:* Mide el error final (la pérdida, *loss*).
3. Backward pass: use the chain rule to find how much each weight caused the error.
   - *ES:* Recorre la red de atrás hacia adelante calculando cuánta culpa tiene cada peso en el error (eso es el gradiente).
4. Update each weight a little against its gradient: w ← w − η · ∂loss/∂w.
   - *ES:* Mueve cada peso un poquito en la dirección que reduce el error (es descenso de gradiente).

**Ejemplo con números:** pesos w = (0, 0), sesgo b = 0, η = 1. Ejemplo x = (1, 1) con respuesta correcta t = 1.
Suma: 0·1 + 0·1 + 0 = 0 → no es mayor que 0 → y = 0. Se equivocó: error = t − y = 1 − 0 = 1.
Corrección: w = (0, 0) + 1·1·(1, 1) = (1, 1); b = 0 + 1·1 = 1.
Probamos otra vez: 1·1 + 1·1 + 1 = 3 > 0 → y = 1. ¡Ahora acierta!

**Say it in the exam (EN):** "A perceptron multiplies each input by a weight, adds a bias, and outputs 1 if the sum is positive. When it is wrong, it moves the weights toward the correct answer: w ← w + η(t − y)x. A single perceptron can only separate data with a straight line, so it cannot learn XOR. Backpropagation computes, for every weight of a multilayer network, how much it contributed to the error, and gradient descent uses that to update it."

**Dilo así (ES):** "Un perceptrón multiplica cada entrada por un peso, suma un sesgo y responde 1 si la suma es positiva. Cuando falla, mueve los pesos hacia la respuesta correcta. Un solo perceptrón solo separa datos con una línea recta, por eso no aprende XOR. Backpropagation calcula cuánto contribuyó cada peso al error en una red de varias capas, y el descenso de gradiente lo corrige."

## Errores comunes y tips de examen

- Un perceptrón **solo** no puede aprender XOR; hace falta al menos una capa oculta y backpropagation.
- Backpropagation **no** actualiza los pesos por sí solo: solo **calcula** los gradientes. Quien actualiza es el descenso de gradiente.

## Relacionado

- [History of AI](history-of-ai.md)
- [Gradient Descent](gradient-descent.md)
- [Particle Swarm Optimization](particle-swarm-optimization.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md)

## Fuentes

- [Slides 01](../sources/slides-01-introduction-to-ai.md), slides 8, 11, 12, 13.
- [Kennedy & Eberhart 1995](../sources/paper-kennedy-eberhart-1995-pso.md), §3.4 y §5.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 19–21 (pendiente de ingestar).
