#!/bin/python3

from geneticSelectors.selector import Selector
import math

class EliteSelector(Selector):
    def __init__(self, N):
        super().__init__(N)
    
    def select(self, group, K):
        sortedGroup = sorted(group, reverse=True)
        sortedGroup
        ns = [math.ceil((self.N-i)/self.N) for i, element in enumerate(sortedGroup)]
        newArray = []
        i = 0
        while i < len(ns) and len(newArray) < self.N:
            for j in range(ns[i]):
                newArray.append(sortedGroup[i])
            i += 1
        return newArray