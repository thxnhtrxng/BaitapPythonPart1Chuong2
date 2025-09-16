#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bài 11: Diện tích cánh đồng theo mẫu Anh

# Nhập chiều dài và rộng (m)
length = float(input("Nhập chiều dài cánh đồng (m): "))
width = float(input("Nhập chiều rộng cánh đồng (m): "))

# Tính diện tích m²
area_m2 = length * width

# Quy đổi sang mẫu Anh
area_acres = area_m2 / 43560

print("Diện tích cánh đồng là:", area_acres, "mẫu Anh")


# In[ ]:




