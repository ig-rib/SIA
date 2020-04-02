import sys
class HeuristicsFactory:
    def __init__(self, H, gS):
        if H==0:
            def h(state):
                sum = 0
                for box in state.boxes:
                    min = sys.maxsize
                    for g in gS:
                        md = abs(g[0]-box[0]) + abs(g[1]-box[1])
                        if md < min:
                            min = md
                    sum += min
                return sum
        if H==1:
            def h(state):
                sum = 0
                for box in state.boxes:
                    min = sys.maxsize
                    for g in gS:
                        md = abs(g[0]-box[0]) + abs(g[1]-box[1])
                        if md < min:
                            min = md
                    sum += min
                sum += min([abs(b[0]-state.user[0]) + abs(b[1]-state.user[1]) for b in state.boxes])
                return sum
        if H==2:
            def h(state):
                for box in state.boxes:
                    max = 0
                    for g in gS:
                        md = abs(g[0]-box[0])**2 + abs(g[1]-box[1])**2
                        if md > max:
                            max = md
                    sum += max
                sum += max([abs(b[0]-state.user[0]) + abs(b[1]-state.user[1]) for b in state.boxes])**2
                return sum
        self.h = h

    def getHeuristic(self):
        return self.h
    