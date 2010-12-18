#!/usr/bin/env python

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**.5)+1, 2) :
        if (n % i) == 0:
            return False
    return True

primes = [2]

for i in range(1,2000000,2):
    if isprime(i):
        primes.append(i)

sum = 0

for j in primes:
    sum += j

print sum
