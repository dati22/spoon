#!/usr/bin/env python
# coding: utf-8

# In[8]:


#калькулятор
print('добро пожаловать в мой калькулятор')
a=int(input('введите число 1:'))
b=int(input('введите число 2:'))
v=int(input('какую опрецию выхотите выполнить? \n 1 сложение\n 2 вычитание\n 3 деление\n 4 умножение'))
if v==1:
    r=a+b
    p='сложение'
    t=p
if v==2:
    r=a-b
    q='вычитание'
    t=q
if v==3:
    r=float(a/b)
    m='деление'
    t=m
if v==4:
    r=a*b
    n='умножение'
    t=n
print('результат',t,"=",r)
    


# In[10]:


x=-6
if (x>0):
  X = x*10
else:
  X = x*8
print(X)


# In[14]:


x=98
if (x > 0):
    print("положительное")
elif(X < 0):
    print("отрицательное")
else :
    print("равно нулю")


# In[18]:


print(True and True)
print(True or True)
print(not False)


# In[ ]:




