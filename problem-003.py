#!/bin/python

def prime_factor(num, primes = []) :
  divider = 2
  while (num >= 3) :
    if ((num % divider) == 0) :
      num = num / divider
      primes.append(divider)
      prime_factor(num, primes)
      break
    else : divider += 1
  return primes

result = prime_factor(600851475143)
print result
