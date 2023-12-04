#! /usr/bin/env python3

# Advent of Code 2023 Day 4

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('4.in').read().strip()
lines = [x for x in data.split('\n')]

p1 = 0
p2 = 0

for line in lines:
    w,l = line.split('|')
    w = w.split()[2:]
    l = l.split()
    # print(w)
    # print(l)
    val = -1
    for n in l:
        if n in w:
            val +=1
    if val > -1:
        p1 += 2**val


cards = list()


for i in range(len(lines)):
    cards.append(i)

p2 = 0

while len(cards) > 0:
    c = cards.pop()
    # print(c)
    p2 += 1
    val = 0
    w,l = lines[c].split('|')
    w = w.split()[2:]
    l = l.split()
    for n in l:
        if n in w:
            val +=1
    # print("card",c,val)
    if val > 0:
        for j in range(1,val+1):
            # print((i,j))
            cards.append(c+j)
            # print(cards)
    # cards.sort()
    # print(cards)

print('p1 is ', p1)
print('p2 is ', p2)


# Pretty good. Only real issue was accidentally
# Double counting initial cards by doing
# p2 = len(lines) to initialize. Kind of outsmarted
# myself with that one. Part 1 was my best placement
# Thus far though, so that's nice.