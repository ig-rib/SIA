#!/bin/python3

import numpy as np
import sys

class Perceptron:

    def __init__(self, dimension, r, w0 = 0.1):
        self.w = np.array(dimension * [0])
        self.w0 = w0
        self.r = r

    def train(self, trainingSet, r=0):
        print('Train unimplemented')

    def classify(self, vector):
        print('Classify unimplemented')


class SimpleNonLinearPerceptron(Perceptron):

    def __init__(self, dimension, r, g, gPrime, w0 = 0.1):
        super().__init__(dimension, r, w0)
        self.g = g
        self.gPrime = gPrime
        # self.w = np.random.random(dimension+1)
    
    def train(self, X, r = None, minError = 1e-3, epochs = 1000):
        if r != None:
            self.r = r
        error = sys.maxsize
        bestError = error
        i = 0
        actualYs = [ x[1] for x in X ]
        points = [ x[0] for x in X ]
        while error > minError and i < epochs:
            for x in X:
                excitation = np.dot(self.w, x[0])
                excitation += self.w0
                prime = self.gPrime(excitation)
                deltaW = (x[1] - self.g(excitation)) * prime * self.r * np.array(x[0])
                self.w = self.w + deltaW
            currentClassifications = [self.classify(y) for y in points]
            absSubtractions = [ np.abs(err) ** 2 for err in np.subtract(actualYs, currentClassifications) ]
            error = sum(absSubtractions) / 2
            if error < bestError:
                bestError = error
                self.bestW = self.w
            # print(self.bestW, self.w, error)
            i += 1
        self.w = self.bestW

    def classify(self, x):
        # return self.g(np.dot(self.w, x))
        return self.g(np.dot(self.w, x )+ self.w0)
