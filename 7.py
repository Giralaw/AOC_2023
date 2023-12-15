#! /usr/bin/env python3

# Advent of Code 2023 Day 7

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('7.in').read().strip()
lines = [x for x in data.split('\n')]

strs = {'A': 15, 'K': 14, 'Q': 13, 'J': 12, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4,'3':3,'2':2}
strsj = {'A': 15, 'K': 14, 'Q': 13, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4,'3':3,'2':2,'J': 1}

def comp(ha1, ha2, j):
    dic = strsj if j else strs
    r1 = 0
    #print(ha1,ha2)
    if not(j):
        h1 = list(ha1)
    elif ha1 == 'JJJJJ':
        h1 = 'KKKKK'
    else:
        h1 = list(ha1.replace('J',mode(ha1.replace('J',''))))

    for c in h1:
        r1 += h1.count(c)
    
    r2 = 0

    if not(j):
        h2 = list(ha2)
    elif ha2 == 'JJJJJ':
        h2 = 'KKKKK'
    else:
        h2 = list(ha2.replace('J',mode(ha2.replace('J',''))))

    for c in h2:
        r2 += h2.count(c)
    
    if r2 > r1:
        hw = ha2
    elif r1 > r2:
        hw = ha1
    else:
        for a,b in zip(list(ha1),list(ha2)):
            if dic[a] > dic[b]:
                hw = ha1
                break
            elif dic[b] > dic[a]:
                hw = ha2
                break
            else:
                continue

    return hw

def sum(lines,part):
    sz = len(lines)
    ord = []
    bids = defaultdict()

    p = 0
    J = True if part == 2 else False
    for line in lines:
        play = line.split(" ")
        hand = play[0]
        bids[hand] = int(play[1])

        if len(ord)==0:
            ord.append(hand)
        else:
            spot = False
            for i in range(len(ord)):
                if comp(hand, ord[i],J) == hand:
                    ord.insert(i, hand)
                    spot = True
                    break
            if not(spot):
                ord.append(hand)

    for i in range(len(ord)):
        # print(ord[i],(sz-i),bids[ord[i]])
        p += bids[ord[i]]*(sz-i)
    return p

print('p1 is ', sum(lines,1),'\n')
print('p2 is ', sum(lines,2))