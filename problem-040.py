#!/usr/bin/python

x=0
numbers = ""

while len(numbers) < 1000001:
    numbers = numbers + str(x)
    x += 1

output = 1
for x in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    print numbers[x]
    output = output * int(numbers[x])

print output
