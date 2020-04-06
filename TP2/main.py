#!/bin/python3

from readers.configFileReader import ConfigFileReader
from readers.generationZeroReader import GenerationZeroReader
from solver import Solver
import os

if __name__ == '__main__':
    charClass = 'WARRIOR'
    charactersDir = 'characters'
    settings = ConfigFileReader('solver.config').getSettings()
    equipmentFiles = [charactersDir + '/' + fileName for fileName in os.listdir(charactersDir)]
    characters = GenerationZeroReader(equipmentFiles, charClass).generateCharacters()
    solver = Solver(characters, settings)
