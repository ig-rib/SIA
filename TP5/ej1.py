#!/bin/python3

import numpy as np
import multiLayerPerceptron as MLP
import constants as ct
from sklearn.decomposition import PCA


setFileLines = open('TP3/ej3Conjunto.tsv').readlines()

def printNumber(numMatrix):
    for i in range(numMatrix.shape[0]):
        for j in range(numMatrix.shape[1]):
            print('%.0g' % (numMatrix.item((i, j))) if numMatrix.item((i, j)) == 1 else ' ', end='')
        print()

numbers = {}

for i in range(10):
    currNumber = []
    for j in range(7):
        currNumber.append(list(map(float, setFileLines[i*7+j].rstrip().split(' '))))
    numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

X = np.asmatrix(np.array(list(numbers.values())))
Y = np.asmatrix(np.array(list(numbers.values())))

nComp = 10

pca = PCA()
pca.fit(X)
PCs = np.asmatrix(pca.components_[:nComp])
asPCs = X * PCs
mlp = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 35, [nComp], 35, backProp=ct.BP_NO_PRIME)
mlp.train(X, Y, epochs=5000)
for i in range(X.shape[0]):
    print(mlp.getLayerOutput(X[i], 1))
mlp