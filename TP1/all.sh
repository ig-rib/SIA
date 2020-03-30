#!/bin/bash
if find maps/$1 > /dev/null 2>&1 ; then
./inf_test.sh $1 0
./inf_test.sh $1 1
./inf_test.sh $1 2
./ninf_test.sh $1 0
else
echo "Can't find ${1} in maps, please make sure ${1} file exists"
fi

