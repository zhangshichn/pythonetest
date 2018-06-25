#!/usr/bin/python
str=raw_input("Enter your input: ");
print "Received input is: ",str
####################################
print "\n";
#str1=input("Enter your input: ");
#print "Received input is: ",str1;
print "\n";
#####################################
fo=open("foo.txt","wb")
print "Name of the file: ",fo.name
print "Closed or not: ", fo.closed;
print "Opening mode: ", fo.mode;
print "Softspace flag: ", fo.softspace
fo.close();
print "\n";
print "Closed or not: ", fo.closed;
