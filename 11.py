#! /usr/bin/env python3

# Advent of Code 2023 Day 11

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('11.in').read().strip()
lineset = data.split('\n')

p1 = 0
p2 = 0

lineset = [list(line) for line in lineset]


rows = []
cols = []

for i in reversed(range(len(lineset))):
    if '#' not in lineset[i]:
        rows.append(i)

lines = [list(line) for line in list(zip(*lineset))]

for i in reversed(range(len(lines))):
    if '#' not in lines[i]:
        cols.append(i)

lines = [list(line) for line in list(zip(*lines))]

stars = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '#':
            stars.append((i,j))


sols = []
for exp in (1,999999):
    p = 0
    for (star1, star2) in itertools.combinations(stars,2):
        dist = 0
        xmin = min(star1[0],star2[0])
        xmax = max(star1[0],star2[0])

        ymin = min(star1[1],star2[1])
        ymax = max(star1[1],star2[1])

        for i in range(xmin,xmax):
            if i in rows:
                dist += exp
        for i in range(ymin,ymax):
            if i in cols:
                dist += exp
        dist += abs(star1[0]- star2[0]) + abs(star1[1]-star2[1])
        p += dist
    sols.append(p)

# for line in lines:
#     print(''.join(line))

p1 = sols[0]
p2 = sols[1]
print('p1 is ', p1)
print('p2 is ', p2)

# Today mainly using itertools to get all desired combinations, and how to rotate a list of lists