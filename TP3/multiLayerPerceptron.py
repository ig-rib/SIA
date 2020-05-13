#!/bin/python3

import numpy as np
from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import sys
from collections import deque
import random

beta = 1

def tanh(x):
    return np.tanh(beta * x)
def tanhPrime(x):
    return 1 - np.power(tanh(beta * x), 2)

#CHECK -- OK
def logistic(x):
    return 1 / (1 + np.exp(-x))

def logisticPrime(x):
    l = logistic(x)
    lc = 1 - l
    return np.multiply(l, lc)

def efficientLogisticPrime(x):
    return x * (1 - x)

# END CHECK -- OK

class MultiLayerPerceptron(Perceptron):
    def __init__(self, r, g, gPrime, inputDimension=2, middleLayerDimensions=[4,5], outputLayerDimension=1, K=5, a=0.0001, b=0.00001):
        self.r = r
        self.g = g
        self.gPrime = gPrime
        self.K = K
        self.a = a
        self.b = b
        
        self.deltas = {1 : np.asmatrix(np.zeros(shape=(middleLayerDimensions[0], 1)))}
        
        self.wByLayer = { #Weights for layer 1
            1: np.asmatrix(np.random.uniform(size=(inputDimension, middleLayerDimensions[0])))
        }
        for i in range(2, len(middleLayerDimensions) + 1): #Weights for layers 2 to (M-1)
            self.deltas[i] = np.asmatrix(np.zeros(shape=(middleLayerDimensions[i-1], 1)))
            self.wByLayer[i] = np.asmatrix(np.random.uniform(size=(middleLayerDimensions[i-2], middleLayerDimensions[i-1])))
        self.wByLayer[len(middleLayerDimensions)+2-1] = np.asmatrix(np.random.uniform(size=(middleLayerDimensions[-1], outputLayerDimension))) #Weights for layer M

        self.bByLayer = {   #Biases for layer 1
            1: np.asmatrix(np.random.uniform(size=(1, middleLayerDimensions[0])))
        }
        for i in range(2, len(middleLayerDimensions) + 2 - 1): #Biases for layers 2 to (M-1)
            self.bByLayer[i] = np.asmatrix(np.random.uniform(size=(1, middleLayerDimensions[i-1])))
        self.bByLayer[len(middleLayerDimensions)+2-1] = np.asmatrix(np.random.uniform(size=(1, outputLayerDimension))) #Biases for layer M
        
        self.deltas[len(middleLayerDimensions)+1] = np.asmatrix(np.zeros(shape=(outputLayerDimension, 1)))

    def train(self, X, y, r=None, minError=1e-6, epochs=100000, adaptative=False):
        if r != None:
            self.r = r
        error = sys.maxsize
        ep = 0
        kA = 0
        kB = 0
        while error > minError and ep < epochs:
            # random.shuffle(X)
            for index in range(len(X)):
                O, h, V = self._forwardPropagate(X[index])
                # deltas = self._backPropagate(O, h, V, y[index])
                deltas = self._backPropagateNoPrime(O, h, V, y[index])
                self._updateWeights(deltas, V, h)
                # self._updateWeightsMomentum(deltas, self.deltas, V, h)
                # self.deltas = deltas
            ## Error part
            newError = 0
            for index in range(len(X)):
                newError += np.power((self.classify(X[index]) - y[index]), 2).mean()
            newError /= 2
            if adaptative:
                ## Adaptative Error
                if newError < error:
                    kA += 1
                    kB = 0
                elif newError > error:
                    kB += 1
                    kA = 0
                if kA >= self.K:
                    kA = 0
                    self.r += self.a
                if kB >= self.K:
                    kB = 0
                    self.r -= self.r * self.b
            error = newError
            ep += 1
        print('Number of epochs', ep, '\nError', error)

    def _updateWeightsMomentum(self, deltas, oldDeltas, V, h):
        for i in sorted(deltas.keys()):
            DeltaW = np.matmul(V[i-1].T, deltas[i].T  * self.r) + 0.9 * oldDeltas[i].T
            self.wByLayer[i] -= DeltaW
            self.bByLayer[i] -= (deltas[i].T * self.r + 0.9 * oldDeltas[i].T)

    def _updateWeights(self, deltas, V, h):
        for i in sorted(deltas.keys()):
            DeltaW = np.matmul(V[i-1].T, deltas[i].T)
            self.wByLayer[i] -= DeltaW * self.r
            self.bByLayer[i] -= deltas[i].T * self.r

    def _backPropagate(self, Output, h, V, y):
        deltas = {}
        M = len(self.wByLayer.keys())
        deltas[M] = np.multiply(self.gPrime(h[M]), V[M] - y).T
        for jj in range(M-1, 0, -1):
            aux = np.matmul(self.wByLayer[jj+1], deltas[jj+1])
            prime = self.gPrime(h[jj]).T
            deltas[jj] = np.multiply(prime, aux)
        return deltas

    def _backPropagateNoPrime(self, Output, h, V, y):
        deltas = {}
        M = len(self.wByLayer.keys())
        deltas[M] = beta * (V[M] - y).T
        for jj in range(M-1, 0, -1):
            aux = np.matmul(self.wByLayer[jj+1], deltas[jj+1])
            deltas[jj] = beta * aux
        return deltas

    def _forwardPropagate(self, x):
        V = { 0: x }
        h = {}
        currV = x
        for layerNo in self.wByLayer.keys():
            h[layerNo] = np.matmul(currV, self.wByLayer[layerNo])
            h[layerNo] += self.bByLayer[layerNo]
            V[layerNo] = self.g(h[layerNo])
            currV = V[layerNo]
        return currV, h, V

    def forwardPropagate(self, x):
        O, _, _ = self._forwardPropagate(x)
        return O
    
    def classify(self, x):
        currV = x
        out = x
        for layerNo in self.wByLayer.keys():
            out = self.g(np.matmul(out, self.wByLayer[layerNo]) + self.bByLayer[layerNo])
        return out