#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# @Author	ZHANG Shi
# @Date		2017/11/26
# @Version	1.0



def findMinAndMax(l):
	if l ==[]:
		return(None,None)
#	elif len(l) == 1:
#		return(l[0],l[0])
	i=0
	Max=l[0]
	Min=l[0]
	for i in l:
		if i  > Max:
			Max=i
		if i < Min:
			Min=i
	return(Min,Max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


