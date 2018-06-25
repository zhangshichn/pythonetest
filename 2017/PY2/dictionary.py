#!usr/bin/python
#coding=utf-8
#Dictionary
dict={'Name':'Zara','Age':7,'Class':'First'};
print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'],'\n';

####################################################
dict['Age']= 8;
dict['School']="DPS school";
print dict['Age'];
print dict['School'],'\n';

######################################################

print str(dict);
del dict['School'];
print str(dict),'\n';
dict.clear();
print str(dict),'\n';
del dict;
print str(dict),'\n';

########################################################
