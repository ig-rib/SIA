#!/bin/python3

from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np
import sys
from multiLayerPerceptron import MultiLayerPerceptron, tanh, tanhPrime, logistic, logisticPrime
import constants as ct

setFileLines = open('ej3Conjunto.tsv').readlines()

numbers = {}

for i in range(10):
    currNumber = []
    for j in range(7):
        currNumber.append(list(map(float, setFileLines[i*7+j].rstrip().split(' '))))
    numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

X = list(numbers.values())
y = [ 1 if index == 2 or index == 3 or index == 5 or index == 7 else -1 for index, x in enumerate(X) ]
# y = [ np.asmatrix([1 if i % 2 == 0 else -1 for i in range(10)])
#     if index == 2 or index == 3 or index == 5 or index == 7
#     else np.asmatrix([1 if i % 2 == 1 else -1 for i in range(10)]) for index, x in enumerate(X) ]

mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 35, [25, 20, 15, 10, 4, 2], 1,  a=1e-7, b=1e-4, backProp=ct.BP_NO_PRIME)
mlp.train(X, y, minError=1e-4, adaptative=True)

for i in range(len(X)):
    print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#
# XOR FUNCTION
#

domain = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
XORys = [ -1 if x[0] == x[1] else 1 for x in domain ]
domain[:] = [ np.asmatrix(x) for x in domain ]

mlp = MultiLayerPerceptron(0.001, tanh, tanhPrime, 2, [10, 4, 2], 1,  a=1e-7, b=1e-4, backProp=ct.BP_NO_PRIME)
mlp.train(domain, XORys, minError=1e-3, adaptative=True)

for i in range(len(domain)):
    print(mlp.classify(domain[i]), XORys[i])

#-----------------------------------------------------#
# LEER CADA LINEA DEL CONJUNTO CARACTERIZANDOLA SEGUN EL ULTIMO BIT
#
# setFile = open('ej3Conjunto.tsv')

# X = [ [np.asmatrix([y[0], y[1], y[2], y[3]]), y[4]] for y in [ [float(x) for x in line.rstrip().split(' ')] for line in setFile.readlines()[:26] ]]

# setFile.close()
# percentage = 0.50
# random.shuffle(X)
# splittingIndex = int(len(X)*percentage)
# trainingX = X[:splittingIndex]
# testX = X[splittingIndex:]

# tX = [ x[0] for x in trainingX ]
# tY = [ x[1] for x in trainingX ]

# mlp = MultiLayerPerceptron(0.1, tanh, tanhPrime, 4, [4, 4, 4, 4, 4, 2], 1,  a=1e-7, b=1e-4)
# mlp.train(tX, tY, adaptative=True)
# for x in X:
#     print(mlp.classify(x[0]), x[1])

#-----------------------------------------------------#
# NUMEROS PRIMOS EXPRESADOS CON VECTORES DE 10
#

# X = [ np.asmatrix([ 1 if i == j else 0 for i in range(10) ]) for j in range(10) ]
# y = [ 1 if index == 2 or index == 3 or index == 5 or index == 7 else -1 for index, x in enumerate(X) ]

# mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 10, [10, 4, 2], 1,  a=1e-7, b=1e-4, backProp=ct.BP_NO_PRIME)
# mlp.train(X, y, adaptative=False)

# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#
# RECONOCE NUMEROS EXPRESADOS EN VECTORES DE 1X35, OUTPUTS DE 1X10? no
#

# numbers = {}

# for i in range(10):
#     currNumber = []
#     for j in range(7):
#         currNumber.append(list(map(float, setFileLines[j].rstrip().split(' '))))
#     numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

# X = list(numbers.values())
# y = [ np.asmatrix([ 1 if i == j else -1 for i in range(10) ]) for j in range(10) ]

# mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 35, [25, 15], 10,  a=1e-7, b=1e-4, update=ct.UPDATE_MOMENTUM)
# mlp.train(X, y, adaptative=True)

# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#
# RECONOCE NUMEROS EXPRESADOS EN VECTORES DE 1X35, OUTPUTS CON LA CADENA EN BINARIO?
#

# numbers = {}

# for i in range(10):
#     currNumber = []
#     for j in range(7):
#         currNumber.append(list(map(float, setFileLines[j].rstrip().split(' '))))
#     numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

# X = list(numbers.values())
# y = [   np.asmatrix([-1, -1, -1, -1]),
#         np.asmatrix([-1, -1, -1, 1]),
#         np.asmatrix([-1, -1, 1, -1]),
#         np.asmatrix([-1, -1, 1, 1]),
#         np.asmatrix([-1, 1, -1, -1]),
#         np.asmatrix([-1, 1, -1, 1]),
#         np.asmatrix([-1, 1, 1, -1]),
#         np.asmatrix([-1, 1, 1, 1]),
#         np.asmatrix([1, -1, -1, -1]),
#         np.asmatrix([1, -1, -1, 1])
#  ]

# mlp = MultiLayerPerceptron(0.1, tanh, tanhPrime, 35, [x for x in range(34, 4, -1)], 4,  a=1e-7, b=1e-4)
# mlp.train(X, y, epochs=10000000, adaptative=True)

# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])

#-----------------------------------------------------#
# RECONOCE NUMEROS EXPRESADOS EN VECTORES DE 1X10, OUTPUTS DE 1X10
#

# numbers = {}

# for i in range(10):
#     currNumber = []
#     for j in range(7):
#         currNumber.append(list(map(float, setFileLines[j].rstrip().split(' '))))
#     numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

# X = list(numbers.values())
# X = [ np.asmatrix([ 1 if i == j else -1 for i in range(10) ]) for j in range(10) ]
# y = [ np.asmatrix([ 1 if i == j else -1 for i in range(10) ]) for j in range(10) ]

# mlp = MultiLayerPerceptron(0.01, tanh, tanhPrime, 10, [35, 10], 10,  a=1e-7, b=1e-4, backProp=ct.BP_NO_PRIME)
# mlp.train(X, y, adaptative=True)

# for i in range(len(X)):
#     print(mlp.classify(X[i]), y[i])