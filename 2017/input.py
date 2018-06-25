#!/usr/bin/python3
#coding=utf-8

#input("\n\n按下Enter键后退出")  #等待用户输入

str = input('请输入字符串')
if len(str) <5:
	print(str,'is a short string')
elif len(str)>5:
	print(str,'is a long string')
else:
	print(str,'is 5 characters')
