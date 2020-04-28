#!/bin/python3

from character.character import Character, Warrior, Archer, Defender, Spy
import math
import random
import re

class GenerationZeroGenerator:
    def __init__(self, characterClass):
        self.characterClass = characterClass

    def generateCharacters(self, N, domains):
        characters =  []
        ## TODO error checking for N variable
        equipmentByCharacter = []
        for i in range(N):
            newEquipment = {}
            for domain in domains.keys():
                newEquipment[domain] = random.sample(domains[domain], 1)[0]
            equipmentByCharacter.append(newEquipment)

        for equipment in equipmentByCharacter:
            height = random.random() * 0.7 + 1.3
            if self.characterClass == 'WARRIOR':
                characters.append(Warrior(height, equipment))                
            elif self.characterClass == 'ARCHER':
                characters.append(Archer(height, equipment))
            elif self.characterClass == 'DEFENDER':
                characters.append(Defender(height, equipment))
            elif self.characterClass == 'SPY':
                characters.append(Spy(height, equipment))
        #print('generated genZero')
        return characters