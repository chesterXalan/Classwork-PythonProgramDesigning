#!/usr/bin/env python
# coding: utf-8

# # 四電二乙 3A712069 徐茂桓

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


img = np.zeros((256, 256, 3), dtype = 'uint8')
row, column = img.shape[:2] #取列與行數量
print('圖像大小：{}x{}'.format(row, column))

for r in range(row):
    img[r, :, 0] = r
    
plt.imshow(img)
plt.show()

cv2.imwrite('HW5 Image.bmp', img[:, :, ::-1])

