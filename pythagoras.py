#!/usr/bin/env python
# coding: utf-8

# In[9]:


p=int(input("Enter side 1 : "))
b=int(input("Enter side 2 : "))
h=int(input("Enter side 3 : "))
def checkright(p,b,h):
    if h==p+b or p==b+h or b==h+p:
        return True
p*=p
h*=h
b*=b
if checkright(p,b,h):
    print("This is right trainagle")
else:
    print("NOT Rigt traingle")


# In[ ]:




