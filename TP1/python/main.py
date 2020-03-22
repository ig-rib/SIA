#!/bin/python3

from mazeReader import MazeReader
from configFileReader import ConfigFileReader
from solver import Solver
import sys

if len(sys.argv) != 2:
    print("Usage: solver.py [mazefile]")
else:
    cfr = ConfigFileReader('solver.config')
    settings = cfr.getSettings()
    solver = Solver(settings)
    solver.solve(sys.argv[1])