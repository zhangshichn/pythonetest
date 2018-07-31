#/usr/bin/python3
# -*- coding: utf-8 -*-


'class_inheritance.py'

class Animal(object):
    def run(self):
        print('Animal is running')

    def stop(self):
        print('Animal is stopping')


class Dog(Animal):
    def run(self):
        print('Dog is running')


a = Animal()
a.run()

b = Dog()
b.run()
b.stop()


def print_twice(Animal):
    Animal.run()
    Animal.run()


print_twice(Animal())
print_twice(Dog())
