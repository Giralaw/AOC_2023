#! /usr/bin/env python3

# Advent of Code 2023 Day 2

dirs = [(-1,1),(1,1),(1,-1),(-1,-1)]
import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *

data = open('2.in').read().strip()
lines = [x for x in data.split('\n')]


tot = 0
for line in lines:
    x=1

print('total is ', tot)