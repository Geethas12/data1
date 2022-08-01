#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np


# In[10]:


df=pd.read_csv('C:/Users/User/Downloads/employees.csv')


# In[11]:



print(df.head())


# In[12]:


print(df.dtypes)
print(df.describe())


# In[13]:


print('Salary')
print(df['Salary'].head(10))


# In[14]:


print(df['Gender'].head(10))


# In[15]:


missing_value_formats = ["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values = missing_value_formats)
print(df['Gender'].head(10))


# In[16]:


import pandas as pd
missing_value_formats = ["n.a","?","NA","n/a","na","--"]
df=pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values = missing_value_formats)
def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
df['Salary']=df['Salary'].map(make_int)
print(df['Salary'].head()) 


# In[17]:


print(df['Salary'].head())


# In[18]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[19]:


null_filter=data1['Gender'].notnull()
print(df[null_filter].head())


# In[20]:


print(df.isnull().values.any())


# In[21]:


print(df.isnull().sum())


# In[22]:


new_df =df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[23]:


new_df =df.dropna(axis=0,how='any')
new_df =df.dropna(axis=0,how='all')
new_df =df.dropna(axis=1,how='any')
new_df =df.dropna(axis=1,how='all')


# In[24]:


print('all')


# In[25]:


new_df =df.dropna(axis=0,how='any')
print(new_df)


# In[26]:


new_df =df.dropna(axis=0,how='all')
print(new_df)


# In[27]:


new_df =df.dropna(axis=1,how='any')
print(new_df)


# In[28]:


new_df =df.dropna(axis=1,how='all')
print(new_df)


# In[29]:


df['Salary'].fillna(0)


# In[30]:


df['Gender'].fillna('no Gender')


# In[31]:


df['Salary'].fillna(method='pad')


# In[32]:


df['Gender'].fillna(method='bfill')


# In[33]:


df['Salary'].fillna(df['Salary'].median())


# In[35]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[36]:


df['Salary'].replace(to_replace =np.nan,value=0)


# In[37]:


df['Salary'].interpolate(method='linear',direction='forward')


# In[ ]:




