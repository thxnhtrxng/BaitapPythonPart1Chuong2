#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bài 13: Tính tổng 1 + 2 + ... + n

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra hợp lệ
if n > 0:
    total = (n * (n + 1)) // 2   # dùng // để ra số nguyên
    print("Tổng từ 1 đến", n, "là:", total)
else:
    print("Vui lòng nhập một số nguyên dương.")


# In[ ]:




