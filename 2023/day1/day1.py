#!/usr/bin/env python3
with open('input', 'r') as f:
    input = f.read()

def getNumber(line):
    for char in line:
        if char.isnumeric():
            return char
    return '0'

def changeTextNumberToNumeric(line):
    textNumbers = {'one' : 'o1e', 'two' : 't2o', 'three' : 't3e', 'four': 'f4r', 'five' : 'f5e', 'six' : 's6x', 'seven' : 's7n', 'eight' : 'e8t', 'nine' : 'n9e' }
    for text, num in textNumbers.items():
        line = line.replace(text.lower(), num)
    return line

day1 = [ int(getNumber(line) + getNumber(line[::-1])) for line in input.strip().split('\n') ]
day2 = [ int(getNumber(changeTextNumberToNumeric(line)) + getNumber(changeTextNumberToNumeric(line)[::-1])) for line in input.strip().split('\n') ]

for line in input.strip().split('\n'):
    print(line)
    print(changeTextNumberToNumeric(line))

print("[*] Day 1: {}".format(sum(day1)))
print("[*] Day 2: {}".format(sum(day2)))

