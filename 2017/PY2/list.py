#!/usr/bin/python
#coding=utf-8
#List

list1=['python','chemistry',2001,2015]
list2=[1,2,3,4,5]
list3=['a','b','c','d']

print "list1[0]: ",list1[0]
print "list2[1:5]: ", list2[1:]
print '\n'
#############################################

print "Value available at list1[2]: ", list1[2]
list1[2]=2014
print "New value available at list1[2]: ", list1[2];
print '\n';
####################################################

print list1;
del list1[3];
print "After remove list1[3]:", list1;
print '\n'
###################################################
print "Length of list1: ",len(list1);
print "Combine of list1 and list2: ", list1+list2;
print "Repeat 4 times: ", list1*4;
print "Element exist: ", 2015 in list1;
print '\n'
###################################################

print cmp(list1,list2), cmp(list1,list1);
print len(list2);
print max(list1);
print min(list1);
print '\n'

######################################################
