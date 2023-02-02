#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Python program to convert
# numpy array to image

# import required libraries
import numpy as np
from PIL import Image as im

# define a main function
def main():

	# create a numpy array from scratch
	# using arange function.
	# 1024x720 = 737280 is the amount
	# of pixels.
	# np.uint8 is a data type containing
	# numbers ranging from 0 to 255
	# and no non-negative integers
	array = np.arange(0, 737280, 1, np.uint8)
	
	# check type of array
	print(type(array))
	
	# our array will be of width
	# 737280 pixels That means it
	# will be a long dark line
	print(array.shape)
	
	# Reshape the array into a
	# familiar resoluition
	array = np.reshape(array, (1024, 720))
	
	# show the shape of the array
	print(array.shape)

	# show the array
	print(array)
	
	# creating image object of
	# above array
	data = im.fromarray(array)
	
	# saving the final output
	# as a PNG file
	data.save('gfg_dummy_pic.png')

# driver code
if __name__ == "__main__":
	
    # function call
    main()


# In[11]:


#automate your image processsing using python

from PIL import Image
import os


# In[12]:


os.getcwd()


# In[16]:


image1 = Image.open("72353House_in_snow.jpg")

image1


# In[17]:


image1.show()


# In[18]:


#chaning file type
image1.save("pic1.png")


# In[19]:


# lists all the files and folders in the current working directory
os.listdir()


# In[20]:


#seprate the name and extension
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn, "&", fext)


# In[21]:


#Looping over the image files
for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)


# In[22]:


# Creating new Directory using OS library
os.mkdir('NewExtnsn')
# Note: If you already have a directory with this name, you will get error.


# In[23]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save("NewExtnsn/{}.pdf".format(fn))


# In[24]:


#resizing
# Creating new multiple Directories using OS library
os.makedirs('resize//small')
os.makedirs('resize//tiny')
# Note: If you already have a directory with this name, you will get error.


# In[25]:


size_small = (600,600) # small images of 600 X 600 pixels
size_tiny = (200,200)  # tiny images of 200 X 200 pixels
for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_small)
        i.save("resize/small/{}_small{}".format(fn, fext))
        i.thumbnail(size_tiny)
        i.save("resize/tiny/{}_tiny{}".format(fn, fext))


# In[29]:


#convertin to black and white
image2 = Image.open("cyclists.jfif")
image2 = image2.convert(mode='L')
image2


# In[30]:


#insert a image
# Creating new Directory using OS library
os.mkdir('b&w')


# In[31]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.convert(mode = 'L')
        im.save("b&w/{}_bw.{}".format(fn, fext))
 


# In[33]:


#rotating the image
#rotating the image to 55 Degree angle
image3 = Image.open("index1.jfif")
image3.rotate(55).save("index2.jfif")
Image3 = Image.open("index3.jfif")


# In[34]:


Image3


# In[35]:


# Creating new Directory using OS library
os.mkdir('rotate')


# In[36]:


for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        im = i.rotate(90)
        im.save("rotate/{}_rot.{}".format(fn, fext))


# In[ ]:




