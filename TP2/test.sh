#!/bin/bash
echo "Start Test"
for i in 1 2 3 4
do
#Runtime
printf "Start Test ${i}\n"
cat solver.config.${i} > solver.config
python3 main.py > test${i}.txt
./plot.sh ${i}
printf "Test ${i} Finished\n"

#Plot Generator
print "set title \'Test ${i}\'\nset grid\nset ylabel \'Fitness\'\nset xlabel \'Generation\'\nset term png size 1024,768\nset output \'plot-test${i}.png\'\nset style fill transparent solid .2 noborder\nplot \"test${i}.txt\" with points" | gnuplot
done
