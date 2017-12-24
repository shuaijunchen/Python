#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Line:
    def __init__(self, length=0.0):
        self.length = length

    def __str__(self):
        return str(self.length)

    def __mul__(self, other):
        return Rect(self.length, other.length)

    def __rmul__(self, other):
        return Line(self.length*other)

class Rect:
    def __init__(self, width=0.0, length=0.0):
        self.width=width
        self.length=length

    def __str__(self):
        return '('+str(self.length)+','+str(self.width)+')'

    def area(self):
        return self.width*self.length

aline = Line(5.87)
bline = 2.9*Line(8.34)
print 'aline = ',aline, 'bline = ',bline

rect = aline*bline
print rect
print rect.area()

