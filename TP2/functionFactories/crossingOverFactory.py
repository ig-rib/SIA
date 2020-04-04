#!/bin/python3

class CrossingOverFactory:

    def __init__(self, type):
        if type == 'SINGLE-POINT':
            def performCrossingOver(generation):

        elif type == 'TWO-POINT':
            def performCrossingOver(generation):

        elif type == 'ANNULAR':
            def performCrossingOver(generation):

        elif type == 'UNIFORM':
            def performCrossingOver(generation):
        else:
            print('Invalid Crossing Over Type')
            exit(1)
        self.performCrossingOver = performCrossingOver
    
    def getCrossingOverFunction(self):
        return self.performCrossingOver