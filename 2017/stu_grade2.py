#!/usr/bin/python3
# -*- coding: UTF-8 -*-



# @Author:	ZHANG Shi
# @Date:	2017/12/9
# @Version:	1.0


s = [[201,77],[202,82],[203,93],[204,87],[205,88],[206,91]] #初始化成績列表
i = 0   #定義循環查找次數變量
num = 0 #定義學號變量
signal = False  #定義標識符


#錄入學號
while True:
    try:
        num = int(input("請輸入學號:"))
        break
    except ValueError:
        print("輸入的不是數字,請重新輸入")

#在成績列表中查找學號,並輸出成績
while i < 6:
    if s[i][0] == num:
        print("學號爲%d的學生成績爲: %d"%(num,s[i][1]))
        signal = True
        break
    else:
        i+=1

#如果不存在,則輸出提示
if signal == False:
    print("學號%d沒有在列表中"%num)