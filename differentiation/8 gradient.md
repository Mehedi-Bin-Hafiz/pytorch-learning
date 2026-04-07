# 🚀 8. Gradient (Core of Deep Learning)

## 1. What is a Gradient?

The **gradient** is a vector of partial derivatives.

It tells how a function changes with respect to all variables at once.

---

## 2. Mathematical Definition

For a function:

f(x, y)

Gradient:

∇f = (∂f/∂x, ∂f/∂y)

For more variables:

∇f = (∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ)

---

## 3. Intuition

Imagine standing on a hill:

- Gradient → direction of steepest **increase**
- Negative gradient → direction of steepest **decrease**

---

## 4. Example

f(x, y) = x² + 3xy + y²

∂f/∂x = 2x + 3y  
∂f/∂y = 3x + 2y  

Gradient:

∇f = (2x + 3y, 3x + 2y)

---

## 5. Interpretation

- Gradient gives **direction + magnitude**
- Magnitude → how steep the slope is
- Direction → where to move

---

## 6. Why Gradient Matters in Deep Learning

Loss function:

L(w₁, w₂, w₃, ...)

Gradient:

∇L = (∂L/∂w₁, ∂L/∂w₂, ...)

This tells:
> How each weight affects the error

---

## 7. Gradient Descent

Update rule:

w = w − η∇L

Where:
- w = weights  
- η = learning rate  
- ∇L = gradient  

We move in **negative gradient direction** to reduce loss.

---

## 8. 1D Example

f(x) = x²  
df/dx = 2x  

- x = 3 → move left  
- x = -3 → move right  

Minimum at x = 0

---

## 9. Key Concepts

- Gradient = direction of fastest increase  
- Negative gradient = direction of learning  
- Works on all parameters together  

---

## 10. Connection to Backpropagation

Backpropagation computes gradients using **chain rule**.

Then updates weights using gradient descent.

---

## 11. Summary

- Gradient combines all partial derivatives  
- It guides how to update parameters  
- Core idea behind deep learning training  

---

## 🔥 One Line

Gradient = direction to change all parameters to increase output  
Deep Learning = move opposite direction to reduce error
