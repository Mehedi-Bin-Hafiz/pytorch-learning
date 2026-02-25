# 4️⃣ Sum Rule

## 🔹 Big Idea

The derivative of a sum is the sum of the derivatives.

If:

f(x) = g(x) + h(x)

Then:

d/dx [ g(x) + h(x) ] = g'(x) + h'(x)

---

## 🧠 What Does This Mean?

Instead of differentiating the whole expression at once:

We differentiate each part separately.

Then add the results.

---

## 🧠 Simple Example

Let:

f(x) = x² + x³

Using power rule:

d/dx (x²) = 2x  
d/dx (x³) = 3x²  

So:

f'(x) = 2x + 3x²

---

## 🧠 Another Example

f(x) = x⁴ + x + 7

Derivative of each term:

d/dx (x⁴) = 4x³  
d/dx (x) = 1  
d/dx (7) = 0  

So:

f'(x) = 4x³ + 1 + 0

Final Answer:

f'(x) = 4x³ + 1

---

## 🧠 More Example

f(x) = 5x² + 3x³ + 10

Step 1: Differentiate each term

d/dx (5x²) = 10x  
d/dx (3x³) = 9x²  
d/dx (10) = 0  

Step 2: Add them

f'(x) = 10x + 9x²

---

## 🧠 Important Pattern

Original Function:

x² + x³ + x⁴

Derivative:

2x + 3x² + 4x³

Each term is treated independently.

---

## 🤖 Why Sum Rule Matters in Deep Learning

Neural network loss functions often look like:

Loss = (prediction − target)² + regularization_term

To compute gradient:

We take derivative of each part separately.

Then add them.

Without sum rule, backpropagation would not work cleanly.

Sum rule allows:

✔ Breaking complex expressions  
✔ Computing gradients term by term  
✔ Building large models easily  

---

## 🧩 Intuition Summary

Derivative of:

A + B + C

Equals:

Derivative of A  
+ Derivative of B  
+ Derivative of C  

Just differentiate each term and add.

---

## 🔹 Practice Questions

1. d/dx (x³ + x²) = ?  
2. d/dx (x⁵ + x + 4) = ?  
3. d/dx (x⁴ + 7) = ?  

Answers:

1. 3x² + 2x  
2. 5x⁴ + 1  
3. 4x³  