#!/bin/python3

from functionFactories.crossingOverFactory import CrossingOverFactory
from functionFactories.mutationFactory import MutationFactory
from functionFactories.selectorFactory import SelectorFactory
from functionFactories.stopCriteriaFactory import StopCriteriaFactory
from functionFactories.implementationFactory import ImplementationFactory
import constants as ct
import datetime as dt

class Solver:
    def __init__(self, genZero, configDict):
        
        stopLimit = configDict[ct.stopCriterion['name']][1]
        
        N = len(genZero)
        
        crossOver = CrossingOverFactory(configDict[ct.crossingOver['name']]).getCrossingOverFunction()
        mutate = MutationFactory(configDict[ct.mutation['name']], float(configDict[ct.mutation['pM']])).getMutationFunction()
        selector = SelectorFactory(configDict[ct.selection['name']], N, configDict[ct.boltzmannTemperature], configDict[ct.tournaments2Threshold]).getSelector()
        isDone = StopCriteriaFactory(configDict[ct.stopCriterion['name']][0]).getDoneFunction()
        implement = ImplementationFactory(configDict[ct.implementation['name']]).getImplementationFunction()
        

        generation = genZero
        
        mutate(generation)

        iterationNo = 0
        
        startTime = dt.datetime.now()
        time = 0

        prevBestFitness = -1
        bestFitness = 0
        equalGenerations = 0
        
        done = False

        while not done:
            
            children = crossOver(generation)
            newChildren = mutate(children)
            selectableIndividuals = implement(generation, newChildren)
            newGeneration = selector.performSelection(selectableIndividuals)
            
            time = startTime - dt.datetime.now()
            
            if configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['time']:
                done = isDone(time, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['generations']:
                done = isDone(iterationNo, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['acceptable']:
                done = isDone(newGeneration, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['struct']:
                #DeepCompare each element from generation with each from newGeneration to determine equality percentage
                #if 
                done = isDone(time, stopLimit)
            elif configDict[ct.stopCriterion['name']][0] == ct.stopCriterion['content']:
                prevBestFitness = bestFitness
                bestFitness = max([x.getFitness() for x in generation])
                if bestFitness == prevBestFitness:
                    equalGenerations += 1
                done = isDone(equalGenerations, stopLimit)
            
            print(max([x.getPerformance() for x in newGeneration]))
            iterationNo += 1

