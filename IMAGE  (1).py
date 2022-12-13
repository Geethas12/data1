#!/usr/bin/env python
# coding: utf-8

# In[46]:


from PIL import Image
im = Image.open('ing.png')
im.convert ('RGB').save('ing.jpg')
print('image converted sucess')


# In[45]:


im = Image.open('ing.png')
print(image.mode)


# In[33]:


doggo=imread('ing.png')
imshow(doggo);
import matplotlib.pyplot as plt
fig, ax=plt.subplots(1, 3, figsize=(12,4), sharey =True)
ax[0].imshow(doggo[:,:,0], cmap= "Reds")
ax[0].set_title('Red')
ax[1].imshow(doggo[:,:,1], cmap= "Greens")
ax[1].set_title('Green')
ax[2].imshow(doggo[:,:,2], cmap= "Blues")
ax[2].set_title('Blue');


# In[36]:


from PIL import Image, ImageDraw
im=Image.open('ing.png')
draw=ImageDraw.Draw(im)
draw.ellipse((125,125,200,250),fill(255,255,255,120))
del draw
im.show()


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
img = np.array(Image.open('ing.png'))
img_R, img_G, img_B = img.copy(), img.copy(), img.copy()
img_R[:, :, (1, 2)] = 0
img_G[:, :, (0, 2)] = 0
img_B[:, :, (0, 1)] = 0
img_rgb = np.concatenate((img_R,img_G,img_B), axis=1)
plt.figure(figsize=(15, 15))
plt.imshow(img_rgb)


# In[27]:


#slicing

fig, ax=plt.subplots(1,3,figsize=(6,4), sharey = True)
ax[0].imshow(doggo[:, 0:130])
ax[0].set_title('First split')

ax[1].imshow(doggo[:, 130:260])
ax[1].set_title('First split')

ax[2].imshow(doggo[:, 260:390])
ax[2].set_title('First split');


# In[26]:


#blending
from PIL import Image
img1=Image.open('ing.png')
img2=Image.open('img2.png')
alphablend1=Image.blend(img1,img2,alpha=.4)
alphablend1=Image.blend(img1,img2,alpha=.2)
alphablend1.show()
alphablend2.show()


# In[31]:


#histogram
im=Image.open('ing.png')
pl=im.histogram()
plt.bar(range(256),pl[:256], color='r', alpha=0.5)
plt.bar(range(256),pl[256:2*256], color='g', alpha=0.4)
plt.bar(range(256),pl[2*256:], color='b', alpha=0.3)
plt.show()


# In[32]:


ch_r,ch_g,ch_b=im.split()
plt.figure(figsize=(18,6))
plt.subplot(1,3,1); plt.imshow(ch_r, cmap=plt.cm.Reds);plt.axis('off')
plt.subplot(1,3,2); plt.imshow(ch_g, cmap=plt.cm.Greens);plt.axis('off')
plt.subplot(1,3,3); plt.imshow(ch_b, cmap=plt.cm.Blues);plt.axis('off')     
plt.tight_layout()
plt.show()


# In[60]:


from PIL import Image,ImageDraw,ImageFont
img =Image.open('ing.png')
d1=ImageDraw.Draw(im)
myFont =ImageFont.truetype('arial.ttf',40)
d1.text((500,500),"Sample text", font=myFont, fill=(25,8,0))
img.show()


# In[43]:


#croped image
cropped = im.crop((1,2,300,300))

cropped.show()


# In[47]:


converting 
from skimage.io import imshow, imread
from PIL import Image
doggo=imread('ing.png')
imshow(doggo);
import matplotlib.pyplot as plt
fig, ax=plt.subplots(1, 3, figsize=(12,4), sharey =True)
ax[0].imshow(doggo[:,:,0], cmap= "Reds")
ax[0].set_title('Red')
ax[1].imshow(doggo[:,:,1], cmap= "Greens")
ax[1].set_title('Green')
ax[2].imshow(doggo[:,:,2], cmap= "Blues")
ax[2].set_title('Blue');


# In[54]:


import PIL

#negative transformation function
def neg_trans(img):

  #get width and height of image
  width,height=img.size

  #traverse through pixels
  for x in range(width):
    for y in range(height):

      pixel_color=img.getpixel((x,y))

      #if image is RGB, subtract individual RGB values
      if type(pixel_color) == tuple: 

        #s=(L-1)-r
        red_pixel=256-1-pixel_color[0]
        green_pixel=256-1-pixel_color[1]
        blue_pixel=256-1-pixel_color[2]

        #replace the pixel 
        img.putpixel((x,y),(red_pixel,green_pixel,blue_pixel))
      
      #if image is greyscale, subtract pixel intensity
      else:

        #s=(L-1)-r
        pixel_color=256-1-pixel_color 

        #replace the pixel
        img.putpixel((x,y),pixel_color)
  return img


# In[57]:


#importing required libraries
import numpy as np
from pylab import imshow, show


# In[58]:


#text
ffrom PIL import Image, ImagreDraw,
  


# In[ ]:




