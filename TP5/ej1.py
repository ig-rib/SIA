#!/bin/python3

import numpy as np
import multiLayerPerceptron as MLP
import constants as ct
from sklearn.decomposition import PCA
from copy import deepcopy


setFileLines = open('TP3/ej3Conjunto.tsv').readlines()

def printNumber(numMatrix):
    for i in range(numMatrix.shape[0]):
        for j in range(numMatrix.shape[1]):
            print('%.0g' % 1 if numMatrix.item((i, j)) > 0.5 else '_', end='') #(numMatrix.item((i, j)))
        print()

# numbers = {}

# for i in range(10):
#     currNumber = []
#     for j in range(7):
#         currNumber.append(list(map(float, setFileLines[i*7+j].rstrip().split(' '))))
#     numbers[i] = np.asmatrix(currNumber).reshape(1, 35)

# X = np.asmatrix(np.array(list(numbers.values())))
# Y = np.asmatrix(np.array(list(numbers.values())))

nComp = 12

# pca = PCA()
# pca.fit(X)
# PCs = np.asmatrix(pca.components_[:nComp])
# asPCs = X * PCs
# mlp = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 35, [nComp], 35, backProp=ct.BP_NO_PRIME)
# mlp.train(X, Y, epochs=5000)
# for i in range(X.shape[0]):
#     # print(mlp.getLayerOutput(X[i], 1))
#     printNumber(numbers[i].reshape(7, 5))
#     print()
#     printNumber(mlp.getLayerOutput(X[i], 1).reshape(4,3))
#     print()
#     printNumber(mlp.getLayerOutput(X[i], 2).reshape(7, 5))

# a) Pasar a 2d: Se convierten los enteros a arrays de bits (quedan ejemplos de 7x8, que se pasan a 56x1 para el autoencoder)
font1m = np.asmatrix(np.array(ct.font1b))
# b) Optimizaciones: sacar el término g'
mlp1 = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 56, [24, nComp, 24], 56, backProp=ct.BP_NO_PRIME)
numberOfLayers = 5
mlp1.train(font1m, font1m, epochs=2500)

for i in range(font1m.shape[0]):
    # print(mlp.getLayerOutput(font1m[i], 1))
    printNumber(font1m[i].reshape(7, 8))
    print()
    printNumber(mlp1.getLayerOutput(font1m[i], numberOfLayers//2).reshape(4,3))
    print()
    # printNumber(mlp1.getLayerOutput(font1m[i], 2).reshape(7, 8))
    print()
    print()

print("\nNuevas muestras generadas\n")
import random as rd
lat1 = np.asmatrix(np.array([1 if rd.random() > 0.5 else -1 for i in range(nComp)]))

lat1Out = mlp1.forwardPropagateFromLayer(lat1, numberOfLayers//2+1)
printNumber(lat1.reshape(4,3))
print()
printNumber(lat1Out.reshape(7,8))

######
# b)
######


def addNoiseEverywhere(letter, rate):
    out = letter
    indices = rd.sample(list(range(letter.shape[1])), int((letter.shape[1] - 1)*rate))
    for index in indices:
        out[0, index] = - out.item((0, index))
    return out

font1mcopy = [addNoiseEverywhere(letter, 0.05) for letter in font1m]
font1mcopy

for i in range(font1m.shape[0]):
    # print(mlp.getLayerOutput(font1m[i], 1))
    printNumber(font1mcopy[i].reshape(7, 8))
    print()
    # printNumber(mlp1.getLayerOutput(font1m[i], 1).reshape(4,3))
    print()
    printNumber(mlp1.getLayerOutput(font1m[i], numberOfLayers-1).reshape(7, 8))
    print()
    print()