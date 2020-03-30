#!/bin/bash

echo "out_file;cost;depth;exp_nodes;frontier;time;"
for file in test/*-$1.txt
do
printf "${file};"
cat ${file} | tail -n 5 | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | sed -z 's/\n/;/g' |  sed 's/\./,/g'
printf "\n"
done
