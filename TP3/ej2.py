from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def printResults(functionVector, perceptron, scaler):
    worked = True
    correct = 0
    error = 0
    for x in functionVector:
        pred = perceptron.classify(x[0])
        error += (pred - x[1])**2
        originalVector = [ x[0][i] * scaler.data_range_[i] + scaler.data_min_[i] for i in range(3) ]
        print('\t', '%.4g %.4g %.4g: %.4g' % (*originalVector, pred * scaler.data_range_[3] + scaler.data_min_[3]), '%.4g' % (x[1] * scaler.data_range_[3] + scaler.data_min_[3]))
        worked = worked and pred == x[1]
        correct += 1 if pred == x[1] else 0
    print(error/2)
    print(f'w = {perceptron.w}')


setFile = open('ej2Conjunto.tsv')
scaler = MinMaxScaler()
data = pd.read_csv('ej2Conjunto.tsv', sep='\t')
data1 = pd.DataFrame(scaler.fit_transform(data), index=data.index, columns=data.columns)
data1 = data1.values
data1

w0 = -0.1
X = [ [(y[0], y[1], y[2]), y[3]] for y in data1]
percentage = 0.7
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
logisticSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.05, logisticFunc, logisticPrime, w0 = w0)

# tanhSNLP.train(trainingX, minError=0.1, epochs=1000)
logisticSNLP.train(trainingX)

# printResults(testX, tanhSNLP)
printResults(trainingX, logisticSNLP, scaler)
printResults(testX, logisticSNLP, scaler)
# printResults(trainingX, tanhSNLP)
# printResults(testX, tanhSNLP)