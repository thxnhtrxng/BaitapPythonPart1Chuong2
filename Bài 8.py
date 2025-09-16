#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Nhập cạnh tam giác đều
a = float(input("Nhập cạnh tam giác đều: "))

# Nửa chu vi
p = (a + a + a) / 2

# Áp dụng công thức Heron
S = math.sqrt(p * (p - a) * (p - a) * (p - a))

print("Diện tích tam giác đều là:", S)


# In[ ]:




