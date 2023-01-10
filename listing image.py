#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#listing the files of png,jpg or jpeg
# import the modules
import os
from os import listdir

# get the path or directory
folder_dir = "C:/Users/User/image processing"
for images in os.listdir(folder_dir):

# check if the image ends with png or jpg or jpeg
 if (images.endswith(".png") or images.endswith(".jpg")	or images.endswith(".jpeg")):
# display
   print(images)


# In[2]:


#listing the png file
# import required module
from pathlib import Path

# get the path/directory
folder_dir = 'C:/Users/User/image processing'

# iterate over files in
# that directory
images = Path(folder_dir).glob('*.png')
for image in images:
	print(image)


# In[3]:


#listing the png file
# import required module
from pathlib import Path

# get the path/directory
folder_dir = 'C:/Users/User/image processing'

# iterate over files in
# that directory
images = Path(folder_dir).glob('*.png')
for image in images:
	print(image)


# In[4]:


#displaying png image name
# import the modules
import os
from os import listdir

# get the path or directory
folder_dir = "C:/Users/User/image processing"
for images in os.listdir(folder_dir):

# check if the image ends with png or jpg or jpeg
 if (images.endswith(".png")): 
# display
   print(images)


# In[5]:


#diaplaying the image of all
#import neccessory packages
import cv2
import os
import glob
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

img_dir="C:/Users/User/image processing"
data_path=os.path.join(img_dir,'*g')
files=glob.glob(data_path)
data=[]
for  f1 in files:
    img=cv2.imread(f1)
    data.append(img)
    plt.figure()
    plt.imshow(img)
    plt.axis("off")


# In[55]:


import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from skimage import io
from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color
import pandas as pd
plt.rcParams['figure.figsize']=(10,8)

def show_image(image, title='image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    
    
def plot_comparison(img_original,img_filtered,img_title_filtered):
    fig,(ax1,ax2)=plt.subplots(ncols=2, figsize=(10,8),sharex=True,sharey=True)
    ax1.imshow(img_original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax2.imshow(img_filtered, cmap=plt.cm.gray)
    ax1.set_title('img_title_filtered')
    ax1.axis('off')

image_with_logo = plt.imread('logo2.png')

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
mask[100:150, 105:600] = 1

# Apply inpainting to remove the logo
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo,mask,multichannel=True)

# Show the original and logo removed images
plot_comparison(image_with_logo, image_logo_removed, 'Image with logo removed')


# In[23]:


# Importing ImageDraw for
# using floodfill function
from PIL import Image, ImageDraw
plt.rcParams['figure.figsize']=(10,8)

# Opening the image and
# converting its type to RGBA
img = Image.open("v.jfif").convert('RGBA')

# Location of seed
seed = (0, 0)

# Pixel Value which would
# be used for replacement
rep_value = (0,0,0, 0)

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
mask[100:100, 100:50] = 1

# Calling the floodfill() function and
# passing it image, seed, value and
# thresh as arguments
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo,mask,multichannel=True)
ImageDraw.floodfill(img, seed, rep_value, thresh = 10)

img.show()


# In[24]:


#diaplaying the image of all
#import neccessory packages
import cv2
import os
import glob
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

img_dir="C:/Users/User/image processing"
data_path=os.path.join(img_dir,'*g')
files=glob.glob(data_path)
data=[]
for  f1 in files:
    img=Image.open(f1)
    new_image=img.resize
    data.append(img)
    plt.figure()
    plt.imshow(img)
    plt.axis("off")


# In[65]:


from PIL import Image
from PIL import ImageFilter
import os

def main():
# path of the folder containing the raw images
 inPath ="C:/Users/User/Desktop/n.jfif"

# path of the folder that will contain the modified image
outPath ="D:\\test"

for imPath in os.listdir(inPath):
# imagePath contains name of the image
 inputPath = os.path.join(inPath, imagePath)

# inputPath contains the full directory name
img = Image.open(inputPath)

fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
# fullOutPath contains the path of the output
# image that needs to be generated
img.rotate(90).save(fullOutPath)

print(fullOutPath)

# Driver Function
if __name__ == '__main__':
     main()


# In[ ]:





# In[ ]:




