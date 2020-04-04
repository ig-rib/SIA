#!/bin/python3

class SelectorFactory:

    def __init__(self, type):
        if type == 'R-WHEEL':
            def performSelection(parents, children):
                
        elif type == 'UNIV':
            def performSelection(parents, children):

        elif type == 'BOLTZMANN':
            def performSelection(parents, children):

        elif type == 'TOURNAMENTS-1':
            def performSelection(parents, children):
        elif type == 'TOURNAMENTS-2':
            def performSelection(parents, children):
        elif type == 'RANKING':
            def performSelection(parents, children):
        else:
            print('Invalid Selection Type')
            exit(1)
        self.performSelection = performSelection
    
    def getSelectionFunction(self):
        return self.performSelection
