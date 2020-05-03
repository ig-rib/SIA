#!/bin/python3

import numpy as np
from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import sys
from collections import deque

class MultiLayerPerceptron(Perceptron):
    def __init__(self, r, g, gPrime, inputDimension=2, middleLayerDimensions=[2], outputLayerDimension=1):
       
        self.layerWeights=[np.random.uniform(size=(inputDimension, middleLayerDimensions[0]))]
        self.layerBiases = [np.zeros(shape=(1, middleLayerDimensions[0]))]
        for i in range(len(middleLayerDimensions)-1):
            self.layerWeights.append(np.random.uniform(size=(middleLayerDimensions[i], middleLayerDimensions[i+1])))
            self.layerBiases.append(np.zeros(shape=(1, middleLayerDimensions[i+1])))
        self.layerWeights.append(np.random.uniform(size=(middleLayerDimensions[-1], outputLayerDimension)))
        self.layerBiases.append(np.zeros(shape=(1, outputLayerDimension)))
        self.g = g
        self.gPrime = gPrime

    def train(self, X, r = None, minError = 1e-3, epochs = 1000):

        error = sys.maxsize
        ep = 0
        while error > minError and ep < epochs:
            xActVsPred = []
            for x in X:
                ## Forward
                currOutput = x[0]
                H = []
                for index, weights in enumerate(self.layerWeights):
                    currOutput = np.dot(currOutput, weights)
                    currOutput = np.add(currOutput, self.layerBiases[index])
                    H.append(currOutput[0])
                    ## Notar que en el caso boolen debería ser 1x1
                    newCurrOutput = [self.g(h) for h in currOutput[0]]
                xActVsPred.append((x[1], newCurrOutput[-1]))
                ## Backwards
                deltas = deque([ self.gPrime(h) * ( x[1] - newCurrOutput[-1] ) for h in H[-1]])
                for m in range(len(self.layerWeights)-2, -1, -1):
                    deltas.appendleft([ [ self.gPrime(h) for h in H[m+1] ] * np.dot(deltas[0], self.layerWeights[m]) ])
                for m in range(len(self.layerWeights)-1, 0, -1):
                    self.layerWeights[m] = np.add(self.layerWeights[m], [ self.gPrime(h) for h in H[m-1] ] * np.dot(deltas[m], self.layerWeights[m]))
            diffVect = [ (x[0] - x[1]) ** 2 for x in xActVsPred ]
            error = sum(diffVect) / 2
            print(error, end=' ')
            ep+=1

    def classify(self, vector):
        currOutput = vector[0]
        for index, weights in enumerate(self.layerWeights):
            currOutput = np.dot(currOutput, weights)
            currOutput = np.add(currOutput, self.layerBiases[index])
            ## Notar que en el caso boolen debería ser 1x1
            newCurrOutput = [self.g(h) for h in currOutput[0]]
        return newCurrOutput[0]
domain = [ (-1, 1), (1, -1), (-1, -1), (1, 1) ]

AndX = [ (x, min(x[0], x[1])) for x in domain ]
XorX = [ (x, -1 if x[0] == x[1] else 1) for x in domain ]
OrX = [ (x, max(x[0], x[1])) for x in domain ]

## Getting the functions and their derivatives
sff1 = sff.SigmoidFunctionFactory(0.5)
tanhFunc, tanhPrime = sff1.getFunctionAndDerivative(sff.tanh)
logisticFunc, logisticPrime = sff1.getFunctionAndDerivative(sff.logistic)

mlp = MultiLayerPerceptron(0.5, tanhFunc, tanhPrime, 2, [3], 1)
mlp.train(AndX, 0.5, 0.1, 1000)

results = [(d, mlp.classify(d)) for d in domain]
results