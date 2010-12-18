#!/usr/bin/env python

a = 1
b = 2
c = 3

while a < 997:
    for b in range(a, 1000-c):
        c = 1000-b-a
        if (a**2 + b**2) == c**2:
            print a, b, c
            print "product a*b*c", a*b*c
    a += 1
