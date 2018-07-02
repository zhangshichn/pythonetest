#/usr/bin/python3
# -*- coding=utf-8 -*-
#Filename: tower_of_hanoi.py


def move(n,a,b,c):
    if n == 1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')
