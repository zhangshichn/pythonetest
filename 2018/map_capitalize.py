#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename: map_capitalize.py

def normalize(name):
#    return str.capitalize(name)
#    return name.title()
    n=name[0].upper()
    n=n+name[1:].lower()
    return n

L1=['adam','LISA','barT']
L2= list(map(normalize, L1))

print(L2)
