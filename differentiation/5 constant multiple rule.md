# 5️⃣ Constant Multiple Rule

## 🔹 Big Idea

If a function is multiplied by a constant,
the derivative keeps the constant.

If:

f(x) = c · g(x)

(where c is a constant)

Then:

d/dx [ c · g(x) ] = c · g'(x)

---

## 🧠 What Does This Mean?

The constant does NOT disappear.

It stays outside.

We only differentiate the function part.

---

## 🧠 Simple Example 1

f(x) = 5x²

Using power rule:

d/dx (x²) = 2x

Now multiply by constant 5:

f'(x) = 5 · 2x

Final Answer:

f'(x) = 10x

---

## 🧠 Example 2

f(x) = 3x³

d/dx (x³) = 3x²

Multiply by constant 3:

f'(x) = 3 · 3x²

Final Answer:

f'(x) = 9x²

---

## 🧠 Example 3

f(x) = -4x⁴

d/dx (x⁴) = 4x³

Multiply by -4:

f'(x) = -4 · 4x³

Final Answer:

f'(x) = -16x³

---

## 🧠 Example 4

f(x) = 7√x

Rewrite first:

√x = x^(1/2)

So:

f(x) = 7x^(1/2)

Derivative of x^(1/2):

= (1/2)x^(-1/2)

Now multiply by 7:

f'(x) = 7 · (1/2)x^(-1/2)

Final Answer:

f'(x) = (7/2)x^(-1/2)

---

## 🧠 Important Pattern

Original → Derivative

5x² → 10x  
3x³ → 9x²  
-4x⁴ → -16x³  

Constant stays.
Only exponent rule applies inside.

---

## 🤖 Why Constant Multiple Rule Matters in Deep Learning

In neural networks:

Weights are constants during differentiation.

Example:

Loss = 5x²

Derivative:

= 5 · 2x  
= 10x

Without constant multiple rule,
we could not compute gradients correctly.

This rule is used in almost every gradient calculation.

---

## 🧩 Intuition Summary

If:

Constant × Function

Then:

Derivative = Constant × Derivative of function

The constant comes along for the ride.

---

## 🔹 Practice Questions

1. d/dx (8x³) = ?  
2. d/dx (-2x⁵) = ?  
3. d/dx (6x²) = ?  

Answers:

1. 24x²  
2. -10x⁴  
3. 12x  