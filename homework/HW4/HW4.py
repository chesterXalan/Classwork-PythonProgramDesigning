#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#四電二乙 3A712069 徐茂桓


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #微軟正黑體

E = R = C = 10
x, y1, y2 = [], [], []

for t in range(101): #t = [0: 0.01: 1.0]
    VChg = E * (1 - np.exp(-(t * 0.01) / (R * C * 0.001)))
    VRel = E * np.exp(-(t * 0.01) / (R * C * 0.001))
    
    x.append(t * 0.01)
    y1.append(VChg)    
    y2.append(VRel)

plt.plot(x, y1, 'r', label = '充電', linewidth = '2.5')
plt.plot(x, y2, 'g', label = '放電', linewidth = '2.5')
plt.legend(fontsize = '12', loc = 'center right')

plt.title('電容充放電曲線', fontsize = '16')
plt.xlabel('t (S)', fontsize = '12')
plt.ylabel('Vc(t) (V)', fontsize = '12', rotation = '0')

plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlim(0, 1.03)
plt.ylim(0, 10.5)

ax = plt.gca()
ax.xaxis.set_label_coords(1.05, -0.03)
ax.yaxis.set_label_coords(-0.07, 1.01)
plt.show()

