#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Filename:reduce_multiple.py

def prod(L):
    return reduce(lambda x,y:x*y,L)

print(prod([3,5,7,9]))

