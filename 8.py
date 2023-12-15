#! /usr/bin/env python3

# Advent of Code 2023 Day 8

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[1,0],[0,1],[-1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('8.in').read().strip()
lines = data.split('\n\n')
instr = lines[0]

nds = lines[1].split('\n')

p1 = 0
p2 = 0

paths = defaultdict()

for line in nds:
    rel = line.split(" ")
    paths[rel[0]] = tuple((rel[2][1:-1], rel[3][:-1]))
    # print(rel[0],paths[rel[0]])


# Part 1
srch = True
curr = 'AAA'
while srch:
    dir = 0 if instr[p1 % len(instr)] == 'L' else 1

    #print(dir,curr,paths[curr])

    curr = paths[curr][dir]
    p1 += 1
    if curr == 'ZZZ':
        srch = False

# Part 2
currs = []
[currs.append(x) for x in paths.keys() if x[-1] == 'A']
print(currs)

cycs = []
for curr in currs:
    pt = curr
    cyc = 0
    srch = True
    while srch:
        dir = 0 if instr[cyc % len(instr)] == 'L' else 1
        pt = paths[pt][dir]
        cyc += 1

        if pt[-1] == 'Z':
            srch = False
            cycs.append(cyc)

# * method for unpacking a list into a...list of vars as individual args
p2 = math.lcm(*cycs)

print('p1 is ', p1)
print('p2 is ', p2)