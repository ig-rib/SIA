#!/bin/python3

class StopCriteriaFactory:

    def __init__(self, type):
                
        if type == 'TIME':
            def done(criterionValue, criticalValue):
                return criterionValue >= criticalValue
        elif type == 'GENERATIONS':
            def done(criterionValue, criticalValue):
                return criterionValue >= criticalValue
        elif type == 'ACCEPTABLE':
            def done(criterionValue, criticalValue):
                return criterionValue > criticalValue
        elif type == 'STRUCT':
            def done(generation, newGeneration, equalGenerations, percentage, stopLimit):
                equalIndividuals = len(list(filter(lambda x: x, [len([ z for z in newGeneration if z.equals(y)]) > 0 for y in generation])))
                equalPercentage = equalIndividuals / len(generation)
                if equalPercentage >= percentage and equalGenerations + 1 < stopLimit:
                    return False, equalGenerations + 1
                elif equalGenerations + 1 == stopLimit:
                    return True, equalGenerations + 1
                return False, 0
        elif type == 'CONTENT':
            def done(criterionValue, criticalValue):
                return criterionValue >= criticalValue
        else:
            print('Invalid Stop Criterion')
            exit(1)
        self.done = done
    
    def getDoneFunction(self):
        return self.done
