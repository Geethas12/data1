#!/usr/bin/env python
# coding: utf-8

# In[7]:


#adaptive and guassian thresholding


import cv2
import numpy as np
img = cv2.imread('d.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)
blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('blur', blur)

ret,th1 = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
cv2.imshow('Global', th1)
cv2.imwrite('Global.jpg',th1)

th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Mean', th2)
cv2.imwrite('AM.jpg',th2)

th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Gaussian', th3)
cv2.imwrite('AG.jpg',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


#basic transformation

import cv2 
import numpy as np 

image = cv2.imread('calvinHobbes.jpeg') 

height, width = image.shape[:2] 
quarter_height, quarter_width = height/4, width/4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(image, T, (width, height)) 

cv2.imshow("Originalimage", image) 
cv2.imshow('Translation', img_translation)
cv2.imwrite('Translation.jpg', img_translation) 
cv2.waitKey() 

cv2.destroyAllWindows() 


# In[13]:


#box filter
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda1.jpg')

blur = cv2.blur(img,(5,5))

plt.imshow(img),plt.title('Original')
plt.show()
cv2.imwrite('orig.png', img)
plt.xticks([]), plt.yticks([])
plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('boxfil.png', blur)


# In[19]:


#shading correction

import cv2

img = cv2.imread('ChessBoardGrad.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImg)
cv2.waitKey(0)
filtersize = 513
gaussianImg = cv2.GaussianBlur(grayImg, (filtersize, filtersize), 128)
cv2.imshow('Converted Image', gaussianImg)
cv2.waitKey(0)
newImg = (grayImg-gaussianImg)
cv2.imshow('New Image', newImg)
cv2.imwrite('Converted.png', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[23]:



#video frames
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




