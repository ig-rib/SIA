#!/bin/python3

from geneticSelectors.selector import Selector
import random as rd

class Tournaments2Selector(Selector):
    def __init__(self, N, threshold):
        super().__init__(N)
        self.threshold = float(threshold)
    def select(self, group, K):
        selected = []
        # threshold = rd.random() * 0.5 + 0.5
        for touranment in range(K):
            x, y = rd.sample(group, 2)
            r = rd.random()
            if r < self.threshold:
                winner = max(x, y)
            else:
                winner = min(x, y)
            selected.append(winner)
        return selected

