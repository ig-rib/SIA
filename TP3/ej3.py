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

X = list(numbers.values())
y = [ 1 if index == 2 or index == 3 or index == 5 or index == 7 else -1 for index, x in enumerate(X) ]

mlp = MultiLayerPerceptron(0.1, tanh, tanhPrime, 35, [16, 16], 1,  a=1e-7, b=1e-4)
mlp.train(X, y, adaptative=False)

for i in range(len(X)):
    print(mlp.classify(X[i]), y[i])

