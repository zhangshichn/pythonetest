#!/usr/bin/python3
# -*- coding:UTF-8 -*-

#階乘


def fact(n):
	amount=1
	if n == 1:
		return 1
	print('n=',n)
	return(n*fact(n-1))
print(fact(8))




#漢諾塔
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

n=int(input("請輸入漢諾塔層數:"))
move(n,'A','B','C')


#move(4, 'A', 'B', 'C')
