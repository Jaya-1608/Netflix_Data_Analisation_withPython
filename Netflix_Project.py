#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd


# In[23]:


data = pd.read_csv("netflix_data.csv")
data


# In[26]:


# ques 1
data.drop_duplicates()


# In[30]:


# ques 2
data.isnull()


# In[31]:


data.info()


# In[32]:


#ques 3


# In[33]:


# ques 4


# In[34]:


# ques 5
data[(data["Category"]=="TV Show")]


# In[42]:


# ques 6
data[(data["Release_Date"] == "2020")]


# In[44]:


# ques 7
data[(data["Country"] == "India")]


# In[46]:


# ques 8
data.head(11)


# In[49]:





# In[ ]:




