#!/bin/python3

import constants as ct

class ImplementationFactory:

    def __init__(self, type):
        if type == 'FILL-PARENT':
            def implement(parents, children):
                # Acá debería ser >= K, pero todavía no sé de dónde sacarlo
                if len(children) >= len(parents):
                    return [ct.oneArray, children]
                children.extend(parents)
                return [ct.childrenAndParents, children, parents]
        elif type == 'FILL-ALL':
            def implement(parents, children):
                children.extend(parents)
                return [ct.oneArray, children]
        else:
            print('Invalid ImplementationType Type')
            exit(1)
        self.implement = implement
    
    def getImplementationFunction(self):
        return self.implement