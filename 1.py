#! /usr/bin/env python3

# Advent of Code 2023 Day 1

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('1.in').read().strip()
lines = [x for x in data.split('\n')]

digdic = {'one': 1, 'two': 2, 'three' : 3, 'four' : 4,\
        'five': 5, 'six' : 6, 'seven' : 7, 'eight' : 8,\
        'nine' : 9, 'zero' : 0}

tot = 0

for line in lines:

    start = 0
    end = 0
    for i in range(len(line)):
        dig = line[i]
        if dig.isdigit():
            start = int(dig)
            min = i
            break

    # Comment out for part A
    for elt in digdic.keys():
        b = line.find(elt)
        if b < min and b > -1:
            start = digdic.get(elt)
            min = b

    for i in range(len(line)):
        dig = line[::-1][i]
        if dig.isdigit():
            end = int(dig)
            max = i
            break


    # Comment out for part A
    for elt in digdic.keys():
        b = line[::-1].find(elt[::-1])
        if b < max and b > -1:
            end = digdic.get(elt)
            max = b
    
    tot += 10*start + end

print('total is',tot)


'''Things today: Dictionaries, python .find() method,
inverted strings + substring search

Hard part 2 for day 1, compared to
how I remember last year!'''