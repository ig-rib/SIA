#!/bin/python3

from geneticSelectors.selector import Selector
import random as rd


class RWheelSelector(Selector):
    def __init__(self, N):
        super().__init__(N)
    
    def select(self, group, K):
        relativePerformances = [x.getPerformance() for x in group]
        totalPerformanceSum = sum(relativePerformances)
        relativePerformances[:] = [ x / totalPerformanceSum for x in relativePerformances]
        cumulativePs = [relativePerformances[0]]
        for i in range(1, len(relativePerformances)):
            cumulativePs.append(cumulativePs[-1] + relativePerformances[i])
        selected = []
        for i in range(K):
            r = rd.random()
            j = 0
            found = False
            while j < len(cumulativePs) and not found:
                if r > cumulativePs[j]:
                    j+=1
                else:
                    found = True
            selected.append(group[j])
        return selected
    
