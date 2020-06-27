#!/bin/python3

import numpy as np
import multiLayerPerceptron as MLP
import constants as ct
from copy import deepcopy
import random as rd
from utils import printNumber


setFileLines = open('TP3/ej3Conjunto.tsv').readlines()

# percentage of the set to consider for learning
lp = .25
# number of elements in feature space
nComp = 24
# number of rows to represent elements from feature space
latRows = 6
# number of columns to represent elements from feature space 
latCols = 4

# 1) Pasar a 2d: Se convierten los enteros a arrays de bits (quedan ejemplos de 7x8, que se pasan a 56x1 para el autoencoder)
font1m = np.asmatrix(np.array(rd.sample(ct.font1b, int(len(ct.font1b)*lp))))
# 2) Optimizaciones: sacar el término g'
mlp1 = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 56, [nComp], 56, backProp=ct.BP_NO_PRIME)
numberOfLayers = len(mlp1.wByLayer.keys())
mlp1.train(font1m, font1m, epochs=2500)

# 3)
for i in range(font1m.shape[0]):
    # print(mlp.getLayerOutput(font1m[i], 1))
    print('Original')
    printNumber(font1m[i].reshape(7, 8))
    print()
    print('In feature space (middle layer)')
    printNumber(mlp1.getLayerOutput(font1m[i], numberOfLayers//2).reshape(latRows,latCols))
    print()
    # printNumber(mlp1.getLayerOutput(font1m[i], 2).reshape(7, 8))
    print()
    print()

# 4)
print("\nGenerated samples\n")
for i in range(5):
    lat1 = np.asmatrix(np.array([1 if rd.random() > 0.5 else -1 for i in range(nComp)]))

    lat1Out = mlp1.forwardPropagateFromLayer(lat1, numberOfLayers//2+1)
    print('In feature space')
    printNumber(lat1.reshape(latRows,latCols))
    print()
    print('Output (generated sample)')
    printNumber(lat1Out.reshape(7,8))
    print('\n\n')

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

noisySamples = {
                r : [addNoiseEverywhere(letter, r) for letter in deepcopy(font1m)] for r in [.05, .15, .25]
                }

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
        printNumber(mlp1.getLayerOutput(noisySamples[r][i], numberOfLayers).reshape(7, 8))
        print()
        print()

for r in noisySamples.keys():
    plotForPercentage(r)