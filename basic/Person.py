#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name=None, age=1, sex='men'):
        self.name = name
        self.age = age
        self.sex = sex
    
    def displayInfo(self):
        print "name : %-20s" % self.name
        print "age : %-20d" % self.age
        print "sex: %-20s" % self.sex
