#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

def print_score(std):
	print '%s %s' % (std.name, std.score)

bart = Student('Bart Zhang', 78)
# print bart.name
# print bart.score
print_score(bart)

