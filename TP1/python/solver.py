#!/bin/python3

from treeNode import Node
from state import State
from mazeReader import MazeReader
from heuristicsFactory import HeuristicsFactory
from configFileReader import ConfigFileReader
import heapq
import sys
from collections import deque
from math import sqrt
import datetime as dt

def findNextStates(curr, goalSquares, maze, E, cornerSense = False):
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
                    if not cornerSense or not toBeAdded.hasUnmovableBox(maze, goalSquares):
                        newStates.append(Node(p=curr, state=toBeAdded, g=curr.g + moveCost))
        return newStates

class Solver:

    def __init__(self, settings):
        self.settings = settings

    def solve(self, mazeFile):

        mr = MazeReader(mazeFile)

        Tr = mr.Tr
        Tr.g = 0

        maze = mr.Q0
        gS = mr.goalSquares

        BFS = self.settings['BFS']
        id = self.settings['IDDFS'] or self.settings['IDA*']
        A = self.settings['A*'] or self.settings['IDA*']
        GG = self.settings['GG']
        H = self.settings['H']

        if not GG:
            def f(node):
                return node.g + node.h
        else:
            def f(node):
                return node.h

        heuristicsFactory = HeuristicsFactory(H, gS)
        h = heuristicsFactory.getHeuristic()

        Tr.h = h(Tr.state)
        Tr.f = f

        start = dt.datetime.now()

        if BFS:
            F = deque()
        else:
            F = []
        E = []
        F.append(Tr)
        E.append(Tr.state)
        if not id:
            solved = False
            Tr.f = f
            while len(F) > 0 and not solved:
                # # Uniform Cost Search
                if A or GG:
                    curr = heapq.heappop(F)
                # BFS
                elif BFS:
                    curr = F.popleft()
                # DFS
                else:
                    curr = F.pop()
                if self.settings['PrintState'] == 1:
                    curr.state.printState(maze)
                if curr.state.checkFinal(gS):
                    solutionNode = curr
                    solved = True
                    totalTime = dt.datetime.now() - start
                else:
                    newNodes = findNextStates(curr, gS, maze, E, self.settings['CornerSense'])
                    for node in newNodes:
                        node.f = f
                        node.h = h(node.state)
                        curr.children.append(node)
                        # Uniform Cost Search
                        if A or GG:
                            heapq.heappush(F, node)
                        # BFS, DFS
                        else:
                            F.append(node)

        elif not A: # iddfs

            limit = Tr.f(Tr)
            solved = False
            while limit < 1000 and not solved:
                F = []
                F.append([Tr, limit])
                while len(F)>0 and not solved:
                    [curr, lim] = F.pop()
                    if self.settings['PrintState'] == 1:
                        curr.state.printState(maze)
                    if lim <= 0:
                        False
                    elif curr.state.checkFinal(gS):
                        solutionNode = curr
                        solved = True
                        totalTime = dt.datetime.now() - start
                    else:
                        if len(curr.children) > 0:
                            newNodes = curr.children
                        else:
                            newNodes = findNextStates(curr, gS, maze, E, self.settings['CornerSense'])
                            curr.children.extend(newNodes)
                        F.extend([[node, lim-1] for node in newNodes])
                limit += 50

        else: # ida*
            solved = False
            limit = Tr.f(Tr)
            while limit < 1000 and not solved:
                F = []
                candidates = []
                heapq.heappush(F, Tr)
                while len(F)>0 and not solved:
                    curr = heapq.heappop(F)
                    if self.settings['PrintState'] == 1:
                        curr.state.printState(maze)
                    if curr.f(curr) > limit:
                        candidates.append(curr.f(curr))
                    elif curr.state.checkFinal(gS):
                        solutionNode = curr
                        solved = True
                        totalTime = dt.datetime.now() - start
                    else:
                        if len(curr.children) > 0:
                            newNodes = curr.children
                        else:
                            newNodes = findNextStates(curr, gS, maze, E, self.settings['CornerSense'])
                            for node in newNodes:
                                node.h = h(node.state)
                                node.f = f
                            curr.children.extend(newNodes)
                        F.extend(newNodes)
                if not solved:
                    limit = min(candidates)
        if solved:
            p = solutionNode
            path = deque()
            while p is not None:
                path.appendleft(p.state)
                p = p.p
            for state in path:
                state.printState(maze)
                print("&&")

            print("Total cost: %ld\nSolution Depth: %ld\nExpanded Nodes: %ld\nRemaining Frontier: %ld" 
            % (solutionNode.g, len(path), len(E), len(F)))
            print(totalTime.total_seconds())
