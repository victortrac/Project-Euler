#!/usr/bin/python

def check_palin(z):
    f = list(str(z))
    r = f[::-1]
    return (f == r)

palins = []

for x in range(1,1000) :
    for y in range(1,1000) :
        if (check_palin(x*y)): palins.append(x*y)
            
palins.sort()
print palins[-1]