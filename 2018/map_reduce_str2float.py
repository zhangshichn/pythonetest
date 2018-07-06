#!/usr/bin/python3
# -*-coding:utf-8-*-
# Filename:map_reduce_str2float.py

def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

def power(n,t):
    s=1
    while t>0:
       s=s*n
       t=t-1
    return s

def str2float(s):
    s=s.split('.')
#    print('s=',s)
    if len(s) == 0:
        return reduce(lambda x,y:x*10+y, map(char2num,s))
    elif len(s)>2:
        print('.多於1個,程序錯誤')
        return
    else:
        t=len(s[1])
        s1=s[0]+s[1]
        n=reduce(lambda x,y:x*10+y,map(char2num,s1))
#        print(n)
        m=float(n)/1000

        return m
#        n1=reduce(lambda x,y:x*10+y,map(char2num,s[0]))
#        print('n1=',n1)
#        n2=reduce(lambda x,y:x*10+y,map(char2num,s[1]))
#        print('n2=',n2)
#        n3=n2/power(10,t)
#        return n1+n3

print(str2float('123.456'))
