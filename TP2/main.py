#!/bin/python3

from configFileReader import ConfigFileReader

if __name__ == '__main__':
    settings = ConfigFileReader('TP2/solver.config').getSettings()
    