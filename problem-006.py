#!/usr/bin/python

def sum_squares(x,y):
    sum = 0
    for i in range(x,y+1):
        sum += i*i
    return sum

def square_sum(x,y):
    sum = 0
    for i in range(x,y+1):
        sum += i
    return sum*sum

print square_sum(1,100) - sum_squares(1,100)
