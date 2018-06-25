#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Filename: def_function.py


from math import sqrt

def quadratic(a,b,c):
    if b*b < 4*a*c:
        print("沒有實數解!")
        return

    elif (b*b == 4*a*c):
        x = -b/2*a
        print("有實數解: ")
        print(x)
        return

    else:
        x1 = (-b+sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-sqrt(b*b-4*a*c))/(2*a)
        print("有兩個實數解: ")
        print(x1,x2)
        return


if __name__ == "__main__":
    a = input("input a: ")
    b = input("input b: ")
    c = input("input c: ")
    quadratic(a,b,c)
    

