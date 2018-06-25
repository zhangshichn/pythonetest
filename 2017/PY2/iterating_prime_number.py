#!/usr/bin/python
#coding=utf-8
#iterating
#Prime number between 2 and 100
i=2
while (i<100):
    j=2
    while(j<=i/j):
        if not (i%j):break
        j+=1
    else:print i, "是素数"
    i+=1
print "Good Bye!"
print '\n'
#####################################

for i in range(2,100):
    j=2
    while (j<=i/j):
        if i%j==0:
            break
        else:
            j+=1
    else:
        print i, "是素数"
print "Good Bye!"
    
