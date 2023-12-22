#! /usr/bin/env python3

# Advent of Code 2023 Day 10

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('10.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

grid = []

types = {'S': (),'.':(-1,-1),'F': (0,3), "J": (2,1), "|": (0,2), "L": (3,2), "-": (1,3), "7": (0,1)}

# check if this whole shindig is even necessary
# print(lines[0])
# print(lines[-1])

for r in range(len(lines)):
    grid.append([])
    for c in range(len(lines[r])):
        grid[r].append(lines[r][c])
        if lines[r][c] == 'S':
            sr,sc = r,c

r = len(lines)
c = len(lines[0])

print(sr,sc)
path = []
pnew = (sr,sc)

exit = False
while (sr,sc) not in path:
    pold = pnew
    
    for i in range(len(dirs2)):
        rr,cc = dirs2[i]

        if 0 <= pold[0]+rr < r and 0 <= pold[1] + cc < c:
            
            pnew = (pold[0]+rr,pold[1]+cc)
            spt = grid[pnew[0]][pnew[1]]

            if spt != "S":

                dir = types[grid[pnew[0]][pnew[1]]]

                oldspt = grid[pold[0]][pold[1]]
                if i in dir and pnew not in path:
                    if (i == 0 and (oldspt =='J' or oldspt == '|' or oldspt == 'L')) or \
                        (i == 1 and (oldspt == 'F' or oldspt == 'L' or oldspt == '-')) or \
                            (i == 2 and (oldspt == '|' or oldspt == 'F' or oldspt == '7')) or \
                                (i == 3 and (oldspt == '-' or oldspt == 'J' or oldspt == '7')) or oldspt == 'S':
                        
                        path.append(pnew)
                        break
        if i == 3:
            exit = True
    if exit:
        break
path.append((sr,sc))

p1 = (len(path)+1)//2

#p2: raycasting algorithm. How elegant.

contained = set()
p2 = 0
for i in range(r):
    for j in range(c):
        if (i,j) not in path:
            ray = grid[i][:j]
            #print(ray)
            count = 0
            for k in range(len(ray)):
                if (i,k) in path and grid[i][k] in ('|','L','J'):
                    count += 1
            if count % 2 == 1:
                p2 += 1
                contained.add((i,k))

for i in range(r):
    for j in range(c):
        if (i,j) in contained:
            grid[i][j] = '#'

print('\n')
for i in range(r):
    print(''.join(grid[i]))

print('\n')

print('p1 is ', p1)
print('p2 is ', p2)