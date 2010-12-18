#!/usr/bin/env python

def collatz(n):
    if n != 1:
        if (n%2) == 0:
            n = n/2
            holder.append(n)
            collatz(n)
        else:
            n = 3*n+1
            holder.append(n)
            collatz(n)

numbers = {}
for n in range(1,1000000):
    holder = [n]
    collatz(n)
    numbers[n] = len(holder)

maxNum = 0
for k,v in numbers.iteritems():
    if v > maxNum:
        maxNum = v
        print "Number: %d - Chain Length %d" % (k,v)
