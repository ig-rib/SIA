#!/bin/bash
mkdir -p config
count=0
for char in "WARRIOR" "ARCHER" "DEFENDER" "SPY"
do
for cross in "SINGLE-POINT" "TWO-POINT" "ANNULAR" "UNIFORM"
do
for mutation in "GEN" "LIM-MULTIGEN" "UNIFORM-MULTIGEN" "COMPLETE"
do
for selec in "ELITE" "R-WHEEL" "UNIV" "BOLTZMANN" "TOURNAMENTS-1" "TOURNAMENTS-2" "RANKING"
do
for imple in "FILL-ALL" "FILL-PARENT"
do
printf "CROSSING-OVER ${cross}\nMUTATION ${mutation}\nSELECTION ELITE ${selec} ELITE ${selec}\nIMPLEMENTATION FILL-ALL\nSTOP-CRITERION GENERATIONS 100\nPM 0.75\nCLASS ${char}\nT 75\nT2Thresh 0.75\na 0.75\nb 0.25\nPQTY 10" > config/solver.config.${count}
count=$((count+1))
done
done
done
done
done
