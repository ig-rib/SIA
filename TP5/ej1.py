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

nComp = 24
latRows = 6
latCols = 4

# 1) Pasar a 2d: Se convierten los enteros a arrays de bits (quedan ejemplos de 7x8, que se pasan a 56x1 para el autoencoder)
font1m = np.asmatrix(np.array(ct.font1b))
# 2) Optimizaciones: sacar el término g'
mlp1 = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 56, [nComp], 56, backProp=ct.BP_NO_PRIME)
numberOfLayers = len(mlp1.wByLayer.keys())
mlp1.train(font1m, font1m, epochs=2500)

# 3)
for i in range(font1m.shape[0]):
    # print(mlp.getLayerOutput(font1m[i], 1))
    printNumber(font1m[i].reshape(7, 8))
    print()
    printNumber(mlp1.getLayerOutput(font1m[i], numberOfLayers//2).reshape(latRows,latCols))
    print()
    # printNumber(mlp1.getLayerOutput(font1m[i], 2).reshape(7, 8))
    print()
    print()

# 4)
print("\nNuevas muestras generadas\n")
import random as rd
lat1 = np.asmatrix(np.array([1 if rd.random() > 0.5 else -1 for i in range(nComp)]))

lat1Out = mlp1.forwardPropagateFromLayer(lat1, numberOfLayers//2+1)
printNumber(lat1.reshape(latRows,latCols))
print()
printNumber(lat1Out.reshape(7,8))

######
# b)
######

# 1) Se define arriba. No hay una justifición formal para la elección, es heurística
#   Agregar capas intermedias no parece hacer una gran diferencia en los resultados,
#   sólo (naturalmente) aumenta el tiempo de ejecución

def addNoiseEverywhere(letter, rate):
    out = letter
    indices = rd.sample(list(range(letter.shape[1])), int((letter.shape[1] - 1)*rate))
    for index in indices:
        out[0, index] = - out.item((0, index))
    return out

# 2)

# Ruido 5%
font1m5 = [addNoiseEverywhere(letter, 0.05) for letter in deepcopy(font1m)]
# Ruido 15%
font1m15 = [addNoiseEverywhere(letter, 0.15) for letter in deepcopy(font1m)]
# Ruido 25%
font1m25 = [addNoiseEverywhere(letter, 0.25) for letter in deepcopy(font1m)]

noisySamples = {0.05: font1m5, 0.15: font1m15, 0.25: font1m25}

## Utility function for plotting input-output given sample noise
def plotForPercentage(r):
    for i in range(font1m.shape[0]):
        # print(mlp.getLayerOutput(font1m[i], 1))
        print('Original input')
        printNumber(font1m[i].reshape(7, 8))
        print()
        print(f'Noisy input {r}:')
        printNumber(noisySamples[r][i].reshape(7, 8))
        print()
        # printNumber(mlp1.getLayerOutput(font1m[i], 1).reshape(latRows,latCols))
        print('Autoencoder output')
        printNumber(mlp1.getLayerOutput(font1m[i], numberOfLayers).reshape(7, 8))
        print()
        print()

for r in noisySamples.keys():
    plotForPercentage(r)