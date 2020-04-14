#!/bin/python3

import random as rd
import copy

class CrossingOverFactory:

    def __init__(self, type):
        if type == 'SINGLE-POINT':
            def performCrossingOver(generation):
                children = []
                keys = list(generation[0].genes.keys())
                locus = rd.randint(0, len(keys)-1)
                rd.shuffle(generation)
                shuffledParents = generation
                for i in range(0, len(shuffledParents), 2):
                    p1, p2 = shuffledParents[i], shuffledParents[i+1]
                    p1p = copy.deepcopy(p1)
                    p2p = copy.deepcopy(p2)
                    for j in range(locus, len(keys)):
                        gene = keys[j]
                        tmp = p1p.genes[gene]
                        p1p.genes[gene] = p2p.genes[gene]
                        p2p.genes[gene] = tmp
                    children.append(p1p)
                    children.append(p2p)
                return children
        elif type == 'TWO-POINT':
            def performCrossingOver(generation):
                children = []
                keys = list(generation[0].genes.keys())
                locus1 = rd.randint(0, len(keys)-2)
                locus2 = rd.randint(locus1+1, len(keys)-1)
                rd.shuffle(generation)
                shuffledParents = generation
                for i in range(0, len(shuffledParents), 2):
                    p1, p2 = shuffledParents[i], shuffledParents[i+1]
                    p1p = copy.deepcopy(p1)
                    p2p = copy.deepcopy(p2)
                    for j in range(locus1, locus2):
                        gene = keys[j]
                        tmp = p1p.genes[gene]
                        p1p.genes[gene] = p2p.genes[gene]
                        p2p.genes[gene] = tmp
                    children.append(p1p)
                    children.append(p2p)
                return children
        elif type == 'ANNULAR':
            def performCrossingOver(generation):
                children = []
                keys = list(generation[0].genes.keys())
                locus = rd.randint(0, len(keys)-1)
                # TODO checkear el // 2 + 1
                length = rd.randint(0, len(keys) // 2)
                rd.shuffle(generation)
                for i in range(0, len(generation), 2):
                    p1, p2 = generation[i], generation[i+1]
                    p1p = copy.deepcopy(p1)
                    p2p = copy.deepcopy(p2)
                    lc = locus
                    for j in range(length):
                        gene = keys[lc]
                        tmp = p1p.genes[gene]
                        p1p.genes[gene] = p2p.genes[gene]
                        p2p.genes[gene] = tmp
                        lc = (lc + 1) % len(keys)
                    children.append(p1p)
                    children.append(p2p)
                return children
        elif type == 'UNIFORM':
            def performCrossingOver(generation):
                children = []
                keys = list(generation[0].genes.keys())
                rd.shuffle(generation)
                shuffledParents = generation
                for i in range(0, len(shuffledParents), 2):
                    p1, p2 = shuffledParents[i], shuffledParents[i+1]
                    p1p = copy.deepcopy(p1)
                    p2p = copy.deepcopy(p2)
                    for j in range(len(keys)):
                        if rd.random() >= 0.5:
                            gene = keys[j]
                            tmp = p1p.genes[gene]
                            p1p.genes[gene] = p2p.genes[gene]
                            p2p.genes[gene] = tmp
                    children.append(p1p)
                    children.append(p2p)
                return children
        else:
            print('Invalid Crossing Over Type')
            exit(1)
        self.performCrossingOver = performCrossingOver
    
    def getCrossingOverFunction(self):
        return self.performCrossingOver