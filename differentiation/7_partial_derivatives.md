# 7. Partial Derivatives

## What is a partial derivative?

A **partial derivative** is used when a function depends on **more than one variable**.

It tells us how the function changes when we change **one variable only**, while keeping the other variables fixed.

We use the symbol:

\[
\frac{\partial f}{\partial x}
\]

instead of the ordinary derivative symbol:

\[
\frac{df}{dx}
\]

---

## Simple intuition

Suppose a function depends on both \(x\) and \(y\):

\[
f(x,y)
\]

Then:

- \(\frac{\partial f}{\partial x}\) means: change **x**, keep **y** constant
- \(\frac{\partial f}{\partial y}\) means: change **y**, keep **x** constant

So a partial derivative looks at the slope in **one direction at a time**.

---

## Example 1

Let:

\[
f(x,y) = x^2 + 3xy + y^2
\]

### Partial derivative with respect to \(x\)

Treat \(y\) as a constant:

- derivative of \(x^2\) is \(2x\)
- derivative of \(3xy\) with respect to \(x\) is \(3y\)
- derivative of \(y^2\) is \(0\), because it does not depend on \(x\)

So:

\[
\frac{\partial f}{\partial x} = 2x + 3y
\]

### Partial derivative with respect to \(y\)

Treat \(x\) as a constant:

- derivative of \(x^2\) is \(0\)
- derivative of \(3xy\) with respect to \(y\) is \(3x\)
- derivative of \(y^2\) is \(2y\)

So:

\[
\frac{\partial f}{\partial y} = 3x + 2y
\]

---

## Example 2

Let:

\[
f(x,y,z) = x^2y + yz^3
\]

### With respect to \(x\)

Treat \(y\) and \(z\) as constants:

\[
\frac{\partial f}{\partial x} = 2xy
\]

### With respect to \(y\)

Treat \(x\) and \(z\) as constants:

\[
\frac{\partial f}{\partial y} = x^2 + z^3
\]

### With respect to \(z\)

Treat \(x\) and \(y\) as constants:

\[
\frac{\partial f}{\partial z} = 3yz^2
\]

---

## Why partial derivatives matter in deep learning

In deep learning, the output of a model depends on **many variables**, especially the **weights** and **biases**.

For example:

- input values
- weights
- bias terms
- loss function

The model’s loss can be written as a function of many parameters:

\[
L(w_1, w_2, w_3, \dots)
\]

A partial derivative tells us:

> If we change just one weight, how does the loss change?

That is exactly what we need during training.

---

## Connection to backpropagation

Backpropagation computes partial derivatives of the loss with respect to each parameter.

Examples:

\[
\frac{\partial L}{\partial w_1}, \quad \frac{\partial L}{\partial w_2}, \quad \frac{\partial L}{\partial b}
\]

These values tell the neural network how to adjust each parameter to reduce error.

---

## Key idea to remember

A **partial derivative** means:

> “Differentiate with respect to one variable, and pretend all other variables are constants.”

---

## Quick summary

- Ordinary derivative: one-variable function
- Partial derivative: multi-variable function
- Change one variable at a time
- Keep all other variables fixed
- Used everywhere in deep learning and backpropagation

---

## Practice question

Find the partial derivatives of:

\[
f(x,y) = 4x^2y + 5y^3
\]

### Answer

With respect to \(x\):

\[
\frac{\partial f}{\partial x} = 8xy
\]

With respect to \(y\):

\[
\frac{\partial f}{\partial y} = 4x^2 + 15y^2
\]
