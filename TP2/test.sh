#!/bin/bash
echo "Start Test"
list=`ls config -l | sed 's/.*[\.:]//' | sed 1d | sed ':a;N;$!ba;s/\n/ /g'`
for i in $list  
do
#Runtime
printf "Start Test ${i}\n"
cat config/solver.config.${i} > solver.config
python3 main.py > test${i}.txt
cat test${i}.txt | sed 's/\([^;]\);\(.\)/\2/' > test${i}-fit.txt
printf "Test ${i} Finished\n"

#Plot Generator
sub=`cat solver.config | sed ':a;N;$!ba;s/\n/ - /g' | sed ':s;s/\(\<\S*\>\)\(.*\)\<\1\>/\1\2/g;ts'`

printf "set title \'${sub}\'\nset grid\nset ylabel \'Fitness\'\nset xlabel \'Generation\'\nset term png size 1600,900\nset output \'plot-test${i}.png\'\nset style fill transparent solid .2 noborder\nplot \"test${i}-fit.txt\" with points" | gnuplot

i=$(($i + 1))
done