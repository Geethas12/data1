#!/usr/bin/env python
# coding: utf-8

# In[2]:


#program to perfrom bitwise

#import opencv
import cv2 

#read the images
img1 = cv2.imread('a.png')
img2 = cv2.imread('b.png')

#compute bitwise and on both image
and_img=cv2.bitwise_and(img1,img2)
or_img=cv2.bitwise_or(img1,img2)
not_img=cv2.bitwise_not(img1,img2)

#display the computed and image
cv2.imshow('Bitwise AND image',and_img)
cv2.imshow('Bitwise OR image',or_img)
cv2.imshow('Bitwise NOT image',not_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




