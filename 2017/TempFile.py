#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018/01/21')

f=now

f()

print(now.__name__,f.__name__)

