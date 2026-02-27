\# 6️⃣ Chain Rule



\## 🔹 Big Idea



The Chain Rule is used when a function is inside another function.



If:



f(x) = g(h(x))



Then:



f'(x) = g'(h(x)) · h'(x)



In simple words:



Derivative of outer function  

×  

Derivative of inner function



---



\## 🧠 Why Do We Need Chain Rule?



Sometimes functions are nested.



Example:



f(x) = (x² + 3)²



Here:



Outer function: something²  

Inner function: x² + 3  



We cannot use power rule directly.



We must use Chain Rule.



---



\## 🧠 Step-by-Step Method



When you see:



(something)^n



Follow these steps:



1\. Differentiate the outer power  

2\. Keep the inside unchanged  

3\. Multiply by derivative of inside  



---



\## 🧠 Example 1



f(x) = (x² + 3)²



Step 1: Differentiate outer function



2(x² + 3)



Step 2: Multiply by derivative of inside



Derivative of (x² + 3) = 2x



Step 3: Multiply everything



f'(x) = 2(x² + 3) · 2x



Final Answer:



f'(x) = 4x(x² + 3)



---



\## 🧠 Example 2



f(x) = (3x + 1)⁴



Step 1: Derivative of outer power



= 4(3x + 1)³



Step 2: Derivative of inside



= 3



Step 3: Multiply



f'(x) = 4(3x + 1)³ · 3



Final Answer:



f'(x) = 12(3x + 1)³



---



\## 🧠 Example 3



f(x) = √(x² + 1)



Rewrite first:



f(x) = (x² + 1)^(1/2)



Step 1: Derivative of outer power



= (1/2)(x² + 1)^(-1/2)



Step 2: Derivative of inside



= 2x



Step 3: Multiply



f'(x) = (1/2)(x² + 1)^(-1/2) · 2x



Simplify:



f'(x) = x(x² + 1)^(-1/2)



---



\## 🧠 Pattern to Remember



If:



f(x) = (u)^n



Then:



f'(x) = n(u)^(n-1) · u'



Where:



u = inner function  

u' = derivative of inner function  



---



\## 🤖 Why Chain Rule Is Extremely Important in Deep Learning



Neural networks are nested functions.



Example:



Loss = L( activation( wx + b ) )



That is:



Function inside function inside function.



Backpropagation uses Chain Rule repeatedly.



Without Chain Rule:



Deep learning cannot work.



Chain Rule = backbone of backpropagation.



---



\## 🧩 Intuition Summary



Outer function changes  

Inner function also changes  



Total change =



(outer change) × (inner change)



Chain Rule connects multiple layers of change.



---



\## 🔹 Practice Questions



1\. d/dx (x² + 5)³ = ?  

2\. d/dx (2x + 1)⁵ = ?  

3\. d/dx √(3x² + 4) = ?  



Answers:



1\. 3(x² + 5)² · 2x  

2\. 5(2x + 1)⁴ · 2  

3\. (1/2)(3x² + 4)^(-1/2) · 6x  

