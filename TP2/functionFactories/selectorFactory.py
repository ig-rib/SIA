#!/bin/python3

import constants as ct

from geneticSelectors.boltzmannSelector import BoltzmannSelector
from geneticSelectors.rWheelSelector import RWheelSelector
from geneticSelectors.eliteSelector import EliteSelector
from geneticSelectors.rankingSelector import RankingSelector
from geneticSelectors.tournaments1Selector import Tournaments1Selector
from geneticSelectors.tournaments2Selector import Tournaments2Selector
from geneticSelectors.univSelector import UnivSelector

class SelectorFactory:

    def __init__(self, type, N, T=None, T2Threshold=None):
        if type == 'ELITE':
            self.selector =  EliteSelector(N)
        elif type == 'R-WHEEL':
            self.selector = RWheelSelector(N)
        elif type == 'UNIV':
            self.selector = UnivSelector(N)
        elif type == 'BOLTZMANN':
            self.selector = BoltzmannSelector(N, T)
        elif type == 'TOURNAMENTS-1':
            self.selector = Tournaments1Selector(N)
        elif type == 'TOURNAMENTS-2':
            self.selector = Tournaments2Selector(N, T2Threshold)
        elif type == 'RANKING':
            self.selector = RankingSelector(N)
        else:
            print('Invalid Selection Type')
            exit(1)
    
    def getSelector(self):
        return self.selector
