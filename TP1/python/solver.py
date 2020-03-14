#!/bin/python3

from treeNode import Node
from collections import deque

file = open('../maps/map1')
lines = file.readlines()
# form initial state from read data
Q0 = []
for line in lines:
    line = line.rstrip("\n")
    Q0.append(list(line))
F = deque()
Tr = Node()
Exp = []