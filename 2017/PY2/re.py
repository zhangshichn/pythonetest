#!/usr/bin/python
#coding=utf-8
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print "matchObj.group(): ", matchObj.group()
    print "matchObj.group(): ", matchObj.group(1)
    print "matchObj.group(): ", matchObj.group(2)
else:
    print "No match!!"



##########################################################

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group(): ",matchObj.group();
else:
    print "No match!";

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group(): ",matchObj.group();
else:
    print "No match!";
