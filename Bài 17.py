#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Nhập dữ liệu từ người dùng
Ta = float(input("Nhập nhiệt độ không khí (°C): "))
V = float(input("Nhập tốc độ gió (km/h): "))

# Công thức tính WCI
WCI = 13.12 + (0.6215 * Ta) - (11.37 * (V ** 0.16)) + (0.3965 * Ta * (V ** 0.16))

# Làm tròn đến số nguyên gần nhất
WCI = round(WCI)

# Xuất kết quả
print("Chỉ số gió lạnh (WCI) là:", WCI)


# In[ ]:




