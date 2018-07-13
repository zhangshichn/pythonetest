#!/usr/bin/python3
#File name: print.py

# --coding:UTF-8--

'''
print("hello world!")



def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018/07/10')

now()
'''



def log(fn):
    def metric():
        print('%s executed in %s ms' %(fn.__name__,10.24))
        return fn
    return metric

@log
def fast(x,y):
    time.sleep(0.0012)
    return x+y

f=fast(11,22)
