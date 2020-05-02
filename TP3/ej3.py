#!/bin/python3

from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random

def printResults(functionVector, perceptron):
    worked = True
    for x in functionVector:
        print('\t', x[0], perceptron.classify(x[0]), f'(valor real es {x[1]})')
        worked = worked and perceptron.classify(x[0]) == x[1]
    print(f'w = {perceptron.w}')
    print('OK') if worked else print('Not OK')

setFile = open('ej3Conjunto.tsv')

X = [ [(y[0], y[1], y[2], y[3]), y[4]] for y in [ [float(x) for x in line.rstrip().split(' ')] for line in setFile.readlines() ]]

sumOfAllYs = max(x[1] for x in X)
X[:] = [ [x[0], x[1]/sumOfAllYs] for x in X]
percentage = 0.50
random.shuffle(X)
splittingIndex = int(len(X)*percentage)
trainingX = X[:splittingIndex]
testX = X[splittingIndex:]

