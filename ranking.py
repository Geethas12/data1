#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# To sort Lexicographically by row or column index,usethe sort_index method,
#which returns a new,sorted object
obj = pd.Series(range(4),index=['d','a','b','c'])
obj.sort_index()


# In[5]:


#with a DataFrame,you can sort by index on either axis
frame = pd.DataFrame(np.arange(8).reshape((2,4)),index=['three', 'one'],columns=['d', 'a', 'b', 'c'])
frame.sort_index()


# In[6]:


frame.sort_index(axis=1)


# In[7]:


# the data is sorted in ascending order by default,but can be sortedin decending order,too
frame.sort_index(axis=1, ascending=False)


# In[8]:


# to sort a series by its values , use its sort_values method
obj = pd.Series([4, 7, -3, 2])
obj.sort_values()


# In[10]:


# any missing values are sorted to the end of the series by default
obj = pd.Series([4, np.nan, np.nan, -3,2])
obj.sort_values()


# In[11]:


# we can use the data in one or more columns as the sort keys
#to do so, pass one or more column names to the key by option of sort_values
frame = pd.DataFrame({ 'a':[0, 1, 0, 1],'b':[4, 7,-3, 2]})
frame


# In[12]:


frame.sort_values(by='b')


# In[13]:


# to sort by multiple columns, pass a list of names
frame.sort_values(by=['a', 'b'])


# In[15]:


# ranking assigns ranks from one through the number of valid data points in an array
# by default rank breaks ties by assigning each group the mean rank
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()


# In[16]:


#ranks can also br assigned according to the order in which they"re observed in the data
obj.rank(method='first')


# In[18]:


# rank in descending order
# assign tie values the maximum rank in the group
obj.rank(ascending=False, method='max')


# In[19]:


# DataFrame can compute ranks over the rows or the columns
frame = pd.DataFrame({'a': [0, 1, 0, 1],'b': [4.3, 7, -3, 2],'c': [-2, 5, 8, -2.5]})
frame


# In[20]:


frame.rank(axis='columns')


# In[ ]:




