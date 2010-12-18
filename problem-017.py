#!/usr/bin/bash
import sys
import pdb

words = {1: "one",
         2: "two",
         3: "three",
         4: "four",
         5: "five",
         6: "six",
         7: "seven",
         8: "eight",
         9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         14: "fourteen",
         15: "fifteen",
         16: "sixteen",
         17: "seventeen",
         18: "eighteen",
         19: "nineteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety",
         100: "hundred",
         1000: "thousand"}

def wordize(x):
    phrase = ""
    thousands = x / 1000
    x = x % 1000
    hundreds = x / 100
    x = x % 100
    tens = x / 10
    x = x % 10
    ones = x
    if thousands:
        phrase = "one thousand"
        return phrase
    if hundreds:
        phrase = words[hundreds] + " hundred"
    if tens:
        if hundreds:
            phrase = phrase + " and" 
        if (ones == 0 and tens != 1):
            phrase = phrase + " " + words[tens*10]
        elif tens == 1:
            phrase = phrase + " " + words[tens*10+ones]
        else:
            phrase = phrase + " " + words[tens*10] + "-"
    if (ones and tens != 1):
        if hundreds and (tens == 0):
            phrase = phrase + " and "
        phrase = phrase + words[ones]

    return phrase.strip()

def count(string):
    return len(string.replace(" ", "").replace("-", ""))

#phrase = wordize(int(sys.argv[1]))

letters = 0
for x in range(1,1001):
    phrase = wordize(x)
    print phrase, count(phrase)
    letters += count(phrase)

print letters
