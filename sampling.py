#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sampling up
import cv2
import matplotlib.pyplot as plt
image=cv2.imread('ing.png')
cv2.imshow("image before pyrUp:",image.shape)

image=cv2.pyrUp(image)
cv2.imshow("image after pyUp:",image.shape)
cv2.imshow('Up sample',image)
fig, ax=plt.subplots()
plt.imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


#sampling down
import cv2
import matplotlib.pyplot as plt
image=cv2.imread('ing.png')
cv2.imshow("image before pyrDown:",image.shape)

image=cv2.pyrDown(image)
cv2.imshow("image after pyrDown:",image.shape)
cv2.imshow('Down sample',image)
fig, ax=plt.subplots()
plt.imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


#quantization with PIL in Downsampling
# Importing Image module from PIL package
from PIL import Image
import PIL

# creating a image object (main image)
im1 = Image.open("f2.jpg")

# quantize a image
im1 = im1.quantize(150)

# to show specified image
im1.show()


# In[7]:


# types of sampling in that up sampling three types nearset neighbour interplotion,bilnear,bicubic interpolation

import cv2
import numpy as np
img=cv2.imread('f2.jpg')


near_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST)

bicubic_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_CUBIC)
linear_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_LINEAR)
cv2.imshow('near_img',near_img)
cv2.imshow('bicubic_img',bicubic_img )
cv2.imshow('linear_img',linear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




