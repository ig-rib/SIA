#!/bin/python3

import numpy as np

class HopfieldNetwork:

    def store(self, examples):
        X = np.asmatrix(examples)
        auxW = [[ (1 / X.shape[1]) * sum([X.item(k, i)*X.item(k, j) for k in range(X.shape[0])]) if i != j else 0 for j in range(X.shape[1]) ] for i in range(X.shape[1])]
        aaux = np.asmatrix(auxW).reshape(X.shape[1], X.shape[1])
        self.w = (1 / X.shape[1]) * np.matmul(X.T, X) - np.eye(X.shape[1])
        self.w = aaux

    def recognize(self, x, iterations=1000):
        # S = np.asmatrix(np.tile(x, self.w.shape[0])).reshape(self.w.shape[1], self.w.shape[1])
        # for it in iterations:
        #     S = np.sign(np.dot(self.w, S))
        S = np.asmatrix(x).T
        oldS = np.asmatrix(np.zeros(S.shape[1])).T
        history = []
        it = 0
        # for i in range(iterations):
        while (oldS - S).any() != 0 and it < iterations:
        # while it < iterations:
            oldS = S
            history.append(oldS)
            S = np.sign(np.matmul(self.w, S))
            it+=1
        return S, history