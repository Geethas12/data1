#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2

# Open the image.
img = cv2.imread('cat_damaged.png')

# Load the mask.
mask = cv2.imread('cat_mask.png', 0)

# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Write the output.
cv2.imwrite('cat_inpainted.png', dst)

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


from PIL import Image
import numpy as np

# Opening the image and converting
# it to RGB color mode
# IMAGE_PATH => Path to the image
img = Image.open("dead letter.png").convert('RGB')

# Extracting the image data &
# creating an numpy array out of it
img_arr = np.array(img)

# Turning the pixel values of the 400x400 pixels to black
img_arr[50 : 200, 100 : 300] = (0, 0, 0)

# Creating an image out of the previously modified array
img = Image.fromarray(img_arr)

# Displaying the image
img.show()


# In[3]:


#contours
import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('test.png')
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


#canvas
import cv2
import numpy as np
from skimage import io     

# Read images
frame = cv2.cvtColor(io.imread('crop.png'), cv2.COLOR_RGB2BGR)
image = cv2.cvtColor(io.imread('nature.jpg'), cv2.COLOR_RGB2BGR)

# Color threshold red frame; single color here, more sophisticated solution would be using cv2.inRange
mask = 255 * np.uint8(np.all(frame == [36, 28, 237], axis=2))


# Find inner contour of frame; get coordinates
contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = min(contours, key=cv2.contourArea)
(x, y, w, h) = cv2.boundingRect(cnt)


# Copy appropriately resized image to frame
frame[y:y+h, x:x+w] = cv2.resize(image, (w, h))


cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[25]:


import matplotlib.pyplot as plt
from PIL.ImageChops import subtract, multiply, screen, difference, add
# load two consecutive frame images from the video
im1 = Image.open("goal1.png")
plt.imshow(im1)
plt.show()
im2 = Image.open("goal2.png")
plt.imshow(im2)
plt.show()
im = ImageChops.difference(im1, im2)
#plt.figure(figsize=(40,50))
im.save("sportoutput.png")
plt.imshow(im)
plt.show()


# In[ ]:





# In[16]:





# In[19]:





# In[18]:





# In[ ]:




