#!/bin/python3

class MutationFactory:

    def __init__(self, type):
                
        if type == 'GEN':
            def performMutation(children):

        elif type == 'LIM-MULTIGEN':
            def performMutation(children):

        elif type == 'UNIFORM-MULTIGEN':
            def performMutation(children):
        elif type == 'COMPLETE':
            def performMutation(children):
        else:
            print('Invalid Mutation Type')
            exit(1)
        self.performMutation = performMutation
    
    def getMutationFunction(self):
        return self.performMutation
