#!/bin/python3

from treeNode import Node
from state import State
from mazeReader import MazeReader
import heapq
from collections import deque

def findNextStates(curr, goalSquares, maze, E):
        boxes = curr.state.boxes
        user = curr.state.user
        newStates = []
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            moveCost = 0
            boxMoved = ()
            newBoxes = boxes
            hasChanged = False
            tdir = (user[0]+dir[0], user[1]+dir[1])
            t = maze[tdir[0]][tdir[1]]
            if tdir in boxes:
                ttdir = (user[0]+2*dir[0], user[1]+2*dir[1])
                tt = maze[ttdir[0]][ttdir[1]]
                moveCost+=1                
                if tt == ' ' or tt == '.' and ttdir not in boxes:
                    hasChanged = True
                    boxMoved = tdir
            elif t == ' ' or t == '.':
                moveCost+=2
                hasChanged = True
            if hasChanged:
                newUser = (user[0]+dir[0], user[1]+dir[1])
                if len(boxMoved) > 0:
                    newBoxes = [b for b in boxes if b != tdir]
                    newBoxes.append(ttdir)
                toBeAdded = State(newBoxes, newUser)
                if not toBeAdded in E:
                    E.append(toBeAdded)
                    if not toBeAdded.hasUnmovableBox(maze, goalSquares):
                        newStates.append(Node(p=curr, state=toBeAdded, g=curr.g + moveCost))
        return newStates

mr = MazeReader()

Tr = mr.Tr
maze = mr.Q0
gS = mr.goalSquares

F = deque()
E = []
F.append(Tr)
E.append(Tr.state)
solved = False
while len(F) > 0 and not solved:
    # Uniform Cost Search
    # curr = heapq.heappop(F)
    # BFS
    # curr = F.popleft()
    # DFS
    curr = F.pop()

    curr.state.printState(maze)

    if curr.state.checkFinal(gS):
        solutionNode = curr
        solved = True
    else:
        newNodes = findNextStates(curr, gS, maze, E)
        for node in newNodes:
            curr.children.append(node)
            # Uniform Cost Search
            # heapq.heappush(F, node)
            # BFS, DFS
            F.append(node)
if solved:
    p = solutionNode
    path = deque()
    while p is not None:
        path.appendleft(p.state)
        p = p.p
    for state in path:
        state.printState(maze)
    print("Total cost: %ld\nSolution Depth: %ld\nExpanded Nodes: %ld\nRemaining Frontier: %ld" 
    % (solutionNode.g, len(path), len(E), len(F)))