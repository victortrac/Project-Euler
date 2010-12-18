#!/usr/bin/python
import pdb
import math

def binom(x,y):
    n = x+y
    k = max(x,y)
    answer = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    return answer

print binom(20,20)
