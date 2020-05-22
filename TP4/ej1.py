#!/bin/python3

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import math
import numpy as np
from kohonenNet import KohonenNetwork
from ojasRule import OjasRuleNeuron

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

# numberOfNeurons = int(10)
# weightsVectorLength = len(headers)-1

# kn = KohonenNetwork(weightsVectorLength, numberOfNeurons)
# kn.train(D, 10000)

# for index in range(len(D)):
#     print('Class: ', kn.getClass(D[index]), _data['Country'][index])

####################################
## PART 2 - PCA with Oja's Rule
####################################

# Centering numbers around zero
nullCenteredPlainNumbers = justPlainNumbers - justPlainNumbers.mean()
neu = OjasRuleNeuron(D.shape[1])
neu.r = 1e-3
neu.train(D, 10000)
print(neu.w)

pca = PCA()
pca.fit(D)
print(pca.components_[0])