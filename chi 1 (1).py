#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


acad = pd.read_excel('acad.xlsx')


# In[6]:


acad


# In[8]:


#cross table between gender and student's motivation
obs =pd.pivot_table(acad[['g','sm']],index ='g',columns='sm',aggfunc=len)
obs


# In[9]:


## perform chi2 test to check independence
from scipy.stats import chi2_contingency


# In[10]:


chi2,p,dof,tbl =chi2_contingency(obs)


# In[11]:


chi2


# In[12]:


p


# In[13]:


dof


# In[14]:


tbl


# In[ ]:




