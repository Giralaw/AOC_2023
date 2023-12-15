#! /usr/bin/env python3

# Advent of Code 2023 Day 15

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[1,0],[0,1],[-1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode

data = open('15.in').read().strip()
lines = [x for x in data.split(',')]

p1 = 0
p2 = 0


def def_value(): 
    return 0


bix = []
[bix.append(defaultdict(def_value)) for i in range(256)]

def day(part1):
    p1 = 0
    p2 = 0


    for line in lines:
        cd = 0
        
        if line.count("-") == 1:
            op = 0
        else:
            op = 1
        code = line.split("=") if op else line.strip("-")
        if op:
            lb,fl = code
        else:
            lb = code
        
        b = line if part1 else lb

        for char in b:
            cd += ord(char)
            cd = 17*cd
            cd = cd % 256
        p1 += cd

        if not(part1):
            bxs = bix[cd]
            assert(bxs[lb] != -1)
            
            if op:
                if not(bxs):
                    bxs[lb] = fl
                elif lb in bxs.keys():
                    bxs[lb] = fl
                else:
                    bxs[lb].insert(0,fl)
            else:
                if lb in bxs.keys():
                    del bxs[lb]
    if not(part1):
        for idx,bx in enumerate(bix):
            for idy,spt in enumerate(bix[idx]):

                a = int((bix[idx][spt]))
                p2 += (idx+1)*(idy+1)*a
        return p2
    
    return p1

print('p1 is ', day(True))
print('p2 is ', day(False))


# In retrospect I definitely didn't actually need a dictionary,
# just a list of lists