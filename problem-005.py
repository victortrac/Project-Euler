#!/bin/python

def get_primes(x,y):
    primes = []
    for i in range(x,y+1):
        if isprime(i):
            primes.append(i)
    return primes
        
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

def multiply(list):
    list.sort()
    primes = get_primes(list[0],list[-1])
    num = 1
    for i in primes: num *= i
    found = False
    while (found == False):
#        print "Trying ", num
        for n in list[::-1]:
            remainder = num % n
            if remainder == 0:
                if (int(n) == int(list[0])): 
                    found = True
            else:
                print num, n, remainder
                num += +20
                break
    return num

print multiply(range(1,21))
