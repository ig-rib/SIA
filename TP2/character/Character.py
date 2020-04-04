#!/bin/python3

import math

class Character:

    def __init__(self, height = 0, equipment = None, attackCoeff = 0.0, defenseCoeff = 0.0):
        self.h = height
        self.equipment = equipment
        self.attackCoeff = attackCoeff
        self.defenseCoeff = defenseCoeff
    
    def __sumEquipmentPropertyValues(self, propertyName):
        total = 0
        for key in self.equipment.keys():
            total += self.equipment[key][propertyName]
        return total

    def calculateStrength(self):
        return 100*math.tanh(0.01 * self.__sumEquipmentPropertyValues('Fu'))
    def calculateAgility(self):
        return math.tanh(0.01 * self.__sumEquipmentPropertyValues('Ag'))
    def calculateExpertise(self):
        return 0.6*math.tanh(0.01 * self.__sumEquipmentPropertyValues('Ex'))
    def calculateResistance(self):
        return math.tanh(0.01 * self.__sumEquipmentPropertyValues('Re'))
    def calculateLife(self):
        return 100*math.tanh(0.01 * self.__sumEquipmentPropertyValues('Vi'))

    def calculateATM(self):
        return 0.7 - (3*self.h-5)**4 + (3*self.h-5)**2 + self.h/4
    def calculateDEM(self):
        return 1.9 + (2.5*self.h - 4.16)**4 - (2.5*self.h-4.16)**2 - 3*self.h/10

    def calculateAttack(self):
        return (self.calculateagility() + self.calculateExpertise()) * self.calculateStrength() * self.calculateATM()
    def calculateDefense(self):
        return (self.calculateResistance() + self.calculateExpertise()) * self.calculateLife() * self.calculateDEM()

    def getPerformance(self):
        return self.attackCoeff * self.calculateAttack() + self.defenseCoeff * self.calculateDefense()

class Warrior(Character):
    def __init__(self, height, equipment):
        super().__init__(height, equipment, 0.6, 0.6)

class Archer(Character):
    def __init__(self, height=0, equipment=None):
        super().__init__(height, equipment, 0.9, 0.1)

class Defender(Character):
    def __init__(self, height=0, equipment=None):
        super().__init__(height, equipment, 0.3, 0.8)
        
class Spy(Character):
    def __init__(self, height=0, equipment=None):
        super().__init__(height, equipment, 0.8, 0.3)