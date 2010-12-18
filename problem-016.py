#!/usr/bin/env python
import math

number = int(math.pow(2,1000))

print number

sum = 0
for i in str(number):
    sum += int(i)

print sum
