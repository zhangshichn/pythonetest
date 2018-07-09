#!/usr/bin/python3
# -*- coding=utf-8 -*-
#Filename: sorted_grade.py


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]

def by_grade(t):
    return t[1]

print(sorted(L,key=by_name))


print(sorted(L,key=by_grade,reverse=True))
