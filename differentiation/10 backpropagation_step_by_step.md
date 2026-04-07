# 🔥 Backpropagation (Step-by-Step)

## 0. What are we trying to do?

We want to **train a neural network**.

That means:

> adjust weights so loss becomes smaller

---

## 1. Simple Neural Network

Let’s take the smallest example:

- Input: `x`
- Weight: `w`

Output:

`y = wx`

Loss function:

`L = (y - t)^2`

Where:
- `t` = true value

---

## 2. Forward Pass

This is the normal calculation step.

1. Compute output:

`y = wx`

2. Compute loss:

`L = (y - t)^2`

This is called the **forward pass**.

---

## 3. Goal

We want to compute:

`∂L/∂w`

This means:

> How does loss change when weight changes?

---

## 4. Chain Rule (Important)

We cannot directly differentiate `L` with respect to `w`.

So we break it into smaller parts:

`∂L/∂w = (∂L/∂y) * (∂y/∂w)`

This is the **chain rule**.

---

## 5. Compute Each Part

### First part

`L = (y - t)^2`

So:

`∂L/∂y = 2(y - t)`

### Second part

`y = wx`

So:

`∂y/∂w = x`

---

## 6. Combine Them

Now combine both pieces:

`∂L/∂w = 2(y - t) * x`

This is the gradient of the loss with respect to the weight.

---

## 7. Update Weight

Using gradient descent:

`w = w - η * 2(y - t)x`

Where:
- `η` = learning rate

This updates the weight in the direction that reduces the loss.

---

## 8. What Just Happened?

You just did **backpropagation**.

Step by step:

1. Forward pass → compute `y`, `L`
2. Backward pass → compute gradient
3. Update weight

---

## 9. Why It Is Called Backpropagation

Because the gradient flows backward:

Loss → Output → Weight

So we propagate error information backward through the network.

---

## 10. Full Flow

### Forward

`x → y → L`

### Backward

`L → y → w`

---

## 11. Intuition

- Error = `y - t`
- Bigger error → bigger update
- Smaller error → smaller update

So the model learns gradually.

---

## 12. Real Neural Network

The same idea works for larger neural networks.

Instead of one weight, a real network has:
- many neurons
- many weights
- many layers

Backpropagation applies the **chain rule again and again**.

---

## 13. One-Line Definition

> Backpropagation = using chain rule to compute gradients from loss back to weights

---

## 14. Summary

Backpropagation has three core steps:

1. Forward pass
2. Compute loss
3. Backward pass to get gradients

Then we update weights using gradient descent.

---

## 15. What You Understand Now

You now understand:

- Gradient
- Gradient Descent
- Chain Rule
- Backpropagation (core idea)

This is the mathematical heart of deep learning.
