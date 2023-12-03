#! /usr/bin/env python3

# Advent of Code 2023 Day 3


dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('3.in').read().strip()
lines = [x for x in data.split('\n')]

p1 = 0
grid = []
ind = 1

dirs = list(itertools.product([-1,0,1],[-1,0,1]))
print(dirs)

for i in range(len(lines)):
    grid.append([])
    for j in range(len(lines[i])):
        grid[i].append(lines[i][j])

for i in range(len(lines)):
    ind += 1
    j = 0
    while(j < len(grid[i])):
        start = j
        count = False

        while grid[i][j].isdigit():
            for [a,b] in dirs:
                if (-1 < i + a < len(grid)) and (-1 < j + b < len(grid[i]))\
                    and grid[i+a][j+b] != '.' and not(grid[i+a][j+b].isdigit()):
                    if re.match('^[*]+$', grid[i+a][j+b]) and count == False:
                        grid[i+a][j+b] += '*'
                    count = True

            if j < len(grid[i])-1:
                j += 1
            else:
                j += 1
                break
        
        if grid[i][start].isdigit() and\
            not(grid[i][start-1].isdigit()) and count:
            num = ''
            for p in range(start,j):
                num += grid[i][p]
                
            if num != '':
                p1 += int(num)   
        j += 1

print('part 1 is ', p1)


p2 = 0
for i in range(len(lines)):
    for j in range(len(grid[i])):
        if grid[i][j].isdigit() and j < len(grid[i])-1 and grid[i][j+1].isdigit():
            grid[i][j+1] = grid[i][j] + grid[i][j+1]

# print(grid[2][89])
print(grid[7][136])
for i in range(len(lines)):
    for j in range(len(grid[i])):
        val = 0
        if grid[i][j] == '***':
            print('pos',i,j)
            val = 1
            for [a,b] in dirs:
                if (-1 < i + a < len(grid)) and (-1 < j + b < len(grid[i]))\
                    and grid[i+a][j+b].isdigit():
                        end = False
                        p = j + b
                        while not(end):
                            if p + 1 < len(grid[i]) and\
                                grid[i+a][p+1].isdigit():
                                p +=1
                            else:
                                end = True
                        val2 = int(grid[i+a][p])
                        if val2 >1:
                            print(val2,end=';')
                        val *= val2
                        grid[i+a][p] = '1'
        if val > 0:
            print(' val is', val)
        p2 += val


print('part 2 is', p2)

# Just terrible. Need better approaches than this for grid/neighbor problems.