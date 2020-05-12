#!/bin/python3

from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np
import sys
from multiLayerPerceptron import MultiLayerPerceptron, tanh, tanhPrime, logistic, logisticPrime

setFileLines = open('ej3Conjunto.tsv').readlines()

numbers = {}

for i in range(10):
    currNumber = []
    for j in range(7):
        currNumber.append(list(map(float, setFileLines[j].rstrip().split(' '))))
    numbers[i] = np.asmatrix(currNumber).reshape(1, 35) / 35

# X = list(numbers.values())
# y = [ 1 if index == 2 or index == 3 or index == 5 or index == 7 else -1 for index, x in enumerate(X) ]

# mlp = MultiLayerPerceptron(0.1, tanh, tanhPrime, 35, [4], 1,  a=1e-7, b=1e-4)
# mlp.train(X, y, adaptative=False)

# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#

# X = []
# for i in range(0, 10, 1):
#     X.append(np.asmatrix(i*0.1))
# y = [ 1 if index == 2 or index == 3 or index == 5 or index == 7 else -1 for index, x in enumerate(X) ]

# mlp = MultiLayerPerceptron(0.1, tanh, tanhPrime, 1, [5, 5, 5], 1,  a=1e-7, b=1e-4)
# mlp.train(X, y, epochs=sys.maxsize, adaptative=False)
# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#

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
mlp.train(tX, tY, epochs=50000, adaptative=True)
for x in X:
    print(mlp.classify(x[0]), x[1])