#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#create a ID array
arr1=np.array([1,2,3])
print(arr1)


# In[5]:


# accessing elements from the array

arr1[2]


# In[6]:


# change an element from the array

arr1[2]=5

arr1


# In[7]:


# create a 2D array

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[9]:


#check the shape of the array

print("the shape is 2 rows and 3 columns:",arr2.shape)


# In[10]:


# Acessing elements from the array

print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[12]:


# Array of type string

arr3=np.array(['India','China','USA','Mexico'])
print(arr3)


# In[13]:


arr3[1]


# In[18]:


# Array of evenly spaced values within a specified interval

arr = np.arange(0, 20, 2)
print (arr)


# In[20]:


# Array of evenly specified interval

arr=np.linspace(0, 10,20)
print(arr)


# In[22]:


# Array of random values between 0 and 1 in a gibven shape

arr = np.random.rand(10)
print(arr)
print('\n')
arr = np.random.rand(3,4)
print(arr)


# In[23]:


# Array of constant values in a given shape

print(np.full((4,6),10))


# In[24]:


# create an array by repetition
# repeat rach element of an array by a specified number of times

arr = [0, 1, 2]
print(np.repeat(arr, 3))


# In[25]:


# repeat an array by a specified number of times

arr =[0, 1, 2]
print(np.tile(arr, 3))


# In[26]:


# create an idenity martrix

identity_matrix = np.eye(3)
print(identity_matrix)


# In[27]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[28]:


arr = np.random.rand(5,5)
print(arr)


# In[29]:


# sum along the column
print(np.sum(arr, axis=0))


# In[31]:


#sum along the row
print(np.sum(arr, axis=1))


# In[33]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[35]:


#sort an array
arr = np.random.rand(5,5)
print(arr)


# In[36]:


#sort along the row

print(np.sort(arr, axis=1))


# In[37]:


# Append elements to an array

arr= np.array([4,5,6,7])


# In[38]:


arr1 = np.append(arr, 8)
arr1


# In[39]:


arr2=np.append(arr, [9,10,11])
print(arr2)


# In[40]:


# delete multiple elements
arr2 = np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5 = np.delete(arr2, [1,4])
print(arr5)


# In[41]:


# combine and split an array

arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[43]:


# combine the array items by column

cat = np.concatenate((arr1,arr2), axis=0)
print(cat)


# In[44]:


# combine array items by row

cat = np. concatenate((arr1, arr2), axis=1)
print(cat)


# In[ ]:




