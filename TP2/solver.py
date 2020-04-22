#!/bin/python3

from functionFactories.crossingOverFactory import CrossingOverFactory
from functionFactories.mutationFactory import MutationFactory
from functionFactories.selectorFactory import SelectorFactory
from functionFactories.stopCriteriaFactory import StopCriteriaFactory
from functionFactories.implementationFactory import ImplementationFactory
from domains import getDomains
import constants as ct
import datetime as dt
import matplotlib.pyplot as plt
import random as rd

class Solver:
    def __init__(self, genZero, configDict):
        
        domains = getDomains(genZero)

        stopLimit = float(configDict[ct.stopCriterion['name']][1])
        
        N = len(genZero)
        
        crossOver = CrossingOverFactory(configDict[ct.crossingOver['name']]).getCrossingOverFunction()
        mutator = MutationFactory(configDict[ct.mutation['name']], float(configDict[ct.mutation['pM']]), domains)
        selector1 = SelectorFactory(configDict[ct.selection['name']][0], N, configDict[ct.boltzmannTemperature], configDict[ct.tournaments2Threshold]).getSelector()
        selector2 = SelectorFactory(configDict[ct.selection['name']][1], N, configDict[ct.boltzmannTemperature], configDict[ct.tournaments2Threshold]).getSelector()
        selector3 = SelectorFactory(configDict[ct.selection['name']][2], N, configDict[ct.boltzmannTemperature], configDict[ct.tournaments2Threshold]).getSelector()
        selector4 = SelectorFactory(configDict[ct.selection['name']][3], N, configDict[ct.boltzmannTemperature], configDict[ct.tournaments2Threshold]).getSelector()
        isDone = StopCriteriaFactory(configDict[ct.stopCriterion['name']][0]).getDoneFunction()
        implement = ImplementationFactory(configDict[ct.implementation['name']]).getImplementationFunction()

        generation = rd.sample(genZero, 10)
        
        iterationNo = 0
        
        startTime = dt.datetime.now()
        time = 0

        prevBestFitness = -1
        bestFitness = 0
        equalGenerations = 0
        
        bestMax = 0
        bestIndividual = None

        done = False
        maxes = []
        while not done:
            
            children = crossOver(generation)
            newChildren = mutator.performMutation(children)
            rdA = rd.random()
            if rdA < float(configDict[ct.a]):
                selector = selector1
            else:
                selector = selector2
            parents = selector.select(generation, len(generation)//2)
            selectableIndividuals = implement(generation, newChildren)
            rdB = rd.random()
            if rdB < float(configDict[ct.b]):
                selector = selector3
            else:
                selector = selector4
            newGeneration = selector.performSelection(selectableIndividuals)
            
            time = startTime - dt.datetime.now()
            
            if configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['time']:
                done = isDone(time, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['generations']:
                done = isDone(iterationNo, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['acceptable']:
                done = isDone(newGeneration, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['struct']:
                done, equalGenerations = isDone(generation, newGeneration, equalGenerations, float(configDict[ct.stopCriterion['name']][2]), stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['content']:
                prevBestFitness = bestFitness
                bestFitness = max([x.getFitness() for x in generation])
                if bestFitness == prevBestFitness:
                    equalGenerations += 1
                done = isDone(equalGenerations, stopLimit)
            
            generationMax = max([(x.getPerformance(), x) for x in newGeneration])

            if bestMax < generationMax[0]:
                bestMax = generationMax[0]
                bestIndividual = generationMax[1]

            maxes.append(generationMax[0])
            

            iterationNo += 1
            generation = newGeneration
        plt.plot(list(range(1, len(maxes)+1)), maxes, linestyle='', marker='o')
        plt.show()
        print(bestMax)
        print(bestIndividual.genes)