#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(self):
        print (str(self.hours)+":"+\
                str(self.minutes)+":"+\
                str(self.seconds))

#now = Time(10, 20, 30)
#now = Time(10)
now = Time(seconds = 30, hours = 10)
now.printTime()
