#!/bin/python3

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import math
import numpy as np
from kohonenNet import KohonenNetwork, Coord
from collections import namedtuple

_data = pd.read_csv('data/europe.csv')
scaler = StandardScaler()
numericHeaders = [c for c in _data.columns if c != 'Country']
data = pd.DataFrame(scaler.fit_transform(_data[numericHeaders]), index=_data.index, columns=numericHeaders)
fullNormalizedData = pd.DataFrame(_data['Country']).join(data)
justPlainNumbers = _data[numericHeaders]
headers = list(_data.columns)
D = data.values

####################################
## PART 1 - Kohonen
####################################


################################################
# TODO PROBAR CON DISTINTOS VALORES DE SIDE, R #
# Y CANT. DE ITERACIONES                       #
##########3#####################################
side = 8

numberOfNeurons = int(side ** 2)
weightsVectorLength = len(headers)-1

kn = KohonenNetwork(weightsVectorLength, numberOfNeurons)
kn.train(D, 5000, R=8)

map = {}

for index in range(len(D)):
    countryClass = kn.getClass(D[index])
    if map.get(countryClass) == None:
        map[countryClass] = []
    map[countryClass].append(_data['Country'][index][0:3])
    # print('Class: ', kn.getClass(D[index]), _data['Country'][index])

print(map)

for i in range(side):
    for j in range(side):
        if map.get(Coord(x=i, y=j)) == None:
            print(['---'], end='\t\t')
        else:
            print(map[Coord(x=i, y=j)], end='')
            if len(map[Coord(x=i, y=j)]) <= 3:
                for ii in range(3-len(map[Coord(x=i, y=j)])):
                    print('\t', end='')
        print(' | ', end='')
    print()