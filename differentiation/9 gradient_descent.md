# 🔥 Gradient Descent (How Models Learn)

## 1. Big Idea

**Gradient Descent** is a method to minimize a function.

In deep learning:
👉 We minimize the **loss function**

---

## 2. Intuition

Imagine:

- You are on a hill 🌄  
- You want to reach the lowest point  

👉 You go downhill step by step  

That’s Gradient Descent.

---

## 3. Core Formula

w = w - η∇L

---

## 4. Meaning of Symbols

- w → weights (parameters)  
- ∇L → gradient (direction of increase)  
- η → learning rate (step size)  

👉 We move in the opposite direction of gradient.

---

## 5. Step-by-step Process

1. Start with random weights  
2. Compute loss  
3. Compute gradient  
4. Update weights  
5. Repeat  

---

## 6. Simple 1D Example

f(x) = x²  

Derivative:

df/dx = 2x  

Update rule:

x = x - η(2x)

### Example

Start: x = 4, η = 0.1  

Step 1: x = 4 - 0.1(8) = 3.2  
Step 2: x = 3.2 - 0.1(6.4) = 2.56  
Step 3: x = 2.56 - 0.1(5.12) = 2.048  

👉 Gradually approaches 0 (minimum)

---

## 7. Learning Rate ⚠️

- Too small → very slow  
- Too large → overshoot / unstable  
- Just right → smooth convergence  

---

## 8. In Deep Learning

Loss:

L(w₁, w₂, ..., wₙ)

Update each weight:

wᵢ = wᵢ - η (∂L/∂wᵢ)

---

## 9. Types of Gradient Descent

- Batch Gradient Descent → full dataset  
- Stochastic Gradient Descent → one sample  
- Mini-batch Gradient Descent → small batches (most common)  

---

## 10. Mental Model

- Gradient → where to go up  
- Gradient Descent → go down  
- Learning rate → step size  

---

## 🔥 One Line Summary

Gradient Descent = move in negative gradient direction to minimize error
