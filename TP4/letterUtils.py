#!/bin/python3

import numpy as np
import random as rd

def addNoiseAround(letter, rate):
    out = letter
    minusOnes = [index for index, x in enumerate(letter[0]) if x == -1]
    indices = rd.sample(minusOnes, int((len(minusOnes) - 1)*rate))
    out = np.asmatrix([ 1 if index in indices and x == -1 else x for index, x in enumerate(letter[0])])
    return out

def addNoiseEverywhere(letter, rate):
    out = letter
    indices = rd.sample(list(range(letter.shape[1])), int((letter.shape[1] - 1)*rate))
    out = np.asmatrix([ -x if index in indices else x for index, x in enumerate(letter[0])])
    return out

def printLetter(letter, plottableSymbol=1):
    for i in range(letter.shape[0]):
        for j in range(letter.shape[1]):
            if letter.item(i, j) == plottableSymbol:
                print(1, end='')
            else:
                print(' ', end='')
        print()

def printLetters(letters, shape=(5, 5), plottableSymbol=1):
    for letter in letters:
        printLetter(letter.reshape(*shape), plottableSymbol)
        print()