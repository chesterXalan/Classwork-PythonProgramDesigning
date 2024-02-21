#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#四電二乙_3A712069_徐茂桓_HW2-1

import random

print("《終極密碼》\n")

n ,r1, r2 = 1, 1, 100
rand = random.randint(1, 100)
#print(rand)

while 1:
    print("第", n, "次猜測")
    print("猜測範圍：", r1, "~", r2)
    guess = int(input("輸入猜測： "))    
    
    if guess <= r2 and guess >= r1:
        if guess < rand:
            print("太小了！\n")
            r1 = guess
        elif guess > rand:
            print("太大了！\n")
            r2 = guess
        else:
            break
    else:
        print("※超出範圍※\n")
        
    n += 1
    
print("猜對了！")

