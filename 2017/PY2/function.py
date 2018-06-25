#!/usr/bin/python
#coding=utf-8
#function
def printme(str):
    "打印"
    print str
    return
##########################
printme("use printme");
printme("again");
print '\n';

############################
def changeme(mylist):
    "modify list"
    mylist.append([1,2,3,4]);
    print "function values:", mylist
    return;
##############################
##use changeme function
mylist=[10,20,30];
changeme(mylist);
print "Function value again: ", mylist
#######################################

mylist1=[1,1,1];
changeme(mylist1);
print mylist1;
