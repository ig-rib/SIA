#!/bin/python3

from TP2.character.Character import Character, Warrior, Archer, Defender, Spy
import math
import random

def readGenzeroFile(fileName, equipmentType, eBC):
    file = open(fileName)
    headers = file.readline().rstrip().split
    line = file.readline()
    while line:
        values = [int(x) for x in line.rstrip().split()]
        if len(eBC) < values[0] + 1:
            for i in range(0, values[0] - len(eBC) +1):
                eBC.append({})
        if eBC.get(equipmentType) == None:
            eBC[equipmentType] = {}
        for i in range(1, len(headers)):
            eBC[values[0]][headers[i]] = values[i]    
    file.close()
class GenerationZeroReader:
    def __init__(self, gZeroFiles, characterClass):
        self.characterClass = characterClass
        equipmentByCharacter = []
        for fileName in gZeroFiles:
            nameArray = fileName.split('.')
            nameArray.pop()
            readGenzeroFile(fileName, nameArray.pop(), equipmentByCharacter)
        self.equipmentByCharacter = equipmentByCharacter

    def generateCharacters(self):
        characters =  []
        for equipment in self.equipmentByCharacter:
            height = random.random() * 0.7 + 1.3
            if self.characterClass == 'WARRIOR':
                characters.append(Warrior(height, equipment))                
            elif self.characterClass == 'ARCHER':
                characters.append(Archer(height, equipment))
            elif self.characterClass == 'DEFENDER':
                characters.append(Defender(height, equipment))
            elif self.characterClass == 'SPY':
                characters.append(Spy(height, equipment))
        return characters