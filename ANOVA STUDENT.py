#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as  plt
import math
from scipy import stats
from scipy.stats import f
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[14]:


a=[4,3,2]
b=[2,4,6]
c=[2,1,3]


# In[15]:


stats.f_oneway(a,b,c)


# In[16]:


data=pd.read_excel("D:/geethanjali/data analytics/oneway.xlsx")


# In[17]:


data


# In[23]:


data_new = pd.melt(data.reset_index(), id_vars=['index'], value_vars=['teaching methodology1','teaching methodology2','teaching methodology 3'])
data_new.columns =['index','Treatments','value']


# In[24]:


data_new


# In[28]:


model = ols('value ~ C(Treatments)', data=data_new).fit()
anova_table =sm.stats.anova_lm(model, typ=1)
anova_table


# In[ ]:





# In[ ]:




