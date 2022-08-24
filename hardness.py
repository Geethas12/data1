#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error


# In[2]:


data=pd.read_excel("HARDNESS.xls")


# In[3]:


data


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


x=data["Hardness"].values.reshape(-1,1)
y=data["Tensile strength"].values.reshape(-1,1)
x_train, x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=88)


# In[6]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[7]:


len(x_train)


# In[8]:


len(x_test)


# In[9]:


x_train


# In[12]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()


# In[13]:


reg.fit(x_train,y_train)


# In[14]:


reg.intercept_


# In[15]:


reg.coef_


# In[16]:


y_predict=reg.predict(x_test)


# In[17]:


y_predict


# In[18]:


mean_squared_error(y_test, y_predict)


# In[19]:


reg.score(x_test,y_test)


# In[20]:


reg.score(x_train,y_train)


# In[ ]:




