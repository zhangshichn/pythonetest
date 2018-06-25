#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#Filename: module_sys


' a test module ' 

__author__ = "ZHANG Shi"


import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world!")
    elif len(args) == 2:
        print("hello %s!" %args[1])
    else:
        print("Too many arguments!")

if __name__ == '__main__':
    test()
