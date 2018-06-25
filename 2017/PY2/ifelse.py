#!usr/bin/python
#coding=utf-8
num = 5
if num == 3:
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
else:
    print 'roadman'
    
print '\n'
########################
flag = False
name = 'python'
if ( name == 'python' ):
     flag= True
     print 'python'
     print flag
else:
     print flag
     print name
print '\n'
###################################
number = 9
if number >= 0 and number <= 10:
    print 'Hello'

number = 10
if number < 0 or number > 10:
    print " Less than 0 or more than 10"
else:
    print number

number = 8
if (number >=0 and number <= 5) or (number >=3 and number <= 13):
    print "unbelievable"
else:
    print number
