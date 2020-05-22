#!/bin/python3

import numpy as np

class OjasRuleNeuron():

    def __init__(self, vectorLength, r=0.01):
        self.w = np.asmatrix(np.random.random(size=(1, vectorLength)))
        self.w /= np.linalg.norm(self.w)
        self.r = r

    def train(self, X, iterations):
        r = self.r
        for it in range(iterations):
            wOld = self.w
            for elemNo in range(X.shape[0]):
                y = np.dot(self.w, X[elemNo].T)
                self.w = self.w + r * y * (X[elemNo] - y * self.w)
            if np.abs(wOld - self.w).all() <= r*100:
                r /= 100