#!/usr/bin/python3
# -*- coding:utf-8 -*-

#输出数字的绝对值


while True:
	a=int(input('请输入一个数字: '))

	if a >=0:
		print('a的绝对值是：',a)
	elif a<0:
		print('a的绝对值是：',-a)
	else:
		print('输入的不是数字')
	
	print('Enter继续，Q退出')
	
	var=input()
	if var== 'Q':
		break
