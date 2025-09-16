#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Nhập số nguyên a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra chia cho 0
if b != 0:
    thuong = a / b
    phan_du = a % b
else:
    thuong = "Không xác định (chia cho 0)"
    phan_du = "Không xác định (chia cho 0)"

# log10(a) chỉ tính được khi a > 0
if a > 0:
    log_a = math.log10(a)
else:
    log_a = "Không xác định (a <= 0)"

# a^b
mu = a ** b

# Xuất kết quả
print("Tổng của a và b:", tong)
print("Hiệu của a và b:", hieu)
print("Tích của a và b:", tich)
print("Thương của a chia cho b:", thuong)
print("Phần còn lại khi a chia cho b:", phan_du)
print("Kết quả log10(a):", log_a)
print("Kết quả a^b:", mu)


# In[ ]:




