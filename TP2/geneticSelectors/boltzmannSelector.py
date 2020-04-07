#!/bin/python3

from geneticSelectors.selector import Selector
import math
import random as rd

class BoltzmannSelector(Selector):
    def __init__(self, N, T):
        super().__init__(N)
        self.T = float(T)
    def select(self, group, K):
        exponentials = [math.exp(x.getPerformance()/self.T) for x in group]
        a = sum(exponentials) / len(exponentials)
        fPrimes = [ x / a for x in exponentials ]
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