#!/bin/python3

import constants as ct

class Selector:
    def __init__(self, N):
        self.N = N

    def performSelection(self, selectableGroup):
        newGeneration = []
        if selectableGroup[0] == ct.oneArray:
            newGeneration = self.select(selectableGroup[1], self.N)
        elif selectableGroup[0] == ct.childrenAndParents:
            selectedChildren = self.select(selectableGroup[1], len(selectableGroup[1]))
            selectedParents = self.select(selectableGroup[2], self.N - len(selectableGroup[1]))
            newGeneration = []
            newGeneration.extend(selectedChildren)
            newGeneration.extend(selectedParents)
        else:
            print('Error during elite selection')
        return newGeneration

    def select(self, group, K):
        print('unimplemented')