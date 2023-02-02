#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Code to apply operations on all the images  present in a folder one by one
# operations such as rotating, cropping,

from PIL import Image
from PIL import ImageFilter
import os

def main():
    inPath ="C:/Users/User/Desktop/image"
    outPath ="C:/Users/User/image"
    for imagePath in os.listdir(inPath):
        inputPath = os.path.join(inPath, imagePath)
        img = Image.open(inputPath)
        fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
        img.rotate(90).save(fullOutPath)
        print(fullOutPath)
if __name__ == '__main__':
    main()


# In[20]:


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




