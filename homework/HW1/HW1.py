#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('四電二乙　3A712069　徐茂桓')
print('作業一\n')


# In[ ]:


n = 0
number1 = []
number2 = []
number3 = []

for i in range(10):
    for j in range(10):
        for k in range(10):
            n += 1
            number1.append(n)
            
        number2.append(number1)
        number1 = []
        
    number3.append(number2)
    number2 = []

print(number3)

