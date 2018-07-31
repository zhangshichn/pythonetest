#/usr/bin/python3
# -*- coding: utf-8 -*-

'class_StudentGender'


class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

bart = Student('bart','male')


print(bart.get_gender())

bart.set_gender('female')
print(bart.get_gender())
