#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import seaborn as sns
import warnings
from pylab import rcParams
from scipy.stats import f_oneway
from scipy.stats import ttest_ind


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings("ignore")
rcParams['figure.figsize'] =20,10
rcParams['font.size'] =30
sns.set()
np.random.seed(8)


# In[7]:


def plot_distribution(inp):
    plt.figure()
    ax = sns.distplot(inp)
    plt.axvline(np.mean(inp), color="k", linestyle="dashed",linewidth=5)
    _, max_=plt.ylim()
    plt.text(
        inp.mean() + inp.mean() / 10,
        max_ - max_ / 10,
        "Mean: {:.2f}".format(inp.mean()),
    )
    return plt.figure
        


# In[8]:


ger_sales = np.load("C:/Users/User/Downloads/germany_sales.npy")


# In[9]:


ger_sales = np.load("C:/Users/User/Downloads/germany_sales.npy")


# In[10]:


ger_sales


# In[11]:


len(ger_sales)


# In[12]:


plot_distribution(ger_sales)


# In[14]:


fr_sales = np.load("C:/Users/User/Downloads/france_sales.npy")


# In[15]:


fr_sales


# In[16]:


len(fr_sales)


# In[17]:


plot_distribution(fr_sales)


# In[18]:


plt.figure()
ax1 = sns.distplot(fr_sales)
ax2 = sns.distplot(ger_sales)
plt.axvline(np.mean(fr_sales),color='b',linestyle='dashed',linewidth=5)
plt.axvline(np.mean(ger_sales),color='orange',linestyle='dashed',linewidth=5)


# In[25]:


def compare_2_groups(arr_1,arr_2,alpha, sample_size):
    stat, p =ttest_ind(arr_1,arr_2)
    print('statistics=%.3f,p=%.3f' % (stat, p))
    if p > alpha:
        print('same distributions(fall to reject H0)')
    else:
        print("different distributions(reject H0)")


# In[26]:


sample_size =15
ger_sampled = np.random.choice(ger_sales, sample_size)
fr_sampled = np.random.choice(fr_sales, sample_size)
compare_2_groups(ger_sampled, fr_sampled, 0.05, sample_size)


# In[ ]:




