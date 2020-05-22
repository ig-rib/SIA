from ojasRule import OjasRuleNeuron
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd


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
neu.train(D, 10000)
print(neu.w)

pca = PCA()
pca.fit(D)
print(pca.components_[0])