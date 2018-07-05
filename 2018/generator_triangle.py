#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Filename:generator_triangle.py

def tri():
    L=[1]
    while True:
        yield L
        L=[(L+[0])[i]+([0]+L)[i] for i in range(len(L)+1)]



t=tri()
for i in range(10):
    print(next(t))
