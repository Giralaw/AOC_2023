#! /usr/bin/env python3

# Advent of Code 2023 Day 6

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('6.in').read().strip()
lines = [x for x in data.split('\n')]

p1 = 1
p2 = 0

t = lines[0].split()[1:]
d = lines[1].split()[1:]
#print(t,d)
print(t,d)
t2 = ''.join(t)
d2 = ''.join(d)
print(t2,d2)


for i in range(len(d)):
    num = 0
    for j in range(int(t[i])):
        if (int(t[i])-j)*j > int(d[i]):
            if j % 1000000 ==0:
                print('hello',j)
            num += 1
    p1 *= num
num = 0

for j in range(int(t2)):
    if (int(t2)-j)*j > int(d2):
        if j % 1000000 ==0:
            print(j)
        num += 1
p2 = num


print('p1 is ', p1)
print('p2 is ', p2)

# Fast one today. Two major bugs in starting up were
# Forgetting to change index in d to be 1, and
# Accidentally adding j when checking the inequality.
# So that slowed down part 1 mostly.
# For part 2, I just manually removed the whitespace
# from the .in file because I didn't have ''.join()
# in recent memory.
# Probably a more efficient algorithm but
# I don't know that I would've been able to save
# A meaningful amount of time with it anyway
# (Part 2 takes ~15 seconds)