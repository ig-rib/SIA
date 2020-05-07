#!/bin/python3

from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np
import sys
from multiLayerPerceptron import MultiLayerPerceptron, tanh, tanhPrime

# def printResults(functionVector, perceptron):
#     worked = True
#     for x in functionVector:
#         print('\t', x[0], perceptron.classify(x[0]), f'(valor real es {x[1]})')
#         worked = worked and perceptron.classify(x[0]) == x[1]
#     print(f'w = {perceptron.w}')

# mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 2, [4, 2], 1,  a=1e-7, b=1e-4)
# D = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
# ys = [-1 if x[0] == x[1] else 1 for x in D]
# # ys = [ min(x) for x in D ]
# D[:] = [ np.matrix(d) for d in D ]
# for d in D:
#     print(mlp.forwardPropagate(d))

# # The working configuration
# mlp.train(D, ys, 0.1, minError= 1e-4, epochs=sys.maxsize, adaptative=False)

# for j in range(len(D)):
#     print(mlp.forwardPropagate(D[j]), ys[j])

setFile = open('ej3Conjunto.tsv')

X = [ [np.asmatrix([y[0], y[1], y[2], y[3]]), y[4]] for y in [ [float(x) for x in line.rstrip().split(' ')] for line in setFile.readlines() ]]

percentage = 0.50
random.shuffle(X)
splittingIndex = int(len(X)*percentage)
trainingX = X[:splittingIndex]
testX = X[splittingIndex:]

tX = [ x[0] for x in trainingX ]
tY = [ x[1] for x in trainingX ]

mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 4, [4, 2], 1,  a=1e-7, b=1e-4)
mlp.train(tX, tY)

for x in X:
    print(mlp.classify(x[0]), x[1])