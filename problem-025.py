#!/usr/bin/env python

f = [1,1]

while len(str(f[-1])) < 1000:
    f.append(f[-1] + f[-2])

print len(f)
