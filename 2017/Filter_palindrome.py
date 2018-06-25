#!/usr/bin/python3
# -*- coding: UTF-8 -*-



def n_list():
    n=1
    while True:
        n+=1
        yield n

def is_palindrome(n):
    return n == int(str(n)[::-1])

def func():
    nlist=n_list()
    while True:
        nlist=filter(is_palindrome,nlist)
        n=next(nlist)
        yield n

for i in func():
    if i < 10000:
        print(i)
    else:
        break
