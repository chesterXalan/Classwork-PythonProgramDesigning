#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#四電二乙_3A712069_徐茂桓_HW2-2

import random

print("《5/39樂透》\n")

data, check, same = [], 0, {}

for i in range(1, 40):
    data.append(i)
lott = random.sample(data, 5)
lott.sort()
#print(lott)

while check == 0:
    guess = input("請輸入5筆不重複的整數，並以空白鍵區隔，範圍為1 ~ 39：")
    guess = guess.split()
    for i in range(len(guess)):
        guess[i] = int(guess[i])
          
    if len(guess) != 5:
        print("資料筆數錯誤，必須是5筆，請重新輸入\n")
    else:      
        if len(set(guess)) != 5:
            print("有重複的數字，請重新輸入\n")
        else:
            for i in range(5):
                if guess[i] > 39 or guess[i] < 1:
                    print("輸入的數超出範圍，請重新輸入\n")                  
                    break
                else:
                    if i == 4:
                        guess.sort()
                        check = 1

same = set(lott) & set(guess)
same = list(same)
same.sort()
                        
print("輸入號碼：", end = "")
for i in guess:
    print(i, end = "\t")
print(end = "\n")

print("開獎號碼：", end = "")
for i in lott:
    print(i, end = "\t")
print(end = "\n")

if len(same) != 0:
    print("中了", len(same), "個號碼：", end = "")
    for i in same:
        print(i, end = "　")
else:
    print("可惜，未中獎！")

