#!/bin/python3

import random as rd
import constants as ct


class MutationFactory:

    # def getNewHeight(self):
    #     return rd.random()*0.7 + 1.3

    # def getModifier(self):
    #     sign = rd.choice([-1, 1])
    #     return sign * rd.random()

    def getNewGeneValue(self, geneName):
        geneDomain = self.domains[geneName]
        return rd.sample(geneDomain, 1)[0]

    def __init__(self, type, pm, domains):
        self.domains = domains

        if type == 'GEN':
            def performMutation(children):
                doPerformMutation = rd.random()
                if doPerformMutation <= pm:
                    keys = list(children[0].genes.keys())
                    selectedKey = keys[rd.randint(0, len(keys)-1)]
                    for child in children:
                        child.genes[selectedKey] = self.getNewGeneValue(selectedKey)
                return children
        elif type == 'LIM-MULTIGEN':
            def performMutation(children):
                keys = list(children[0].genes.keys())
                selectedKeys = rd.sample(keys, rd.randint(0, len(keys)-1))
                for child in children:
                    for selectedKey in selectedKeys:
                        doPerformMutation = rd.random()
                        if doPerformMutation <= pm:
                            child.genes[selectedKey] = self.getNewGeneValue(selectedKey)
                return children
        elif type == 'UNIFORM-MULTIGEN':
            def performMutation(children):
                keys = list(children[0].genes.keys())
                for child in children:
                    for key in keys:
                        doPerformMutation = rd.random()
                        if doPerformMutation <= pm:
                            child.genes[key] = self.getNewGeneValue(key)
                return children
        elif type == 'COMPLETE':
            def performMutation(children):
                for child in children:
                    doPerformMutation = rd.random()
                    if doPerformMutation <= pm:
                        keys = list(children[0].genes.keys())
                        for key in keys:
                            child.genes[key] = self.getNewGeneValue(key)
                return children
        else:
            print('Invalid Mutation Type')
            exit(1)
        self.performMutation = performMutation
    
    def getMutationFunction(self):
        return self.performMutation
