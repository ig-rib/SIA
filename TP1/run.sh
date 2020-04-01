#!/bin/bash
if find maps/$1 > /dev/null 2>&1 ; then
echo "PARAMETRES"
echo "------------------"
cat solver.config
echo "------------------"
echo "START"
echo "------------------"
python3 python/main.py maps/$1
else
echo "Can't find ${1} in maps, please make sure ${1} file exists"
fi