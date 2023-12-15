#! /usr/bin/env python3

# Advent of Code 2023 Day 14

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [[1,0],[0,1],[-1,0],[0,-1]]

import sys
import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('14.ex').read().strip()
lines = [x for x in data.split('\n')]

p1 = 0
p2 = 0

r = len(lines)
c = len(lines[0])

grid = np.zeros((r,c), dtype = str)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        grid[i,j] = lines[i][j]


cyc = 0
stores = []
notFound = True
for q in range(200):
    p1 = 0
    for s in range(4):
        dir = dirs2[s % 4]
        rr = dir[0]
        cc = dir[1]
        # print(dir)
        for p in range(len(lines)):
            for i in range(len(lines)):
                for j in range(len(lines[0])):
                    if (rr == 1 and i > 0) or (rr == -1 and i < r-1) or (cc == 1 and j > 0) or (cc == -1 and j < c-1):
                        # print(i,j,rr,cc,r,c)
                        if grid[i][j] == 'O' and grid[i-rr][j-cc] == '.':
                            grid[i,j] = '.'
                            grid[i-rr,j-cc] = 'O'

    # print('\n','cycle', (q+1))
    # for i in range(r):
    #     print(''.join(list(grid[i])), r-i)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if grid[i,j] == 'O':
                p1 += r - i
    
    if p1 in stores[:-1] and notFound:
        while stores.pop() != p1:
            cyc += 1
        notFound = False
        print(cyc) # cycle is 7 for 
    print(q, p1)
    if q > 40:
        stores.append(p1)
    


# print('\n','cycle', q)
# for i in range(r):
#     print(''.join(list(grid[i])), r-i)

#np.set_printoptions(threshold=sys.maxsize)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if grid[i,j] == 'O':
            p1 += r - i

print('p1 is ', p1)
print('p2 is ', p2)