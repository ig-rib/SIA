from treeNode import Node
from state import State

class MazeReader:
    def __init__(self):
        self.Tr = Node()
        self.Q0 = []
        self.goalSquares = []
        file = open('../maps/map1')
        lines = file.readlines()
        boxes = []
        for num, line in enumerate(lines):
            line = list(line.rstrip("\n"))
            try:
                j = line.index("@")
                user = (num, j)
                line[j] = ' '
            except ValueError:
                self
            try:
                js = [ (num, i) for i, elem in enumerate(line) if elem == '.']
                self.goalSquares.extend(js)
            except ValueError:
                self
            try:
                js = [ (num, i) for i, elem in enumerate(line) if elem == '$']
                boxes.extend(js)
                for j in js:
                    line[j[1]] = ' '
            except ValueError:
                self
            self.Q0.append(line)
        self.Tr.state = State(boxes, user)
        file.close()