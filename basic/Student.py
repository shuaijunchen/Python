#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(Person):
    def __init__(self, name=None, age=1,sex="men", grade=0):
        Person.__init__(self, name, age, sex)
        self.grade = grade

    def dsiplayInfo(self):
        Person.displayInfo(self)
        print "grade : %-20d" % self.grade
