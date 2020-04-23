#!/bin/bash
echo "Start Test"
for i in 1 2 3 4
do
printf "Start Test ${i}\n"
cat solver.config.${i} > solver.config
python3 main.py > test${i}.txt
printf "Test ${i} Finished\n"
done
