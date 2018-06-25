#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#定義篩選規則
def _not_divisible(n):
    return lambda x:x%n>0

#定義生成素數的函數
def func(a):
    nlist=[]
    for i in range(2,a):
        nlist.append(i) #構造數列

    i=0
    rlist=[]    #構造接收數列

    #循環篩選數列,將數列中的素數逐一篩出 nlist[0]
    while i<a:
        nlist=list(filter(_not_divisible(nlist[0]),nlist))
        if nlist==[]:   #當數列爲空時,跳出循環
            break
        rlist.append(nlist[0])  #逐一接收篩出的素數
        i+=1
    return(rlist)

print(func(500))