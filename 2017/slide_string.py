#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Author:	ZHANG Shi
# @Date:	2017/11/25
# @Version:	1.0


#輸入一組字符串,輸入時去除收尾的空格


def slide(s):
	r=0
	i=0
	f=0
	e=-1

	for r in s:
		i+=1
	print('字符串長度爲:<%d>'%(i))
	print('輸入的字符串是:<%s> '%(s))

#打印字符串內容和長度




#找到第一個不爲空的字符位置
	for r in s:
		if s[f] == ' ':
			f+=1
		else:
			break
	print('前端空格至第<%d>字符'%(f))
	print('第一個非空格字符是:<%s>'%(s[f]))



#找到最後一個非空格字符位置
	for r in s:
		if s[e] == ' ':
			e-=1
		else:
			break

	if e == -1:
		print('後端沒有空格')
		print('最後一個非空格字符是:<%s>'%(s[e]))
		print('去除尾端的空格後,字符串是:<%s>,字符串長度爲:<%d>'%(s[f:],i-f))
	
	else:
	
		print('後端空格在第<%d>字符處'%(i+e+2))
		print('最後一個非空格字符是:<%s>'%(s[e]))
		print('去除尾端的空格後,字符串是:<%s>,字符串長度爲:<%d>'%(s[f:e+1],(i-f+e+1)))



strings = input('請輸入字符串:')
slide(strings)

