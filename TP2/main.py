#!/bin/python3

from readers.configFileReader import ConfigFileReader

if __name__ == '__main__':
    settings = ConfigFileReader('TP2/solver.config').getSettings()
    