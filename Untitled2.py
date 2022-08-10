#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats


# In[5]:


x = stats.norm.rvs(30,10,30)
results = stats.ttest_1samp(x, 27)
alpha = 0.05
if(results[0] < 0) & (results[1]/2 < alpha):
    print("reject null hypothesis, mean is greayer than 27")
else:
    print("accept null hypothesis")


# In[7]:


y = stats.norm.rvs(30,10,30)
res = stats.ttest_1samp(x, 505)


# In[8]:


res# cont use stats.ttest as alpha is changed


# In[9]:


import math
xbar =505
SEM =(10/math.sqrt(30))


# In[10]:


mu=500
z = (xbar - mu)/SEM
z


# In[15]:


pval =2*(1-stats.norm.cdf(z))
pval


# In[16]:


# pvali<alpha, so reject null hypothesis


# In[18]:


alpha=0.003
if (pval<alpha):
    print("reject the hypothesis")
else:
    print("accept the hypothesis")


# In[ ]:




