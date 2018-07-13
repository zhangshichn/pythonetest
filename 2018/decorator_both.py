#/usr/bin/python3
# -*-coding:utf-8-*-
# Filename: decorate_both.py


from inspect import isfunction
from functools import wraps

def log(arg):
    if isfunction(arg):
        @wraps(arg)
        def wrapper(*args, **kwargs):
            print('裝飾器沒有傳入文字')
            arg(*args, **kwargs)

        return wrapper

    else:
        def dec(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                print('装饰器接收的参数是 %s' % arg)
                fn(*args, **kwargs)

            return wrapper

        return dec

@log
def old():
    print('old')

old()



@log('executor')
def new():
    print('new')

new()




