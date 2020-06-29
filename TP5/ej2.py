#!/bin/python3

import constants as ct
import random as rd
import numpy as np
import multiLayerPerceptron as MLP
from utils import printNumber

# percentage of the set to consider for learning
lp = .3
# number of elements in feature space
nComp = 24
# number of rows to represent elements from feature space
latRows = 6
# number of columns to represent elements from feature space 
latCols = 4

font2m = np.asmatrix(np.array(rd.sample(ct.font2b, int(len(ct.font2b)*lp))))
mlp1 = MLP.MultiLayerPerceptron(0.01, MLP.tanh, MLP.tanhPrime, 56, [nComp], 56, backProp=ct.BP_NO_PRIME)
numberOfLayers = len(mlp1.wByLayer.keys())
mlp1.train(font2m, font2m, epochs=2500)

print("\nGenerated samples\n")
for i in range(len(font2m)):
    lat1 = np.asmatrix(np.array([rd.random() * 2 -1 for i in range(nComp)]))

    lat1Out = mlp1.forwardPropagateFromLayer(lat1, numberOfLayers//2+1)
    print('In feature space (actual array)')
    print(lat1)
    print()
    print('In feature space (binary representation)')
    printNumber(lat1.reshape(latRows,latCols))
    print()
    print('Output (generated sample)')
    printNumber(lat1Out.reshape(7,8))
    print('\n\n')