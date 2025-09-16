#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Bài 3: Trích xuất host từ email + thời gian
data = "minhnhutvh@gmail.com Sat Jan 5 09:14:16"

# Tìm vị trí bắt đầu (sau @)
start_position = data.find("@")   # 10

# Tìm vị trí kết thúc (khoảng trắng đầu tiên sau @)
end_position = data.find(" ", start_position)

# Cắt chuỗi từ sau @ tới trước dấu cách
host = data[start_position + 1 : end_position]

print("Host là:", host)


# In[ ]:




