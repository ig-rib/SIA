#!/bin/python3
from stepPerceptron import SimpleStepPerceptron
from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff
import numpy as np
import matplotlib.pyplot as plt

andSimplePer = SimpleStepPerceptron(2, 0.5)
xorSimplePer = SimpleStepPerceptron(2, 0.5)
orSimplePer = SimpleStepPerceptron(2, 0.5, w0 = -0.1)
domain = [ (-1, 1), (1, -1), (-1, -1), (1, 1) ]

AndX = [ (x, min(x[0], x[1])) for x in domain ]
XorX = [ (x, -1 if x[0] == x[1] else 1) for x in domain ]
OrX = [ (x, max(x[0], x[1])) for x in domain ]

## Training with AND function
andSimplePer.train(AndX, 0.5, 0.0)
xorSimplePer.train(XorX, 0.5, 0.0)
orSimplePer.train(OrX, 0.5, 0.0)
def printResults(functionVector, perceptron):
    worked = True
    print(f'\tDomain\t\tPredicted\tActual')
    for x in functionVector:
        print('\t', x[0], '\t', perceptron.classify(x[0]), '\t\t', f'{x[1]}')
        worked = worked and perceptron.classify(x[0]) == x[1]
    print(f'w = {perceptron.w}')
    print('OK') if worked else print('Not OK')

def plotLine(perceptron, functionVector, title):
    x = np.linspace(-3, 3, 100)
    slope = -perceptron.w[1]/perceptron.w[2]
    intercept = perceptron.w[0]/perceptron.w[2]
    y = [ xi*slope + intercept for xi in x ]
    plt.plot(x, y)
    plusOne = [ x[0] for x in functionVector if x[1] == 1 ]
    minusOne = [ x[0] for x in functionVector if x[1] == -1 ]
    plt.scatter([r[0] for r in plusOne], [r[1] for r in plusOne], color='blue')
    plt.scatter([r[0] for r in minusOne], [r[1] for r in minusOne], color='red')
    plt.ylim(-3, 3)
    plt.xlim(-3, 3)
    plt.title(title)
    plt.savefig(f'{title}.png')
    plt.show()
    print(f'{slope}*x + {intercept}')


print('AND Function...\nResults: ')
printResults(AndX, andSimplePer)
plotLine(andSimplePer, AndX, 'AND')
print('\n\nXOR Function...\nResults: ')
printResults(XorX, xorSimplePer)
plotLine(xorSimplePer, XorX, 'XOR')
print('\n\nOR Function...\nResults: ')
printResults(OrX, orSimplePer)
plotLine(orSimplePer, OrX, 'OR')
