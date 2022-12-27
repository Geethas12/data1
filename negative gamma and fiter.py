#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import imageio
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
pic=imageio.imread("ima.jfif")
plt.figure(figsize=(6,6))
plt.imshow(pic)
plt.axis('off');


# In[10]:


negative=255-pic#neg=(L-1)-img
plt.figure(figsize= (6,6))
plt.imshow(negative);
plt.axis('off');


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic=imageio.imread('ima.jfif')
gray=lambda rgb : np.dot(rgb[...,:3],[0.299,0.587,0.114])
gray=gray(pic)

max_=np.max(gray)

def log_transform():
    return(255/np.log(1+max_))*np.log(1+gray)
plt.figure(figsize=(5,5))
plt.imshow(log_transform(),cmap=plt.get_cmap(name='gray'))
plt.axis('off');


# In[15]:


import imageio
import matplotlib.pyplot as plt
#gama encoding
 
pic=imageio.imread('ima.jfif')
gamma=2.2#gama<1-dark;gama >1- bright

gamma_correction=((pic/255)**(1/gamma))
plt.figure(figsize=(5,5))
plt.imshow(gamma_correction)
plt.axis('off');


# In[ ]:




