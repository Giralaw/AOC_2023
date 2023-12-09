#! /usr/bin/env python3

# Advent of Code 2023 Day 9

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('9.in').read().strip()
lines = [x for x in data.split('\n')]

p1 = 0
p2 = 0
def ext(series,rev):
    seq = [eval(i) for i in series.split(" ")]
    seq = seq[::-1] if rev else seq
    # print(seq)
    diff = False
    ch = [seq]
    i = 0
    while diff == False:
        i +=1
        ch.append([])
        for j in range(len(ch[i-1])-1):
            ch[i].append(ch[i-1][j+1]-ch[i-1][j])

        diff = True
        for j in range(len(ch[i-1])-1):
            if ch[i][j]-ch[i][j-1] != 0:
                diff = False

    ch.reverse()
    for k in range(1,len(ch)):
        ch[k].append(ch[k][-1]+ch[k-1][-1])
    return ch[-1][-1]
    


for line in lines:
    p1 += ext(line,False)

for line in lines:
    p2 += ext(line,True)

print('p1 is ', p1)
print('p2 is ', p2)