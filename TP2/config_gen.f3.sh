#!/bin/bash
mkdir config
count=0
for char in "WARRIOR" "ARCHER" "DEFENDER" "SPY"
do
for mutation in "GEN" "LIM-MULTIGEN" "UNIFORM-MULTIGEN" "COMPLETE"
do
for imple in "FILL-ALL" "FILL-PARENT"
do
for parent in "10" "20" "40" "80" "160" "320"
do
printf "CROSSING-OVER TWO-POINT\nMUTATION ${mutation}\nSELECTION ELITE ELITE ELITE ELITE\nIMPLEMENTATION FILL-ALL\nSTOP-CRITERION GENERATIONS 1000\nPM 0.75\nCLASS ${char}\nT 75\nT2Thresh 0.75\na 0.75\nb 0.25\nPQTY ${parent}" > config/solver.config.${count}
count=$((count+1))
done
done
done
done