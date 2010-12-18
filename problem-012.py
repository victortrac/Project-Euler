#!/usr/bin/env python

def triangle(n):
    i = [1]
    for x in range(2,n+1):
        i.append(x + i[len(i)-1])
    return i[-1]

def factor(n):
    i = [1,n]
    for x in range(2,n/2):
        if (n%x == 0) and x not in i:
            i.append(x)
            i.append(n/x)
    i.sort()
    return i

n = 1
while True:
    tri = triangle(n)
    if len(factor(tri)) < 500:
        n += 1
    else:
        print tri
        break
