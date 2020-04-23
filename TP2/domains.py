#!/bin/python3

import constants as ct
from copy import copy
import os

# def getDomains(characters):
#     domains = { key : [] for key in characters[0].genes.keys()}
#     for character in characters:
#         for key in character.genes.keys():
#             domains[key].append(copy(character.genes[key]))
#     return domains

def getDomain(fileName, equipmentType):
    file = open(fileName)
    headers = file.readline().rstrip().split()
    line = file.readline()
    domain = []
    while line:
        newItem = {}
        values = [float(x) for x in line.rstrip().split()]
        values[0] = int(values[0])
        for i in range(1, len(headers)):
            newItem[headers[i]] = values[i]
        domain.append(newItem)
        line = file.readline()
    file.close()
    return domain
def readDomains(domainsPath):
    domains = {}
    for fileNm in os.listdir(domainsPath):
        eqType = fileNm.split('.')[0]
        domains[eqType] = getDomain(domainsPath + fileNm, eqType)
    return domains