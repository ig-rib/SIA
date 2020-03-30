#!/bin/bash
echo "TEST START MAP: $1 Heuristic $2"
echo "------------------"

echo "GG START"
printf "DFS 0\nBFS 0\nIDDFS 0\nGG 1\nA* 0\nIDA* 0\nH ${2}\nPrintState 0\nCornerSense 1\n" > solver.config
date +"%T.%3N"
python3 python/main.py maps/$1 > H$2-gg-$1.txt
date +"%T.%3N"
echo "GG FINISH"
echo "------------------"

echo "A* START"
printf "DFS 0\nBFS 0\nIDDFS 0\nGG 0\nA* 1\nIDA* 0\nH ${2}\nPrintState 0\nCornerSense 1\n" > solver.config
date +"%T.%3N"
python3 python/main.py maps/$1 > H$2-Astar-$1.txt
date +"%T.%3N"
echo "A* FINISH"
echo "------------------"

echo "IDDFS START"
printf "DFS 0\nBFS 0\nIDDFS 1\nGG 0\nA* 0\nIDA* 0\nH ${2}\nPrintState 0\nCornerSense 1\n" > solver.config
date +"%T.%3N"
python3 python/main.py maps/$1 > H$2-IDDFS-$1.txt
date +"%T.%3N"
echo "GG FINISH"
echo "------------------"

echo "IDA* START"
#printf "DFS 0\nBFS 0\nIDDFS 0\nGG 0\nA* 0\nIDA* 1\nH ${2}\nPrintState 0\nCornerSense 1\n" > solver.config
#date +"%T.%3N"
#python3 python/main.py maps/$1 > H$2-IDAstar-$1.txt
#date +"%T.%3N"
echo "skip" > H$2-IDAstar-$1.txt
echo "IDA* FINISH"
echo "------------------"

#Create Stats
echo "Creating Stats"
mkdir stats
./stats.sh $1 > stats/$1-stats.txt
cat stats/$1-stats.txt
echo "Finished"
