#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

# @Author:	Z.S
# @Date:	2017/11/25
# @Version:	1.0

import math	#導入math函數



#自定義方程式函數equa
def equa(a,b,c):
	x1=0
	x2=0


	if (a==0):	#a=0時,爲一元一次方程
		print("a不能爲0,不是一元二次方程")

	elif (b*b<4*a*c):	#b平方小於4ac,方程無實數解
		print("該方程無實數解")

	elif (b*b==4*a*c):	#b平方等於4ac,方程有一個實數解
		x1=-b/(2*a)
		print("該方程有一個實數解: x=%f"%(x1))

	else:			#b平方大於4ac,方程有兩個實數解
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		print("該方程有兩個實數的解: x1=%f, x2=%f"%(x1,x2)) 	# 使用math.sqrt函數求平方跟
		


#輸入a,b,c
a=float(input("請輸入a:"))
b=float(input("請輸入b:"))
c=float(input("請輸入c:"))

#使用函數equa求解
equa(a,b,c)

