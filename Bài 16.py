#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Nhập chiều cao từ người dùng
d = float(input("Nhập chiều cao rơi (m): "))

# Các hằng số
vi = 0      # vận tốc đầu (m/s)
a = 9.8     # gia tốc trọng trường (m/s^2)

# Tính vận tốc cuối
vf = math.sqrt(vi**2 + 2 * a * d)
print(f"Vận tốc của vật khi chạm đất: {vf:.2f} m/s")


# In[ ]:




