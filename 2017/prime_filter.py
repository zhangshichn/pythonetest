#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n


def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for i in primes():
    if i<100:
        print(i)
    else:
        print("這是%d以內的素數" % i)
        break
