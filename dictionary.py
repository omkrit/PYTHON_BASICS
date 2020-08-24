#!/usr/bin/env python
# coding: utf-8

# In[30]:


print("hello")

#dictionary

dict1={"animal":"lion","sweet":"rasgulla","number":1}
print(dict1)

#dictonary key

dict2={"govind":"choclate","dipSardar":"rasgulla","vedansh":"golgappe"}
print(dict2["govind"])

#nested dictionary

dict3={"govind":"choclate","dipSardar":"rasgulla","vedansh":"golgappe","jessica":{"lunch":"rice","dinner":"roti"}}
print(dict3["jessica"])

#length of dictionary

print(len(dict3))

#addition

dict2["str"]="kind"
print(dict2)

#deletion in dictionary 2

del dict2["str"]
print(dict2)

#pop function & pop item

dict2.pop("govind")
print(dict2)
dict1.popitem()   #pop ite from last
print(dict1)

#no repetatiion of key otherwie it overwrites
d3={"number":7,"number":3}
print(d3)

# deletion of dictionary

#del d3
# print(d3)  #cause error of not found dictionary
d3.clear()
print(d3)

# copy one dictionary to another

d4=d3.copy()
print(d4)
d3["number"]=2020

#pint value of key
print(d3.get("number"))

#update number

d3.update({"har":"jas","om":"krit","nav":"een"})
print(d3)
d3["om"]="singh"
print(d3)

#print keys only & values only seperatly

print(d3.keys())
print(d3.values())
z=dict(list(d3.items())+list(d4.items()))
print(z)


# In[ ]:




