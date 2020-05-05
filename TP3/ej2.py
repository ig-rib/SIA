from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np

def printResults(functionVector, perceptron):
    worked = True
    correct = 0
    for x in functionVector:
        pred = perceptron.classify(x[0])
        print('\t', x[0], pred, f'(valor real es {x[1]})')
        worked = worked and pred == x[1]
        correct += 1 if pred == x[1] else 0
    print(f'w = {perceptron.w}')
    print('OK') if worked else print('Not OK', correct / len(functionVector))


setFile = open('ej2Conjunto.tsv')

w0 = -0.1
X = [ [(y[0], y[1], y[2]), y[3]] for y in [ [float(x) for x in line.rstrip().split('\t')] for line in setFile.readlines() ]]
maxY = max(x[1] for x in X)
X[:] = [ [x[0], x[1]/maxY] for x in X]
percentage = 0.5
random.shuffle(X)
splittingIndex = int(len(X)*percentage)
trainingX = X[:splittingIndex]
testX = X[splittingIndex:]

## Getting the functions and their derivatives
sff1 = sff.SigmoidFunctionFactory(0.5)
tanhFunc, tanhPrime = sff1.getFunctionAndDerivative(sff.tanh)
logisticFunc, logisticPrime = sff1.getFunctionAndDerivative(sff.logistic)

## Instantiating non-linear perceptrons
tanhSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.1, tanhFunc, tanhPrime, w0 = w0)
logisticSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.01, logisticFunc, logisticPrime, w0 = w0)

# tanhSNLP.train(trainingX, minError=0.1, epochs=1000)
logisticSNLP.train(trainingX, minError=0.1, epochs=1000)

# printResults(testX, tanhSNLP)
printResults(trainingX, logisticSNLP)
printResults(testX, logisticSNLP)