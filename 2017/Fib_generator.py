#!/usr/bin/python3
# -*- coding: UTF-8 -*-


def fib(n):
    a=1
    b=2
    i=0
    while i<n:
        i+=1
        yield b
        a,b=b,a+b


f=fib(6)
for i in f:
    print(i)
