from ojasRule import OjasRuleNeuron
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import numpy as np

_data = pd.read_csv('data/europe.csv')
scaler = StandardScaler()
numericHeaders = [c for c in _data.columns if c != 'Country']
data = pd.DataFrame(scaler.fit_transform(_data[numericHeaders]), index=_data.index, columns=numericHeaders)
fullNormalizedData = pd.DataFrame(_data['Country']).join(data)
justPlainNumbers = _data[numericHeaders]
headers = list(_data.columns)
D = data.values

####################################
## PART 2 - PCA with Oja's Rule
####################################

# Centering numbers around zero
nullCenteredPlainNumbers = justPlainNumbers - justPlainNumbers.mean()
neu = OjasRuleNeuron(D.shape[1])
neu.r = 1e-3
neu.train(D, 5000)
print(neu.w)

pca = PCA()
pca.fit(D)
print(pca.components_[0])
firstPC = np.asmatrix(D)*np.asmatrix(pca.components_[0]).T
fullDataW1PC = pd.concat([fullNormalizedData, pd.DataFrame(firstPC)], axis=1)
fullDataW1PC.rename({0:'Poverty'}, axis=1, inplace=True)
print(fullDataW1PC.sort_values('Poverty'))