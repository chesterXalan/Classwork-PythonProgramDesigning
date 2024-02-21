#!/usr/bin/env python
# coding: utf-8

# ### 四電二乙 3A712069 徐茂桓

# In[ ]:


import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


img = cv2.cvtColor(cv2.imread('20190718134521_1.jpg', -1), cv2.COLOR_BGR2RGB)

plt.figure(figsize = (15, 5))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)

RGB = ['r', 'g', 'b']
for i, color in enumerate(RGB):
    imgHist = cv2.calcHist(img, [i], None, [256], [0, 256])
    plt.plot(imgHist, RGB[i])

