#!/usr/bin/env python

n = 100

def fact(x): return (1 if x==0 else x * fact(x-1))

fact_n = fact(n)

sum = 0
for i in str(fact_n):
    sum += int(i)

print sum
