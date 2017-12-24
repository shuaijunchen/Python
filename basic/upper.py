#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point:
	pass

class Rectangle:
	pass

def findUpperRight(rectangle):
	p = Point()
	p.x = rectangle.width+rectangle.cornor.x
	p.y = rectangle.height+rectangle.cornor.y
	return p

r = Rectangle()
r.width = 50.0
r.height = 70.00
r.cornor = Point()
r.cornor.x = 10
r.cornor.y = 5

up = findUpperRight(r)
print '('+str(up.x)+','+str(up.y)+')'