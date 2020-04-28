#!/bin/python3

from geneticSelectors.selector import Selector
import random as rd

class RankingSelector(Selector):
    def __init__(self, N):
        super().__init__(N)
    
    def select(self, group, K):
        ranking = sorted(group)
        fPrimes = [ (len(ranking) - (i+1)) / len(ranking) for i, elem in enumerate(ranking) ]
        totalPerformanceSum = sum(fPrimes)
        fPrimes[:] = [ x / totalPerformanceSum for x in fPrimes]
        cumulativePs = [fPrimes[0]]
        for i in range(1, len(fPrimes)):
            cumulativePs.append(cumulativePs[-1] + fPrimes[i])
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
