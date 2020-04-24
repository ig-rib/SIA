#!/bin/bash
mkdir config
count=0
for char in "WARRIOR" "ARCHER" "DEFENDER" "SPY"
do
for cross in "SINGLE-POINT" "TWO-POINT" "ANNULAR" "UNIFORM"
do
for mutation in "GEN" "LIM-MULTIGEN" "UNIFORM-MULTIGEN" "COMPLETE"
do
for imple in "FILL-ALL" "FILL-PARENT"
do
printf "CROSSING-OVER ${cross}\nMUTATION ${mutation}\nSELECTION ELITE R-WHEEL ELITE BOLTZMANN\nIMPLEMENTATION ${impl}\nSTOP-CRITERION GENERATIONS 500\nPM 0.75\nCLASS ${char}\nT 75\nT2Thresh 0.75\na 0.75\nb 0.25\nPQTY 10" > config/solver.config.${count}
count=$((count+1))
done
done
done
done
