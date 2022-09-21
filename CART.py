#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data =pd.read_excel('CART.xlsx')
data


# In[3]:


import sklearn
from sklearn.preprocessing import LabelEncoder


# In[4]:


le_age =LabelEncoder()
le_income=LabelEncoder()
le_student=LabelEncoder()
le_credit_rating=LabelEncoder()
le_buys_computer=LabelEncoder()


# In[5]:


data['age_n']=le_age.fit_transform(data['age'])
data['income_n']=le_income.fit_transform(data['income'])
data['student_n']=le_student.fit_transform(data['student'])
data['credit_rating_n']=le_credit_rating.fit_transform(data['credit_rating'])
data['buys_computer_n']=le_buys_computer.fit_transform(data['buys_computer'])


# In[6]:


data.head()


# In[8]:


data_new= data.drop(['age','income','student','credit_rating','buys_computer'],axis='columns')
data_new


# In[9]:


feature_cols=['age_n','income_n','student_n','credit_rating_n']
x=data_new.drop(['buys_computer_n','RID'],axis='columns')
y=data_new['buys_computer_n']


# In[10]:


x


# In[11]:


y.head()


# In[12]:


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
dt=clf.fit(x,y)
dt


# In[13]:


get_ipython().system('pip install py')


# In[19]:


from sklearn.tree import export_graphviz
import six
import sys
sys.modules['sklearn.externals.six']=six
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus


# In[22]:


dot_data=StringIO()
export_graphviz(dt, out_file=dot_data,
               filled=True,rounded=True,
               special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph =pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Decision_Tree.png')


# In[24]:


Image(graph.create_png())


# In[ ]:





# 
