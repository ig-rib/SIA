#!/bin/python3

from geneticSelectors.selector import Selector

import random as rd

class Tournaments1Selector(Selector):
    def __init__(self, N):
        super().__init__(N)
    
    def select(self, group, K):
        selected = []
        for touranment in range(K):
            x, y = rd.sample(group, 2)
            winner = max(x, y)
            selected.append(winner)
        return selected

