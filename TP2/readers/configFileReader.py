#!/bin/python3

from collections import deque

class ConfigFileReader:

    def __init__(self, filename):
        self.settings = {}
        settingsFile = open(filename)
        line = settingsFile.readline()
        while line:
            keyValuePair = deque(line.rstrip().split())
            key = keyValuePair.popleft()
            self.settings[key] = keyValuePair.popleft()
            if len(keyValuePair) > 0:
                self.settings[key] = [self.settings[key], keyValuePair.popleft()]
            line = settingsFile.readline()

    def getSettings(self):
        return self.settings