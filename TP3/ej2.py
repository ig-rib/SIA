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

setFile = open('ej2Conjunto.tsv')

X = [ [(y[0], y[1], y[2]), y[3]] for y in [ [float(x) for x in line.rstrip().split('\t')] for line in setFile.readlines() ]]
sumOfAllYs = max(x[1] for x in X)
X[:] = [ [x[0], x[1]/sumOfAllYs] for x in X]
percentage = 0.50
random.shuffle(X)
splittingIndex = int(len(X)*percentage)
trainingX = X[:splittingIndex]
testX = X[splittingIndex:]

## Getting the functions and their derivatives
sff1 = sff.SigmoidFunctionFactory(0.5)
tanhFunc, tanhPrime = sff1.getFunctionAndDerivative(sff.tanh)
logisticFunc, logisticPrime = sff1.getFunctionAndDerivative(sff.logistic)

## Instantiating non-linear perceptrons
tanhSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.5, tanhFunc, tanhPrime, w0 = 0.8)
logisticSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.5, logisticFunc, logisticPrime, w0 = 0.8)

# tanhSNLP.train(trainingX, minError=0.1, epochs=1000)
logisticSNLP.train(trainingX, minError=0.1, epochs=1000)

# printResults(testX, tanhSNLP)
printResults(testX, logisticSNLP)