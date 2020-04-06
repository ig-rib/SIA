#!/bin/python3

import random as rd
import copy

class CrossingOverFactory:

    def __init__(self, type):
        if type == 'SINGLE-POINT':
            def performCrossingOver(generation):
                children = []
                keys = list(generation[0].genes.keys())
                locus = rd.randint(0, len(keys))
                for i in range(len(generation)//2):
                    # TODO checkear que no se repitan parejas...
                    [ p1, p2 ] = rd.sample(generation, 2)
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
                locus1 = rd.randint(0, len(keys)-1)
                locus2 = rd.randint(locus1, len(keys))
                for i in range(len(generation)//2):
                    [ p1, p2 ] = rd.sample(generation, 2)
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
                return None
        elif type == 'UNIFORM':
            def performCrossingOver(generation):
                return None
        else:
            print('Invalid Crossing Over Type')
            exit(1)
        self.performCrossingOver = performCrossingOver
    
    def getCrossingOverFunction(self):
        return self.performCrossingOver