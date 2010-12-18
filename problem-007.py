#!/usr/bin/python

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

primes = [2,3,5,7]

n = 11

while (len(primes) != 10001):
    if (isprime(n)): primes.append(n)
    n += 2
    
print primes[-1]