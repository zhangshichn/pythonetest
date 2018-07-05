#!/usr/bin/python3
# -*- coding=utf-8
# Filename: iteration.py

def findMinAndMax(L):
	if len(L) != 0:
		Min=L[0]
		Max=L[0]
		for i in L:
			if i < Min:
				Min = i
			elif i > Max:
				Max = i
	else:
		Min=None
		Max=None
	return (Min,Max)


print(findMinAndMax([7]))
print(findMinAndMax([]))
print(findMinAndMax([3,6,-1,10]))

