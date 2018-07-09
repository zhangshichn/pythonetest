#!/usr/bin/python
# -*-coding:utf-8-*-
#Filename: closure_counter.py

'''

def createCounter():
    def arrange():
        i=1
        while True:
            yield i
            i = i+1
    iter=arrange()

    def counter():
        return next(iter)
    return counter
'''


def createCounter():
    j=0
    def counter():
        nonlocal j
        j+=1
        return j
    return counter

counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA())

