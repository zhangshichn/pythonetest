#!/usr/bin/python3
# -*-coding:utf-8-*-
#Filename: decorator.py

import functools

'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s()' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018/08/10')

now()

'''

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018/08/11')

now()
print(now.__name__)

