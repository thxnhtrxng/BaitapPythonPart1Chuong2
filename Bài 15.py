#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Nhập dữ liệu
M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập độ thay đổi nhiệt độ (°C): "))

# Nhiệt dung riêng của nước
C = 4.186  

# Tính năng lượng Q (Joules)
Q = M * C * delta_T
print(f"Năng lượng cần thiết: {Q:.2f} Joules")

# Đổi sang kWh
kWh = Q * 2.777e-7
print(f"Tương đương: {kWh:.6f} kWh")

# Tính chi phí (8.9 cent/kWh)
cost = kWh * 8.9
print(f"Chi phí: {cost:.4f} cent")


# In[ ]:




