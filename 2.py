#! /usr/bin/env python3

# Advent of Code 2023 Day 2

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('2.in').read().strip()
lines = [x for x in data.split('\n')]


p1 = 0
ID = 0
for line in lines:
    valid = True
    ID += 1
    sets = line.split(';')
    for set in sets:
        words = set.replace(',','').split(' ')
        for i in range(1, len(words)):
            if words[i] == 'red':
                if int(words[i-1]) > 12:
                    valid = False

            if words[i] == 'green':
                if int(words[i-1]) > 13:
                    valid = False

            if words[i] == 'blue':
                if int(words[i-1]) > 14:
                    valid = False                
    print(valid)
    if valid:
        p1 += ID


print('p1 is', p1)

p2 = 0
for line in lines:
    gmin = 0
    bmin = 0
    rmin = 0

    sets = line.split(';')

    for set in sets:
        words = set.split(' ')

        for i in range(1, len(words)):

            if words[i] == 'red' or words[i] == 'red,':
                if int(words[i-1]) > rmin:
                    rmin = int(words[i-1])
            
            if words[i] == 'green' or words[i] == 'green,':
                if int(words[i-1]) > gmin:
                    gmin = int(words[i-1])

            if words[i] == 'blue' or words[i] == 'blue,':
                if int(words[i-1]) > bmin:
                    bmin = int(words[i-1])              
    p2 += gmin * rmin * bmin

print('p2 is', p2)


'''Part 1 was Brute force comma casework.
Bad combo of not realizing
the comma issue and then not figuring out how to either
use .strip(',') or or statements for string comparison
 correctly :/
Part 2 was easy enough, spent most of the time copy
pasting part 1 and then removing lines
Need to get faster at appropriating part 1 code
into part 2 solution/accept the speed need to delete
code from part 1

.replace() was what you wanted.
Did not correctly remember how .strip() operated.

Or issue was due to any string with
char in it being evaluated as True

BBA showed that this type of situation is perfect for regex, e.g.:
RD = re.compile(r'(\d+) red')
'''
