# 2️⃣ Power Rule

## 🔹 Big Idea

The Power Rule makes taking derivatives very easy.

If:

f(x) = xⁿ

Then:

d/dx (xⁿ) = n xⁿ⁻¹

That’s it. Just:

1. Bring the power down  
2. Subtract 1 from the power  

---

## 🧠 Why Do We Need This?

Using the definition of derivative every time is slow.

Example:

To compute derivative of x² using limit definition takes many steps.

The Power Rule gives the answer instantly.

---

## 🧠 Basic Examples

### Example 1

f(x) = x²  

Using power rule:

d/dx (x²) = 2x¹ = 2x

---

### Example 2

f(x) = x³  

d/dx (x³) = 3x²

---

### Example 3

f(x) = x⁵  

d/dx (x⁵) = 5x⁴

---

### Example 4

f(x) = x¹⁰  

d/dx (x¹⁰) = 10x⁹

---

## 🧠 What About Square Root?

Remember:

√x = x^(1/2)

So:

d/dx (x^(1/2)) = (1/2)x^(-1/2)

Which can also be written as:

1 / (2√x)

---

## 🧠 What About 1/x ?

Rewrite first:

1/x = x⁻¹

Now apply power rule:

d/dx (x⁻¹) = -1 x⁻²

= -1 / x²

---

## 🧠 Important Pattern

Original → Derivative

x² → 2x  
x³ → 3x²  
x⁴ → 4x³  
xⁿ → n xⁿ⁻¹  

Power decreases by 1 every time.

---

## 🤖 Why Power Rule Matters in Deep Learning

In neural networks:

Loss functions often contain:

- x²  
- x³  
- polynomial terms  

Example:

Loss = (prediction − target)²

To minimize loss, we take derivative.

Without power rule, training neural networks would be slow and messy.

Power rule makes gradient computation fast.

---

## 🧩 Intuition Summary

Power Rule says:

If f(x) = xⁿ

Then:

Derivative = n xⁿ⁻¹

Just:

✔ Bring exponent down  
✔ Reduce exponent by 1  

---

## 🔹 Practice Questions

1. d/dx (x⁷) = ?  
2. d/dx (x⁴) = ?  
3. d/dx (x⁻³) = ?  

Try to solve before checking answer:

Answers:

1. 7x⁶  
2. 4x³  
3. -3x⁻⁴  