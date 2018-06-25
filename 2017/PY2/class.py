#!/usr/bin/python
#coding=utf-8
#Class

class Employee:
    'information'
    empcount=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount +=1

    def displayCount(self):
        print " Total Employee %d" % Employee.empcount

    def displayEmployee(self):
        print "Name :", self.name, ",Salary: ", self.salary


emp1 = Employee("Zara", 2000);

emp2 = Employee("Manni", 5000);

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empcount
emp1.salary = 3000;
print emp1.salary
del emp1.salary
setattr(emp1,'salary',1000)
hasattr(emp1,'salary')

print Employee.__doc__
print Employee.__dict__
print Employee.__module__
print Employee.__bases__
print Employee.__init__


################################################################
class Parent:
    def myMethod(self):
        print 'Parent'

class Child(Parent):
    def ChildMethod(self):
        print 'child'

c = Child()
c.ChildMethod()
c.myMethod();
print issubclass(Child,Parent);
print isinstance(c,Parent);

class Child(Parent):
    def myMethod(self):
        print 'Children';
b=Child();
b.myMethod();
