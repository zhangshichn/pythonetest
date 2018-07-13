#!/usr/bin/python3
# -*-coding:utf-8-*-
# Filename:decorator_ExeTime.py

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        starttime=time.time()
        fn(*args,**kw)
        endtime=time.time()
        print('%s executed in %s ms' %(fn.__name__,endtime-starttime))
        return fn(*args,**kw)
    return wrapper

'''
@metric
def now():
    print('2018/08/11')

now()

'''

@metric
def fast(x,y):
    time.sleep(0.0112)
    return x+y

f=fast(11,22)
print(f)
