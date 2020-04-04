#!/bin/python3

class CrossingOverFactory:

    def __init__(self, type):
        if type == 'SINGLE-POINT':
            def implement(parents, children):

        elif type == 'TWO-POINT':
            def implement(parents, children):
        else:
            print('Invalid ImplementationType Type')
            exit(1)
        self.implement = implement
    
    def getImplementationFunction(self):
        return self.implement