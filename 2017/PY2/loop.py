#!/usr/bin/python
#coding=utf-8
count = 0
while ( count < 9 ):
    print 'The count is :',count
    count += 1

print "Good Bye!"
print "\n"

##################################
i=1
while i < 10:
    i += 1
    if i%2>0:
        continue
    print i
print '\n'
i=1
while 1:
    print i
    i+=1
    if i>10:
        break
print '\n'

#####################################
var=1
while var == 1:
    num=raw_input("Enter a number： ")
    if num=='stop':
        break
    print "You entered: ", num

print "Good Bye!"
print '\n'

######################################


count=0
while count<5:
    print count, " is less than 5."
    count += 1
    if count==5:
        print count, " is 5."
        continue
else:
    count +=1
    print count, " is more than 5."
