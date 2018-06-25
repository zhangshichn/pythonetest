#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def equation(a,b,c):
	r=b*b-4*a*c
	for i in (a,b,c):
		if not isinstance(i,(int,float)):
			raise TypeError('Type Error!')
	if a==0:
		print('一元一次方程組')
		return('x=%f'%(-c/b))
		
	elif r<0:
		return('方程無解')

	elif r==0:
		return('x=%f'%(b/2*a))
	
	else:
		x1=(-b+math.sqrt(r)/2*a)
		x2=(-b-math.sqrt(r)/2*a)
		return('此方程有兩個解,%f,%f'%(x1,x2))

a=int(input("請輸入a:"))
b=int(input("請輸入b:"))
c=int(input("請輸入c:"))

print(equation(a,b,c))

