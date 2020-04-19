#!/bin/python3

import math
import constants as ct

class Character:

    def __init__(self, height = 0, equipment = None, attackCoeff = 0.0, defenseCoeff = 0.0):
        # self.h = height
        self.genes = {}
        self.genes[ct.height] = height
        for key in equipment.keys():
            self.genes[key] = equipment[key]
        # self.equipment = equipment
        self.attackCoeff = attackCoeff
        self.defenseCoeff = defenseCoeff
    
    def __sumEquipmentPropertyValues(self, propertyName):
        total = 0
        for key in filter(lambda x: x != ct.height, self.genes.keys()):
            total += self.genes[key][propertyName]
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
        return 0.7 - (3*self.genes[ct.height]-5)**4 + (3*self.genes[ct.height]-5)**2 + self.genes[ct.height]/4
    def calculateDEM(self):
        return 1.9 + (2.5*self.genes[ct.height] - 4.16)**4 - (2.5*self.genes[ct.height]-4.16)**2 - 3*self.genes[ct.height]/10

    def calculateAttack(self):
        return (self.calculateAgility() + self.calculateExpertise()) * self.calculateStrength() * self.calculateATM()
    def calculateDefense(self):
        return (self.calculateResistance() + self.calculateExpertise()) * self.calculateLife() * self.calculateDEM()

    def getPerformance(self):
        return self.attackCoeff * self.calculateAttack() + self.defenseCoeff * self.calculateDefense()

    def equals(self, other : Character):
        for gene in self.genes.keys():
            if gene == ct.height:
                if self.genes[gene] != other.genes[gene]:
                    return False
            else:
                for key in self.genes[gene].keys():
                    if self.genes[gene][key] != other.genes[gene][key]:
                        return False
        return True

    def __repr__(self):
        return self.getPerformance()

    def __ge__(self, other):
        return self.getPerformance() >= other.getPerformance()
    def __gt__(self, other):
        return self.getPerformance() > other.getPerformance()
    def __le__(self, other):
        return self.getPerformance() <= other.getPerformance()
    def __lt__(self, other):
        return self.getPerformance() < other.getPerformance()
    def __eq__(self, other):
        return self.getPerformance() == other.getPerformance()
    def __ne__(self, other):
        return self.getPerformance() != other.getPerformance()

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