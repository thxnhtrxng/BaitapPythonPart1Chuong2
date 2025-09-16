#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bài 12: Tính tiền bữa ăn

# Nhập chi phí bữa ăn
meal_cost = float(input("Nhập chi phí bữa ăn: "))

# Tính tiền boa (18%) và thuế (5%)
tip = 0.18 * meal_cost
tax = 0.05 * meal_cost

# Tổng cộng
total = meal_cost + tip + tax

# Xuất kết quả với 2 chữ số thập phân
print(f"Tiền bữa ăn: {meal_cost:.2f}")
print(f"Tiền boa (18%): {tip:.2f}")
print(f"Tiền thuế (5%): {tax:.2f}")
print(f"Tổng cộng: {total:.2f}")


# In[ ]:




