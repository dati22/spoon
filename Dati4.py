#!/usr/bin/env python
# coding: utf-8

# In[3]:


#задание №1
winter=(12,1,2)
spring=(3,4,5)
summer=(6,7,8)
fall=(9,10,11)
a=int(input("введите номер месяца:"))
if (a in winter):
    print("сейчас зима")
elif (a in spring):
    print("сейчас весна")
elif (a in summer):
    print("сейчас лето")
elif (a in fall):
    print("сейчас осень")
else:
    print("неверный ввод")


# In[8]:


#задание №2
a=int(input())
if a<=0:
    print(False)
else:
    print(True)


# In[ ]:




