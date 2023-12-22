#! /usr/bin/env python3

# Advent of Code 2023 Day 18

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[1,0],[0,1],[-1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('18.ex').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0
dirs = {'L': [-1,0], 'R': [1,0], 'U': [0,1],'D': [0,-1]}

space = set()
space.add((0,0))
x,y = 0,0

for line in lines:
    data = line.split(" ")
    dir = data[0]
    amt = int(data[1])
    clr = data[2][2:-1]
    for i in range(amt):
        x += dirs[dir][0]
        y += dirs[dir][1]
        space.add((x,y))

    ymax = max([pt[1] for pt in space])
    ymin = min([pt[1] for pt in space])

xmax = max([pt[0] for pt in space])

for lvl in range(ymax,ymin-1,-1):
    xs = [(x,y) for (x,y) in space if y == lvl]
    xlocmax = max([pt[0] for pt in xs])
    # if lvl == -1:
    #     print(lvl)
    #     print(xs)
    start = True
    end = False
    par = False
    for (px,py) in xs:
        if (px+1,py) not in xs and px+1 < xlocmax:
            a = 1

            if (px-1,py) not in xs:
                start = True
            if (px+1,py) not in xs and start:
                end = True
            if start and end:
                par = not(par)
                start = False
                end = False

            while (px+a,py) not in space and px+a < xlocmax and par:
                space.add((px+a,py))
                a += 1

xmin = min([pt[0] for pt in space])
xmax = max([pt[0] for pt in space])
ymax = max([pt[1] for pt in space])
ymin = min([pt[1] for pt in space])

print(xmin,xmax,ymin,ymax)
for y in range(ymax,ymin-1,-1):
    for x in range(xmin,xmax+1):
    # for x in range(xmin,xmin+40):
        if (x,y) in space:
            print("#",end='')
        else:
            print('.',end='')
    print('')
p1 = len(space)



# R 2 (#0dc571)
# U 2 (#0dc571)
# R 2 (#0dc571)
# D 3 (#0dc571)
# L 4 (#0dc571)

print('p1 is ', p1)
print('p2 is ', p2)