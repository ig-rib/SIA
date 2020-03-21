#!/bin/bash
echo "TEST START MAP: $1"
echo "------------------"

echo "GG START"
printf "DFS 0\nBFS 0\nIDDFS 0\nGG 1\nA* 0\nIDA* 0" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > gg-$1.txt
date +"%T.%3N"
echo "GG FINISH"
echo "------------------"

echo "A* START"
printf "DFS 0\nBFS 0\nIDDFS 0\nGG 0\nA* 1\nIDA* 0" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > Astar-$1.txt
date +"%T.%3N"
echo "A* FINISH"
echo "------------------"

echo "IDDFS START"
printf "DFS 0\nBFS 0\nIDDFS 1\nGG 0\nA* 0\nIDA* 0" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > IDDFS-$1.txt
date +"%T.%3N"
echo "GG FINISH"
echo "------------------"

echo "IDA* START"
printf "DFS 0\nBFS 0\nIDDFS 0\nGG 0\nA* 0\nIDA* 1" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > IDAstar-$1.txt
date +"%T.%3N"
echo "IDA* FINISH"
echo "------------------"


echo "DFS START"
printf "DFS 1\nBFS 0\nIDDFS 0\nGG 0\nA* 0\nIDA* 0" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > DFS-$1.txt
date +"%T.%3N"
echo "DFS FINISH"
echo "------------------"

echo "BFS START"
printf "DFS 0\nBFS 1\nIDDFS 0\nGG 0\nA* 0\nIDA* 0" > solver.config
date +"%T.%3N"
python3 python/solver.py maps/$1 > BFS-$1.txt
date +"%T.%3N"
echo "BFS FINISH"
echo "------------------"

#Create Stats
echo "Creating Stats"
./stats.sh $1 > /stats/$1-stats.txt
cat /stats/$1-stats.txt
echo "Finished"
