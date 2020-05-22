#!/bin/python3

import numpy as np
import random

def alpha(s):
    return 1 / (s+1)

def theta1(i, j, s, R=None):
    return np.abs(i - j) / (s+1)

def theta(i, j, s, R=2):
    return 1 / (s+1) if np.abs(i-j) < R else 0

class KohonenNetwork:

    ## vectorDimension is the length of an input vector,
    ## which is the same as for weight vectors
    ## M is the number of nodes
    ## 
    def __init__(self, vectorDimension, M):
        self.vDim = vectorDimension
        self.M = M
        self.W = np.asmatrix(np.random.random(size=(M, vectorDimension)))

    def train(self, D, lda, R=4):

        for it in range(lda):
            curr = random.choice(D)
            distances = [ [np.linalg.norm(curr - x), i] for i, x in enumerate(self.W) ]
            minIndex = min(distances, key=lambda x: x[0])[1]
            for rowNo in range(self.W.shape[0]):
                self.W[rowNo] = self.W[rowNo] + theta1(minIndex, rowNo, it) * alpha(it) * (curr - self.W[rowNo])
            # R = 1 if R*0.99 < 1 else R*0.99
    
    def getClass(self, vector):
        distances = [ [np.linalg.norm(vector - x), i] for i, x in enumerate(self.W) ]
        return min(distances, key=lambda x: x[0])[1]