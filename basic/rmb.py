#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RMB:
    def __init__(self, sum=0.0):
        self.sum = sum

    def __str__(self):
        return str(self.sum)

    def __add__(self, other):
        return RMB(self.sum+other.sum)

    def __sub__(self, other):
        return RMB(self.sum-other.sum)

a = RMB(20000)
b = RMB(234.987)
print a+b
print a-b

print a.__add__(b), a+b
print a.__sub__(b), a-b
