#!/usr/bin/python3
# -*- coding: UTF-8 -*-


def Triangle():
    t=[1]
    while True:
        yield t
        t=[t[x]+t[x+1] for x in range(len(t)-1)]
        t.insert(0,1)
        t.append(1)

n=0
for t in Triangle():
    print(t)
    n=n+1
    if n == 10:
        break
