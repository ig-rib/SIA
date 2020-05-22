#!/bin/python3

import numpy as np

class HopfieldNetwork:

    def store(self, examples):
        X = np.asmatrix(examples)
        auxW = [[ 1 / X.shape[1] * sum([X.item(k, i)*X.item(k, j) for k in range(X.shape[0])]) if i != j else 0 for i in range(X.shape[1]) ] for j in range(X.shape[1])]
        self.w = np.asmatrix(auxW).reshape(X.shape[1], X.shape[1])
        self.w

    def recognize(self, x, iterations=1000):
        # S = np.asmatrix(np.tile(x, self.w.shape[0])).reshape(self.w.shape[1], self.w.shape[1])
        # for it in iterations:
        #     S = np.sign(np.dot(self.w, S))
        S = np.asmatrix(x)
        oldS = np.zeros(x.shape[1])
        while (S-oldS).any() != 0:
            oldS = S
            S = np.sign(np.dot(S, self.w))
        return S