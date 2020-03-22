#!/bin/bash
echo "Not Informed Test"

echo "DFS START"
printf "DFS 1\nBFS 0\nIDDFS 0\nGG 0\nA* 0\nIDA* 0\nH ${2}\nPrintState 1\nCornerSense 1\n" > solver.config
date +"%T.%3N"
python3 python/main.py maps/$1 > DFS-$1.txt
date +"%T.%3N"
echo "DFS FINISH"
echo "------------------"

echo "BFS START"
printf "DFS 0\nBFS 1\nIDDFS 0\nGG 0\nA* 0\nIDA* 0\nH ${2}\nPrintState 1\nCornerSense 1\n" > solver.config
date +"%T.%3N"
python3 python/main.py maps/$1 > BFS-$1.txt
date +"%T.%3N"
echo "BFS FINISH"
echo "------------------"

#Create Stats
echo "Creating Stats"
mkdir stats
./stats.sh $1 > stats/$1-stats.txt
cat stats/$1-stats.txt
echo "Finished"

