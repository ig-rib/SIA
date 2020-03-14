class Node:
    def __init__(self, p = None, state = None, g = None):
        self.p = p
        self.children = []
        self.state = state
        self.g = g
    def __repr__():
        return '{ "g": {}}'.format(self.g)