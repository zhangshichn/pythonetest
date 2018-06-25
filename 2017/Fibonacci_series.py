#!/usr/bin/python3
#coding=utf-8

a, b = 0, 1
while b>-1:
	print(b,end=',')
	a, b = b, a+b
print('...')
#Fibonacci数列
#前两个数字的和等于第三个数字
