#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bài 5: Xử lý chuỗi

# (1) Nhập chuỗi
st = input("Enter your string: ")

# (2) 5 ký tự đầu tiên
first_five_characters = st[:5]

# (3) 5 ký tự cuối cùng
last_five_characters = st[-5:]   # cách viết ngắn hơn so với len(st)-5

# (4) Lặp lại 4 lần trên 1 dòng, cách nhau 1 khoảng trắng
four_str_one_line = (st + " ") * 4

# (5) Lặp lại 4 lần trên 4 dòng
four_str_four_line = (st + "\n") * 4

# (6) Xuất kết quả
print("First five characters are:", first_five_characters)
print("Last five characters are:", last_five_characters)
print("Four strings of one line are:", four_str_one_line)
print("Four strings of four lines are:\n" + four_str_four_line)


# In[ ]:




