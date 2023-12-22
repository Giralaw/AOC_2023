#! /usr/bin/env python3

# Advent of Code 2023 Day 21

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[1,0],[0,1],[-1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('21.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

grid = []
for r in range(len(lines)):
    grid.append([])
    for c in range(len(lines[r])):
        grid[r].append(lines[r][c])
        if lines[r][c] == 'S':
            sr,sc = r,c

rows = len(lines)
cols = len(lines[0])

paths = [[(sr,sc)]]

# This is the naive way.
# Gotta figure out the actual soln.

i = 0
steps = 64
while i < steps:
    print(i)
    i += 1
    paths.append([])
    for path in paths[-2]:
        # print(path)
        r = path[0]
        c = path[1]
        for rr,cc in dirs2:
            if 0 <= r+rr < rows and 0 <= c+cc < cols:
                if grid[r+rr][c+cc] != "#":
                    paths[i].append((r+rr,c+cc))
                    
# print(paths)
# print(len(paths[-1]))
# print(len(paths))
p1 = len(set(paths[-1]))
print('p1 is ', p1)
print('p2 is ', p2)