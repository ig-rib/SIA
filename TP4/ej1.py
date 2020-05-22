#!/bin/python3

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import math
import numpy as np
from kohonenNet import KohonenNetwork

_data = pd.read_csv('TP4/data/europe.csv')
scaler = MinMaxScaler()
numericHeaders = [c for c in _data.columns if c != 'Country']
data = pd.DataFrame(scaler.fit_transform(_data[numericHeaders]), index=_data.index, columns=numericHeaders)
_data = pd.DataFrame(_data['Country']).join(data)

headers = list(_data.columns)
D = data.values

numberOfNeurons = int(1*math.sqrt(len(D)))
weightsVectorLength = len(headers)-1

kn = KohonenNetwork(weightsVectorLength, numberOfNeurons)
kn.train(D, 100)

for index in range(len(D)):
    print('Class: ', kn.getClass(D[index]), _data['Country'][index])