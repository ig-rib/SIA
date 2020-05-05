#!/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt

tanh = 'TANH'
logistic = 'LOGISTIC'

class SigmoidFunctionFactory:

    def __init__(self, beta):
        self.beta = beta

    def getFunctionAndDerivative(self, funcType):
        if funcType == tanh:
            def g(x):
                return math.tanh(self.beta * x)
            def gPrime(x):
                return g(x) * (1-g(x))
        elif funcType == logistic:
            def g(x):
                return 1 / (1 + math.exp(-2*self.beta*x))
            def gPrime(x):
                expPart = math.exp(-2*self.beta*x)
                return 2*self.beta*expPart / (1+expPart) ** 2
        return g, gPrime

# Testeos OK

# sff = SigmoidFunctionFactory(0.5)
# tanhFunc, tanhPrime = sff.getFunctionAndDerivative(tanh)
# logisticFunc, logisticPrime = sff.getFunctionAndDerivative(logistic)


# X = np.linspace(-5, 5, 500)

# plt.figure(1)
# plt.plot(X, [ tanhFunc(x) for x in X ])
# plt.plot(X, [logisticFunc(x) for x in X ])
# plt.figure(2)
# plt.plot(X, [ tanhPrime(x) for x in X ])
# plt.plot(X, [logisticPrime(x) for x in X ])
# plt.show()