#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#四電二乙 3A712069 徐茂桓


# In[ ]:


import time

startList = time.time()
for x in range(1000):
    lst, lstSum = [], 0
    for i in range(1, 101):
        lst.append(i)
    for i in range(100):
        lstSum += lst[i] ** 4
endList = time.time()

#print(lst)
print("運算結果：", lstSum)
print("總執行時間：", endList - startList)


# In[ ]:


import numpy

startNumpy = time.time()
for i in range(1000):
    arr = numpy.arange(1, 101)
    arrSum = numpy.sum(arr ** 4)
endNumpy = time.time()

#print(arr)
print("運算結果：", arrSum)
print("總執行時間：", endNumpy - startNumpy)

