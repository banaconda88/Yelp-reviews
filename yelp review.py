#!/usr/bin/env python
# coding: utf-8

# In[10]:


file = open("yelp_review.txt")
yelp = file.read().split()


# In[11]:


rev = []
for y in yelp:
    if int(y) >= 5 or int(y)<= 1:
        continue
    else:
        rev.append(int(y))
print(rev)

