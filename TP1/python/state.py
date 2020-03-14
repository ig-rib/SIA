class State:
    def __init__(self, boxes=[], user=None):
        self.boxes = boxes
        self.user = user
    
    def checkFinal(self, goalSquares):
        for gS in goalSquares:
            if gS not in self.boxes:
                return False
        return True
    
    def __eq__(self, other):
        for box in self.boxes:
            if not box in other.boxes:
                return False
        if self.user != other.user:
            return False
        return True

    def printState(self, maze):
        for i, row in enumerate(maze):
            for j, el in enumerate(row):
                if (i, j) in self.boxes:
                    print('$', end=" ")
                elif (i, j) != self.user:
                    print(el, end=" ")
                else:
                    print('@', end=" ")
            print()
    
    def hasUnmovableBox(self, maze, gS):
        for b in self.boxes:
            dirns = []
            walls = 0
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if maze[b[0]+dir[0]][b[1]+dir[1]] == '#':
                    dirns.append(dir)
            for dir1 in dirns:
                for dir2 in dirns:
                    if dir1 != dir2 and maze[b[0]+dir1[0]+dir2[0]][b[1]+dir1[1]+dir2[1]] == '#' and b not in gS:
                        return True
        return False
