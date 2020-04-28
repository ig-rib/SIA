#!/bin/python3

from readers.configFileReader import ConfigFileReader
from solver import Solver
from geneticSelectors.eliteSelector import EliteSelector
import os
from domains import readDomains
import sys

if __name__ == '__main__':
    settings = ConfigFileReader('solver.config').getSettings()
    if len(sys.argv) == 3:
        testChar = sys.argv[1]
        charactersDir = sys.argv[2] + '/'
    else:
        testChar = settings['CLASS']
        charactersDir = 'characters.test/'
    # characters = GenerationZeroReader(equipmentFiles, charClass).generateCharacters()
    domains = readDomains(charactersDir)
    # domains = readDomains(charactersDir)
    solver = Solver(domains, testChar, settings)