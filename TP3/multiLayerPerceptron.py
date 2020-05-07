#!/bin/python3

import numpy as np
from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import sys
from collections import deque


def tanh(x):
    return np.tanh(x)
def tanhPrime(x):
    return 1 - np.power(tanh(x), 2)

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
    def __init__(self, r, g, gPrime, inputDimension=2, middleLayerDimensions=[4,5], outputLayerDimension=1):
        self.r = r
        self.g = g
        self.gPrime = gPrime

        #Weights for layer 1
        self.wByLayer = {
            1: np.asmatrix(np.random.uniform(size=(inputDimension, middleLayerDimensions[0])))
        }
        #Weights for layers 2 to (M-1)
        for i in range(2, len(middleLayerDimensions) + 1):
            self.wByLayer[i] = np.asmatrix(np.random.uniform(size=(middleLayerDimensions[i-2], middleLayerDimensions[i-1])))
        #Weights for layer M
        self.wByLayer[len(middleLayerDimensions)+2-1] = np.asmatrix(np.random.uniform(size=(middleLayerDimensions[-1], outputLayerDimension)))

        #Biases for layer 1
        self.bByLayer = {
            1: np.asmatrix(np.random.uniform(size=(1, middleLayerDimensions[0])))
        }
        #Biases for layers 2 to (M-1)
        for i in range(2, len(middleLayerDimensions) + 2 - 1):
            self.bByLayer[i] = np.asmatrix(np.random.uniform(size=(1, middleLayerDimensions[i-1])))
        #Biases for layer M
        self.bByLayer[len(middleLayerDimensions)+2-1] = np.asmatrix(np.random.uniform(size=(1, outputLayerDimension)))

    def train(self, X, y, r=None, minError=1e-3, epochs=1000):
        if r != None:
            self.r = r
        error = [sys.maxsize]
        ep = 0

        while error[0] > minError and ep < epochs:
            for index in range(len(X)):
                O, h, V = self._forwardPropagate(X[index])
                deltas = self._backPropagate(O, h, V, y[index])
                self._updateWeights(deltas, V, h)
            error = 0
            for index in range(len(X)):
                error += (self.classify(X[index]) - y[index]) ** 2
            error /= 2

    def _updateWeights(self, deltas, V, h):
        for i in sorted(deltas.keys()):
            DeltaW = np.matmul(V[i-1].T, deltas[i].T)
            self.wByLayer[i] -= DeltaW * self.r
            self.bByLayer[i] -= deltas[i].T * self.r

    def _backPropagate(self, Output, h, V, y):
        deltas = {}
        M = len(self.wByLayer.keys())
        deltas[M] = np.multiply(self.gPrime(h[M]), V[M] - y)
        for jj in range(M-1, 0, -1):
            aux = np.matmul(self.wByLayer[jj+1], deltas[jj+1])
            prime = self.gPrime(h[jj]).T
            deltas[jj] = np.multiply(prime, aux)
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

mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 2, [4, 3, 4], 1)
D = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
ys = [-1 if x[0] == x[1] else 1 for x in D]
# ys = [ min(x) for x in D ]
D[:] = [ np.matrix(d) for d in D ]
for d in D:
    print(mlp.forwardPropagate(d))

mlp.train(D, ys, 0.01, epochs=sys.maxsize)

for j in range(len(D)):
    print(mlp.forwardPropagate(D[j]), ys[j])
