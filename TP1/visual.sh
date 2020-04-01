#!/bin/bash
if find test/$1 > /dev/null 2>&1 ; then
python3 visual.py test/$1
else
echo "Can't find ${1} in test, please make sure ${1} file exists"
fi
