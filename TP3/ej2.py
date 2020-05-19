from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def printResults(functionVector, perceptron, scaler):
    worked = True
    correct = 0
    error = 0
    for x in functionVector:
        pred = perceptron.classify(x[0])
        error += (pred - x[1])**2
        originalVector = [ x[0][i] * scaler.data_range_[i] + scaler.data_min_[i] for i in range(3) ]
        print('\t', '%.4g\t%.4g\t%.4g:\t%.4g' % (*originalVector, pred * scaler.data_range_[3] + scaler.data_min_[3]), '(Actual: %.4g)' % (x[1] * scaler.data_range_[3] + scaler.data_min_[3]))
        worked = worked and pred == x[1]
        correct += 1 if pred == x[1] else 0
    print('Mean Square Error with normalized data:', error/len(functionVector))
    print(f'w = {perceptron.w}')
    return error/len(functionVector)


setFile = open('ej2Conjunto.tsv')
scaler = MinMaxScaler()
data = pd.read_csv('ej2Conjunto.tsv', sep='\t')
data1 = pd.DataFrame(scaler.fit_transform(data), index=data.index, columns=data.columns)
data1 = data1.values
data1

w0 = -0.1
X = [ [(y[0], y[1], y[2]), y[3]] for y in data1]
percentage = 0.7
random.shuffle(X)
splittingIndex = int(len(X)*percentage)
trainingX = X[:splittingIndex]
testX = X[splittingIndex:]

## Getting the functions and their derivatives
sff1 = sff.SigmoidFunctionFactory(0.5)
tanhFunc, tanhPrime = sff1.getFunctionAndDerivative(sff.tanh)
logisticFunc, logisticPrime = sff1.getFunctionAndDerivative(sff.logistic)

## Instantiating non-linear perceptrons
tanhSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.1, tanhFunc, tanhPrime, w0 = w0)
logisticSNLP = SimpleNonLinearPerceptron(len(X[0][0]), 0.05, logisticFunc, logisticPrime, w0 = w0)

# tanhSNLP.train(trainingX, minError=0.1, epochs=1000)
logisticSNLP.train(trainingX, r=0.1, minError=5e-3)

# printResults(testX, tanhSNLP)
print('\n\n######################################\nRESULTS FOR TRAINING SET:\n######################################\n')
printResults(trainingX, logisticSNLP, scaler)
print('\n\n######################################\nRESULTS FOR TEST SET:\n######################################\n')
printResults(testX, logisticSNLP, scaler)
# printResults(trainingX, tanhSNLP)
# printResults(testX, tanhSNLP)

# errorVsEpochs = {}

# for r in [0.1, 0.05, 0.01]:
#     errorVsEpochs[r] = {'trainingError': [], 'testError': [], 'epochs': []}
#     for epochs in [10, 50, 500, 1000, 10000, 25000]:
#         logisticSNLP = SimpleNonLinearPerceptron(len(X[0][0]), r, logisticFunc, logisticPrime)
#         logisticSNLP.train(trainingX, minError=0.0, epochs=epochs)
#         print('R=', r, 'Epochs:', epochs)
#         print('Training Set')
#         trainingError = printResults(trainingX, logisticSNLP, scaler)
#         print('Test Set')
#         testError = printResults(testX, logisticSNLP, scaler)
#         errorVsEpochs[r]['trainingError'].append(trainingError)
#         errorVsEpochs[r]['testError'].append(testError)
#         errorVsEpochs[r]['epochs'].append(epochs)

# figNo = 1
# for r in [0.1, 0.05, 0.01]:
#     plt.figure(figNo)
#     plt.plot(errorVsEpochs[r]['epochs'], errorVsEpochs[r]['trainingError'], marker='o', linestyle='--')
#     plt.plot(errorVsEpochs[r]['epochs'], errorVsEpochs[r]['testError'], marker='o', linestyle='--')
#     plt.legend(['Training Error', 'Test Error'])
#     plt.xscale('log')
#     plt.xlabel('Epochs')
#     plt.ylabel('Mean Square Error')
#     plt.title(f'Learning Rate = {r}')
#     plt.savefig(f'MSEVsEpochs-r={r}.png')
#     figNo+=1
    # plt.show()