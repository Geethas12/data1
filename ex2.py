#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
im=cv2.imread('ing.png')
grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
LAB=cv2.cvtColor(im,cv2.COLOR_BGR2LAB)
RGB=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
HSV=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
HLS=cv2.cvtColor(im,cv2.COLOR_BGR2HLS)
YUV=cv2.cvtColor(im,cv2.COLOR_BGR2YUV)

cv2.imshow("convert BGR to GRAY",grey)
cv2.imshow("convert BGR to LAB",LAB)
cv2.imshow("convert BGR to RGB",RGB)
cv2.imshow("convert BGR to HSV",HSV)
cv2.imshow("convert BGR to HLS",HLS)
cv2.imshow("convert BGR to YUSV",YUV)
           
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


import cv2
a=cv2.imread('in1.jpg')
b=cv2.imread('in1.jpg')
sum=a+b
sub=a-b
mul=a*b
div=a/b
cv2.imshow("sum",sum)
cv2.imshow("sub",sub)
cv2.imshow("mul",mul)
cv2.imshow("div",div)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




