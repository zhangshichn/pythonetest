#!/usr/bin/python
#coding=utf-8
#For
for letter in 'Python':
    print 'Current Letter: ', letter
fruits=['banana','apple','orange']
for fruit in fruits:
    print 'Current fruit: ', fruit

print 'Good Bye!'
print '\n'
###########################################

print len(fruits)
print fruits[1]
print '\n'

############################################

for i in range(10,20):
    for j in range(2,i):
        if i%j==0:
            num=i/j
            print '%d Equal %d * %d' %(i,j,num)
            break
    else:
        print i,' is a prime number'
