#!/bin/bash
i=$1
printf "num;max;min;avg\n"
while [ "$i" -le "$2" ]; do
if [ -f "test${i}-fit.txt" ]
then
max=`cat test${i}-fit.txt | sort -g | tail -n1`
min=`cat test${i}-fit.txt | sort -g | head -n1`
avg=`awk '{ total += $1; count++ } END { print total/count }' test${i}-fit.txt`
printf "${i};${max};${min};${avg}\n" | sed 's/\./,/g'
else
printf "${i}; ; ; \n"
fi
i=$(($i + 1))
done