#!/bin/python3

from collections import deque

class ConfigFileReader:

    def __init__(self, filename):
        self.settings = {}
        settingsFile = open(filename)
        line = settingsFile.readline()
        while line:
            keyValuePair = deque(line.rstrip().split())
            self.settings[keyValuePair.popleft()] = keyValuePair.pop()
            line = settingsFile.readline()

    def getSettings(self):
        return self.settings