#! /usr/bin/env python3

# Advent of Code 2023 Day 5

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('5.in').read().strip()
lines = [x for x in data.split('\n\n')]

p1 = 0
p2 = 0

#naive way, for reference
# seeds = [[]]
seedset = list(map(int,lines[0].split()[1:]))
# for i in range(int(len(seedset)/2)):
#     for j in range(seedset[2*i+1]):
#         seeds[0].append(seedset[2*i]+j)

seeds = [list(map(int,lines[0].split()[1:]))]

mxs = max(seeds[0])
print(mxs)

i = 0
for line in lines[1:]:
    seeds.append([])
    rules = line.split('\n')[1:]
    for seed in seeds[i]:
        ch = False
        for rule in rules:
            spot = seed
            words = list(map(int,rule.split()))
            if words[1] <= seed < words[1]+words[2]:
                spot = words[0]+seed-words[1]
                break
        seeds[i+1].append(spot)

        
    i += 1

p1 = min(seeds[i])
# index_min = np.argmin(seeds[i])
# p1 = seeds[0][index_min]
    

print('p1 is ', p1)



# Part 2 reverse order probably going to have to be from scratch
# This takes about ~5 minutes to run. I added a nice 100,000 benchmarking
# so you know what it's up to. The result is 6082852 for my dataset.

l = 0
noFind = True
while noFind:
    num = l
    for line in lines[1::][::-1]:
        # print(line.split('\n')[0])
        rules = line.split('\n')[1:]
        for rule in rules:
            words = list(map(int,rule.split()))
            # print('num is',num)
            # print('start is',words[0])
            if words[0] <= num < words[0]+words[2]:
                num = words[1]+num-words[0]
                break
    
    # print('finally',num)
    for i in range(int(len(seedset)/2)):
        if seedset[2*i] <= num < seedset[2*i]+seedset[2*i+1]:
            noFind = False
    if l % 100000 == 0:
        print(l)
        
    l += 1
p2 = l -1

print('p2 is ', p2)

# Pretty happy with this. Spent maybe 40 minutes on part 1 and 45 on part 2.
# Arguably I should've been much faster on part 2, but I think I also was relatively quick
# on reasoning for part 2, minus the part where I intentionally spent time trying the
# Naive approach, which is something I don't plan to repeat for similar puzzles in the
# Future. One downside is this algo still wasn't very fast - intersections would've given
# A faster result, but I definitely would've spent more than the time difference reasoning
# About how to write that algorithm.