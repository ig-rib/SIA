#!/bin/python3

import constants as ct
from copy import copy

def getDomains(characters):
    domains = { key : [] for key in characters[0].genes.keys()}
    for character in characters:
        for key in character.genes.keys():
            domains[key].append(copy(character.genes[key]))
    return domains