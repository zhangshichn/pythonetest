#/usr/bin/python3
# -*- coding=utf-8 -*-
#Filename: trim.py

def trim(s):
    if (len(s) == 0 or (s[0] != ' ' and  s[-1] != ' ')):
        return s
    else:
#        return trim(s[0] == ' ' and s[1:] or s[:-1])
        if s[0] == ' ':
            return trim(s[1:])
        else:
            return trim(s[:-1])
            
    
    
print(trim("   Hello "),'end')
print(trim(" hello world  "),'end')
print(trim(''),'end')
print(trim('  '),'end')

    
    
        
