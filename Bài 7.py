#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Nhập các cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Nhập góc C (radian)
C = float(input("Nhập góc C (radian): "))

# Tính diện tích
S = 0.5 * a * b * math.sin(C)

print("Diện tích tam giác là:", S)


# In[ ]:




