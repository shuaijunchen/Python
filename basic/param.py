#!/usr/bin/env python
# -*- coding: utf-8 -*-

def total(head, tail, step=1):
    temp = 0
    while head<=tail:
        temp = temp+head
        head = head+step
    return temp

print total(1,100)

print total(1,100,2)
