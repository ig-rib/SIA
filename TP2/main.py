#!/bin/python3

from readers.configFileReader import ConfigFileReader
from readers.generationZeroReader import GenerationZeroReader
from solver import Solver
from geneticSelectors.eliteSelector import EliteSelector
import os

if __name__ == '__main__':
    charClass = 'ARCHER'
    charactersDir = 'characters'
    settings = ConfigFileReader('solver.config').getSettings()
    equipmentFiles = [charactersDir + '/' + fileName for fileName in os.listdir(charactersDir)]
    characters = GenerationZeroReader(equipmentFiles, charClass).generateCharacters()
    solver = Solver(characters, settings)
