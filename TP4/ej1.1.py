#!/bin/python3

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import math
import numpy as np
from kohonenNet import KohonenNetwork

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

numberOfNeurons = int(4)
weightsVectorLength = len(headers)-1

kn = KohonenNetwork(weightsVectorLength, numberOfNeurons)
kn.train(D, 1000)

for index in range(len(D)):
    print('Class: ', kn.getClass(D[index]), _data['Country'][index])
