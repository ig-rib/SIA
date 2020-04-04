#!/bin/python3

class MutationFactory:

    def __init__(self, type):
                
        if type == 'TIME':
            def done(criterionValue, criticalValue):

        elif type == 'GENERATIONS':
            def done(criterionValue, criticalValue):

        elif type == 'ACCEPTABLE':
            def done(criterionValue, criticalValue):
        elif type == 'STRUCT':
            def done(criterionValue, criticalValue):
        elif type == 'CONTENT':
            def done(criterionValue, criticalValue):

        else:
            print('Invalid Stop Criterion')
            exit(1)
        self.done = done
    
    def getDoneFunction(self):
        return self.done
