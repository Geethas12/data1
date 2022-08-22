#!/usr/bin/env python
# coding: utf-8

# In[4]:


import scipy
from scipy.stats import chi2
from scipy.stats import poisson


# In[5]:


import pandas as pd
import numpy as np


# In[6]:


data = pd.read_excel('p_distribution.xlsx')
data


# In[9]:


Observed_Freq =data['Frequency']


# In[10]:


Observed_Freq


# In[12]:


total_arrival =600
total_time_period =100
mu = total_arrival/total_time_period


# In[13]:


mu


# In[15]:


Expected_Freq = []
for i in range(len(Observed_Freq)):
    E_Freq = 100*poisson.pmf(i, mu)
    Expected_Freq.append( E_Freq)


# In[16]:


Expected_Freq


# In[17]:


Expected_Freq_round_off=[round(elem, 2) for elem in Expected_Freq]
Expected_Freq_round_off


# In[18]:


df= pd.DataFrame(list(zip(Observed_Freq,Expected_Freq_round_off)),columns =['Obseved Frequency','Expected Frequency'])
df


# In[22]:


obs_freq=[5,10,14,20,12,12,9,8,10]
Expected_Freq =[6.20,8.92,13.39,16.06,16.06,13.77,10.33,6.88,8.39]


# In[23]:


scipy.stats.chisquare(obs_freq, Expected_Freq)


# In[ ]:




