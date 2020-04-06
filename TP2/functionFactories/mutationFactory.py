#!/bin/python3

import random as rd
import constants as ct

def getNewHeight():
    return rd.random()*0.7 + 1.3

def getModifier():
    sign = rd.choice([-1, 1])
    return sign * rd.random()

class MutationFactory:

    def __init__(self, type, pm):
        
        if type == 'GEN':
            def performMutation(children):
                doPerformMutation = rd.random()
                if doPerformMutation <= pm:
                    keys = list(children[0].genes.keys())
                    selectedKey = keys[rd.randint(0, len(keys))]
                    if selectedKey == ct.height:
                        for child in children:
                            child.genes[ct.height] = getNewHeight()
                    else:
                        for child in children:
                            for key in child.genes[selectedKey]:
                                child.genes[selectedKey][key] += getModifier()
                return children
        elif type == 'LIM-MULTIGEN':
            def performMutation(children):
                keys = list(children[0].genes.keys())
                selectedKeys = rd.sample(keys, rd.randint(0, len(keys)))
                for child in children:
                    for selectedKey in selectedKeys:
                        doPerformMutation = rd.random()
                        if doPerformMutation <= pm:
                            if selectedKey == ct.height:
                                child.genes[selectedKey] = getNewHeight()
                            else:
                                for key in child.genes[selectedKey]:
                                    child.genes[selectedKey][key] += getModifier()
                return children
        elif type == 'UNIFORM-MULTIGEN':
            def performMutation(children):
                keys = list(children[0].genes.keys())
                for child in children:
                    for key in keys:
                        doPerformMutation = rd.random()
                        if doPerformMutation <= pm:
                            if key == ct.height:
                                child.genes[key] = getNewHeight()
                            else:
                                for subKey in child.genes[key]:
                                    child.genes[key][subKey] += getModifier()
                return None
        elif type == 'COMPLETE':
            def performMutation(children):
                keys = list(children[0].genes.keys())
                for child in children:
                    for key in keys:
                        if key == ct.height:
                                child.genes[key] = getNewHeight()
                        else:
                            for subKey in child.genes[key]:
                                child.genes[key][subKey] += getModifier()
                return None
        else:
            print('Invalid Mutation Type')
            exit(1)
        self.performMutation = performMutation
    
    def getMutationFunction(self):
        return self.performMutation
