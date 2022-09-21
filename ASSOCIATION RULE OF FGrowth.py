#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


dataset=pd.read_csv('retail_bakery_transactions.csv')


# In[5]:


dataset.columns =dataset.columns.str.lower()


# In[6]:


dataset =dataset.applymap(lambda s: s.lower() if type(s) == str else s)


# In[7]:


dataset.head()


# In[8]:


dataset.info()


# In[9]:


dataset.isnull().sum()


# In[20]:


transaction_list =dataset.groupby(['transaction','date_time'])['item'].apply(lambda x: list(x))


# In[22]:


transaction_list.head()


# In[23]:


df=transaction_list.values.tolist()


# In[24]:


df[:5]


# In[25]:


from mlxtend.preprocessing import TransactionEncoder


# In[26]:


encoder= TransactionEncoder().fit(df)


# In[27]:


onehot =encoder.transform(df)


# In[29]:


transf_df =pd.DataFrame(onehot, columns =encoder.columns_)


# In[30]:


transf_df.head()


# In[31]:


from mlxtend.frequent_patterns import fpgrowth


# In[33]:


frequent_itemsets = fpgrowth(transf_df, min_support = 0.05,use_colnames =True)


# In[34]:


frequent_itemsets.sort_values('support', ascending=False)


# In[36]:


frequent_itemsets['length'] =frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets


# In[37]:


frequent_itemsets['length'].value_counts()


# In[39]:


from mlxtend.frequent_patterns import association_rules


# In[40]:


rules = association_rules(frequent_itemsets,metric ='lift', min_threshold =1.0)


# In[41]:


rules.head()


# In[ ]:




