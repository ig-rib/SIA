#!/bin/python3

class MutationFactory:

    def __init__(self, type):
                
        if type == 'GEN':
            def performMutation(children):
                return None
        elif type == 'LIM-MULTIGEN':
            def performMutation(children):
                return None
        elif type == 'UNIFORM-MULTIGEN':
            def performMutation(children):
                return None
        elif type == 'COMPLETE':
            def performMutation(children):
                return None
        else:
            print('Invalid Mutation Type')
            exit(1)
        self.performMutation = performMutation
    
    def getMutationFunction(self):
        return self.performMutation
