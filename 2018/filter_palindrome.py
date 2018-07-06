#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Filename: filter_palindrome.py




def palindrome(n):
    s=str(n)
    return s==s[::-1]

output = filter(palindrome,range(1,100))
print(list(output))



#Prime filter

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

    
