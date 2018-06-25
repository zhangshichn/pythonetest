#!/usr/bin/python3
# -*- coding: UTF-8 -*-




def is_palindrome(n):
    return n == int(str(n)[::-1])

output=list(filter(is_palindrome,range(1,100)))

print(output)
