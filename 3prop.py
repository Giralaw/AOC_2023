#! /usr/bin/env python3

# Advent of Code 2023 Day 3

# A second attempt, this time
# working through logic of JPaulson's solution
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/3.py


dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('3.in').read().strip()
lines = [x for x in data.split('\n')]


g = [[c for c in line] for line in lines]

grid2 = []
for line in lines:
    grid2.append([])
    for c in line:
        grid2[-1].append(c)

# Check that these are equivalent
# confirming inline for-loop tech
assert(grid2 == g) 

R = len(g)
C = len(g[0])

p1 = 0

rates = defaultdict(list)
for r in range(len(g)):
    gears = set()
    count = False
    n = 0

    for c in range(len(g[0])+1):
        if c < C and g[r][c].isdigit():
            n = 10*n+int(g[r][c])
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if 0 <= r + rr < R and 0 <= c + cc < C:
                        ch = g[r+rr][c+cc]
                        if not ch.isdigit() and ch != '.':
                            count = True
                        if ch == '*':
                            gears.add((r+rr,c+cc))
                            print("pos is",r,c)

        elif n > 0 and count:
            p1 += n
            for gear in gears:
                rates[gear].append(n)
            count = False
            n = 0
            gears = set()
        else:
            n = 0

p2 = 0
for k,v in rates.items():
    if len(v) == 2:
        p2 += v[0]*v[1]
        # p2 += np.prod(np.array(v))

print('p1 is', p1)

print('p2 is', p2)