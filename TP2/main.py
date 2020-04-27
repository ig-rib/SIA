#!/bin/python3

from readers.configFileReader import ConfigFileReader
from solver import Solver
from geneticSelectors.eliteSelector import EliteSelector
import os
from domains import readDomains

if __name__ == '__main__':
    charactersDir = 'characters/'
    settings = ConfigFileReader('solver.config').getSettings()
    equipmentFiles = [charactersDir + '/' + fileName for fileName in os.listdir(charactersDir)]
    # characters = GenerationZeroReader(equipmentFiles, charClass).generateCharacters()
    domains = readDomains('characters/')
    # domains = readDomains(charactersDir)
    solver = Solver(domains, settings['CLASS'], settings)