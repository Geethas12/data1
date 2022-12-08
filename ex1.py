#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
image=cv2.imread("C:/Users/User/Desktop/ing.png")
cv2.imshow("to display a image",image)
cv2.waitKey(0)


# In[2]:


cv2.imwrite('C:/Users/User/Desktop/ing.png',image)


# In[3]:


import matplotlib.pyplot as plt
fig, ax=plt.subplots()
plt.imshow(image)


# In[6]:





# In[7]:


import cv2
image=cv2.imread("D:/ing.png",0)
cv2.imshow('to display a image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


# find R,G,B colors
import cv2
imgi=cv2.imread("ing.png",1)
B, G, R=cv2.split(imgi)
print(B)
print(G)
print(R)


# In[9]:


imgi=cv2.imread("ing.png",1)
cv2.imshow("original",imgi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


cv2.imshow("blue",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:


cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


print(imgi.size)


# In[15]:


#find height and width
from PIL import Image
x="ing.png"
img=Image.open(x)
width=img.width
height=img.height
print("the height of the image is",height)
print("the width of the image is",width)


# In[16]:


#height ,width of channel
print(imgi.shape)


# In[19]:


#finding no.of channel
import numpy
Image=cv2.imread("ing.png",0)
print("no of channel is : "+str(Image.ndim))
#finding the height , width together
print("no. of channel is:"+str(Image.shape))
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


# resize image by giving number
from PIL import Image
filepath='ing.png'
img=Image.open(filepath)
new_image=img.resize((300,200))
new_image


# In[ ]:




