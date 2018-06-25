#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def sorted_name(t):
    return t[0]

def sorted_grade(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2=sorted(L,key=sorted_name)
print(L2)

L3=sorted(L,key=sorted_grade,reverse=True)
print(L3)
