class Node:
    def __init__(self, p = None, state = None, g = 0, f = 0):
        self.p = p
        self.children = []
        self.state = state
        self.g = g
        self.f = f

    def __eq__(self, value):
        return self.g == value.g
    def __ge__(self, value):
        return self.g >= value.g
    def __gt__(self, value):
        return self.g > value.g
    def __le__(self, value):
        return self.g <= value.g
    def __lt__(self, value):
        return self.g < value.g
    def __ne__(self, value):
        return self.g != value.g
        
    def __repr__(self):
        return "(%s, %s, %s)" % (self.p, self.g)