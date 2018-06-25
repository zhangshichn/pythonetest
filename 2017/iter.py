#!/usr/bin/python3
#coding=utf-8
'''
#迭代器
list=[1,2,3,4]
it=iter(list)
print(next(it))
print(next(it))




list=[1,2,3,4]
it=iter(list)
for x in it:
	print(x,end=' ')
	print(next(it))


'''


import sys

list=[1,2,3,4]
it=iter(list)

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()
