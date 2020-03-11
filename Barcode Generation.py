#!/usr/bin/env python
# coding: utf-8

# ![MoaiLogo.jpg](attachment:MoaiLogo.jpg)

# If you are finding the best AI solution and projects using python then connect with team moai at www.moai.blog and see how worlds change in every second with AI. if you are started with us then got best Computer Vision and Deep Learning contents which easier than you think. We created the moai website to show you what I believe is the best possible way to get your start. Follow me and I promise you’ll find your way in Computer Vision, Deep Learning field.

# ### If you are thinking about why moai? Then come and feel it.
# 
# ## Like, share and subscribe to our YouTube channel "Moai Vision".
# website: www.moai.blog
# 
# #### Follow us on
# 
# Github: https://github.com/moai-vision
# 
# Kaggle: https://www.kaggle.com/moaivision
# 
# Facebook: https://www.facebook.com/moaivision
# 
# Instagram: https://www.instagram.com/moai_vision
# 
# 
# ### "moai of today is the future of tomorrow." -Team Moai

# # Project 1: Create 10000+ Barcodes per minute using python

# # Required Package

# ### Url: https://pypi.org/project/python-barcode/
# 
# >pip install PyQRCode

# # Import Modules

# In[1]:


import barcode
from barcode.writer import ImageWriter
from tqdm.auto import tqdm
from random import randint


# # Random Digit Generator

# In[2]:


def digit_generator(n):
    start=10**(n-1)
    end=(10**n)-1
    return randint(start,end)


# In[3]:


digit_generator(10)#Test digit generator


# # Bar Code Generator

# In[4]:


def bargenerator(data,image):
    Type=barcode.get_barcode_class('code128')
    code=Type(str(data),writer=ImageWriter())
    code.save("barcodes/"+image)


# In[6]:


bargenerator(123456789,"test") #Test bargenerator


# # Create List For Barcode Creation

# In[7]:


number_list=[]

for i in tqdm(range(10000)):
    value=digit_generator(16)
    number_list.append(value)


# In[8]:


number_list[-10:] #print first 10 values


# In[9]:


len(number_list) #length of values


# # Barcode Generation From Number List

# In[ ]:


counter=0
for code in tqdm(number_list):
    text='bar'+str(counter)
    bargenerator(code,text)
    counter+=1

