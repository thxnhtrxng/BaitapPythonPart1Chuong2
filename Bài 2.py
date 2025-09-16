#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bài 2: Trích xuất host từ email
data = "minhnhutvh@gmail.com"

# Tìm vị trí dấu @
position = data.find("@")   # Kết quả: 10

# Lấy chuỗi từ sau @ đến hết
host = data[position + 1:]

print("Host là:", host)

