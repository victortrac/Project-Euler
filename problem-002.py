#!/bin/python

x = 1
y = 2

def fib (x,y,max) :
  seq = [x,y]
  while (x and y) < max :
    seq.append(x+y)
    x = seq[len(seq)-2]
    y = seq[len(seq)-1]
  return seq

result = fib(1,2,4000000)

sum = 0

for x in result:
  if (x < 4000000) and (x % 2 == 0):
    print x
    sum += x

print sum
