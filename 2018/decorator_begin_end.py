#/usr/bin/python3
# -*-coding:utf-8-*-
# Filename:decorator_begin_end.py

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call")
        func(*args,**kw)
        print("end call")
    return wrapper


@decorator
def now():
    print("here is the function")


now()
