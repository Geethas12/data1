#!/usr/bin/env python
# coding: utf-8

# In[8]:


#image sharpen
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

# load the image
my_image=Image.open('d.jpg')

#use sharpen function
sharp = my_image.filter(ImageFilter.SHARPEN)
#save the image
sharp.save('D:/image_sharpen.jpg')
sharp.show()
plt.imshow(sharp)
plt.show()


# In[10]:


#Image flip
import matplotlib.pyplot as plt

#load the image
img=Image.open('d.jpg')
plt.imshow(img)
plt.show()

#use the flip funnction
flip = img.transpose(Image.FLIP_LEFT_RIGHT)

#save the image
flip.save('D:/image_flip.jpg')
plt.imshow(flip)
plt.show()


# In[ ]:





# In[ ]:




