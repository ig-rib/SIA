#!/bin/bash
i=$1
echo "Start Test"
while [ "$i" -le "$2" ]; do
#Runtime
printf "Start Test ${i}\n"
cat config/solver.config.${i} > solver.config
python3 main.py > test${i}.txt
printf "Test ${i} Finished\n"

#Plot Generator
sub=`cat solver.config | sed ':a;N;$!ba;s/\n/ - /g'`
printf "set title \'${sub}\'\nset grid\nset ylabel \'Fitness\'\nset xlabel \'Generation\'\nset term png size 1600,900\nset output \'plot-test${i}.png\'\nset style fill transparent solid .2 noborder\nplot \"test${i}.txt\" with points" | gnuplot

i=$(($i + 1))
done
head -12 config/solver.config.* > all.config.test
rm config/solver.config.*
