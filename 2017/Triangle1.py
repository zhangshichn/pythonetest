#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#定義triangle函數,判斷是哪類三角形
def triangle(a,b,c):
    if a == b == c:
        print("這是等邊三角形")
    elif a == b or b == c:
        print("這是等腰三角形")
    elif a**2 == b**2 + c**2:
        print("這是直角三角形")
    else:
        print("這是一般三角形")



#輸入三角形3條邊的長度,如果輸入的是非數字或者小於0的數字,提示重新輸入
tri=[]
i=0
n=0
while i < 3:
    while True:
        try:
            n=float(input("請輸入三角形第%d條邊的長度:"%(i+1)))
            break
        except ValueError or tri[i]<=0:
            print("輸入的變長無效,請輸入大於0的數字")
    tri.append(n)
    i+=1




tri.sort(reverse=True)

print(tri)
a,b,c = tri[0], tri[1],tri[2]
#根據三角形定義,最長的邊如果大於兩條短邊之和,則無法組成三角形
if a > b + c:
    print("輸入的邊長無法組成三角形")
else:
    triangle(a,b,c) #調用函數,判斷三角形的類型