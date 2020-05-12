#!/bin/python3
from stepPerceptron import SimpleStepPerceptron
from perceptron import Perceptron, SimpleNonLinearPerceptron
import sigmoidFunctionFactory as sff

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
    for x in functionVector:
        print('\t', x[0], perceptron.classify(x[0]), f'(valor real es {x[1]})')
        worked = worked and perceptron.classify(x[0]) == x[1]
    print(f'w = {perceptron.w}')
    print('OK') if worked else print('Not OK')
    
print('Función AND...\nResultados: ')
printResults(AndX, andSimplePer)
print('\n\nFunción XOR...\nResultados: ')
printResults(XorX, xorSimplePer)
print('\n\nFunción OR...\nResultados: ')
printResults(OrX, orSimplePer)
