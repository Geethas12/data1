#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[17]:


# load the dataset
data1=pd.read_csv('D:/geethanjali/data analytics/gapminder_full (1).csv')


# In[18]:


data1


# In[19]:


#display the head of the dataset(shows only 5 rows)
data1.head()


# In[20]:


#get number of rows and columns
print(data1.shape)


# In[21]:


#get column names
data1.columns


# In[22]:


#get the dtype of each column
data1.dtypes


# In[23]:


#get more information about data
data1.info()


# In[24]:


#looking at columns,rows and cells
#get the country column and save it in a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[26]:


#show the last 5 observation
country_data.tail()


# In[27]:


#looking at contry, continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[28]:


subset.tail()


# In[29]:


#analytical sumary of the dataset
data1.describe(include='all')


# In[30]:


#histogram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[34]:


#relation ship between cataagrical and continious variable
sns.boxplot(x="year",y="life_exp",data=data1)


# In[35]:


#drop irrelevant coloumns
data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[41]:


#renaming the column name
data1=data1.rename(columns={"country" : "countries"})
data1.head(5)


# In[43]:


#rows containing duplicate data
duplicate_rows=data1[data1.duplicated()]
print('number of duplicate rows:',duplicate_rows.shape)


# In[44]:


#count the rows before moving the data
data1.count()


# In[ ]:




