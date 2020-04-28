# Requerimientos
Python 3

# Ejecución
Para ejecutar el programa, situarse en la carpeta TP2 y ejecutar en consola:
```
python3 main.py [Clase Objetivo] 
```

CROSSING-OVER ANNULAR
MUTATION LIM-MULTIGEN
SELECTION ELITE UNIV ELITE UNIV
IMPLEMENTATION FILL-ALL
STOP-CRITERION GENERATIONS 100
PM 0.75
CLASS WARRIOR
T 75
T2Thresh 0.75
a 0.75
b 0.25
PQTY 10

Operadores Genéticos
CROSSING-OVER (Cruce):
    SINGLE-POINT (Cruce de un punto)
    TWO-POINT (Cruce de dos puntos)
    ANNULAR (Cruce anular)
    UNIFORM (Cruce Uniforme)
MUTATION (Mutación):
    GEN (Gen)
    LIM-MULTIGEN (Multigen Limitado)
    UNIFORM-MULTIGEN (Multigen Uniforme)
    COMPLETE (Completa)
SELECTION (Selección):
    ELITE (Elite)
    R-WHEEL (Ruleta)
    UNIV (Universal)
    BOLTZMANN (Boltzmann)
    TOURNAMENTS-1 (Torneos 1)
    TOURNAMENTS-2 (Torneos 2)
    RANKING (Ranking)
IMPLEMENTATION (Implementación):
    FILL-ALL
    FILL-PARENT
STOP-CRITERION (Criterio de finalización):
    TIME (Tiempo)
    GENERATIONS (Generación)
    ACCEPTABLE (Aceptable)
    STRUCT (Estructura)
    CONTENT (Contenido)