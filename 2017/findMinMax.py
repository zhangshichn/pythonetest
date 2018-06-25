#!/usr/bin/python3
# -*- coding: UTF-8 -*-


def findMinMax(list):
    min=list[0]
    max=list[0]
    for i in list:
        if i>max:
            max=i
        if i<min:
            min=i
    return(min,max)

a=[43,234,53,35,53,2,3,353,2,32,43]
print(findMinMax(a))