#!/usr/bin/python
#coding=utf-8
#Time and Date
import time;

ticks=time.time()
print "Number of ticks sine 12:00am, January 1, 1970:", ticks
print "\n";
###############################
localtime=time.localtime(time.time());
print "Local current time: ", localtime;
print "\n";
################################
localtime=time.asctime(time.localtime(time.time()));
print "Local Current Time: ", localtime;
print "\n";
##################################


import calendar;
cal=calendar.month(2008,1)
print "Here is the calendar: "
print cal;
print '\n';
