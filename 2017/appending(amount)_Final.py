#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#定義append函數,根據輸入的奇偶數,輸出最終的alist
def append(alist,i):
    sum = 0
    if i == 0:
        print("輸入的是偶數")
        for a in alist:
            if a%2 == 0:
                sum += a
    else:
        print("輸入的是奇數")
        for a in alist:
            if a%2 == 1:
                sum += a
    alist.append(sum)
    print("最終的alist是:",alist)


alist=[12,34,51,66,31,7,87,58,92]

#判斷輸入的是否爲整數
while True:
    try:
        t = int(input("請輸入一個整數:"))
        break
    except ValueError:
        print("輸入的不是整數,請重新輸入!")

i = t%2  #判斷輸入的整數是奇數還是偶數

append(alist,i)

'''
程序運行結果:

請輸入一個整數:8
輸入的是偶數
最終的alist是: [12, 34, 51, 66, 31, 7, 87, 58, 92, 262]
'''