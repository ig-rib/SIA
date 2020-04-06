#!/bin/python3

import constants as ct

class SelectorFactory:

    def __init__(self, type):
        if type == 'ELITE':
            def performSelection(parents, children):
                
                return None
        elif type == 'R-WHEEL':
            def performSelection(parents, children):
                return None
        elif type == 'UNIV':
            def performSelection(parents, children):
                return None
        elif type == 'BOLTZMANN':
            def performSelection(parents, children):
                return None
        elif type == 'TOURNAMENTS-1':
            def performSelection(parents, children):
                return None
        elif type == 'TOURNAMENTS-2':
            def performSelection(parents, children):
                return None
        elif type == 'RANKING':
            def performSelection(parents, children):
                return None
        else:
            print('Invalid Selection Type')
            exit(1)
        self.performSelection = performSelection
    
    def getSelectionFunction(self):
        return self.performSelection
